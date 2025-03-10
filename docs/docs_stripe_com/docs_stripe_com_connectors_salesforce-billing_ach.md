# ACH Considerations for Salesforce Billing

## Learn about the ACH considerations for using Stripe for Salesforce Billing and CPQ.

Using Stripe as a payment gateway for ACH means that you can’t create new ACH
payment methods in the Payment Center UI for Accounts. The Payment Center flow
charges the payment method immediately, but Stripe requires an added
verification step when using a bank account for ACH payments. Because of this
incompatibility, adding an ACH payment method from this screen will always fail.

!

Creating ACH payment methods in the Payment Center UI will always fail

Use the [New Payment Method
ACH](https://docs.stripe.com/connectors/salesforce-billing/configuration#add-an-ach-payment-method-button-to-the-related-list-on-account-objects)
flow directly from the **Payment Method Related List** on the **Account** within
Salesforce instead.

## Links

- [New Payment Method
ACH](https://docs.stripe.com/connectors/salesforce-billing/configuration#add-an-ach-payment-method-button-to-the-related-list-on-account-objects)