# Testing financial account integration

## Learn how to ensure your financial accounts are functioning correctly.

Stripe Treasury includes a live mode and test mode. You can toggle between modes
from your Dashboard using the mode toggle in the upper-right corner.

![Upper-corner of Dashboard with a red box highlighting the test mode
toggle.](https://b.stripecdn.com/docs-statics-srv/assets/test-mode.13546c94012a516a6d6069120f064c99.png)

Test mode toggle

#### Note

You must complete the [Gaining API access to
Treasury](https://docs.stripe.com/treasury/access) guide’s live mode steps
before you have access to live mode financial accounts.

To access test mode in the API, use the test mode API key with your requests.
The test mode API key is included within most documentation code examples, but
you can also find it in the **Developers** page of your
[Dashboard](https://dashboard.stripe.com/test/apikeys). Make sure to use the
test key for testing and not the live one. The test key has the form
`sk_test_xxx`, whereas the live key is in the form `sk_live_xxx`.

Before creating a test financial account, create a test connected account using
`POST /v1/accounts`. Use the connected account ID you receive from the response
to assign the financial account you create in the next step to this account.
Treasury is supported only in the US, so assign `US` to the `country` parameter.
You’re also requesting capabilities for the connected account that Treasury
requires to function properly. Make note of the `id` value in the response. As
mentioned, you use the ID as the value for the `Stripe-Account` header in the
following code example.

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d country=US \
 -d type=custom \
 -d business_type=company \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 -d "capabilities[treasury][requested]"=true
```

If successful, the response returns the new connected account
[Account](https://docs.stripe.com/api/accounts) object.

```
{
 "id": "{{CUSTOM_ACCOUNT_ID}}",
 "livemode": false,
 ...
}
```

Next, create a financial account using `POST /v1/treasury/financial_accounts`.
Include a `Stripe-Account` header set to the value of the connected account ID
you created in the previous instruction. The only required value in the body is
to set `supported_currencies[]` to `usd`. To learn more about financial
accounts, see [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
or the
[FinancialAccounts](https://docs.stripe.com/api/treasury/financial_accounts)
object description in the Stripe API reference.

```
curl https://api.stripe.com/v1/treasury/financial_accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "supported_currencies[]"=usd \
 -d "features[financial_addresses][aba][requested]"=true
```

If successful, the response returns the newly created `FinancialAccount` object.

```
{
 "id": "{{FINANCIAL_ACCOUNT_ID}}",
 "livemode": false,
 "active_features": [],
 "pending_features": [],
 "restricted_features": ["financial_addresses.aba"],
 ...
}
```

You now have a test mode financial account attached to a test mode connected
account. However, the connected account hasn’t been onboarded so required
information is missing from the `requirements` hash. If you call `GET
/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}` using the financial
account ID in the JSON response of the previous instruction, you see the
`financial_addresses` array of hashes has an entry for the requested `aba` with
a `status` of `restricted` because the connected account has
`requirements_past_due`.

```
{
 …
 "financial_addresses": {
 "aba": {
 "requested": true,
 "status": "restricted",
 "status_details": [
 {
 "code": "requirements_past_due",
 "resolution": "provide_information"
 }
 ]
 }
 }
 …
}
```

To enable requested features on your test mode financial account without first
going through connected account onboarding, you must use `POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}` to [provide test
values](https://docs.stripe.com/connect/testing-verification) that fulfill all
the requirements, as in the following request that uses a previously created
connected account to apply the required account details.

#### Note

You can’t create a test mode financial account attached to a live mode connected
account.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "tos_acceptance[date]"=1547923073 \
 -d "tos_acceptance[ip]"="172.18.80.19" \
 -d "settings[treasury][tos_acceptance][date]"=1547923073 \
 -d "settings[treasury][tos_acceptance][ip]"="172.18.80.19" \
 -d "business_profile[mcc]"=5045 \
 --data-urlencode "business_profile[url]"="https://bestcookieco.com" \
 -d "company[address][city]"=Schenectady \
 -d "company[address][line1]"="123 State St" \
 -d "company[address][postal_code]"=12345 \
 -d "company[address][state]"=NY \
 -d "company[tax_id]"=000000000 \
 -d "company[name]"="The Best Cookie Co" \
 -d "company[phone]"=8888675309 \
 -d "individual[first_name]"=Jenny \
 -d "individual[last_name]"=Rosen
```

## Links

- [Gaining API access to Treasury](https://docs.stripe.com/treasury/access)
- [Dashboard](https://dashboard.stripe.com/test/apikeys)
- [Account](https://docs.stripe.com/api/accounts)
- [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [FinancialAccounts](https://docs.stripe.com/api/treasury/financial_accounts)
- [provide test values](https://docs.stripe.com/connect/testing-verification)
- [https://bestcookieco.com](https://bestcookieco.com)