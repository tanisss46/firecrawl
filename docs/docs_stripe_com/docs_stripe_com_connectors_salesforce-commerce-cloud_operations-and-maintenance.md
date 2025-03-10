# Stripe LINK Cartridge Operations and Maintenance

## Learn how to operate and maintain the Stripe LINK cartridge.

## Data storage

The Stripe LINK cartridge extends Commerce Cloud to store several data points.

Customer profile: Stripe Customer ID, used to retrieve information about the
customer’s record in your Stripe account.

- `stripeCustomerID(string)` - Store Stripe Customer ID

Order/basket custom attributes:

- `stripePaymentIntentID(String)` - Store PaymentIntent ID
- `stripeIsPaymentIntentInReview(Boolean)` - Store PaymentIntent in review

Payment transaction custom attributes:

- `stripeChargeId(string)` - Store Charge ID
- `stripeChargeOutcomeData(text)` - Store Charge outcome data
- `stripeClientSecret(string)` - Store client secret
- `stripeJsonData(text)` - Store webhook JSON data
- `stripeOrderNumber(number)` - Store order number
- `stripeSourceCanCharge(boolean)` - Store if Stripe Source can be charged
- `stripeSourceId(string)` - Store Stripe Source ID

Payment transaction custom attributes:

- `stripeChargeId(string)` - Store Charge ID
- `stripeCardID(string)` - Store card ID
- `stripeCustomerID(string)` - Store Customer ID
- `stripeDefaultCard(boolean)` - Store Stripe default card
- `stripeClientSecret(string)` - Store client secret
- `stripePRUsed(boolean)` - Store payment request button used
- `stripeSavePaymentInstrument(boolean)` - Store save payment instrument
- `stripeSourceID(string)` - Store Stripe Source ID

Custom objects: The custom objects are listed in the Business Manager. Navigate
to **Merchant Tools > Custom Objects > Custom Objects** to see the list of
custom objects.

- `StripeWebhookNotifications`

## Availability

Refer to the [Stripe service level agreement](https://stripe.com/legal) to
determine specific uptimes for the service. In case the service fails, no
failover exists to allow transactions to proceed. Users receive a meaningful
error message in this case.

## Failover and recovery process

If the Stripe service is unavailable, the user won’t be able to check out. You
can track the service availability in SFCC using the Service Status.

## Support

If you experience problems or have recommendations for improvements, please
contact [Stripe Support](https://support.stripe.com/).

## Upgrading the LINK cartridge

Before you upgrade, we recommend:

- Backing up your files and any other custom dependencies
- Installing the latest version from [LINK
Marketplace](https://www.salesforce.com/products/commerce-cloud/partner-marketplace/partners/stripe/)
in your test environment
- Testing the frontend UI and backend data integration
- Keeping a copy of any customizations you made to the module’s original code
- Porting over any customizations you made to the module’s code after upgrading
and resolving any potential conflicts

## See also

- [Catridge user
guide](https://docs.stripe.com/connectors/salesforce-commerce-cloud/user-guide)
-
[Testing](https://docs.stripe.com/connectors/salesforce-commerce-cloud/testing)

## Links

- [Stripe service level agreement](https://stripe.com/legal)
- [Stripe Support](https://support.stripe.com/)
- [LINK
Marketplace](https://www.salesforce.com/products/commerce-cloud/partner-marketplace/partners/stripe/)
- [Catridge user
guide](https://docs.stripe.com/connectors/salesforce-commerce-cloud/user-guide)
-
[Testing](https://docs.stripe.com/connectors/salesforce-commerce-cloud/testing)