# Capital financing promotionPrivate preview

## Show promotional content about a connected account's Capital financing offer and launch a Capital application.

Render a UI component for connected accounts to view their Capital [Financing
Offer](https://docs.stripe.com/api/capital/connect_financing_object), along with
educational and promotional content explaining the program’s functionality. They
can open the application flow in a dialog by clicking **Start application**.

SizeDesktopLocale (United States)This demo is read-only. Write operations
(like performing a refund or saving account information) are not supported for
this demo.
## No-offer states

If the connected account doesn’t have a current financing offer, the component
renders differently depending on their financing status:

- If the account has active financing in progress or under review, the component
renders as null.
- If the connected account doesn’t have active financing, the component displays
generic information about eligibility and the lending program.

## Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
Capital financing promotion component by specifying
`capital_financing_promotion` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[capital_financing_promotion][enabled]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the Capital financing promotion component in the front end:

```
// Include this element in your HTML
const capitalFinancingPromotion =
stripeConnectInstance.create('capital-financing-promotion');
container.appendChild(capitalFinancingPromotion);
```

HTML + JSReactMethodTypeDescriptionDefault`setOnApplicationSubmitted``() =>
void`The connected account has successfully submitted their application for
financing.`setLayout``full | banner`Controls the layout of the component.
`banner` mode greatly reduces the vertical size of the component, which is
useful when stacking the component with other content on the
page.`full``setOnEligibleFinancingOfferLoaded``({productType: standard | refill
| none}) => void`The connected account’s financing offer has been loaded. The
`productType` field corresponds to the `product_type` field on the [Financing
Offer](https://docs.stripe.com/api/capital/connect_financing_object#financing_offer_object-product_type)
object.`setPrivacyPolicyUrl``string`Absolute URL of a page containing your
privacy
policy.`https://stripe.com/privacy``setHowCapitalWorksUrl``string`Absolute URL
of a page with information about the Capital
program.`https://docs.stripe.com/capital/how-stripe-capital-works``setEligiblityCriteriaUrl``string`Absolute
URL of a page with information about eligibility criteria for the Capital
program.`https://docs.stripe.com/capital/eligibility`

## Links

- [Financing
Offer](https://docs.stripe.com/api/capital/connect_financing_object)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [Financing
Offer](https://docs.stripe.com/api/capital/connect_financing_object#financing_offer_object-product_type)