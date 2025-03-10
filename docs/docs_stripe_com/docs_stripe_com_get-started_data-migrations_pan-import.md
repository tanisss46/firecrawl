# Request a payment data import

## Securely import sensitive payment data.

Stripe enables you to retain your existing customer and payment data when you
migrate to Stripe. We work with your team and current payment provider, as
needed, to securely migrate your information in a few steps:

- [Build your Stripe
integration](https://docs.stripe.com/get-started/data-migrations/pan-import#build-integration).
- [Request and confirm the migration
details](https://docs.stripe.com/get-started/data-migrations/pan-import#request-migration).
- [Update your
integration](https://docs.stripe.com/get-started/data-migrations/pan-import#update-integration)
to complete the migration.
- (Optional) [Migrate
subscriptions](https://docs.stripe.com/get-started/data-migrations/pan-import#subscription-migrations).

This process allows you to accept and charge new customers on Stripe and
continue charging your existing customers with your current processor until the
migration is complete. Your customers incur no downtime. After the migration
process completes, you can process all payments on Stripe.

Build and test your Stripe integration before requesting data from your current
processor. This gives you plenty of time to verify and test your new
integration. If you have any questions about the migration process or
integrating with Stripe, [let us
know](https://support.stripe.com/contact/login?email=true&topic=migrations).

[Build your Stripe
integration](https://docs.stripe.com/get-started/data-migrations/pan-import#build-integration)
Stripe simplifies your security requirements so that your customers don’t have
to leave your site to complete a payment. This is done through a combination of
client-side and server-side steps:

- From your website running in the customer’s browser, Stripe securely collects
their payment details.
- Stripe responds with a representative token.
- The browser submits the token to your server, along with any other form data.
- Your server-side code uses that token in an API request (for example, when
[creating a charge](https://docs.stripe.com/payments/charges-api)).

This approach streamlines your website’s checkout flow, while sensitive payment
information never touches your server. This allows you to operate in accordance
with
[PCI-compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
regulations, which can save you time and provide financial benefits.

![Stripe's payment process
flow](https://b.stripecdn.com/docs-statics-srv/assets/charge-workflow.6d5c025c1b1e62a53803f1908104e0a8.png)

Stripe’s payment process flow

Compared to other payment processors, a Stripe integration can differ in the
following ways:

- Your customer never leaves your website.
- Token creation isn’t tied to a specific product or amount.
- There’s no need to create a client-side key on-demand. You use a set,
publishable [API key](https://docs.stripe.com/keys) instead.

### Prepare your integration

For all new customer tokens (not imported), implement the following:

- Use [Customer](https://docs.stripe.com/api#create_customer) objects to [save
the card information](https://docs.stripe.com/saving-cards).
- Collect and tokenize customer card information with one of our recommended
[payments
integrations](https://docs.stripe.com/payments/online-payments#compare-features-and-availability).
- [Create charges](https://docs.stripe.com/api#create_charge-customer) for these
new customers.

Using this approach, you can accept payments from your new customers on Stripe
without impacting your current customers in your existing processor during the
migration process.

### Integration considerations

Designing your integration before you ask your payment processor to transfer
data to Stripe is the most efficient way to handle imported data. Some actions
you can take before requesting an import include:

- Complete your Stripe account setup.
- Remap customer records.
- Handle updates to payment information during the migration.
- Enable all optimizations, such as [Adaptive
Acceptance](https://stripe.com/guides/optimizing-authorization-rates#adaptive-acceptance),
Card Account Updater (CAU), and [network
tokens](https://stripe.com/guides/understanding-benefits-of-network-tokens).

#### Remap customer records

If you prefer, you can configure your integration to [import the payment method
data from prior records into existing Stripe customer
objects](https://docs.stripe.com/get-started/data-migrations/map-payment-data).
Doing so prevents the migration from creating a new (possibly duplicate)
customer in your Stripe account for each unique customer ID in the files we
receive from your prior processor.

After migrating, you might still have to update some records to correspond with
the new Stripe [Customer](https://docs.stripe.com/api/customers) identifier, if:

- You created the Stripe customer before migration, then we imported the payment
information to update this customer record.
- We imported the payment information as a new customer record.

For example, customer jenny.rosen@example.com might have ID `42` in your
database, corresponding to ID `1893` in your previous processor’s system, but is
ID `cus_12345` in your Stripe account. In this case, you must now map your ID
`42` to the Stripe ID `cus_12345` in your database. Stripe provides a
post-import [mapping
file](https://docs.stripe.com/get-started/data-migrations/pan-import#update-integration)
to help you identify required remapping.

#### Handle updates to payment information

If customers update their payment information with your previous processor in
the window between transferring the data and completing the import, those
changes are lost.

Update your site’s process for handling updates to saved payments to prevent
errors or billing issues for your customers. This includes preparations to
perform a self-migration for any customer without a stored Stripe customer ID:

- Create a new [Customer object](https://docs.stripe.com/api/customers/object)
in Stripe for your customer.
- Attach the payment method to the Customer object.
- If necessary, [migrate
subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit).

After migration completes, Stripe [automatically handles card-triggered
updates](https://stripe.com/blog/smarter-saved-cards), such as expiration date
changes.

[Request and confirm the migration
details](https://docs.stripe.com/get-started/data-migrations/pan-import#request-migration)-
After you complete your integration and are ready to process payments on Stripe,
[request your payment data from your previous
processor](https://support.stripe.com/questions/request-data-from-a-current-processor-for-a-data-import-to-stripe).
Many processors require the account owner to request a data transfer.
- Log in to your Stripe account to submit the [migration request
form](https://support.stripe.com/contact/email?topic=migrations) to request your
import migration.
- Engage with Stripe through the authenticated email thread we create upon
receipt of your migration request.

#### Warning

Never send sensitive credit card details or customer information directly to
Stripe. If you have this data, let us know in your migration request form so we
can help you securely transfer your data.

Stripe can import your customer billing address information and payment details.
For details on migrating specific payment types, see:

- [Cards](https://docs.stripe.com/get-started/data-migrations/card-imports)
- [ACH](https://docs.stripe.com/get-started/data-migrations/ach-imports)
- [SEPA](https://docs.stripe.com/get-started/data-migrations/sepa-imports)
- [Bacs](https://docs.stripe.com/payments/bacs-debit/import-data)
- [PADs/ACSS](https://docs.stripe.com/get-started/data-migrations/pads-imports)

Data migrations doesn’t migrate subscriptions, but you can
[recreate](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions)
them separately or import them using the [Billing Migration
Toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit).

Your previous processor might take a few days or several weeks to transfer the
final data to Stripe. Allow for this transition time in your migration plan.

After your previous processor transfers your data, Stripe reviews the data and
identifies any problems with the import. We work with you and your previous
processor to correct any issues. We then share a summary of the import for your
final review and approval.

After your approval, Stripe imports the data into your account. We create a
[Customer](https://docs.stripe.com/api#customer_object) for each unique customer
in the transferred data file, and create and attach the customer’s cards as
[Card](https://docs.stripe.com/api#card_object) or [Payment
Method](https://docs.stripe.com/api/payment_methods/object) objects. If the
transferred data specifies the customer’s default card, we set that as the
customer’s [default payment
method](https://docs.stripe.com/api#customer_object-default_source) for charges
and [subscription](https://docs.stripe.com/api/subscriptions/create) payments.

If your Stripe account has accumulated significant customer records by the time
you migrate, consider [mapping import date into existing Stripe customer
objects](https://docs.stripe.com/get-started/data-migrations/map-payment-data)
instead of creating new Customer objects.

Stripe typically imports data within 10 business days of receiving the correct
data from your previous processor, along with any supplementary data files you
want to share with our team.

[Update your
integration](https://docs.stripe.com/get-started/data-migrations/pan-import#update-integration)
After completing the import, Stripe sends you a choice of a CSV or JSON file
that shows the mapped relationship between your current processor’s IDs and the
imported Stripe object IDs. Parse this mapping file and update your database
accordingly. Make sure your integration [handled any card
updates](https://docs.stripe.com/get-started/data-migrations/pan-import#handle-card-updates)
that took place during the transition.

### Post import mapping file

After you update your integration with this mapping file, you can begin charging
all of your customers on Stripe.

```
{
 "1893": {
 "cards": {
 "2600": {
 "id": "card_2222222222",
 "fingerprint": "x9yW1WE4nLvl6zjg",
 "last4": "4242",
 "exp_month": 1,
 "exp_year": 2020,
 "brand": "Visa"
 },
 "3520": {
 "id": "card_3333333333",
 "fingerprint": "nZnMWbJBurX3VHIN",
 "last4": "0341",
 "exp_month": 6,
 "exp_year": 2021,
 "brand": "Mastercard"
 }
 },
 "id": "cus_abc123def456"
 }
}

```

The example JSON mapping above shows:

- Imported customer ID 1893 as a new Stripe Customer with ID `cus_abc123def456`.
- Imported customer card ID 2600 as a new Stripe Card with ID `card_2222222222`.
- Imported customer card ID 3520 as a new Stripe Card with ID `card_3333333333`.

Stripe can import card data as
[PaymentMethods](https://docs.stripe.com/api#payment_method_object) instead of
Card objects if you specify it in your migration request. The following examples
show the mapping files for different types of payment information imports.

Card as card_ CSVCard as PaymentMethod (pm_) CSVACH as bank account (ba_) CSVACH
as PaymentMethod (pm_) CSVBACs as PaymentMethod (pm_) CSVSEPA as PaymentMethod
(pm_) CSV
```

old_customer_id,customer_id,old_card_id,card_id,card_fingerprint,card_last4,card_exp_month,card_exp_year,card_brand

old_cus_100,cus_abc123def456,old_src_100,card_2222222222,x9yW1WE4nLvl6zjg,424242,09,2024,Visa

```

### Post import payment declines

After migrating, monitor your payments performance to make sure the acceptance
rate for imported payment data matches your expectations.

Payment acceptance (or issuer authorization rate) is the percentage of
transactions that issuers successfully authorize out of all transactions
submitted for payment. This metric excludes blocked transactions (for example
due to Radar rules) because those are never submitted for authorization.

In both your general approach and post migration, align your [payment
authorization
optimization](https://stripe.com/guides/optimizing-authorization-rates) goals
with your business objectives. For example, a digital goods business with low
unit cost might set their risk level to block fewer payments. Consider the
potential effects:

- Increased conversion rates due to less friction.
- Increased exposure to fraud due to riskier payments getting through.
- Lower raw issuer authorization rates due to fraud model blocks by the issuer.

Make sure you provide accurate data (such as cardholder name, billing address,
and email). Reflecting the cardholder’s *intent* maximizes successful
authorization potential.

#### Identify cards on file

Payment data migrations involve *cards on file* (cards saved for a future
[merchant-initiated or off
session](https://support.stripe.com/questions/what-is-the-difference-between-on-session-and-off-session-and-why-is-it-important)
payment for the same customer). Make sure you store imported payment data and
label payments using those cards on file with the correct `off_session`
parameter. If you improperly identify cards on file:

- Issuers who can’t confirm a cardholder’s consent to future or recurring
payments might [decline](https://docs.stripe.com/declines#issuer-declines) them.
- The payment data might be ineligible for certain Stripe optimization products
such as Card account updater (CAU) and Network tokens (NT).

#### Monitor decline reasons for optimization opportunities

Following your migration, your [issuer decline
reasons](https://docs.stripe.com/declines/codes) can help you identify whether
migrated payment data is transacting as expected. Spikes in certain types of
declines might benefit from the following optimization products:

- [Card account
updater](https://docs.stripe.com/saving-cards#automatic-card-updates): Stripe’s
partnerships with card networks allows us to automatically obtain updates for
expired or replaced cards in both real-time and the background.
- **Automatic retries** (Dunning): Use caution because retrying numerous cards
(such as after a migration) can appear suspicious to issuers. If you use
Stripe’s [Smart
retries](https://stripe.com/guides/optimizing-authorization-rates#smart-retries)
for your billing payments, the machine learning model analyzes decline code,
payment method updates, and bank risk threshold activity to retry recurring
revenue payments more strategically.
- [Network
tokens](https://stripe.com/guides/optimizing-authorization-rates#network-tokens):
Replace a specific payment account number (PAN) with a secure token from the
card network to make sure PAN updates (like renewal or replacement)
automatically reflect in the token.
- [Adaptive
acceptance](https://stripe.com/guides/optimizing-authorization-rates#adaptive-acceptance):
Stripe uses machine learning to assess the effect of minor adjustments (such as
formatting) to an authorization request in real-time, then refines the payment
retry before returning the original decline to the customer.
- **Customer outreach**: Asking your customer to log in and re-enter or
re-verify their payment details often re-establishes your business’s
trustworthiness with the customer and the payment providers. Consider notifying
customers through channels other than email, such as text messages or in-app
notifications.

The following table shows which optimization products offer improvement for a
variety of decline reasons.

Decline codes might include Migration effectDoDon’t
`incorrect_number`

`invalid_number`

`expired_card`

Updates to card data during the natural migration lag can cause saved card data
to be out of date.

- Card account updater
- Network tokens
- Adaptive acceptance
- Contact customer

Retry

`generic_decline`

`do_not_honor`

Changes to your statement descriptor or other identification markers might
trigger issuer risk models or confuse your customer.

- Retry
- Network tokens
- Adaptive acceptance
- Contact customer

Card account updater

`transaction_not_allowed`

`try_again_later`

`authentication_required`

`incorrect_cvc`

Some migrated payment data might be missing initial card validation details,
such as the network token or original transaction ID.

- Card account updater
- Retry
- Adaptive acceptance
- Contact customer

Network tokens

`lost_card`

`stolen_card`

`invalid_account`

`pickup_card`

`card_not_supported`

Customers might report lost or stolen cards during a migration lag. Look out for
a special CONTAC event in conjunction with these declines.

- Network tokens
- Contact customer
- CAU
- Retry1
- Adaptive acceptance

1 Retrying lost or stolen payment data can appear suspicious to card issuers.

[OptionalWork with
subscriptions](https://docs.stripe.com/get-started/data-migrations/pan-import#subscription-migrations)[Migration
PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)
If you’re unfamiliar with PGP, see [GPG](http://gnupg.org/) and start by
[importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84). After
you familiarize yourself with the basics of PGP, use the following PGP key to
encrypt sensitive data (such as credit card information) for PCI-compliant
migration.

### PGP migration key

This creates **FILENAME.gpg** with the following information:

- Key ID: `9C78B7620C1E99AD`
- Key type: `RSA`
- Key size: `4096 bits`
- Fingerprint: `AEBF 7C48 38C4 4D2F DC99 A3F9 9C78 B762 0C1E 99AD`
- User ID: `Stripe Import Key (PCI) <support-migrations@stripe.com>`

After you import our key, you can encrypt files to send by running this command
in your command line prompt:

`gpg --encrypt --recipient 9C78B7620C1E99AD FILENAME`

For more details on providing encrypted data to Stripe, see [Upload
supplementary
data](https://docs.stripe.com/get-started/data-migrations/supplementary-data).

## See also

- [Multiple
accounts](https://docs.stripe.com/get-started/account/multiple-accounts)
- [Account checklist](https://docs.stripe.com/get-started/account/checklist)

## Links

- [let us
know](https://support.stripe.com/contact/login?email=true&topic=migrations)
- [creating a charge](https://docs.stripe.com/payments/charges-api)
-
[PCI-compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [API key](https://docs.stripe.com/keys)
- [Customer](https://docs.stripe.com/api#create_customer)
- [save the card information](https://docs.stripe.com/saving-cards)
- [payments
integrations](https://docs.stripe.com/payments/online-payments#compare-features-and-availability)
- [Create charges](https://docs.stripe.com/api#create_charge-customer)
- [Adaptive
Acceptance](https://stripe.com/guides/optimizing-authorization-rates#adaptive-acceptance)
- [network
tokens](https://stripe.com/guides/understanding-benefits-of-network-tokens)
- [import the payment method data from prior records into existing Stripe
customer
objects](https://docs.stripe.com/get-started/data-migrations/map-payment-data)
- [Customer](https://docs.stripe.com/api/customers)
- [Customer object](https://docs.stripe.com/api/customers/object)
- [migrate
subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)
- [automatically handles card-triggered
updates](https://stripe.com/blog/smarter-saved-cards)
- [request your payment data from your previous
processor](https://support.stripe.com/questions/request-data-from-a-current-processor-for-a-data-import-to-stripe)
- [migration request
form](https://support.stripe.com/contact/email?topic=migrations)
- [Cards](https://docs.stripe.com/get-started/data-migrations/card-imports)
- [ACH](https://docs.stripe.com/get-started/data-migrations/ach-imports)
- [SEPA](https://docs.stripe.com/get-started/data-migrations/sepa-imports)
- [Bacs](https://docs.stripe.com/payments/bacs-debit/import-data)
- [PADs/ACSS](https://docs.stripe.com/get-started/data-migrations/pads-imports)
-
[recreate](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions)
- [Customer](https://docs.stripe.com/api#customer_object)
- [Card](https://docs.stripe.com/api#card_object)
- [Payment Method](https://docs.stripe.com/api/payment_methods/object)
- [default payment
method](https://docs.stripe.com/api#customer_object-default_source)
- [subscription](https://docs.stripe.com/api/subscriptions/create)
- [PaymentMethods](https://docs.stripe.com/api#payment_method_object)
- [payment authorization
optimization](https://stripe.com/guides/optimizing-authorization-rates)
- [merchant-initiated or off
session](https://support.stripe.com/questions/what-is-the-difference-between-on-session-and-off-session-and-why-is-it-important)
- [decline](https://docs.stripe.com/declines#issuer-declines)
- [issuer decline reasons](https://docs.stripe.com/declines/codes)
- [Card account
updater](https://docs.stripe.com/saving-cards#automatic-card-updates)
- [Smart
retries](https://stripe.com/guides/optimizing-authorization-rates#smart-retries)
- [Network
tokens](https://stripe.com/guides/optimizing-authorization-rates#network-tokens)
- [GPG](http://gnupg.org/)
- [importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84)
- [Upload supplementary
data](https://docs.stripe.com/get-started/data-migrations/supplementary-data)
- [Multiple
accounts](https://docs.stripe.com/get-started/account/multiple-accounts)
- [Account checklist](https://docs.stripe.com/get-started/account/checklist)