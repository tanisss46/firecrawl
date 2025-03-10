# Mirakl Connector configuration

## Define your integration variables.

Before installing the connector, prepare a file with the variables below.

We provide a [configuration file
sample](https://github.com/stripe/stripe-mirakl-connector/blob/master/.env.dist)
in our repository that you can copy and rename to `.env`.

## General settings

ParameterDescriptionAPP_SECRETTo be generated. Commonly used to add more entropy
to security related operations. Learn more on the [Symfony
documentation](https://symfony.com/doc/current/reference/configuration/framework.html#secret).OPERATOR_PASSWORDTo
be generated. Used to secure requests to the API exposed by the connector. Set
the `X-AUTH-TOKEN` header to this value when calling the API.DATABASE_URLThe
connection URL to your database. Learn more on the [Doctrine
documentation](https://www.doctrine-project.org/projects/doctrine-dbal/en/2.9/reference/configuration.html#connecting-using-a-url).
For example,
`pgsql://symfony:symfony@db:5432/symfony?charset=UTF-8`.MESSENGER_TRANSPORT_DSNThe
transport used for the queuing system. See the [Symfony Messenger
documentation](https://symfony.com/doc/current/messenger.html#transports-async-queued-messages)
for supported transports. For example,
`amqp://guest:guest@localhost:5672/%2f/messages`. Defaults to
`doctrine://default`.STRIPE_CLIENT_SECRETYour Stripe API secret key available in
your [API keys settings](https://dashboard.stripe.com/apikeys). We recommend
creating a specific API key for the connector. Restricted keys are not
supported.MIRAKL_HOST_NAMEHost name of your Mirakl Instance. For example,
`https://mymarketplace.mirakl.net`.MIRAKL_API_KEYThe Mirakl operator key. Can be
generated as a Mirakl operator in your API settings. We recommend creating a
specific operator for the connector.
## Onboarding

ParameterDescriptionREDIRECT_ONBOARDINGThe connector redirects the seller to
this URL after completing their account creation on Stripe. Defaults to
`$MIRAKL_HOST_NAME/mmp/shop/account/shop`.BASE_HOSTThe domain of the server
hosting your connector. For example, `stripe-mirakl.example.com`.SCHEMEThe
scheme used by your base host. Defaults to
`https`.STRIPE_SELLERS_WEBHOOK_SECRETYour Stripe webhook secret available in
your [Connect webhook settings](https://dashboard.stripe.com/webhooks) when
adding the endpoint, see below.MIRAKL_CUSTOM_FIELD_CODECode of the custom field
that you have to add, see below. Defaults to `stripe-url`.
### Add a Stripe webhook endpoint for connected accounts

- Go to your [webhook settings](https://dashboard.stripe.com/webhooks).
- Add a [webhook](https://docs.stripe.com/webhooks) endpoint.
- Set the URL to `<BASE_HOST>/api/public/webhook/sellers`.
- Select **Listen to events on Connected accounts**.
- Add `account.updated` in the **Events to send**:
- Click **Add endpoint**.
- Use the webhook secret for the `STRIPE_SELLERS_WEBHOOK_SECRET` environment
variable.

### Add a custom field to your Mirakl shops

- Log in to your Mirakl back office as an Operator.
- Visit **Settings** > **Advanced Parameters** > **Shops**.
- Go to the **Custom Fields** tab.
- Use the following values to create a new field:
Parameter DescriptionCodeUse `stripe-url` unless you chose a different key in
your environment file.Type`Link`Shops permissions`Read only`Required field`No`
## Payments

ParameterDescriptionPAYMENT_METADATA_COMMERCIAL_ORDER_IDMetadata key used in
Charges to convey the Mirakl commercial order ID. Defaults to
`mirakl_commercial_order_id`.ENABLE_PRODUCT_PAYMENT_SPLITEnable the [payment
split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-split) for
product orders. Defaults to `false`.ENABLE_SERVICE_PAYMENT_SPLITEnable the
[payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-split) for
service orders. Defaults to `false`.ENABLE_PRODUCT_PAYMENT_REFUNDEnable the
[payment refund
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-refund) for
product orders. Defaults to `false`.ENABLE_SERVICE_PAYMENT_REFUNDEnable the
[payment refund
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-refund) for
service orders. Defaults to `false`.STRIPE_OPERATOR_WEBHOOK_SECRETYour Stripe
webhook secret available in your [account webhook
settings](https://dashboard.stripe.com/webhooks) when adding the endpoint, see
below.
### Add a Stripe webhook endpoint for your account

- Go to your [webhook settings](https://dashboard.stripe.com/webhooks).
- Add a webhook endpoint for your **account**.
- Set the URL to `<BASE_HOST>/api/public/webhook/operator`.
- Add the following in the **Events to send**: `charge.succeeded`,
`charge.updated`.
- Click **Add endpoint**.
- Use the webhook secret for the `STRIPE_OPERATOR_WEBHOOK_SECRET` environment
variable.

## Notifications and alerting

ParameterDescriptionMAILER_DSNThe entire Symfony Mailer configuration using a
DSN-like URL format. Learn more on the [Symfony
documentation](https://symfony.com/doc/current/components/mailer.html#mailer-dsn).
For example, `smtp://user:pass@host:port`. Defaults to `smtp://null` (mailer
disabled).TECHNICAL_ALERT_EMAILThe recipicient of all technical alerts. For
example, `myemail@example.com`. Defaults to empty. Required if mailer is enabled
per `MAILER_DSN`.TECHNICAL_ALERT_EMAIL_FROMThe sender of all technical emails.
Defaults to empty, required if mailer is configured. For example,
`noreply@example.com`.OPERATOR_NOTIFICATION_URLThe endpoint on your server set
to receive notifications from the connector. Defaults to empty (notifications
disabled).MAIL_ON_NOTIFICATION_ENDPOINT_DOWNEnable email alerts if a URL is
provided in `OPERATOR_NOTIFICATION_URL` and that URL is not available or
responds with an error. Defaults to
`true`.MAIL_ON_NOTIFICATION_ENDPOINT_DOWN_COOLDOWNTime between each email alert.
Use `0` to disable throttling. The maximum value depends on the notification
worker maximum life, that is, `3600` by default. Defaults to `10`.
## See also

- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps).

## Links

- [configuration file
sample](https://github.com/stripe/stripe-mirakl-connector/blob/master/.env.dist)
- [Symfony
documentation](https://symfony.com/doc/current/reference/configuration/framework.html#secret)
- [Doctrine
documentation](https://www.doctrine-project.org/projects/doctrine-dbal/en/2.9/reference/configuration.html#connecting-using-a-url)
- [Symfony Messenger
documentation](https://symfony.com/doc/current/messenger.html#transports-async-queued-messages)
- [API keys settings](https://dashboard.stripe.com/apikeys)
- [Connect webhook settings](https://dashboard.stripe.com/webhooks)
- [webhook](https://docs.stripe.com/webhooks)
- [payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-split)
- [payment refund
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-refund)
- [Symfony
documentation](https://symfony.com/doc/current/components/mailer.html#mailer-dsn)
- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps)