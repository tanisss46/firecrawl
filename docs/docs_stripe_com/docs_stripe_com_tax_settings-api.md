# Use the Settings API to configure Stripe Tax

## Learn how to configure tax settings, and check whether an account is ready to perform tax calculations.

The [Stripe Tax Settings API](https://docs.stripe.com/api/tax/settings) lets you
retrieve and configure the settings required to calculate tax without relying on
the [Stripe Dashboard](https://docs.stripe.com/tax/set-up).

- **Connect platform**: As a platform, you can use this API to set up your
connected accounts to use Stripe Tax, or to validate whether an account is
already set up appropriately.
- **Direct usage**: You can use this API to set up Stripe Tax, or to validate
whether you’re already set up appropriately.
Connect platformDirect usage
## Check if the connected account is ready to use Stripe Tax

Complete this check when the Standard account configures Stripe Tax through the
Stripe Dashboard but your platform needs to assess if Stripe Tax can be enabled.

Use our official libraries for access to the Stripe API from your application.
To check the Stripe Tax settings on the connected account, [retrieve the
tax.settings object](https://docs.stripe.com/api/tax/settings/retrieve) using
the `Stripe-Account` header with a value of the connected account ID:

```
curl https://api.stripe.com/v1/tax/settings \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

You can also listen to the
[tax.settings.updated](https://docs.stripe.com/api/events/types#event_types-tax.settings.updated)
webhook event which triggers when accounts update their tax settings or when new
required tax settings are introduced. See [take webhooks
live](https://docs.stripe.com/webhooks#register-webhook) to learn how to add a
webhook endpoint, and make sure you select **Listen to events on Connected
accounts** in the Dashboard.

An account is ready to use Stripe Tax if the response `tax.settings` object
retrieved by the API or webhook event returns `"active"` for `status`. The
`defaults.tax_code` and `defaults.tax_behavior` settings are only required if
not provided in the product or price on each API call.

```
{
 "object": "tax.settings",
 "defaults": {
 "tax_code": null,
 "tax_behavior": null
 },
 "head_office": {
 "address": {
 "country": "DE"
 }
 },
 "livemode": false,
 "status": "active",
 "status_details": {
 "active": {}
 }
}
```

An account isn’t ready to use Stripe Tax if the response `tax.settings` object
returns `"pending"` for `status`. The
[status_details[pending][missing_fields]](https://docs.stripe.com/api/tax/settings/object#tax_settings_object-status_details-pending-missing_fields)
has a list of all required missing fields.

```
{
 "object": "tax.settings",
 "defaults": {
 "tax_code": null,
 "tax_behavior": null
 },
 "head_office": null,
 "livemode": false,
 "status": "pending",
 "status_details": {
 "pending": {
 "missing_fields": ["head_office"]
 }
 }
}
```

## Configure connected account settings

Complete this step when you manage all Stripe Tax configuration through an
interface on your platform.

You can modify the connected account settings through an [update
settings](https://docs.stripe.com/api/tax/settings/update) call. Perform a call
providing the head office location, the preset tax code, and the tax behavior by
using the `Stripe-Account` header with a value of the connected account ID.

```
curl https://api.stripe.com/v1/tax/settings \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "defaults[tax_code]"=txcd_10000000 \
 -d "defaults[tax_behavior]"=inclusive \
 -d "head_office[address][country]"=DE
```

The updated `tax.settings` object now has a head office, a preset tax code, and
a default tax behavior, which allows you to enable Stripe Tax for this connected
account.

```
{
 "object": "tax.settings",
 "defaults": {
 "tax_code": "txcd_10000000",
 "tax_behavior": "inclusive"
 },
 "head_office": {
 "address": {
 "country": "DE"
 }
 },
 "livemode": false,
 "status": "active",
 "status_details": {
 "active": {}
 }
}
```

### Validations and errors

The tax codes must refer to [available tax
codes](https://docs.stripe.com/tax/tax-codes) and the [tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior)
must be set as `inclusive`, `exclusive`, or `inferred_by_currency` (after being
set, it can’t be set to null). The `head_office` must include a supported
address.

The `head_office[address]` has the fields `line1`, `line2`, `city`, `state`,
`postal_code`, and `country`. The tables below describe the supported address
formats.

United StatesCanadaUkraineEverywhere elseExample addresses ExplanationSupported
- `line1`: 27 Fredrick Ave
- `city`: Brothers
- `state`: OR
- `postal_code`: 97712
- `country`: US

**Full address**

A full address includes at least a line1 (street address or PO Box), city,
state, postal code, and country.

The address is matched to the closest address or street in the US Postal Service
address database. If a match isn’t found, we use the geographical center
(average location of addresses) of the 5-digit postal code as a fallback.

9-digit postal code:

- `postal_code`: 97712-4918
- `country`: US

5-digit postal code:

- `postal_code`: 97712
- `country`: US

**Country and postal code**

If you provide a 5-digit or 9-digit postal code, our system only uses the
initial 5 digits for tax calculations. The tax is calculated at the geographical
center, which reflects the average location of addresses within the 5-digit
postal code area. Check that this is [suitable for your
business](https://docs.stripe.com/tax/customer-locations#us-postal-codes).

- `state`: OR
- `country`: US

**Country and state**

We can’t calculate tax for US customers with only an ISO [country
code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and [state
code](https://en.wikipedia.org/wiki/ISO_3166-2).

- `country`: US

**Country**

We can’t calculate tax for US customers with only an [ISO country
code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).

Use one of the above address formats to make sure that we can consistently
recognize your connected account’s head office location. The country field must
always be a valid [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1).

#### Note

The validation and errors listed here are part of the setup phase. You can still
see other errors when trying to [call the API on your Stripe
integration](https://docs.stripe.com/tax/set-up#integrate).

## See also

- [Use the Registrations API to manage tax
registrations](https://docs.stripe.com/tax/registrations-api)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)

## Links

- [Stripe Tax Settings API](https://docs.stripe.com/api/tax/settings)
- [Stripe Dashboard](https://docs.stripe.com/tax/set-up)
- [retrieve the tax.settings
object](https://docs.stripe.com/api/tax/settings/retrieve)
-
[tax.settings.updated](https://docs.stripe.com/api/events/types#event_types-tax.settings.updated)
- [take webhooks live](https://docs.stripe.com/webhooks#register-webhook)
-
[status_details[pending][missing_fields]](https://docs.stripe.com/api/tax/settings/object#tax_settings_object-status_details-pending-missing_fields)
- [update settings](https://docs.stripe.com/api/tax/settings/update)
- [available tax codes](https://docs.stripe.com/tax/tax-codes)
- [tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior)
- [suitable for your
business](https://docs.stripe.com/tax/customer-locations#us-postal-codes)
- [country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)
- [state code](https://en.wikipedia.org/wiki/ISO_3166-2)
- [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1)
- [call the API on your Stripe
integration](https://docs.stripe.com/tax/set-up#integrate)
- [Use the Registrations API to manage tax
registrations](https://docs.stripe.com/tax/registrations-api)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)