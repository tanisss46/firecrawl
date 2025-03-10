# Use the Registrations API to manage tax registrations

## Learn how to add, schedule, and check active tax registrations.

Businesses are required to register to collect taxes in locations where they
have tax obligations. The [Tax Registration
API](https://docs.stripe.com/api/tax/registrations) lets you retrieve and
configure tax registrations using an API instead of the Dashboard. Adding your
registrations in Stripe turns on tax calculation and collection for your
transactions made through Stripe.

Different rules determine when and how a business needs to register to collect
tax depending on the location. You can also use [Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register) on your behalf or
do it yourself. [Learn more about tax collection in different
locations](https://docs.stripe.com/tax/supported-countries).

- **Connect platform**: As a platform, you can use this API to manage the
registrations of your connected accounts or to check an account’s active
registrations.
- **Direct usage**: You can use this API to manage and check your registrations.
Connect platformDirect usage
## List all tax registrations for your connected accounts

To get a list of your connected accounts’ tax registrations, make a [list
registrations](https://docs.stripe.com/api/tax/registrations/all) call. You can
filter the response by setting the `status` parameter to `active`, `expired`, or
`scheduled`.

```
curl -G https://api.stripe.com/v1/tax/registrations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d status=active \
 -d limit=3
```

If your connected accounts don’t have access to the Stripe Dashboard, your
platform can provide a UI for them to manage their tax registrations. The
registrations endpoint helps you implement that functionality.

## Add a tax registration for your connected account

If a tax obligation and registration of the connected account is known to the
platform, you can perform a [create
registration](https://docs.stripe.com/api/tax/registrations/create) call using
the `Stripe-Account` header with a value of the connected account ID to add or
schedule the registration for the connected account.

```
curl https://api.stripe.com/v1/tax/registrations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d country=IE \
 -d "country_options[ie][type]"=oss_union \
 -d active_from=now
```

In this case, a `tax.registration` object is created in the connected account.

```
{
 "object": "tax.registration",
 "active_from": 1669249440,
 "country": "IE",
 "country_options": {
 "ie": {
 "type": "oss_union"
 }
 },
 "livemode": false,
 "status": "active",
 ...
}
```

Alternatively, for connected accounts with access to the Stripe Dashboard (for
example, Standard accounts), you can instruct them to [set up Stripe
Tax](https://docs.stripe.com/tax/set-up) using the Dashboard, which includes
adding tax registrations.

### Head office address requirement

To add a tax registration, the connected account must first set up a head office
address. Without a defined head office address, an `invalid_request_error` gets
triggered with a message about setting your head office address.

Use the [tax settings API](https://docs.stripe.com/tax/settings-api) to add a
head office address as a platform:

```
curl https://api.stripe.com/v1/tax/settings \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "head_office[address][country]"=DE
```

Location-specific validation and errors might occur, details of which are found
in our [tax settings
guide](https://docs.stripe.com/tax/settings-api?tax-integration=connect-platform#validations-and-errors).

## Update and expire a tax registration for your connected account

You can’t delete a registration after it’s created, but you can end it by
setting `expires_at` to a time when the registration is no longer active. Update
the registrations with an [update
registration](https://docs.stripe.com/api/tax/registrations/update) call using
the Stripe-Account header with a value of the connected account ID:

```
curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d expires_at=now
```

In this case, the registration expires immediately. [Tax
calculations](https://docs.stripe.com/api/tax/calculations) performed for the
connected account after the `expires_at` won’t use this registration.

```
{
 "object": "tax.registration",
 "active_from": 1669248000,
 "created": 1669219200,
 "expires_at": 1669334400,
 "livemode": false,
 "status": "active",
 ...
}
```

[OptionalAdd a tax registration for the retail delivery
feeServer-side](https://docs.stripe.com/tax/registrations-api#tax-registration-retail-delivery-fee)
## See also

- [Use the Settings API to configure Stripe
Tax](https://docs.stripe.com/tax/settings-api)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)

## Links

- [Tax Registration API](https://docs.stripe.com/api/tax/registrations)
- [Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
- [Learn more about tax collection in different
locations](https://docs.stripe.com/tax/supported-countries)
- [list registrations](https://docs.stripe.com/api/tax/registrations/all)
- [create registration](https://docs.stripe.com/api/tax/registrations/create)
- [set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [tax settings API](https://docs.stripe.com/tax/settings-api)
- [tax settings
guide](https://docs.stripe.com/tax/settings-api?tax-integration=connect-platform#validations-and-errors)
- [update registration](https://docs.stripe.com/api/tax/registrations/update)
- [Tax calculations](https://docs.stripe.com/api/tax/calculations)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)