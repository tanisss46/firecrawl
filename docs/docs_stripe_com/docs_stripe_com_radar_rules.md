# Fraud prevention rules

## Use fraud prevention rules to guard your business.

Fraud prevention rules allow you to take action whenever a payment matches
certain criteria.

Stripe Radar provides built-in rules to help detect and guard against fraud risk
for all Stripe users.

[Radar for Fraud Teams](https://docs.stripe.com/radar) users can use the
[Dashboard](https://dashboard.stripe.com/test/radar/rules) to create custom
rules based on the unique business logic specific to your business. For example,
you can:

- **Request 3D Secure** (3DS) for all payments that support it and are made by a
new customer
- **Allow** all payments from your call center’s IP address
- **Block** payments made from a location or card issued outside your country
- **Review** all payments greater than 1,000 USD that have been made with a
prepaid card

#### Caution

EU merchants might be affected by the [Geo-blocking
Regulation](https://support.stripe.com/questions/eu-geo-blocking-regulation-changes)
and its prohibitions on blocking payments from customers based in EU member
states.

## Built-in rules

The following rules are available by default for all Radar users.

### Machine learning risk checks

Stripe Radar and Stripe Radar for Fraud Teams provide a set of default rules
based on the judgments of our machine learning models, which are:

`Block if :risk_level: = 'highest'`

The rule blocks and won’t process payments with a high risk of fraud. This rule
is enabled by default for users of Radar or Radar for Fraud Teams.

`Review if :risk_level: = 'elevated'`

The default behavior for Stripe Radar for Fraud Teams is to place payments into
review that we suspect have an elevated risk of fraud.

### Traditional card checks

A payment can still succeed even when the
[CVC](https://docs.stripe.com/disputes/prevention/verification) or address
([AVS](https://docs.stripe.com/disputes/prevention/verification)) check fails
because issuers evaluate numerous signals when deciding to authorize a payment.
A card issuer might still consider a payment that fails CVC or postal code
verification legitimate, and therefore approve it.

You can enable Radar’s built-in rules to block certain payments that the card
issuer approved. When enabled, these rules also affect attaching a card to a
customer, and creating a customer, if you create the card and customer together.

CVC and AVS RulesLegacy CVC and AVS Rules
Effective December 17, 2024, the Dashboard shows these rules to new customers
and existing customers who haven’t used the legacy CVC or AVS rules.

`Block if CVC verification fails based on risk score`

Enable this rule to block payments that fail a card issuer’s CVC verification
check, unless Stripe evaluates it as low-risk. This rule doesn’t block payments
where the customer doesn’t provide the CVC number because they, for example, use
a [wallet](https://docs.stripe.com/payments/payment-methods), or their card’s
issuer doesn’t support its verification.

`Block if Postal code verification fails based on risk score`

Enable this rule to block payments that fail a card issuer’s postal code
verification check, unless Stripe evaluates it as low-risk. This rule doesn’t
block payments where the customer doesn’t provide the postal code, or their
card’s issuer doesn’t support its verification.

### Built-in rules to request 3D Secure

Using [3DS](https://docs.stripe.com/payments/3d-secure) prompts customers to
complete an additional authentication step before they can complete the purchase
flow. If 3DS authenticates a payment, the
[liability](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
for any fraud-related disputes for that payment typically shift from the seller
to the issuer. This means that in most cases, the seller isn’t responsible for
fraud costs on 3DS authenticated payments.

Stripe automatically handles soft decline codes indicating that 3DS is required
by issuers. We also trigger 3DS when necessary, adhering to regulations such as
the [Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication) (SCA)
mandated by the PSD2. Disabling Radar doesn’t prevent 3DS from being triggered
in cases where it’s necessary.

Stripe provides three default disabled rules you can enable to dynamically
request 3DS when using Radar with [Payment
Intents](https://docs.stripe.com/payments/accept-a-payment) or [Setup
Intents](https://docs.stripe.com/payments/save-and-reuse):

- `Request 3D Secure if 3D Secure is recommended for card`- Disabled by default.
Enabling this rule prompts the customer for 3DS authentication when Stripe
believes that 3DS authentication can take place with minimal impact on
conversion rates.
- Enable this if you want to maximize the number of payments that have liability
shift.
- `Request 3D Secure if 3D Secure is supported for card`- Disabled by default.
Enabling this rule prompts the customer for 3DS authentication as long as their
card supports it.
- Use this rule instead of the previous one if you want to maximize the number
of payments that have liability shift. Be aware that this additional requirement
might decrease conversion rates.
- `Request 3D Secure if 3D Secure is required for card` Deprecated- Enabling
this rule prompts the customer for 3DS authentication if the card historically
[required
3DS](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-cards).
- Regardless of this rule, Stripe automatically triggers 3DS:- If a soft decline
code indicates the issuer requires 3DS.
- In adherence to regulations such as PSD2’s [Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication)
mandate.

Because 3DS requires your customer to go through an additional layer of
authentication, indiscriminate use of 3DS might lower conversion rates.

Requesting 3DS doesn’t necessarily mean the issuer actually performs 3DS. For
more details about possible outcomes, refer to the [3D Secure
documentation](https://docs.stripe.com/payments/3d-secure).

#### Custom rules to request 3D Secure and act on specific outcomes

After attempting 3DS authentication, if you have [Radar for Fraud
Teams](https://stripe.com/radar/fraud-teams), you can evaluate the result in
allow, block, or review rules.

The most important attributes for custom Radar rules are:

- `is_3d_secure` which is true if the card is supported, 3DS was attempted by
the issuer and the user didn’t fail authentication. We generally recommend using
this in block rules.
- `is_3d_secure_authenticated` which is true if 3DS was attempted by the issuer
and the user successfully went through a full authentication. Using this
attribute in a block rule excludes legitimate transactions that might have an
SCA exemption or don’t fall into a clear failure or successful authentication
such as processing errors.
- `has_liability_shift` which is true if Stripe expects the payment to be
covered under the liability shift rule. This might [not always be the same as
3DS](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments),
for example Apple Pay in certain regions.

For custom rules, we recommend keeping `Request 3DS` and `Block` rules aligned
depending on your [risk
appetite](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data).
However, don’t block transactions where 3DS isn’t supported, such as some
wallets.

Here are some examples that show how to achieve this for different use cases:

#### Request 3D Secure based on Radar risk level

You want to use Radar to request 3DS on all charges based on Radar risk level
and above a certain amount.

Radar ruleDescription`Request 3D Secure if :risk_level: != 'normal' and
:amount_in_usd: > 25`This rule checks for Radar’s risk level then requests 3DS
on all charges with an elevated or high risk level above a certain amount.
In this case, without a block rule, cards or wallets that don’t support 3DS
aren’t blocked. 3DS attempts with failed authentication don’t continue to charge
authorization.

#### Always require 3D Secure based on Radar risk level

You want to use Radar to request 3DS on all charges based on Radar risk level of
elevated or high, and above a certain amount. If cards don’t support 3DS, you
don’t want to accept them.

Radar ruleDescription`Request 3D Secure if :risk_level: != 'normal' and
:amount_in_usd: > 25`This rule checks for Radar’s risk level then requests 3DS
on all charges with an elevated or high risk level above a certain amount.`Block
if not :is_3d_secure: and :risk_level: != 'normal' and :amount_in_usd: > 25 and
not :is_off_session: and :digital_wallet: != 'apple_pay' and not
(:digital_wallet: = 'android_pay' and :has_cryptogram:)`This rule blocks
payments without a 3DS flow for charges with an elevated or high risk level
above a certain amount. However, it accepts legitimate transactions that might
have an SCA exemption or don’t have a clear failure or successful authentication
such as `attempt_acknowledged`. It accepts off-session payments such as
recurring subscription charges and wallets such as Apple Pay or Google Pay to
succeed.
#### Only accept fully 3D Secure authenticated transactions if 3D Secure is supported

You rely on Stripe triggering 3DS when necessary in cases such as [Strong
Customer
Authentication](https://stripe.com/guides/strong-customer-authentication) (SCA),
but don’t want to accept [edge
cases](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result)
such as processing errors.

Radar ruleDescription`Block if :is_3d_secure: and not
:is_3d_secure_authenticated:`This rule blocks payments where the card is
enrolled in 3DS and 3DS was attempted but the user didn’t successfully
authenticate. Cards that don’t support 3DS, SCA exemptions, off-session payments
(such as recurring subscription charges), and wallets (such as Apple Pay or
Google Pay) are accepted.
#### Request 3D Secure based on Metadata

You want to use Radar to request 3DS on all charges with a custom metadata
attribute.

Radar ruleDescription`Request 3D Secure if ::foo:: = 'bar'`This rule checks for
a metadata condition and then requests 3DS. To check Customer metadata, replace
`::foo:: = 'bar'` with a value like `::customer:trusted:: = 'false'`.
In this case, without a block rule, cards or wallets that don’t support 3DS
aren’t blocked. 3DS attempts with failed authentication don’t continue to charge
authorization.

#### Always require 3D Secure based on Metadata

You want to use Radar to request 3DS on all charges with a custom metadata
attribute and block cards that don’t support it.

Radar ruleDescription`Request 3D Secure if ::foo:: = 'bar'`This rule checks for
a metadata condition and then requests 3DS. To check Customer metadata, replace
`::foo:: = 'bar'` with a value like `::customer:trusted:: = 'false'`.`Block if
::foo:: = 'bar' and not :is_3d_secure and not :is_off_session: and
:digital_wallet: != 'apple_pay' and not(:digital_wallet: = 'android_pay' and
:has_cryptogram:)`This rule blocks payments without a 3DS flow for charges with
a custom metadata attribute. However, it accepts legitimate transactions that
might have an SCA exemption or don’t have a clear failure or successful
authentication such as `attempt_acknowledged`. It accepts off-session payments
(such as recurring subscription charges), and wallets (such as Apple Pay or
Google Pay) to succeed.
#### Request 3D Secure for all new cards and review if 3D Secure wasn’t supported

You want to use Radar to request 3DS on all new cards and manually review
charges from cards that don’t support 3DS.

Radar ruleDescription`Request 3D Secure if
is_missing(:seconds_since_card_first_seen:)`This rule requests 3DS on all cards
that haven’t been used on your account. To reduce user friction, you can add an
additional condition to only request 3DS if `:risk_level: != 'normal'`.`Request
3D Secure if :is_new_card_on_customer:`As an alternative to the rule above, this
rule requests 3DS on all cards that are newly used on a
[Customer](https://docs.stripe.com/api/customers). To reduce user friction, you
can add an additional condition to only request 3DS if `:risk_level: !=
'normal'`.`Review if not :is_3d_secure and not:is_off_session: and
:digital_wallet: != 'apple_pay' and not(:digital_wallet: = 'android_pay' and
:has_cryptogram:)`This rule marks payments where 3DS is expected but isn’t
supported for manual review. It ignores off-session payments (such as recurring
subscription charges) and wallets (such as Apple Pay or Google Pay). Payments
marked for review continue to authorization and can give additional signals,
such as issuer CVC checks.
In this case, without a block rule, cards or wallets that don’t support 3DS
aren’t blocked. 3DS attempts with failed authentication don’t continue to charge
authorization.

#### Always require 3D Secure for certain issuer countries

You want to use Radar to request 3DS on all charges from card issuers
originating from countries on a [custom
list](https://docs.stripe.com/radar/lists) and block cards that don’t support
it.

Radar ruleDescription`Request 3D Secure if :card_country: in
@enforce_3ds_list`This rule checks for a condition based on card issuers
originating from countries and compares them to a [custom
list](https://docs.stripe.com/radar/lists). If they match, it requests
3DS.`Block if :card_country: in @enforce_3ds_list and not :is_3d_secure and not
:is_off_session: and :digital_wallet: != 'apple_pay' and not(:digital_wallet: =
'android_pay' and :has_cryptogram:)`This rule blocks payments without a 3DS flow
for charges originating from countries on the custom list. However, it accepts
legitimate transactions that might have an SCA exemption or don’t have a clear
failure or successful authentication, such as `attempt_acknowledged`. It accepts
off-session payments (such as recurring subscription charges) and wallets (such
as Apple Pay or Google Pay) to succeed.
#### Always require 3D Secure based on Radar risk level and review edge cases

You want to use Radar to request 3DS on all charges based on Radar risk level
and block cards that don’t support 3DS, but manually review edge cases.

Radar ruleDescription`Request 3D Secure if :risk_level: != 'normal'`This rule
checks for Radar’s risk level then requests 3DS on all charges with an elevated
or high risk level above a certain amount.`Block if not :is_3d_secure: and
:risk_level: != 'normal' and not :is_off_session: and :digital_wallet: !=
'apple_pay' and not (:digital_wallet: = 'android_pay' and :has_cryptogram:)`This
rule blocks payments without a 3DS flow for charges with an elevated or high
risk level above a certain amount. However, it accepts legitimate transactions
that might have an SCA exemption. It accepts off-session payments (such as
recurring subscription charges) and wallets (such as Apple Pay or Google Pay) to
succeed.`Review if not :is_3d_secure_authenticated: and :risk_level: != 'normal'
and not :is_off_session: and :digital_wallet: != 'apple_pay' and not
(:digital_wallet: = 'android_pay' and :has_cryptogram:)`This rule marks payments
for manual review that were using 3DS, but didn’t result in a fully
authenticated flow. This would review [edge
cases](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result)
such as `attempt_acknowledged` and would also mark legitimate payments despite
SCA exemptions. Because review rules are evaluated after block rules, cards that
don’t support 3DS are blocked.
## When to create rules

Stripe’s default rules can block a substantial number of fraudulent payments.
Businesses that need more control over which payments they want to review,
allow, or block can write custom rules through Radar for Fraud Teams.

Consider the following when deciding whether to enable custom rules:

- Whether you see certain features or user behaviors as more risky (for example,
use of a disposable email).
- Whether you want to implement rules based on payment amounts or perceived risk
level (for example, automatically review if the payment is over 500 USD,
automatically allow if the payment is under 5 USD).
- Whether your existing disputed and refunded payments share any common patterns
(for example, similar amounts, card types, or countries).
- Whether you have existing rules you want to migrate to Stripe—many of these
rules might already be covered by Stripe’s machine learning models, and you can
check how our system performs for your business before customizing it.

### How to create effective rules

While rules can help you automate your existing workflows, they can also
negatively affect your business if used incorrectly. For example, a rule can
automatically allow a large number of payments that are fraudulent or block a
large number of legitimate payments if it’s not set up properly.

Keep the following in mind while setting up rules:

- Rules only apply to future payments and don’t apply to any that you’ve already
processed.
- Request 3DS rules only apply when using [Stripe
Checkout](https://docs.stripe.com/payments/checkout), [Payment
Intents](https://docs.stripe.com/payments/accept-a-payment), or [Setup
Intents](https://docs.stripe.com/payments/save-and-reuse), and are evaluated
before review, block, and allow rules.
- Before implementing any block rule to block all payments that meet its
criteria, consider whether you’d rather review such payments first.
- Implement allow rules minimally, because they override Stripe’s default rules
along with any other custom rules that match the same criteria.
- You can create a maximum of 200 rules across all rule types per account.

## Construct rules

You can add and manage rules from the [Rules tab of the Radar
page](https://dashboard.stripe.com/test/radar/rules) in the Dashboard.

To add a new rule:

- Click **+ Add rule**.
- Choose the type rule type from the sub-menu.
- In the rule editor, construct a rule using the syntax `{action} if {attribute}
{operator} {value}` where:- `{action}`: How Radar responds when the rule
criteria is met. This value is pre-populated based on the rule type selection
you chose.
- `{attribute}`: The element of the transaction to evaluate, such as the amount
or card type. Begin typing with `:` to open a list of valid attributes. You can
also evaluate your custom metadata by enclosing it in double colons, for
example, `::product_sku::`.
- `{operator}`: How to compare the attribute to the value, such as `=`, `>`,
`!=`, and so on.
- `{value}`: The value of the attribute to evaluate.
- Click **Test rule**.
- Correct any detected validation errors, if necessary.
- On the **Review new rule** page, review how this rule performs against your
recent transactions to confirm whether you want to enable it.
- Click **Add rule** to begin applying this rule to all future transactions.

### Use Radar Assistant

Stripe’s rule editor has a built-in LLM assistant that constructs a Radar rule
from a natural language prompt.

To use Radar Assistant:

- From the [Rules tab of the Radar
page](https://dashboard.stripe.com/test/radar/rules) in the Dashboard, click **+
Add rule**.
- Choose rule type from the sub-menu.
- In the rule editor, click **Radar Assistant**.

![Manual rule
writing](https://b.stripecdn.com/docs-statics-srv/assets/manual-rule-writing-view.598ac04a039b6222f5f7b46e14a74204.png)

Manual rule writing

![Radar
assistant](https://b.stripecdn.com/docs-statics-srv/assets/radar-assistant-view.4b7580fb9a503ae6df62990b4dea0a68.png)

Radar Assistant

- In the message field, enter your rule request. You might ask to:- *Review
payments where the card and IP countries are different.*
- *Block Discover card payments of more than $1000.*
- *Allow payments from stripe.com email addresses.*
- When the Assistant returns its suggestion, you can either enter an additional
command to make adjustments to the rule or you can click **Test rule** to see
how the rule performs against your recent transaction history.
- When you’re satisfied with the rule, click **Add rule** to enable it for all
future transactions.

**Training data consent:** By using Radar Assistant you agree that Stripe can
log and use your chat entries to train and improve the Radar Assistant
capabilities. If you don’t want to have your chat entries used for this purpose,
write rules manually.

Learn more about [Stripe AI
services](https://support.stripe.com/questions/use-of-artificial-intelligence-(ai)-in-stripe-services).

### Review rules

Stripe still processes payments normally when they meet a review rule’s
criteria. But we place them into your [review
queue](https://dashboard.stripe.com/test/radar) so your team can look at them
more closely. Setting up a rule that’s too broad can result in too many payments
being placed into your review queue, slowing down your customers and burdening
your review team.

Stripe’s rule testing interface runs a simulation on the last 6 months of
charges to determine how many legitimate, fraudulent, and blocked payments would
have been affected by the rule, had it been implemented. While testing a rule
and examining the last 6 months, make sure that:

- **Overall volume of payments is low**. Reviewing these payments shouldn’t
create a burden to your team.
- **Human reviewers add value**. A human reviewer can generally identify if a
payment was fraudulent with greater confidence than the automated system.
- **The rule results in a mix of successful and refunded or disputed payments**.
This means that additional inspection on these types of payments can help
separate legitimate payments from those that are fraudulent.

The following is an example of how to improve a review rule created by a
business that wants to review pre-paid credit cards.

Original ruleImproved rule`Review if :card_funding: = 'prepaid'``Review if
:is_disposable_email: and :card_funding: = 'prepaid'`Too broad—results in too
many reviewsMore focused—results in a smaller number of reviews
### Block rules

You can use block rules to block payments that you’re confident are fraudulent,
or based on any restrictions your business has in place (such as blocking
payments from prepaid cards). If you’re not sure how to apply block rules, we
recommend placing payments in review using a review rule. After spending some
time reviewing these payments for potential false positives, you can confirm
whether you want to create a block rule instead.

Block rules only impact fraudulent and successful payments, because
already-blocked payments are unaffected. While testing a rule, make sure that
you:

- **Keep false positives as low as possible**. During testing, Stripe identifies
the number of successful and disputed payments that would’ve been matched by the
rule. A good block rule results in significantly more fraudulent payments
blocked than legitimate payments.
- **Minimize unnecessary rules**. If your rule appears to perform very well but
is already covered by an existing rule, your newer rule might not be necessary.
Similarly, if the results during testing appear to be mixed, consider setting up
a review rule instead so you can gather more information about those types of
payments.

The following is an example of how to improve a block rule created by a business
that’s suffering from a high level of fraud from payments outside the US:

Original ruleImproved rule`Block if :card_country: != 'US'``Block if
:card_country: != 'US' and :risk_level: = 'elevated'`Too broad—high number of
legitimate payments blockedMore focused—results in a smaller number of reviews
### Allow rules

Allow rules override all of your other rules, so use them with caution. Many
businesses might not need to implement allow rules. If you have concerns that an
allow rule could let through even a small number of fraudulent payments,
consider adjustments to further restrict these rules before implementing them.

Allow rules apply to all new payments as soon as you create the rule. This
includes any payments that are similar to previously blocked payments. While
testing a rule, make sure that you:

- **Examine the number of previously blocked payments that would have been
allowed**. Allow rules override all other rules and Stripe’s risk assessment.
When testing a new allow rule, all of the payments shown would have been allowed
if this rule were active. This can include payments that had been blocked or
disputed, impacting your future dispute rates.
- **Continue to block any high-risk payments**. You can do this by adding the
following to any allow rule: `and :risk_level: != 'highest'`
- **Evaluate a history of legitimate transactions at your business**. You can
analyze connections between your own customers to allow a higher volume of
transactions based on a history of legitimate purchases. This helps you block
fewer payments from customers that have a proven history at your business. To do
this, review the [attributes
list](https://docs.stripe.com/radar/rules/reference#supported-attributes) and
look for attributes that include the word “customer.”

The following is an example of how to improve an allow rule for a business that
generally (but not always) sees good payments coming from customers in the
United Kingdom:

Original ruleImproved rule`Allow if :ip_country: = 'GB'``Allow if :ip_country: =
'GB' and :risk_level: != 'highest'`Too broad—some fraudulent payments are
allowedMore focused—a smaller number of fraudulent payments are allowed
## Maintaining your rules

As your business continues to grow, you want to be sure that your rules continue
to reflect the types of customers that you want to do business with. The
following are some best practices to keep rules current for the state of your
business.

### Regularly monitor rules to ensure they’re still effective

#### Rule metrics

Fraud patterns constantly change, so we provide
[metrics](https://dashboard.stripe.com/settings/radar/rules) to show how these
rules are performing. These metrics vary depending on the type of rule, because
the rule types perform different actions.

!

Use the **rule performance chart** to understand the behavior of your Radar
rules. Look for unexpected spikes or declines in the number of payments matching
your rules, such as allow rules letting too many payments through or block rules
blocking too many. These spikes may indicate a change in the types of payments
your business is receiving or that might warrant updates to the rules
themselves. Updates made to rules are displayed as triangles on the graph and
can help you compare the impact of the change before and after you make it.

**Color-coded lines** track the number of payments that match
[3DS](https://docs.stripe.com/issuing/3d-secure) rules, allow rules, block
rules, and review rules. **Triangular symbols** on these graph lines represent
updates to rules of the corresponding type.

You can find information about the effectiveness of your rules and see how many
payments each one has taken action against. You can also view and download a
filtered list of every payment that a rule has been applied to. Evaluate this
information to help you decide if you need to make changes to any rules or
remove them entirely.

To view additional commands, click the overflow menu () menu. Additional
commands include: **Disable**, **Enable**, **Edit** or **Delete** for any rule.

You can also use our reporting products Sigma and Data Pipelines to [query
disputes and fraud
data](https://docs.stripe.com/stripe-data/query-disputes-and-fraud-data),
including rule decisions and attributes for each individual payment.

#### Evaluate rule effectiveness

You can find information about the effectiveness of your rules and see how many
payments each one has affected. You can also view and download a filtered list
of every payment that a rule has been applied to. Review the sample questions in
the following table to help you decide if you need to make changes to any rules
or remove them entirely.

Rule TypeEvaluateActions to considerGeneralIf this rule no longer match any
payments at allRemove the rule.If this rule has anomalous behavior, such as
allowing more payments than in previous time periods.Manually review payments
that matched this rule to determine if this is the behavior that you want.3DSIf
3DS completion rate is high, but the number of disputes or EFWs is low.Remove
the rule since you may be issuing friction to good users.If fraud is high for
transactions that pass 3DS.Consider modifying your 3DS rule into a block rule to
prevent these users from passing frictionless flow (controlled by issuers) or
committing first party fraud.If the conversion rate for 3DS is low.This might be
a good rule since it might be mostly blocking fraudsters, but consider manually
investigating matched payments to make sure your good users aren’t abandoning
due to additional friction.AllowIf the number of disputes, EFWs, Refunds, or
Failed payments are high.Remove the rule that allows bad payments
through.BlockIs the number of blocks going down, but your fraud is still steady
or is increasing?Modify your rule because it might no longer be effective.If the
number of blocks is going up, but your fraud is still steady or
increasing.Modify your rule since it might be blocking good users.If the number
of blocks is going up and your fraud is going down.This suggests that your rule
is effective, but consider manually reviewing a few transactions to make sure
that you’re not blocking too many good users.Manual ReviewIf the percentage of
payments that get reviewed is low.Make the rule more restrictive since it might
be too broad.If the number of successful or approved payments is high.Remove the
manual review rule entirely or write an allow rule to target those payments.If
the number of refunds or disputes and Early Fraud Warnings are high.Convert to a
block rule.
**Request 3DS rules**

For request 3DS rules, we display:

- **3DS Requested**—the number of times a rule triggered a 3DS request.

Click a 3DS rule to see the following metrics:

!

**Allow rules**

For allow rules, Radar for Fraud Teams users can view:

- **Allowed payments**—The total number of payments allowed by your rules.
- **Volume, allowed payments**—The total amount, in your local currency,
associated with payments allowed by your rules.
- **Risk score**—The corresponding [risk
outcomes](https://docs.stripe.com/radar/risk-evaluation#risk-outcomes) assigned
by Stripe machine learning models to the set of payments allowed by your rules.
- **Disputes from overrides**—The total number of allowed payments that were
disputed.
- **Volume, disputes from overrides**—The total amount, in your local currency,
associated with disputes from allowed payments.

Click an Allow rule to see the following metrics:

!

**Block rules**

For block rules, we display:

- **Blocked payments**—The total number of payments blocked by your rules.
- **Volume, blocked payments**—The total amount, in your local currency,
associated with payments blocked by your rules.

Radar for Fraud Teams users can also view:

- **Risk score**—The corresponding [risk
outcomes](https://docs.stripe.com/radar/risk-evaluation#risk-outcomes) assigned
by Stripe machine learning models to the set of payments allowed by your rules.
- **Est. false positive rate**—The estimated percentage of non-fraudulent
payments that were blocked for both your block rules as a set and by individual
rules. (These estimates are made using the estimated false positive rates of the
corresponding machine learning risk scores, which we calculate with experiments
across the Stripe network.)
- **Est. fraudulent payments prevented**—The estimated number of fraudulent
payments that your block rules prevented. Stripe uses machine learning risk
scores, calculated by analyzing millions of transactions across the Stripe
network, to predict payments with a high probability of being disputed or
declined due to fraud and estimate which of those payments were successfully
blocked by your rules.

Click a Block rule to see the following metrics:

!

**Review rules**

For review rules, Radar for Fraud Teams users can view:

- **Payments sent to review**—The total number of payments that were sent to
manual review by your rules.
- **Volume, approved reviews**—The total amount, in your local currency,
associated with approved payment reviews.
- **Refund rate**—The percentage of reviews that were refunded.
- **Disputes from approved reviews**—The total number of payments that were
approved in your review, but were ultimately disputed.
- **Volume, disputes from approved reviews**—The total amount, in your local
currency, associated with disputes from approved payment reviews.

Click a Review rule to see the following metrics:

!

### Regularly monitor your manual review queue

If your review queue is getting too large to manage, check to see if you have
the right rules in place. If most reviews end up being refunded as fraudulent,
consider some additional rules to block payments. Likewise, if most payments are
approved, consider making your review rules more focused.

### Analyze your disputed and refunded payments

[Disputes](https://docs.stripe.com/disputes) are inherently linked to fraud, so
the more you do to reduce fraud, the lower your dispute rate. Check to see if
disputed payments share any similar characteristics (for example, from the same
locations or of similar amounts). You can also perform this type of
investigation by looking at payments that have been refunded during a review. If
you see trends, you can test and create the appropriate rules. If any payments
appear to be fraudulent, refund and report them as fraud to avoid potential
disputes.

You can also use our reporting products, Sigma and Data Pipeline, to [query
disputes and fraud
data](https://docs.stripe.com/stripe-data/query-disputes-and-fraud-data).

You can respond to any incoming disputes using the Dashboard or through the API,
and our [dispute documentation](https://docs.stripe.com/disputes) includes some
suggestions on how to present a well documented case.

### Anticipate large changes to your business that might impact your fraud rate

If you’re planning any major product releases or changes to your service (for
example, a new, high-value product or expanding your service into new
countries), you might want to monitor these payments in the beginning. For these
kinds of changes, it’s a good practice to set up some review rules so you can
examine any new payments. Reviewing these payments and identifying patterns can
help you set up new rules to protect your business from fraud.

## See also

- [3DS Rule Examples](https://docs.stripe.com/radar/rules#request-3d-secure)
- [Continuous Fraud Management
Guide](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [Query Disputes and Fraud
Data](https://docs.stripe.com/stripe-data/query-disputes-and-fraud-data)
- [Rules Reference](https://docs.stripe.com/radar/rules/reference)
- [Supported
Attributes](https://docs.stripe.com/radar/rules/supported-attributes)

## Links

- [Radar for Fraud Teams](https://docs.stripe.com/radar)
- [Dashboard](https://dashboard.stripe.com/test/radar/rules)
- [Geo-blocking
Regulation](https://support.stripe.com/questions/eu-geo-blocking-regulation-changes)
- [CVC](https://docs.stripe.com/disputes/prevention/verification)
- [wallet](https://docs.stripe.com/payments/payment-methods)
- [3DS with Stripe
Billing](https://docs.stripe.com/billing/migration/strong-customer-authentication)
- [3DS](https://docs.stripe.com/payments/3d-secure)
-
[liability](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
- [Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication)
- [Payment Intents](https://docs.stripe.com/payments/accept-a-payment)
- [Setup Intents](https://docs.stripe.com/payments/save-and-reuse)
- [required
3DS](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-cards)
- [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)
- [risk
appetite](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [edge
cases](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result)
- [Customer](https://docs.stripe.com/api/customers)
- [custom list](https://docs.stripe.com/radar/lists)
- [team
members](https://support.stripe.com/questions/can-i-invite-other-team-members-or-my-developer-to-use-my-stripe-account)
- [team settings](https://dashboard.stripe.com/settings/team)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Stripe AI
services](https://support.stripe.com/questions/use-of-artificial-intelligence-(ai)-in-stripe-services)
- [review queue](https://dashboard.stripe.com/test/radar)
- [contact us](https://support.stripe.com/contact)
- [attributes
list](https://docs.stripe.com/radar/rules/reference#supported-attributes)
- [metrics](https://dashboard.stripe.com/settings/radar/rules)
- [3DS](https://docs.stripe.com/issuing/3d-secure)
- [query disputes and fraud
data](https://docs.stripe.com/stripe-data/query-disputes-and-fraud-data)
- [risk outcomes](https://docs.stripe.com/radar/risk-evaluation#risk-outcomes)
- [Disputes](https://docs.stripe.com/disputes)
- [3DS Rule Examples](https://docs.stripe.com/radar/rules#request-3d-secure)
- [Rules Reference](https://docs.stripe.com/radar/rules/reference)
- [Supported
Attributes](https://docs.stripe.com/radar/rules/supported-attributes)