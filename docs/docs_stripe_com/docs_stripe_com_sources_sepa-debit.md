# SEPA Direct Debit payments with Sources

## Use Sources to accept payments using SEPA Direct Debit, a popular European banking payment method.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with SEPA Direct Debit using the Sources
API, you must [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about integrating SEPA Direct Debit with the current APIs, see
[SEPA Direct Debit payments](https://docs.stripe.com/payments/sepa-debit).

Stripe users in Europe and the United States can use
[Sources](https://docs.stripe.com/sources)—a single integration path for
creating payments using any supported method—to accept SEPA Direct Debit
payments from customers in countries within the [Single Euro Payments
Area](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area).

During the payment process, your integration collects your customer’s
EUR-denominated
[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) bank
account information. SEPA Direct Debits require the bank account holder to
accept a
[mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate)
(debit authorization) that allows you to debit their account. A `Source` object
is then created and your integration uses this to make a charge request and
complete the payment.

Within the scope of Sources, SEPA Direct Debit is a
[pull](https://docs.stripe.com/sources#pull-or-push-of-funds)-based,
[reusable](https://docs.stripe.com/sources#single-use-or-reusable) and
[asynchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
method of payment. This means that you take action to debit the amount from the
customer’s account. It can take up to 14 business days to confirm the success or
failure of a payment.

#### Caution

SEPA direct debit transactions have a limit of 10,000 EUR each. For new users,
there’s an additional weekly limit of 10,000 EUR, which quickly increases as you
process more SEPA direct debit payments. If you need higher limits, please
[contact support](https://support.stripe.com/contact).

## Prerequisite: Collect mandate acceptance

Before a source can be created, your customer must accept the [SEPA Direct Debit
mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate).
Their acceptance authorizes you to collect payments for the specified amount
from their bank account using SEPA Direct Debit.

When your customer confirms the payment they’re making, they’re also accepting a
mandate. Their acceptance authorizes you to collect payments for the specified
amount from their bank account via SEPA Direct Debit. You must display the
following standard authorization text, replacing **Rocketship Inc.** with your
company name, close to the payment confirmation button so that your customer can
read and accept it.

#### Caution

By providing your IBAN and confirming this payment, you authorise (A) Rocketship
Inc. and Stripe, our payment service provider, to send instructions to your bank
to debit your account and (B) your bank to debit your account in accordance with
those instructions. You are entitled to a refund from your bank under the terms
and conditions of your agreement with your bank. A refund must be claimed within
8 weeks starting from the date on which your account was debited.

The details of the accepted mandate is generated as part of the `Source` object
creation. A URL to view the mandate is returned as the value for
`sepa_debit[mandate_url]`. Since this is the mandate that the customer has
implicitly signed when accepting the terms suggested above, it must be
communicated to them, either on the payment confirmation page or by email.

[Create a Source
object](https://docs.stripe.com/sources/sepa-debit#create-source)
Bank account information is sensitive by nature. To securely collect your
customer’s IBAN details and create a source, use
[Stripe.js](https://docs.stripe.com/payments/elements) and the [IBAN
Element](https://docs.stripe.com/payments/sepa-debit). This prevents your
customer’s bank account information from touching your server and reduces the
amount of sensitive data that you need to handle securely.

Follow the [IBAN Element
Quickstart](https://docs.stripe.com/payments/sepa-debit) to create your payment
form, collect your customers’ IBAN, and create a source. Once you’ve created a
source object, you can proceed to charge the source in the next step.

### Custom client-side source creation

If you choose to handle bank account numbers yourself, you can create your own
form and call `stripe.createSource` as described in the [Stripe.js
reference](https://docs.stripe.com/js#stripe-create-source). When doing so, make
sure to collect the following information from your customer:

ParameterValue`type`sepa_debit`currency`eur (bank accounts used for SEPA Direct
Debit must always use Euros)`sepa_debit[iban]`The IBAN number for the bank
account that you wish to debit, collected by the IBAN Element. For custom
integrations, you must collect this yourself and include it in when calling
`stripe.createSource`.`owner[name]`The full name of the account
holder.`owner[address]`Address of the account holder. Required only for IBANs
with these country codes: AD, PF, TF, GI, GB, GG, VA, IM, JE, MC, NC, BL, PM,
SM, CH, WF. Required sub-fields: `country` and `line1`. See the [Sources
API](https://docs.stripe.com/api/sources/create#create_source-owner-address)
reference for a complete list of address sub-fields.
### Server-side source creation

Use Stripe.js to create a SEPA Direct Debit source. Although doing so is
optional, if you forgo this step and pass the information directly to Stripe
when creating a `Source` object, you must take appropriate steps to safeguard
the sensitive bank information that passes through your servers.

```
curl https://api.stripe.com/v1/sources \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=sepa_debit \
 -d "sepa_debit[iban]"=DE89370400440532013000 \
 -d currency=eur \
 -d "owner[name]"="Jenny Rosen" \
 -d "owner[address][city]"=Frankfurt \
 -d "owner[address][country]"=DE \
 -d "owner[address][line1]"="Genslerstraße 24" \
 -d "owner[address][postal_code]"=15230 \
 -d "owner[address][state]"=Brandenburg
```

#### Note

Only IBANs with the following country codes require the owner address: AD, PF,
TF, GI, GB, GG, VA, IM, JE, MC, NC, BL, PM, SM, CH, WF

Using either method, Stripe returns a `Source` object containing the relevant
details for the method of payment used. Information specific to SEPA Direct
Debit is provided within the `sepa_debit` subhash.

```
{
 "id": "src_18HgGjHNCLa1Vra6Y9TIP6tU",
 "object": "source",
 "amount": null,
 "client_secret": "src_client_secret_XcBmS94nTg5o0xc9MSliSlDW",
 "created": 1464803577,
 "currency": "eur",
 "flow": "none",
 "livemode": false,
 "owner": {
```

See all 37 lines
As SEPA Direct Debit payments are a pull-based payment method, there is no
movement of funds during the creation of a source. Only when a successful charge
request has been made is the customer’s bank account debited and you eventually
receive the funds.

### Source creation in mobile applications

If you’re building an iOS or Android app, you can implement sources using our
mobile SDKs. Refer to our sources documentation for
[iOS](https://docs.stripe.com/mobile/ios/sources) or
[Android](https://docs.stripe.com/mobile/android/sources) to learn more.

### Error codes

Source creation for SEPA Direct Debit payments may return any of the following
errors:

ErrorDescription`payment_method_not_available`The payment method is currently
not available. You should invite your customer to fallback to another payment
method to proceed.`processing_error`An unexpected error occurred preventing us
from creating the source. The source creation should be
retried.`invalid_bank_account_iban`The IBAN provided appears to be invalid.
Request the customer to check their information and try
again.`invalid_owner_name`The owner name is invalid. It must be at least three
characters in length.[Charge the
source](https://docs.stripe.com/sources/sepa-debit#charge-request)
Unlike most other payment methods, SEPA Direct Debit payments do not require any
customer action after the source has been created. Once the customer has
provided their IBAN details and accepted the mandate, no further action is
needed and the resulting source is directly `chargeable`.

Before creating a charge request to complete the payment, you should attach the
source to a [Customer](https://docs.stripe.com/api#customers) for later reuse.

### Attaching the source to a Customer

You must attach a source to a [Customer](https://docs.stripe.com/api#customers)
object if you plan to reuse it for future payments (for example, with a [billing
product](https://docs.stripe.com/billing)).

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode email="paying.user@example.com" \
 -d source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

Refer to our [sources and customers](https://docs.stripe.com/sources/customers)
documentation for more details on how to attach sources to new or existing
`Customer` objects and how they interact together.

### Making a charge request

Once attached, you can use the `Source` object’s ID along with the `Customer`
object’s ID to perform a charge request and finalize the payment.

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount="1099" \
 -d currency="eur" \
 -d customer=cus_AFGbOSiITuJVDs \
 -d source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

The resulting [Charge](https://docs.stripe.com/api#charge_object) object is
created with a status of `pending`. At this stage, the payment is in progress.

By default, your account’s [statement
descriptor](https://docs.stripe.com/get-started/account/activate#public-business-information)
appears on customer statements whenever you create a SEPA Direct Debit payment.
If you need to provide a custom description for a payment, include the
`statement_descriptor` parameter when making a charge request. Statement
descriptors are limited to 22 characters and cannot use the special characters
`<`, `>`, `'`, or `"`.

[Confirm that the charge has
succeeded](https://docs.stripe.com/sources/sepa-debit#charge-confirmation)
SEPA Direct Debit payments are an
[asynchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
method, so funds are not immediately available. A charge created from a SEPA
Direct Debit source can remain in a pending state for up to 14 business days
from its creation, though the average time is around five business days. Once
the charge is confirmed, its status is updated to `succeeded`.

The following events are sent when the charge’s status is updated:

EventDescription`charge.succeeded`The charge succeeded and the payment is
complete.`charge.failed`The charge has failed and the payment could not be
completed.
After confirming that the charge has succeeded, notify your customer that the
payment process has been completed and their order is confirmed. Refer to our
[best practices](https://docs.stripe.com/sources/best-practices) for more
details on how to best integrate payment methods using
[webhooks](https://docs.stripe.com/webhooks).

A charge is successful once we receive funds from the customer’s bank. However,
this often occurs before the bank has debited their customer’s bank account. If
there is a problem debiting the customer’s bank account after a charge has been
successful, the funds are retrieved in the form of a
[dispute](https://docs.stripe.com/sources/sepa-debit#disputed-payments).

## Testing Sepa Direct Debit

You can mimic a successful or failed charge by first creating a test source with
one of the following test IBAN account numbers. Use the resulting source in a
charge request to create a test charge that is either successful or failed.

AustriaBelgiumDenmarkEstoniaFinlandFranceGermanyIrelandItalyLithuaniaLuxembourgNetherlandsNorwayPortugalSpainSwedenSwitzerlandUnited
KingdomAccount NumberDescription`AT611904300234573201`The charge status
transitions from pending to succeeded.`AT861904300235473202`The charge status
transitions from pending to failed.`AT591904300235473203`The charge status
transitions from pending to succeeded, but a dispute is immediately created.
## Handling failed charges

If a charge is not confirmed, its status automatically transitions from
`pending` to `failed`. Should a charge fail, notify your customer immediately
upon receipt of the `charge.failed` event. When using SEPA Direct Debit, you may
prefer not to fulfill orders until the `charge.succeeded`
[webhook](https://docs.stripe.com/webhooks) has been received.

If a SEPA Direct Debit charge fails and we have reason to believe that
subsequent charges will also fail, we will update the source to `failed`.

#### Note

SEPA Direct Debit charges can fail due to exceeding your rolling-window
processing limits. If charging the source fails with error code
`charge_exceeds_source_limit`, then you can retry the charge later. Please [get
in touch](https://support.stripe.com/email) if you need to request higher
processing limits.

## Notifying customers of recurring payments

The [SEPA Direct Debit
rulebook](http://www.europeanpaymentscouncil.eu/index.cfm/sepa-direct-debit/sepa-direct-debit-core-scheme-sdd-core)
requires that you notify your customer each time a debit is to be made on their
account. You can send these notifications separately or together with other
documents (for example, an [invoice](https://docs.stripe.com/api/invoices)).

These notifications should be sent at least 14 calendar days before you create a
payment. You can send them closer to the payment date as long as your mandate
makes it clear when your customer can expect to receive them. The mandate
provided by Stripe specifies this can happen up to two calendar days in advance
of future payments, allowing you to send notifications during charge creation.
For recurring payments of the same amount (for example, a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) of a
fixed amount), you may indicate multiple upcoming debits with corresponding
dates in a single notice.

When sending your customers a notice, it must include:

- The last 4 digits of the debtor’s bank account
- The mandate reference (`sepa_debit[mandate_reference]` on the `Source` object)
- The amount to be debited
- Your SEPA creditor identifier
- Your contact information

### Using webhooks or automated emails

Source objects provide tooling to help you notify your users compliantly. At
Source creation it is possible to specify a `mandate[notification_method]`. The
possible values are the following:

ValueDescription`email`As you create Charges, we automatically notify your
customers over email.`manual`As you create Charges, we emit a
`source.mandate_notification` webhook with all the required information to
generate a compliant notification. On reception of this webhook you should
notify your customer using the channel of your choice.`none`None of the above,
you opt to generate debits notifications entirely outside of Stripe.
By default, `mandate[notification_method]` is set to *none* at Source creation
but can be updated later.

### Obtaining a creditor identifier for EU businesses

#### Note

This section applies to EU businesses only.

For EU businesses, your [SEPA creditor
identifier](https://www.sepa.ch/en/home/direct-debits/creditor-identifier.html)
is associated with each SEPA Direct Debit payment instruction and identifies the
company making the payment. While companies may have multiple creditor
identifiers, each creditor identifier is unique and allows your customers to
easily identify the debits on their account. This can help reduce the likelihood
of disputed payments. Some payment providers don’t request that you provide your
own SEPA creditor identifier. Stripe requests a SEPA creditor identifier to
improve the experience of your customers.

You can request a SEPA creditor identifier from a financial institution in the
country in which you have your main office or residence. For example, you can
request the SEPA creditor identifier from the bank that holds your account. This
is commonly done online and can sometimes take a few days. In some cases, your
bank may take additional steps to issue a creditor identifier. When contacting
your bank for your SEPA creditor identifier, clarify that you are not requesting
they process SEPA Direct Debit payments for you.

If you have trouble obtaining your creditor identifier, [let us
know](https://support.stripe.com/contact).

## Disputed payments

SEPA Direct Debit provides a dispute process for bank account holders to dispute
payments. As such, you should make the appropriate decisions regarding your
business and how you approach SEPA Direct Debit payments.

For a period of eight weeks after their account was debited, an account holder
can dispute a payment through their bank on a “no questions asked” basis. Any
disputes within this period are automatically honored.

Beyond the eight-week period after the creation of the payment, and for up to 13
months, a customer may only dispute a payment with their bank if they consider
the debit had not been authorized. In this event, we automatically provide the
customer’s bank with the mandate that the customer approved. This does not
guarantee that the dispute can be canceled as the customer’s bank can still
decide that the debit was not authorized by the mandate—and that their customer
is entitled to a refund.

A dispute can also occur if the customer’s bank is unable to debit their account
because of a problem (for example, the account is frozen or has insufficient
funds), but it has already provided the funds to make a charge successful. In
this instance, the bank reclaims those funds in the form of a dispute.

If a dispute is created, a `charge.dispute.created` webhook event is sent and
Stripe deducts the amount of the dispute and dispute fee from your Stripe
balance. This fee varies based on your account’s default settlement currency:

Settlement Currency Dispute FeeCHF10.00
FrDKK75.00-kr.EUR€7.50GBP£7.00NOK75.00-kr.SEK75.00-kr.USD$10.00
Unlike [credit card disputes](https://docs.stripe.com/disputes), all SEPA Direct
Debit disputes are final and there is no appeals process. If a customer
successfully disputes a payment, you must reach out to them if you would like to
resolve the situation. If you’re able to come to an arrangement and your
customer is willing to return the funds to you, they will need to make a new
payment.

In general, each dispute includes the reason for its creation, though this can
vary from country to country. For instance, disputed payments in Germany do not
provide additional information for privacy reasons.

## Refunds

Payments made with SEPA Direct Debit can only be submitted for refund within 180
days from the date of the original charge. After 180 days, it is no longer
possible to refund the charge. Similar to the delays introduced to payments with
SEPA Direct Debit, refunds also require additional time to process (typically
3-4 business days). Should you accidentally debit your customer, please contact
them immediately to avoid having the payment disputed.

A refund can only be processed after the payment process has completed. If you
create a full or partial refund on a payment that hasn’t yet been completed, the
refund is actioned once the `Charge` object’s status has transitioned to
`succeeded`. In the event of a payment where the `Charge` object’s status
transitioned to `failed`, full and partial refunds are marked as canceled, as
the money never left the customer’s bank account.

SEPA does not explicitly label refunds when the funds are deposited back to the
customer’s account. Instead, they’re processed as a credit and include a visible
reference to the original payment’s statement descriptor.

Due to longer settlement time periods and the nature of how banks process SEPA
Direct Debit transactions, there is potential for confusion between you, your
customer, your customer’s bank, and Stripe. For instance, your customer may
contact both you and their bank to dispute a payment. If you proactively issue
your customer a refund while the customer’s bank also initiates the dispute
process, your customer could end up receiving two credits for the same
transaction.

When issuing a refund, it’s important that you immediately inform your customer
that it may take up to five business days for the refund to arrive in their bank
account.

## See also

- [Other supported payment methods](https://docs.stripe.com/sources)
- [Sources API reference](https://docs.stripe.com/api#sources)
- [Best practices](https://docs.stripe.com/sources/best-practices)

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [SEPA Direct Debit payments](https://docs.stripe.com/payments/sepa-debit)
- [Sources](https://docs.stripe.com/sources)
- [Single Euro Payments
Area](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)
- [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
-
[mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate)
- [pull](https://docs.stripe.com/sources#pull-or-push-of-funds)
- [reusable](https://docs.stripe.com/sources#single-use-or-reusable)
-
[asynchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
- [contact support](https://support.stripe.com/contact)
- [European Payments
Council](https://www.europeanpaymentscouncil.eu/other/core-sdd-mandate-translations)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [Stripe.js reference](https://docs.stripe.com/js#stripe-create-source)
- [Sources
API](https://docs.stripe.com/api/sources/create#create_source-owner-address)
- [iOS](https://docs.stripe.com/mobile/ios/sources)
- [Android](https://docs.stripe.com/mobile/android/sources)
- [Customer](https://docs.stripe.com/api#customers)
- [billing product](https://docs.stripe.com/billing)
- [sources and customers](https://docs.stripe.com/sources/customers)
- [Charge](https://docs.stripe.com/api#charge_object)
- [statement
descriptor](https://docs.stripe.com/get-started/account/activate#public-business-information)
- [webhooks](https://docs.stripe.com/webhooks)
- [best practices](https://docs.stripe.com/sources/best-practices)
- [get in touch](https://support.stripe.com/email)
- [SEPA Direct Debit
rulebook](http://www.europeanpaymentscouncil.eu/index.cfm/sepa-direct-debit/sepa-direct-debit-core-scheme-sdd-core)
- [invoice](https://docs.stripe.com/api/invoices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [SEPA creditor
identifier](https://www.sepa.ch/en/home/direct-debits/creditor-identifier.html)
- [SEPA Direct Debit
rulebook](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-payment-schemes/sepa-direct-debit/sepa-direct-debit-core-rulebook-and)
- [credit card disputes](https://docs.stripe.com/disputes)
- [create a partial refund](https://docs.stripe.com/api#create_refund)
- [Sources API reference](https://docs.stripe.com/api#sources)