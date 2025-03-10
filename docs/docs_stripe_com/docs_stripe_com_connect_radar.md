# Use Radar with Connect

## Learn how to use Stripe Radar to identify fraud in Connect account charges.

[Stripe Radar](https://docs.stripe.com/radar) uses machine learning to identify
fraudulent payments in real time. When you use Radar with connected accounts, it
checks only external charges. It doesn’t check fund transfers between Stripe
accounts.

[Charges in a Connect
integration](https://docs.stripe.com/connect/charges#types) fall into two
categories:

- **Direct charges**: Paid directly to a connected account; Stripe applies only
the collecting account’s Radar configuration and rules
- **Transferred charges** (for example, destination charges or separate charges
and transfers): Paid to the platform account and transferred to a connected
account; Stripe applies only the platform account’s Radar configuration and
rules

## Radar fees

Stripe charges Radar fees based on the rate for the account that collected the
payment. For payments collected by the platform account and transferred to a
connected account, you can pass Radar fees to the connected account by reducing
the transferred amount.

## Radar configuration for a connected account

The Dashboard you use to configure Radar for a connected account depends on the
connected account type. The following table shows which Dashboard to use for
each account type.

Dashboard access of the connected account Connected account Dashboard Platform
account Dashboard Connect page Connected accounts with access to the Stripe
Dashboard Connected accounts with access to the Express Dashboard Connected
accounts with no dashboard access
## Radar behavior

Radar behavior for connected account payments depends on the charge category and
connected account type. The following table describes each scenario.

Charge type Radar config rules used Charges visible in connected account
Dashboard Charges visible in platform account Dashboard Connect page Direct for
connected accounts with access to the Stripe Dashboard Connected account Direct
for connected accounts with access to the Express Dashboard Connected account
Direct for connected accounts with no dashboard access Connected account
Transferred from platform account Platform account
## Radar for Fraud Teams

If you have [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you
can [customize your
rules](https://docs.stripe.com/radar/rules#request-3d-secure) to include
[destination charge](https://docs.stripe.com/connect/destination-charges)
attributes. You can either use the `destination` attribute in the [supported
rule attributes](https://docs.stripe.com/radar/rules/supported-attributes), or
use custom [metadata on the destination
account](https://docs.stripe.com/radar/rules/reference#metadata-attributes).

## See also

- [Choose your connected account type](https://docs.stripe.com/connect/accounts)
- [Radar documentation](https://docs.stripe.com/radar)

## Links

- [Stripe Radar](https://docs.stripe.com/radar)
- [Charges in a Connect
integration](https://docs.stripe.com/connect/charges#types)
- [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)
- [customize your rules](https://docs.stripe.com/radar/rules#request-3d-secure)
- [destination charge](https://docs.stripe.com/connect/destination-charges)
- [supported rule
attributes](https://docs.stripe.com/radar/rules/supported-attributes)
- [metadata on the destination
account](https://docs.stripe.com/radar/rules/reference#metadata-attributes)
- [Choose your connected account type](https://docs.stripe.com/connect/accounts)