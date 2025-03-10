# External payment methods

## Add external payment methods to the Payment Element.

The [Payment Element](https://docs.stripe.com/payments/payment-element) can
display external payment methods that you support in addition to the payment
methods processed through Stripe. Integrating external payment methods requires
additional integration work, because external payment method transactions are
processed and finalized outside of Stripe.

#### External payment methods disclaimer

When customers choose an external payment method, they’re redirected to a URL
you configured for the external payment method. Learn about [what you’re
responsible for and the ongoing availability of external payment
methods](https://docs.stripe.com/payments/external-payment-methods#external-payment-methods-disclaimer).

This guide adds an external payment method, Divido, using the HTML/JS example
from the [Payment Element
quickstart](https://docs.stripe.com/payments/quickstart).

## Before you begin

- [Create a Stripe account](https://dashboard.stripe.com/register) or [sign
in](https://dashboard.stripe.com/login).
- Follow the [Payment Element
quickstart](https://docs.stripe.com/payments/quickstart) to complete a payments
integration.
- For each external payment method you want to add, ensure you have completed
the integration with each external payment method and confirmed that it is
working in the region that you want to enable them in.
[Add external payment method
types](https://docs.stripe.com/payments/external-payment-methods#add-external-payment-method-types)
In your `checkout.js` file, where you [initialize Stripe
Elements](https://docs.stripe.com/payments/quickstart#init-elements), specify
the external payment methods you want to add to the Payment Element. This
example adds Divido:

```
elements = stripe.elements({
 clientSecret: clientSecret,
 externalPaymentMethodTypes: ['external_divido']
 });
```

[Handle payment method selection
listener](https://docs.stripe.com/payments/external-payment-methods#handle-external-payment-method-selection)
There are two ways to handle the redirect to the external payment method:

- Replace the action of the Stripe **Pay now** button to redirect to the
external payment method.
- Replace the Stripe **Pay now** button with the external payment method
provider’s button.
Replace actionReplace button
This listener replaces the action of the Stripe **Pay now** button to redirect
the customer to the Divido checkout page where they can complete the
transaction. In `checkout.js`, add the listener code after the
`paymentElement.mount` call:

```
paymentElement.mount("#payment-element");

// Track selected payment method
let selectedPaymentMethod;
paymentElement.on('change', (event) => {
 selectedPaymentMethod = event?.value?.type;
});
```

Update the `handleSubmit` function to redirect to the Divido checkout page:

```
async function handleSubmit(e) {
 if (selectedPaymentMethod === 'external_divido') {
 // Redirect customer to the Divido checkout page to complete the transaction
 const dividoRedirectUrl = "<< fill the Divido redirect URL here >>";
 window.location.href = dividoRedirectUrl;
 } else {
 ...
 }
```

[OptionalPosition external payment
methods](https://docs.stripe.com/payments/external-payment-methods#position-payment-methods)[Test
your
integration](https://docs.stripe.com/payments/external-payment-methods#testing)-
Go through your checkout flow and verify that the Payment Element displays
Divido. This example configures Divido in the second position after cards.

![Screenshot of what Payment Element looks like when Divido is
added](https://b.stripecdn.com/docs-statics-srv/assets/display-divido.cbee45d770b63f3938f71ad6682f3ecd.png)

Payment Element with Divido
- Choose the Divido payment method to verify messaging about the next step
redirecting to Divido.

![Screenshot of what Payment Element looks like when Divido is
selected](https://b.stripecdn.com/docs-statics-srv/assets/select-divido.f695a72908b8e4b97d37c5bc89e9a2ba.png)
- Click **Pay now** to test your existing Divido integration. Verify that you
are redirected to Divido to complete the transaction and any post-payment
actions (for example, display a confirmation page, success message, or failure
message) still work with your Divido integration.

## Dashboard considerations

[PaymentIntents](https://docs.stripe.com/api/payment_intents) for transactions
processed with an external payment method provider have an `incomplete` status
in the Stripe Dashboard. Stripe isn’t involved in external payment method
transactions and can’t determine the status of these transactions.

If you [collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred), you won’t
see any `incomplete` transactions in the Stripe Dashboard for transactions that
were processed with an external payment method provider.

## External payment methods disclaimer

You can use the Stripe Payment Element to show some external payment methods
that aren’t supported by Stripe but that you directly integrate with. When
customers choose an external payment method, they’re redirected to a URL that
you configure for the external payment method. You acknowledge that:

- External payment methods aren’t offered nor supported by Stripe. The operation
and support of external payment methods is provided by the external payment
method provider.
- You’re responsible for maintaining a direct integration with the external
payment method provider.
- You need to maintain an agreement with the external payment method provider
and are responsible for complying with your agreements with each external
payment method provider.
- You’re responsible for obtaining all necessary rights to use the external
payment method provider’s marks and logos within your checkout as described in
these docs.
- Stripe isn’t responsible for the processing of any transactions with any
external payment method provider including, for example, any charges, refunds,
disputes, settlements or funds flows.
- You or the external payment method provider are responsible for the completion
of the purchase flow after a customer has selected an external payment method,
including, for example, the order confirmation and reconciliation of orders.
- You’re responsible for properly configuring the redirect URL for the external
payment method.
- You must immediately remove any external payment methods in the event your
agreements with any external payment method provider terminate or Stripe removes
the availability of an external payment method.
- You’re only permitted to integrate with and present in the Payment Element the
external payment methods listed in this guide.
- You’re solely responsible for making sure that buyers are redirected correctly
to their chosen external payment method.

### Ongoing availability of external payment methods

Stripe might at any time decide to remove the availability of any payment method
as an external payment method. Stripe will notify you of any removal of an
external payment method that you’re using, and you must immediately remove the
external payment method in your code. Failure to do so will result in the
external payment method not rendering to your customers.

## Available external payment methods

You can display the following external payment methods. You must use the
corresponding external payment method type in your code.

RegionPayment methodExternal payment method
typeAMERInterac`external_interac`APACau
PAY`external_au_pay`APACatone`external_atone`APACTouch’n
Go`external_tng_ewallet`APACソフトバンクまとめて支払い (Softbank carrier
payments)`external_softbank_carrier_payment`APACToss
Pay`external_toss_pay`APACLaybuy`external_laybuy`APACBank
Pay`external_bank_pay`APACauかんたん決済 (au easy
payments)`external_au_easy_payment`APACBitCash`external_bitcash`APACAzupay`external_azupay`APACd払い
(d-barai)`external_dbarai`APACFamiPay`external_famipay`APACGCash`external_gcash`APACGrabPay
Later`external_grabpay_later`APACMoMo`external_momo`APACNET
CASH`external_net_cash`APACOctopus`external_octopus`APACPaidy`external_paidy`APACPayPay`external_paypay`APACPlanPay`external_planpay`APACペイジー
(Pay-easy)`external_pay_easy`APAC楽天ペイ (Rakuten
Pay)`external_rakuten_pay`APACメルペイ
(Merpay)`external_merpay`APACWebMoney`external_webmoney`APAC, EuropeShopback
Pay`external_shopback_pay`EuropeAplazame`external_aplazame`EuropeBizum`external_bizum`EuropeDivido`external_divido`EuropeFonix`external_fonix`EuropeIwocapay`external_iwocapay`EuropeKBC`external_kbc`EuropeNexi
Pay`external_nexi_pay`EuropeOney`external_oney`EuropePayconiq`external_payconiq`EuropePayPo`external_paypo`EuropeSofinco`external_sofinco`EuropePostepay`external_postepay`EuropePostFinance`external_postfinance`EuropeScalapay`external_scalapay`EuropeTrueLayer`external_truelayer`EuropeWalley`external_walley`EuropeYounitedPay`external_younited_pay`GlobalLINE
Pay`external_line_pay`Globalpaysafecard`external_paysafecard`GlobalSamsung
Pay`external_samsung_pay`GlobalSezzle`external_sezzle`LATAMDapp`external_dapp`LATAMPicPay`external_picpay`MEATabby`external_tabby`MEABenefit`external_benefit`MEAFawry`external_fawry`

## Links

- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Payment Element quickstart](https://docs.stripe.com/payments/quickstart)
- [Create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [initialize Stripe
Elements](https://docs.stripe.com/payments/quickstart#init-elements)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred)