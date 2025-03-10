# Create a pricing scheme

## Define custom pricing strategies to assess your connected accounts.

A pricing scheme is a list of conditional fees. For each applicable transaction,
Stripe evaluates the list in the order you specify and applies the first
matching conditional fee. If no conditional fees match the transaction, Stripe
applies your default fee. Stripe calculates the fee in the specified currency,
and then converts it to the settlement currency of the payment, if needed.

To create a pricing scheme:

- From the [Platform
pricing](https://dashboard.stripe.com/settings/connect/platform_pricing) page in
your Stripe Dashboard (**Settings** > **Connect** > **Platform pricing**), click
**Get Started**.
- In the **Set a default payment pricing scheme** editor, click **Add pricing
rule**.
- Define the rule.- **Condition**: Use the dropdown menus to write one or more
conditions based on a transaction property, an operator, and a value.
- **Fee type**: Specify how to calculate the fee.- **Fixed**: Charge a specific
amount, such as 1.10 USD, for every payment.
- **Variable**: Charge a percentage, such as .45%, of the total amount of the
payment.- Minimum (optional): Specify a minimum amount to charge, even if the
percentage calculation is less.
- Maximum (optional): Specify a maximum amount to charge, even if the percentage
calculation is more.
- **Blended**: Charge a percentage of the total payment, plus a fixed amount.-
Maximum (optional): Specify a maximum amount to charge, even if the calculated
fee is more.

![Shows the Add pricing rule dialog in the
Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/customize-pricing-dialog.a5c604b458b41a572834087aa0d7118a.png)

- Add up to 125 rules for the scheme in the order to evaluate them. Stripe
applies the first rule that matches the payment and discontinues the evaluation.
- After you define all your pricing rules, **Set fallback rule** lets you define
the fee to apply when a transaction doesn’t match any of the scheme rules. - Set
a variable amount, fixed amount, or both.
- If you set a zero amount fallback rule fee, you won’t recoup your processing
cost for any transactions that don’t match any of the scheme rules.
- (Optional) Click [Add
modifier](https://docs.stripe.com/connect/platform-pricing-tools/pricing-schemes#fee-modifier)
to increase or decrease the calculated application fee by a specified percentage
(0-100).
- Click **Save and enable** or close the editor without saving to cancel.

#### Explicit application fees override pricing scheme

Enabled pricing tools apply fees to all eligible payments, unless overridden by
an explicit `application_fee` or `transfer_data[amount]` parameter on the
payment. Remove these parameters from your payment integration to apply your
pricing scheme configuration.

Saving the pricing scheme applies it to all eligible connected accounts. You can
view the progress of this update on your [Platform
Pricing](https://dashboard.stripe.com/settings/connect/platform_pricing/payments)
page. The time to complete depends on the number of connected accounts on your
platform.

Review Stripe’s [Pricing page](http://stripe.com/pricing) for guidance in
defining your pricing schemes. Factors to consider include, but aren’t limited
to:

- Which countries you support connected accounts in
- Whether any connected accounts support cross-border transactions
- Which payment methods you support
- How much Stripe charges you based on your contract

## Override a specific account

After you set up a pricing scheme, you can override the rules for connected
accounts if the fee payer is the platform.

- Select the account from the [Connected
accounts](https://dashboard.stripe.com/connect/accounts/overview) page in your
Dashboard.
- In the **Account Pricing** section, click the Payment pricing default overflow
menu () and select **Customize pricing** to create a new override, or click
**Edit** to update an existing override, if one exists.
- For a new override scheme, choose:- **Create a new scheme**: define the
override rules from scratch.
- ** from default platform pricing scheme**: define the override rules by
editing your default platform scheme.
- Create the override scheme for the connected account using the same steps for
creating the default platform scheme in the previous section.
- Click **Save** or close the editor without saving to cancel.

## Revert overridden pricing schemes

After you create an override scheme, any updates to your platform pricing scheme
don’t affect the pricing scheme of overridden connected accounts. To reapply
your platform pricing scheme to an overridden connected account:

- Select the account from the [Connected
accounts](https://dashboard.stripe.com/connect/accounts/overview) page in your
Dashboard.
- In the **Account Pricing** section, click the Custom scheme overflow menu ()
and select **Revert to platform pricing**.

## Export pricing schemes

You can export all pricing schemes as CSV files. To export your platform pricing
scheme:

- From the Platform pricing page in your Stripe Dashboard (**Settings** >
**Connect** > **Platform pricing**), click **Get Started**.
- Navigate to the overflow menu () next to a scheme. Under **Scheme actions**,
select **Export pricing**.
- When you export pricing, it downloads a file with the name `pricing-<schema
name>-<live|testmode>.csv`

To export an override scheme:

- Select the account from the Connected accounts page in your Dashboard.
- In the **Account Pricing** section, click the Custom scheme overflow menu ()
and select **Export pricing**.
- When you export pricing, it downloads a file with the name `pricing-<connected
account>-<schema name>-<live|testmode>.csv`

### Available columns

Column nameDescriptionRule #This is the rule number as shown in the pricing
scheme.Fee modifier #If present, the “Rule #” column is empty. This indicates
configured markups or discounts and their order of application.Fixed amountThe
specific amount charged with this rule.MinimumThe minimum amount this rule
charges.MaximumThe maximum amount this rule charges.Variable rate percentThe
percentage of the payment amount charged with this rule.ConditionConfigured
conditions expressed as a semicolon delimited list.
Rule type

One of `conditional`, `default`, `markup`, or `discount`:

`conditional`: Indicates that the rule is chosen when all conditions are met.

`default`: Indicates that the rule is chosen if no other rules have their
conditions met.

`markup`: Indicates that the collected application fee is marked up by this
percentage, regardless of the rule chosen.

`discount`: Indicates that the collected application fee is discounted by this
percentage, regardless of the rule chosen.

## Supported rule conditions by payment type

The following table describes some of the properties you can use to define a
pricing schedule rule condition, and the types of payments they apply to.

Condition propertyRelevant payment typeDescriptionPayment methodAll paymentsThe
payment method used, for example card, us_bank_account, or boleto.Presentment
currencyAll paymentsThe currency that the customer paid in.Settlement merchant
countryAll paymentsThe country of the payment settlement merchant.Card brandCard
paymentsThe card network provider, such as Visa or Mastercard.Card presentCard
paymentsWhether or not the payment is in-personCard countryCard paymentsThe
issuing country of the card that the customer paid with.[Card product
code](https://docs.stripe.com/connect/platform-pricing-tools/card-product-codes)Card
paymentsThe product code of the card that the customer paid with.Card typeCard
paymentsFunding source of the card, such as a credit card or debit card.Card
product categoryCard paymentsCard class classification, such as a Standard or
Premium card.Card borderCard paymentsWhether the card used is a domestic or
international card.Manually enteredCard paymentsWhether a business entered card
details into the Stripe Dashboard to process the payment rather than using an
online payment form or terminal.UK or European Economic Area card chargeCard
paymentsWhether the merchant and the card country are both within the European
Economic Area or the United Kingdom.UK and European Economic Area cross border
chargeCard paymentsWhether the merchant is in the European Economic Area or the
UK, and the card holder is in the other.Klarna payment categoryKlarna
paymentsThe Klarna payment category used on a Klarna payment.Klarna customer
countryKlarna paymentsThe country of the customer making the Klarna payment.US
Bank Account availabilityUS Bank Account paymentsThe settlement timing of the
ACH Direct Debit payment.Payment metadataAll paymentsCustom key-value metadata
that you include on the captured charge. You can [create pricing rules based on
this
metadata](https://docs.stripe.com/connect/platform-pricing-tools/complex-pricing-rule-conditions#metadata).Payout
currencyAll Instant PayoutsThe currency of the Instant Payout.
## Fee modifier

You can use a fee modifier to adjust the application fee calculated by the
conditional and fallback rules:

- **Markup** increases the fee amount by the specified percentage.
- **Discount** decreases the fee amount by the specified percentage.

Fee modifiers compound based on their sequence in the scheme definition. For
example, adding a 5% discount followed by a 10% markup adjusts a 1.00 USD fee to
a 1.05 USD fee (1.00 USD × 0.95 x 1.1 = 1.05 USD).

## View platform pricing details

Select an applied fee from [Collected
Fees](https://dashboard.stripe.com/connect/application_fees) on the Payments
page in your Dashboard. The **Platform pricing** details section shows the
following details about how Stripe calculated the application fee from the
pricing scheme:

- **Matched rules**: Shows which rule conditions matched the payment and were
used to calculate the fee based on the captured payment and fee type.
- **Additional markups applied**: Shows whether the final calculation included
any markups or discount adjustments.
- **Historical pricing scheme**: Shows a snapshot of the pricing scheme in place
at the time of payment processing and fee calculation.

For example, assume a purchase of 500 USD. The payment matched a rule with the
following conditions of the pricing scheme:

- The payment method is cards.

The pricing scheme also applied the following fee modifiers:

- 4% markup
- 3% discount

For this case, the platform pricing details show:

- The 2.9% + 0.30 USD rule applies because the payment method is a card. The
calculation against the 500 USD payment equals a fee subtotal of 14.80 USD.
- The scheme also defines a 4% markup and a 3% discount. This calculates 14.8 ×
1.04 × 0.97 = 14.93024, rounding to a total fee charged to the connected account
of 14.93 USD.

![Sample application fee details shown in the
Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/view-fee-calculation.375a290a9a613cb4b4ae7c2b71005267.png)

## Links

- [Platform
pricing](https://dashboard.stripe.com/settings/connect/platform_pricing)
- [Platform
Pricing](https://dashboard.stripe.com/settings/connect/platform_pricing/payments)
- [Pricing page](http://stripe.com/pricing)
- [Connected accounts](https://dashboard.stripe.com/connect/accounts/overview)
- [Card product
code](https://docs.stripe.com/connect/platform-pricing-tools/card-product-codes)
- [create pricing rules based on this
metadata](https://docs.stripe.com/connect/platform-pricing-tools/complex-pricing-rule-conditions#metadata)
- [Collected Fees](https://dashboard.stripe.com/connect/application_fees)