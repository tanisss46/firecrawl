# Documents

## Show a list of documents available for download.

Documents renders a list of [tax
invoices](https://support.stripe.com/topics/tax-invoices) available for download
for the connected account.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable documents
by specifying `documents` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[documents][enabled]"=true
```

After creating the account session, you can [initialize
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
and render the documents component in the front end:

```
// Include this element in your HTML
const documents = stripeConnectInstance.create('documents');
container.appendChild(documents);
```

## Links

- [tax invoices](https://support.stripe.com/topics/tax-invoices)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initialize
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)