# User roles

## Give team members controlled access to your Stripe account.

Admin roles
##### Administrator

This role is for anyone who needs similar access as the account owner—they can
see and manage almost everything.They can't delete the default bank account, or
change the account owner.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:adminView details
##### IAM Administrator

The Identity and Access Management (IAM) Admin role is for people who need to
invite team members and assign roles. They can also remove any user, including
Administrators and Super Administrators.They can't do anything beyond access
management. They also can't assign a user to the Administrator or Super
Administrator role.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:iam_adminView details
##### Super Admininistrator

This role is assigned to the creator of a business account and should only be
assigned to users who are allowed to perform all privileged actions. Only a
Super Administrator can assign the Super Administrator role to other team
members.Change the account owner (only the owner can transfer
ownership).[SSO](https://docs.stripe.com/dashboard/sso) Role ID:super_adminView
detailsImportantThese roles can invite additional users to your account, and if
compromised by an attacker would allow them to invite users under their
control.Account ownerAn Account Owner is a special type of Administrator that
can perform all actions, including closing the account.
There can only be one Owner for an account. To change the Account Owner, please
refer to [this
guide](https://support.stripe.com/questions/change-the-owner-of-a-stripe-account).Connect
rolesThese roles are only available if you use
[Connect](https://docs.stripe.com/connect)
##### Connect Onboarding Analyst

This role is for people who need to create connected accounts and edit their
identity information.They can't do anything on the platform account except view
and edit connected accounts.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:connect_onboarding_analystView details
##### Transfer Analyst

Your account must require [two-step
authentication](https://support.stripe.com/questions/two-step-authentication-requirement)
in order to allow non-Administrators with this role to transfer funds.This role
is for people who need to transfer funds to connected accounts and view the
platform’s balance and historical payouts.They can't pay out money to external
bank accounts, add or edit bank accounts, or create new connected
accounts.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:transfer_analystView detailsDeveloper roles
##### Developer

This role is for developers who need to set up a Stripe integration. This role
has access to the secret key, which grants access to almost all API
resources.They can't invite team members or change the account
owner.[SSO](https://docs.stripe.com/dashboard/sso) Role ID:developerView
detailsIdentity rolesThese roles are only available if you use
[Identity](https://docs.stripe.com/identity)
##### Identity Analyst

This role is for Identity users who need to create, review, cancel, or redact
verifications.This role can’t edit verifications for connected
accounts.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:identity_analystView details
##### Identity View Only

This role is for Identity users who need to view verification data.This role
can’t create, review, cancel, or redact
verifications.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:identity_view_onlyView detailsPayment roles
##### Analyst

This role is for people who need to pay out money, refund payments, and export
data.They can't edit payout schedules or account
settings.[SSO](https://docs.stripe.com/dashboard/sso) Role ID:analystView
details
##### Dispute Analyst

This role is for people who need need to view, submit evidence for, and accept
disputes.They can't do anything that's not related to
disputes.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:dispute_analystView details
##### Refund Analyst

This role is for people who need to refund payments and issue credit notes on
invoices.They can’t create payments, view balance, or view connected
accounts.[SSO](https://docs.stripe.com/dashboard/sso) Role ID:refund_analystView
detailsSupport roles
##### Data Migration Specialist

This role is for people who need to perform data migrations (copy, import,
export) for their account.They can't create connected accounts, transfer funds,
payout money, or edit any account and product
settings.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:data_migration_specialistView details
##### Support Associate

This role is for people who need to refund payments and resolve disputes, but
should not have the ability to edit products. It has administration permissions
for connected accounts, where it can edit the payout schedule, update the legal
entity, update the bank account, and more.They can't create connected accounts,
transfer funds, payout money, or edit any account or product
settings.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:support_associateView details
##### Support Communications

This role is for people who need to authenticate email support cases, use
Support Center to view and respond to support cases, or share files securely
with Stripe.They can’t access financial information, transfer funds, access or
edit connected accounts, or edit any account and product
settings.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:support_communicationsView details
##### Support Specialist

This role is for people who need to refund payments, resolve disputes, and may
need to update products. It has administration permissions for connected
accounts, where it can edit the payout schedule, update the legal entity, and
more. This role can add, edit, and delete products.They can't create connected
accounts, transfer funds, payout money, or edit any account
settings.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:support_specialistView detailsTax form rolesThese roles are only available if
you use [1099s](https://docs.stripe.com/connect/tax-reporting)
##### Tax Analyst

This role is for people who need to configure tax form settings, file tax forms
for connected accounts, and export data.They can't create connected accounts,
transfer funds, payout money, or edit account and non-Tax product
settings.[SSO](https://docs.stripe.com/dashboard/sso) Role ID:tax_analystView
detailsView only roles
##### View Only

This role is for people who need to view payments, balance, and connected
accounts, but can’t edit any of them. This role can also export data and
download reports.They can't create connected accounts, transfer funds, payout
money, or edit any account and product
settings.[SSO](https://docs.stripe.com/dashboard/sso) Role ID:view_onlyView
detailsOther roles
##### Top-up Specialist

This role gives access to the Top-ups feature, including creating, viewing, and
updating top-ups, as well as viewing balance and payouts. Accountants or
Financial employees may find this useful.They can't access any other Stripe
features.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:topup_specialistView details
##### Financial Connections Specialist

This role gives edit access to the Financial Connections settings page and
Financial Connections application.They can't access any other Stripe
features.[SSO](https://docs.stripe.com/dashboard/sso) Role
ID:financial_connections_specialistView details

## Links

- [SSO](https://docs.stripe.com/dashboard/sso)
- [this
guide](https://support.stripe.com/questions/change-the-owner-of-a-stripe-account)
- [Connect](https://docs.stripe.com/connect)
- [two-step
authentication](https://support.stripe.com/questions/two-step-authentication-requirement)
- [Identity](https://docs.stripe.com/identity)
- [1099s](https://docs.stripe.com/connect/tax-reporting)