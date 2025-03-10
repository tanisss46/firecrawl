# Mirakl Connector installation

## Install and validate the Miraki connector for Stripe.

## Requirements

Installing and running the application requires the following:

- PHP 7.3+
- PostgreSQL
- A web server, Nginx recommended
- A valid SSL/[TLS](https://docs.stripe.com/security/guide#tls) certificate
- Supervisord or equivalent
- Crontab or equivalent

## Install using Docker

You can build and start the application by embedding it in a container. See our
[Docker
sample](https://github.com/stripe/stripe-mirakl-connector/tree/master/examples/docker)
for more information.

## Install manually

- Install [Composer](https://getcomposer.org/download/).
- Clone or download the [Mirakl
Connector](https://github.com/stripe/stripe-mirakl-connector.git) from GitHub.
- Move the content to your web server directory, for example, `/var/www`.
- Download dependencies:

```
composer install --prefer-dist --no-dev
```

- Make sure you properly configured the [.env
file](https://docs.stripe.com/connectors/mirakl/configuration).
- Run the migrations to set up the database:

```
bin/console doctrine:migration:migrate --no-interaction
```

If you encounter any errors at this stage, check the `DATABASE_URL` variable in
your .env file.

- Update your supervisor to automatically start and restart the workers.

A [configuration
example](https://github.com/stripe/stripe-mirakl-connector/blob/master/examples/docker/app/config/supervisord.conf)
is available in our Docker sample. You can skip this step in a development
environment and start the workers manually when needed, for example:

```
php bin/console messenger:consume process_transfers --time-limit=3600 --env=prod
```

- Update your job scheduler to run the commands periodically.

A [configuration
example](https://github.com/stripe/stripe-mirakl-connector/blob/master/examples/docker/app/config/crontab)
is available in our Docker sample. You can skip this step in a development
environment and start the jobs manually when needed, for example:

```
php bin/console connector:dispatch:process-transfer -q 2>&1
```

- Make sure that your web server is configured to use the `public` directory as
document root.

## Check your installation

Open your terminal and run the following command to confirm that your
application is up and running correctly:

```
curl -X GET "https://connector-url/api/mappings" \
 -H "accept: application/json" \
 -H "X-AUTH-TOKEN: $OPERATOR_PASSWORD"
```

You should get a `200` response code along with an empty payload.

## Security

On your server, *restrict all inbound traffic* to the connector except for the
following endpoints:

- **/api/public/onboarding/refresh**

Stripe redirects the seller to this URL to get a new onboarding link if it
expires.
- **/api/public/webhook/operator**

Stripe notifies this endpoint when a payment is updated to map it with a Mirakl
order within the connector.
- **/api/public/webhook/sellers**

Stripe notifies this endpoint when a Stripe account is updated to synchronize
the seller’s status within the connector.

These endpoints are safe to expose, they each have an internal protection
mechanism. Other endpoints are not safe to expose unless protected by a strong
`OPERATOR_PASSWORD`.

## See also

- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps).

## Links

- [TLS](https://docs.stripe.com/security/guide#tls)
- [Docker
sample](https://github.com/stripe/stripe-mirakl-connector/tree/master/examples/docker)
- [Composer](https://getcomposer.org/download/)
- [Mirakl Connector](https://github.com/stripe/stripe-mirakl-connector.git)
- [.env file](https://docs.stripe.com/connectors/mirakl/configuration)
- [configuration
example](https://github.com/stripe/stripe-mirakl-connector/blob/master/examples/docker/app/config/supervisord.conf)
- [configuration
example](https://github.com/stripe/stripe-mirakl-connector/blob/master/examples/docker/app/config/crontab)
- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps)