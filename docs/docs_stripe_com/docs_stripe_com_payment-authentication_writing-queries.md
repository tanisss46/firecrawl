# Querying authentication conversion

## Use Stripe Sigma to retrieve information about authentication, conversion, and the SCA exemptions used.

See the `authentication_report_attempts` table under the **Analytics Tables**
section of the Sigma schema. Each row within the
`authentication_report_attempts` table represents data about an individual
attempt object. Our [full-page
documentation](https://dashboard.stripe.com/stripe-schema?tableName=authentication_report_attempts)
also shows the schema in a split-view format.

## Attempt conversion information

You can get a report for every attempt, with each
[PaymentIntent](https://docs.stripe.com/api/payment_intents) or
[SetupIntent](https://docs.stripe.com/api/payment_intents) having possibly more
than one attempt.

#### Note

In some cases there are multiple attempts for a single transaction, such as when
a payment is declined and then retried. To filter to a specific transaction, use
the `is_final_attempt` column. This column is eventually consist after a few
days.

The following example query uses the `authentication_report_attempts` table to
retrieve a list of payment intents that were successfully authenticated using
the challenge flow.

```
select
 attempt_id,
 intent_id,
 payment_method,
 threeds_reason as step_up_reason,
 charge_outcome
from authentication_report_attempts
where intent_type = 'payment'
 and threeds_outcome_result = 'authenticated'
 and authentication_flow = 'challenge'
 and is_final_attempt
limit 5
```

attempt_idintent_idpayment_methodstep_up_reasoncharge_outcomepayatt_1IRdZ9F…pi_1Hn8d…card_chargerequested_by_radar_ruleauthorizedpayatt_1I4AFxF…pi_1J8Ljt…card_chargerequested_by_radar_ruleauthorizedpayatt_1HvmxU…pi_1HhsH…card_chargerequested_by_radar_ruleauthorizedpayatt_1I5npGF…pi_1IdKak…card_chargerequested_by_radar_ruleauthorizedpayatt_1HcbWZ…pi_1IAhBh…card_chargerequested_by_radar_ruleauthorized
## SCA exemption information

You can also query information on the [SCA
exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)
used by Stripe or the issuing bank. See [Exemptions to Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication).

The following query shows the payments that used a low risk direct authorization
SCA exemption that was declined for a reason unrelated to the requested
exemption.

```
select
 attempt_id,
 intent_id,
 charge_outcome,
 charge_outcome_reason
from authentication_report_attempts
where intent_type = 'payment'
 and sca_exemption_requested = 'low_risk'
 and sca_exemption_mechanism = 'authorization' -- direct to authorization
 and sca_exemption_status = 'non_sca_decline'
 and is_final_attempt
limit 5
```

attempt_idintent_idcharge_outcomecharge_outcome_reasonpayatt_3JeL…pi_3JeL…issuer_declinedinsufficient_fundspayatt_1Itw…pi_1Itw…issuer_declineddo_not_honorpayatt_1Ini3…pi_1Ini3…issuer_declineddo_not_honorpayatt_1IiO7…pi_1IiO7…issuer_declineddo_not_honorpayatt_1I0hGm…pi_1I0hGk…issuer_declinedinsufficient_funds
## Impact of deduplication

The following query shows how removing duplicates with `is_final_attempt`
affects the calculation of the authentication rate for setups.

#### Note

Our deduplication logic looks for groups of declined transactions (except for
the last, potentially) with the same `customer_id​`, `currency`, and `amount​`,
appearing close together in time. Such groups are treated as a single unit for
conversion calculations. In the Sigma table, we include all raw data, but also
include a column, `is_final_attempt​`, that you can use to filter to a
representative transaction from each group.

```
with setup_attempts as (
 select
 created,
 is_final_attempt,
 threeds_outcome_result in (
 'attempt_acknowledged',
 'authenticated',
 'delegated',
 'exempted'
 ) as threeds_succeeded
 from authentication_report_attempts
 where created between date'2021-10-29' and date'2021-11-03'
 and intent_type = 'setup'
 and is_threeds_triggered
)
select
 date_trunc('day', created) as day,
 1. * count_if(threeds_succeeded)
 / count(*) as authentication_rate__raw,
 2. * count_if(threeds_succeeded and is_final_attempt)
 / nullif(count_if(is_final_attempt), 0) as authentication_rate__deduped
from setup_attempts
group by 1
order by 1
```

dayauthentication_rate__rawauthentication_rate__deduped2021-10-290.590.802021-10-300.600.812021-10-310.590.812021-11-010.610.832021-11-020.620.83

## Links

- [full-page
documentation](https://dashboard.stripe.com/stripe-schema?tableName=authentication_report_attempts)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [SCA
exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)