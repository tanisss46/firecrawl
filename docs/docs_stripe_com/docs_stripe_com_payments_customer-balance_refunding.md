# Refund bank transfer payments

## Refund payments made with bank transfers, or refund a customer’s available cash balance.

You can refund customer balance payments through the
[Dashboard](https://dashboard.stripe.com/payments) or
[API](https://docs.stripe.com/api#create_refund).

## Refund a payment to the customer

Stripe requires customer bank account details to process the refund. In some
cases, Stripe receives the customer’s bank account details when performing the
transfer. Stripe emails the customer to let them know that the refund is in
process.

When we can’t determine the destination bank account automatically due to
unavailable or ambiguous customer bank account information, Stripe requests it
by contacting the customer at the email address in the customer object you
created. If you didn’t include an email address when you created the customer
object, creating a refund results in an error. Update the customer object with a
valid email address for the customer, and try creating the refund again. You can
specify a new email address when you create a refund.

In some cases, Stripe performs additional checks before processing a refund or
asking your customers for bank account information. Stripe contacts you if we
require more information before finalizing the refund.

Customers have 45 days from receipt of the request to submit bank account
details. After 45 days without a valid response, Stripe cancels the refund and
returns the funds to the customer’s account cash balance. We recommend you then
contact your customer to discuss alternative ways of returning the funds.

You can refund a payment up to 180 days after it was created.

### Creating a payment refund using the Dashboard

- To refund a payment made with a bank transfer, navigate to the payment page
and click **Refund**.

!

- In the following dialog, enter the amount you want to refund, if different
than the full payment amount, and any other details about the refund. Then click
**Refund**.

### Creating a payment refund using the API

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={{PAYMENT_INTENT_ID}} \
 --data-urlencode instructions_email="customeremail@example.com"
```

Refunds are sent to the customer’s bank account, and the customer receives a
notification at their default email address. If you want to override the default
email address used to contact the customer, specify the new email address using
the
[instructions_email](https://docs.stripe.com/api/refunds/object#refund_object-instructions_email)
parameter.

The refund’s status transitions as follows:

EventRefund statusRefund is created`requires_action`Customer submits bank
account details, and Stripe begins processing the refund`pending`Refund is
expected to arrive in customer’s bank`succeeded`Customer’s bank returns the
funds back to Stripe`requires_action`Refund is in `requires_action` 45 days
after creation`failed`Refund is canceled from a `requires_action`
state`canceled`
If the customer’s bank can’t successfully complete the transfer, the funds are
returned to Stripe and the refund transitions to `requires_action`. This can
happen if the account holder’s name doesn’t match what the recipient bank has on
file or if the provided bank account number has a typo. In these cases, Stripe
emails the customer to inform them of the failure and to request that they
resubmit their bank account details.

If your customer doesn’t provide their bank account details within 45 days, the
refund’s status transitions to `failed` and we send the
[refund.failed](https://docs.stripe.com/api/events/types#event_types-refund.failed)
event. This means that Stripe can’t process the refund, and you must [return the
funds to your customer outside of
Stripe](https://docs.stripe.com/refunds#failed-refunds).

The
[instructions_email](https://docs.stripe.com/api/refunds/object#refund_object-instructions_email)
field on the refund is the email that the refund was sent to. While a refund is
waiting for a response from the customer, details of the email sent to the
customer can also be found under the
[next_action.display_details.email_sent](https://docs.stripe.com/api/refunds/object#refund_object-next_action-display_details-email_sent)
field on the refund.

Each individual refund (including each partial refund) may incur a fee. Please
reach out to your point of contact at Stripe to learn more about this.

## Cancel a payment refund sent to the customer

If a bank transfer payment refund has been sent to the customer, and the
customer hasn’t submitted their bank details, you can still cancel the refund.

### Canceling a payment refund using the Dashboard

- To cancel a refund for a bank transfer payment, navigate to the payment page
and click **Cancel refund**.

!

- If the payment has multiple partial refunds in the `requires_action` state,
select the correct refund from the **Refund** dropdown in the following dialog.
- Confirm the cancellation by selecting **Cancel refund** in the dialog.

### Canceling a payment refund using the API

```
curl https://api.stripe.com/v1/refunds/{{REFUND_ID}}/cancel \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X POST
```

After the payment refund has been canceled, the refund transitions from
`requires_action` to `canceled`. If there are no other refunds, the payment
transitions back to its original pre-refund state.

## Refund a payment to the customer’s cash balance

A refund to the customer balance succeeds immediately. Refunds to the customer
balance are free of charge.

### Creating a payment refund using the Dashboard

- To refund a payment made with a bank transfer, navigate to the payment page
and click **Refund**.

!

- In the following dialog, select **Customer balance** in the **Destination**
dropdown. Selecting this option deposits the refund into the customer’s Stripe
account, which allows them to use the funds for future payments on your site.

## Refund the cash balance to the customer

You can return a customer’s cash balance directly to them. For example, you
might need to do this when a customer transfers more funds than expected for a
payment.

### Refund a customer’s cash balance using the Dashboard

- Navigate to the [Customer list](https://dashboard.stripe.com/customers) page.
- Click the customer in the list of customers.
- Expand the **Cash Balance** row in the **Payment methods** section.
- Click **Initiate Refund** button at the end of the row.

!

- In the next dialog, enter the amount to refund.
- Click **Initiate Refund**.

View the status of the refund on the customer balance transactions list page.

### Refund a customer’s cash balance using the API

To refund a customer’s cash balance with the API, set the
[origin](https://docs.stripe.com/api/refunds/object#refund_object-origin)
parameter to `customer_balance` and specify the
[customer](https://docs.stripe.com/api/refunds/object#refund_object-customer).
The customer’s default email address is used to contact them. To override it,
specify the new email address using the
[instructions_email](https://docs.stripe.com/api/refunds/object#refund_object-instructions_email)
parameter.

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d customer={{CUSTOMER_ID}} \
 --data-urlencode instructions_email="jenny.rosen@example.com" \
 -d origin=customer_balance
```

## Cancel a cash balance refund sent to the customer

You can only cancel un-processed refunds. After the customer submits their bank
account details, you can’t cancel a refund. Currently, you must use the Stripe
Dashboard to cancel a refund:

- Navigate to the [Customer list](https://dashboard.stripe.com/customers) page.
- Click the customer in the list of customers.
- Expand the **Cash Balance** row in the **Payment methods** section.
- Click the **View balance details** link.

!

- Click the overflow menu (**•••**) next to the refund you want to cancel and
click the **Cancel** link

!

The refund amount is credited back to the available cash balance.

## Track state of a refund

You can track the state of a refund through the
[Dashboard](https://dashboard.stripe.com/payments) or
[API](https://docs.stripe.com/api/refunds).

### When and where refund email is sent

Stripe sends an email to the email address provided in the
[instructions_email](https://docs.stripe.com/api/refunds/object#refund_object-instructions_email)
field on the refund. While a refund is waiting for a response from the customer,
you can also check the refund’s
[next_action.display_details.email_sent](https://docs.stripe.com/api/refunds/object#refund_object-next_action-display_details-email_sent)
field for details such as the sent time and the address. The sent time is also
the time when the refund transitioned to the `requires_action` state.

### Pending refunds

If the customer has submitted their bank account details, the refund transitions
to `pending`.

### Successful refunds

The refund transitions to `succeeded` when the refund is successfully paid out
to the customer.

## Test refunds

You can test refund behavior in a sandbox using the following test bank accounts
on the bank account details collection page linked in the email sent to the
customer. Bank account details outside of these test bank accounts won’t be
accepted.

#### Note

In a sandbox, refund instruction emails are only sent to email addresses linked
to the Stripe account.

IBANJapanMexicoUnited KingdomUnited States
Specify the appropriate [country
code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
(for example, GB, IL, CR, and so on) to test IBANs for any IBAN country and any
valid currency for that country. For instance, the following IBANs specify
Germany with the `DE` prefix.

NumberType`DE89370400440532013000`Refund succeeds.
`DE62370400440532013001`

`DE89370400440532013002`

`DE89370400440532013003`

`DE89370400440532013004`

`DE89370400440532013005`

Refund fails.

#### Testing Refunds Expiry

You can make an API call to simulate the expiry of a testmode refund.

```
curl https://api.stripe.com/v1/test_helpers/refunds/{{REFUND_ID}}/expire \
 -X POST \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

## Links

- [Dashboard](https://dashboard.stripe.com/payments)
- [API](https://docs.stripe.com/api#create_refund)
-
[instructions_email](https://docs.stripe.com/api/refunds/object#refund_object-instructions_email)
-
[refund.failed](https://docs.stripe.com/api/events/types#event_types-refund.failed)
- [return the funds to your customer outside of
Stripe](https://docs.stripe.com/refunds#failed-refunds)
-
[next_action.display_details.email_sent](https://docs.stripe.com/api/refunds/object#refund_object-next_action-display_details-email_sent)
- [Customer list](https://dashboard.stripe.com/customers)
- [origin](https://docs.stripe.com/api/refunds/object#refund_object-origin)
- [customer](https://docs.stripe.com/api/refunds/object#refund_object-customer)
- [API](https://docs.stripe.com/api/refunds)
- [country
code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)