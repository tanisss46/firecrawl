# Supported Organization setupsPublic preview

## Learn about different account setups that you can add to an organization.

Organizations support the following account setups: multiple standalone
accounts, platforms, and connected accounts.

## Multiple standalone accounts

It’s common to manage multiple Stripe accounts that represent different business
lines, countries of operation, legal entities, and acquisitions.

![Multiple standalone
accounts](https://b.stripecdn.com/docs-statics-srv/assets/structure_1_before.c8b529f41e4ff0dbe8beea36e1dca3b6.png)

Multiple standalone accounts representing different business lines.

After you [add these accounts to an
organization](https://docs.stripe.com/get-started/account/orgs/build), you can
search and download consolidated reports across your accounts without any
changes to your Stripe integration. After you create an organization, you can
add new business lines or add existing accounts.

![Organization with multiple standalone
accounts](https://b.stripecdn.com/docs-statics-srv/assets/structure_1.fccd75f80ce664be76a7f5dc6f51008b.png)

Organization with multiple accounts representing different business lines.

## Multiple platform accounts

If you have several platform accounts that correspond to different countries of
operation or business lines, you can add them to an organization.

![Organization with multiple Connect
platforms](https://b.stripecdn.com/docs-statics-srv/assets/structure_2_before.fba9132b399f3a6155b36fdb092493b2.png)

Multiple standalone platform accounts representing different business lines,
each with connected accounts.

After you add your platforms to an organization, you can search for connected
accounts under all your platforms, as well as data within each platform account.

![Organization with multiple Connect
platforms](https://b.stripecdn.com/docs-statics-srv/assets/structure_2.7a6b0bd2eb1da064944eb16f21e047d0.png)

Organization with multiple platform accounts representing different business
lines, each with connected accounts.

## Multiple connected accounts under a Connect platform

In certain cases, you might own multiple connected accounts under a platform.
This commonly occurs in franchise groups where several franchises are under
common ownership.

![Organization with multiple Connect
platforms](https://b.stripecdn.com/docs-statics-srv/assets/structure_3_before.702c4fa894523d6e1a66e1111b9d3bac.png)

Multiple connected accounts (Acme Dealer of Seattle and Acme Dealer of Tacoma)
that belong to the same owner and under a platform.

Even though your connected accounts are under a platform, you can still add them
to an organization. This allows you to use the unified search and reporting
across your accounts.

![Organization with multiple Connect
platforms](https://b.stripecdn.com/docs-statics-srv/assets/structure_3.e8675ca3654841a4397bc2e2eacc4771.png)

Organization (Acme Dealer Group) with multiple connected accounts (Acme Dealer
of Seattle and Acme Dealer of Tacoma) under common ownership.

## Multiple business lines represented as connected accounts

In some cases, you might have represented different business lines as connected
accounts under one platform account, even though your business isn’t a
traditional platform or marketplace. This is common if you want to consolidate
payment integrations or clone payment methods stored in the platform to
connected accounts.

![Organization with multiple accounts setup using
Connect](https://b.stripecdn.com/docs-statics-srv/assets/structure_4_before.e35e09f6d8127fb01f240a30834b99b7.png)

A platform account and multiple connected accounts, each representing different
business lines.

You can create an organization that encompasses the platform account and
connected accounts so that your team can benefit from unified search and
reporting across all the accounts, without impacting your payment integrations.

![Organization with multiple accounts setup using
Connect](https://b.stripecdn.com/docs-statics-srv/assets/structure_4.29084c115c8f08dc82468dfc03005096.png)

Organization with a platform account and multiple connected accounts,
representing different business lines.

## See also

- [Build an
organization](https://docs.stripe.com/get-started/account/orgs/build)

## Links

- [add these accounts to an
organization](https://docs.stripe.com/get-started/account/orgs/build)