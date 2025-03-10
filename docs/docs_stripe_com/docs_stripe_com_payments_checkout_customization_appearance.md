# Customize appearance

## Customize your checkout page's colors, fonts, shapes, and more.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
## Apply branding

You can apply custom branding to Checkout. Go to [Branding
Settings](https://dashboard.stripe.com/settings/branding/checkout) to:

- Upload a logo or icon
- Customize the Checkout page’s background color, button color, font, and shapes

### Branding with Connect

For platforms performing direct charges, and destination charges with
`on_behalf_of`, Checkout uses the brand settings of the connected account. For
connected accounts without access to the full Stripe Dashboard (includes Express
and Custom accounts), platforms can configure the brand settings with the
[Accounts](https://docs.stripe.com/api/accounts/object#account_object-settings-branding)
API.

## Change your brand name

You can change a Checkout page’s name by modifying the **Business name** field
in [Business details
settings](https://dashboard.stripe.com/settings/business-details).

You can also [customize the domain
name](https://docs.stripe.com/payments/checkout/custom-domains) of a
Stripe-hosted Checkout page.

## Font compatibility

Each custom font is compatible with a [subset of
locales](https://docs.stripe.com/js/appendix/supported_locales). You can either
explicitly set the locale of a Checkout Session by passing the locale field when
creating the Session, or use the default `auto` setting where Checkout chooses a
locale based on the customer’s browser settings.

The following table lists unsupported locales for each font. Languages in these
locales might fall outside of the supported character range for a given font. In
those cases, Stripe renders the Checkout page with an appropriate system
fallback font. If you choose a Serif font but it’s unsupported in a locale,
Stripe falls back to a Serif-based font.

Font familyUnsupported localesBe Vietnam Pro`bg`, `el`, `ja`, `ko`, `ru`, `th`,
`zh`, `zh-HK`, `zh-TW`Bitter`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`Chakra
Petch`bg`, `el`, `ja`, `ko`, `ru`, `zh`, `zh-HK`, `zh-TW`Hahmlet`bg`, `el`,
`ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`Inconsolata`bg`, `el`, `ja`, `ko`,
`ru`, `th`, `zh`, `zh-HK`, `zh-TW`Inter`ja`, `ko`, `th`, `zh`, `zh-HK`,
`zh-TW`Lato`bg`, `cs`, `el`, `hr`, `ja`, `ko`, `lt`, `lv`, `mt`, `ro`, `ru`,
`sl`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`Lora`el`, `ja`, `ko`, `th`, `zh`,
`zh-HK`, `zh-TW`M PLUS 1 Code`bg`, `el`, `ko`, `lt`, `lv`, `ru`, `sk`, `sl`,
`th`, `tr`Montserrat`el`, `hr`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`,
`zh-TW`Nunito`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`Noto Sans`ja`, `ko`,
`th`Noto Serif`th`Open Sans`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`PT Sans`el`,
`ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`PT Serif`el`, `ja`, `ko`, `th`,
`vi`, `zh`, `zh-HK`, `zh-TW`Pridi`bg`, `el`, `ja`, `ko`, `ru`, `zh`, `zh-HK`,
`zh-TW`Raleway`el`, `ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`Roboto`ja`, `ko`,
`zh`, `zh-HK`, `zh-TW`Roboto Slab`ja`, `ko`, `th`, `zh`, `zh-HK`, `zh-TW`Source
Sans Pro`bg`, `el`, `ja`, `ko`, `ru`, `th`, `zh`, `zh-HK`, `zh-TW`Titillium
Web`bg`, `el`, `ja`, `ko`, `th`, `vi`, `zh`, `zh-HK`, `zh-TW`Ubuntu Mono`ja`,
`ko`, `th`, `zh`, `zh-HK`, `zh-TW`Zen Maru Gothic`bg`, `cs`, `el`, `hr`, `ko`,
`lt`, `lv`, `pl`, `ro`, `ru`, `sk`, `th`, `vi`

## Links

- [Branding Settings](https://dashboard.stripe.com/settings/branding/checkout)
-
[Accounts](https://docs.stripe.com/api/accounts/object#account_object-settings-branding)
- [Business details
settings](https://dashboard.stripe.com/settings/business-details)
- [customize the domain
name](https://docs.stripe.com/payments/checkout/custom-domains)
- [subset of locales](https://docs.stripe.com/js/appendix/supported_locales)