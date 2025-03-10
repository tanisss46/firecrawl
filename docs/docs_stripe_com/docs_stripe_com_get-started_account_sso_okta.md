# Single sign-on with OktaPublic preview

## Learn how to setup single sign-on in the Dashboard with Okta.

Stripe supports Single Sign-On (SSO), allowing you to manage your team’s access
and roles through your identity provider (IdP). This means your team can access
Stripe without needing separate passwords. When SSO is configured, users (team
members) are automatically redirected to your IdP for authentication when they
sign in to Stripe.

Your IdP verifies if they have a valid role assignment to your Stripe accounts
or [organization](https://docs.stripe.com/get-started/account/orgs/sso), and
generates a SAML assertion used by Stripe to assign the proper roles in the
Stripe Dashboard. When your account requires SSO, you must update team roles
through your Identity Provider (IdP) for security. Changes to a team member’s
roles only appear in Stripe after they sign in to the Dashboard again using the
updated SAML assertion.

[Verify domain
ownership](https://docs.stripe.com/get-started/account/sso/okta#verify-domain-verification)
A domain is the portion of an email address after the `@` symbol (such as
`kavholm.com`). You must configure SSO for Stripe for each of your business’s
email domains. To verify domain ownership:

- Navigate to [User
authentication](https://dashboard.stripe.com/settings/security/authentication)
in the Stripe Dashboard, and click **+ New domain** to view your account’s
unique verification code.
```
 stripe-verification=4242424242424242424242

```
- Add the verification code as a `TXT` record to your Domain Name System (DNS)
provider.
- Return to the Stripe Dashboard, and click **Save and verify**. Depending on
your DNS provider, it can take 24 hours or more to verify your domain.
- After successful verification, don’t delete the `TXT` record from your DNS
provider. If you delete it, you might lose access to the Dashboard because
Stripe frequently checks the DNS records of your domain.

#### Multiple Stripe accounts support

If you’re configuring SSO for multiple Stripe accounts, you must create an
[organization](https://docs.stripe.com/get-started/account/orgs) to centrally
configure SSO across all of your accounts. Alternatively, contact [Stripe
support](https://support.stripe.com/) to verify your domain across separate
accounts with one shared verification code.

[Create a Stripe app in
Okta](https://docs.stripe.com/get-started/account/sso/okta#create-app)
Create an app in Okta to represent the relationship between the Stripe Dashboard
and Okta:

- Open and log in to the Okta admin portal.
- In the left navigation pane, navigate to **Dashboard** > **Applications** >
**Add Application**.
- Click **Create App Integration** > **SAML 2.0** > **Next**.
- Enter an **App name** (for example `Stripe Integration`), then click **Next**.
- Configure your SAML settings in Okta:- For **Single sign-on URL**, add the
value: `https://dashboard.stripe.com/login/saml/consume`.
- For **Audience URI**, add the value:
`https://dashboard.stripe.com/saml/metadata`.
- For **Name ID format**, select `EmailAddress`.
- For **Application username**, select `Email`.
- Next, click **Show Advanced Settings**:- For **Signature Algorithm**, select
`RSA-SHA256`.
- For **Digest Algorithm**, select `SHA256`.
- Click **Next**, then select **This is an internal app that we created** for
**App type**.
- Click **Finish**.
[Assign Stripe roles in
Okta](https://docs.stripe.com/get-started/account/sso/okta#assign-stripe-roles)
Assign Stripe roles for your users by creating attribute statements in your
Stripe app in Okta. Stripe roles give users different degrees of access to the
Stripe Dashboard. An attribute statement consists of two components. The `name`
represents the Stripe account where you want to assign roles. The `value`
represents the roles you want to assign to the Stripe account. Users can have
different roles in a single account or across multiple accounts in an
[organization](https://docs.stripe.com/get-started/account/orgs/sso).

Stripe supports the following roles. Some of these roles are only available if
your account uses the applicable Stripe product. For more information, see [User
roles supported by
Stripe](https://docs.stripe.com/get-started/account/teams/roles).

RoleValueAdministrator`admin`Analyst`analyst`Cardholder`cardholder`Connect
Onboarding Analyst`connect_onboarding_analyst`Connect Risk
Analyst`connect_risk_analyst`Data Migration
Specialist`data_migration_specialist`Developer`developer`Dispute
Analyst`dispute_analyst`Financial Connections
Specialist`financial_connections_specialist`IAM Admin`iam_admin`Identity
Analyst`identity_analyst`Identity View only`identity_view_only`Issuing Support
Agent`issuing_support_agent`Opal View only`opal_view_only`Sandbox
Administrator`sandbox_admin`Sandbox User`sandbox_user`Super
Administrator`super_admin`Support Associate`support_associate`Support
Communications`support_communications`Support only`support_only`Support
Specialist`support_specialist`Refund Analyst`refund_analyst`Tax
Analyst`tax_analyst`Terminal Specialist`terminal_specialist`Topups
only`topups_only`Top-up Specialist`topup_specialist`Transfer
Analyst`transfer_analyst`View only`view_only`
### Create a custom role attribute

- In the left navigation pane, navigate to **Directory** > **Profile Editor**.
- Click the name of your Stripe app, then click **Add Attribute**.
- Set **Data type** to `String Array`.
- For **Display name**, enter `Stripe Roles`.
- For **Variable name**, enter `stripe_roles`.
- Select **Define enumerated list of values**, then add an attribute member for
each Stripe role you want to assign to your users. For example, Display name:
`Administrator`, Value: `admin`.
#### Warning

Make sure to assign at least one user or group the `super_admin` role. This
ensures your organization receives important notifications about your account
health. Only users with the Super Admin role can make changes to your account
structure, close the account, or change the default bank account.
- For **Attribute required**, select **Yes**.
- For **Attribute type**, select **Group**.
- For **Group Priority**, select **Combine values across groups**. Select this
if you want to assign a user multiple roles across multiple Stripe accounts.
- Click **Save**, and copy the variable name of the attribute you created for
later use.

!

### Create a group of users

- In the left navigation pane, navigate to **Directory** > **Groups**.
- Click **Add group**, enter a group name (such as Super Admins in Stripe), then
click **Save**.
- In the group list, click the name of your group, then click **Assign people**.
- Add users by searching for their first name, primary email address, or
username.

### Grant the group access to the Stripe app

- Click the **Applications** tab > **Assign applications**.
- Next to the name of your Stripe app, click **Assign**.
- Select any Stripe roles you want to give to the group, then click **Save and
go back** > **Done**. This assigns the roles to all the users in this group. All
the users in this group can log into Stripe, and their role is automatically set
to the value you set.

!

If a user belongs to multiple groups, Okta combines the roles assigned across
all the groups. For example, if a user belongs to the following groups:

- `IAM Group`
- `Stripe Admin Group`
- `Stripe Developer Group`

Then, they’re assigned the roles from all of the groups:

!

### Update the value of your attribute statement

- In the left navigation pane, navigate to **Applications**, then click your
Stripe app.
- Click the **General** tab > **SAML settings** > **Edit**.
- In the **Attribute Statements** section, assign a dynamic role to a user:- For
**Name**, enter the Stripe account ID. Use the format
`Stripe-Role-<account-id>`. For example, if the account ID is
`acct_1JgxGwHIzIlFIyZf`, enter the name `Stripe-Role-acct_1JgxGwHIzIlFIyZf`. For
a list of account ids, navigate to the **Accounts** section in your
[Profile](https://dashboard.stripe.com/settings/user) in the Stripe Dashboard.
- For **Name format**, select `Basic`.
- For **Value**, enter `appuser.<variable-name>`. If you didn’t save the
variable name, navigate to **Directory** > **Profile Editor**, click your Stripe
app, and use the variable name next to the applicable attribute. For example,
`appuser.stripe_roles`.
- Click **Save**. This tells Okta to send an attribute statement with each
assertion for the account and role.

### (Optional) Assign roles in multiple Stripe accounts

To assign roles across multiple Stripe accounts, create a separate attribute
statement in your app for each of your accounts.

!

### (Optional) Assign roles in your organization

If you use [Organizations](https://docs.stripe.com/get-started/account/orgs) to
unify your business across multiple Stripe accounts, grant team members access
to your organization by assigning roles in your organization. Remember that
[organization-level
roles](https://docs.stripe.com/get-started/account/orgs/team#organization-level-and-account-level-roles)
grant access to organization dashboard and as well as all accounts in the
organization.

- Find your `organization-id` in Stripe by account switching to your
organizations and navigating to **Settings > Organizations management**.
- In Okta, in your app’s list of **Attribute Statements**, create an attribute
statement using the format `Stripe-Role-<organization-id>`.
[Configure
Stripe](https://docs.stripe.com/get-started/account/sso/okta#configure-stripe)
To configure Stripe with SSO:

### Retrieve the following values from Okta

- Open the Okta admin portal.
- In the left navigation pane, navigate to **Applications**, then select your
Stripe app.
- Click the **Sign On** tab > **View SAML Setup Instructions** to open a page
that displays the following values:- **Identity provider Issuer**: An identifier
of your identity provider.
- **Identity provider single Sign-On URL**: The URL of your identity provider
that your users are redirected to, so they can authenticate.
- **X.509 Certificate**: The X.509 certificate that your identity provider uses
to sign assertions.

### Configure your Stripe account to connect with Okta

- In the Stripe Dashboard, navigate to **Settings** > **Team and security** >
[User authentication](https://dashboard.stripe.com/account/user_authentication).
- Next to the domain name, click the overflow button () > **Manage SSO
settings**.
- Click **Test your configuration** > **Next**.
- Provide info for your identity provider:

- For **Issuer ID**, enter the value for **Identity provider Issuer** in Okta.
- For **Identity provider URL**, enter the value for **Identity provider single
Sign-On URL** in Okta.
- For **Identity provider certificate**, enter the value for **X.509
Certificate** in Okta.
- Click **Test configuration** to open a new window to test your configuration.
Exit this window, and return to the original window.
- If you pass the test, click **Done**.

If the test fails, refer to [Troubleshoot
SSO](https://docs.stripe.com/get-started/account/sso/troubleshooting), and
address the reported issues in your Stripe app in Okta.
- Select SSO enforcement. You can choose between **Off**, **Optional**, or
**Mandatory**. You can change enforcement type in the future.
- Click **Save settings** > **Done**.
[Authenticate with
SSO](https://docs.stripe.com/get-started/account/sso/okta#authenticate-sso)
After you finish configuring SSO, you can inform your users to sign in with any
of these methods:

### Stripe’s sign in page

Users can navigate to the [Stripe sign in
page](https://dashboard.stripe.com/login), enter their email, then select **Use
single sign-on (SSO)**.

If a user has access to multiple accounts, Stripe authenticates them with the
default account connected to the user. If a user only has access to SAML
merchants, or doesn’t have access to any merchants, Stripe redirects them to the
IdP, regardless of the contents in the password field.

### IdP-initiated login

To use IdP-initiated login, your [IdP needs to support Service
Provider-initiated
login](https://docs.stripe.com/get-started/account/sso/troubleshooting). Verify
if this is possible using your IdP’s documentation.

### SSO URL

Use the following login URL with your domain to directly sign in to your account
with SSO. This URL includes the domain and account you want to use for SSO
authentication. If you change the account token at the end of the URL, it
authenticates you against a different account.

```

https://dashboard.stripe.com/login/saml_direct/domain/{{YOUR_DOMAIN}}/merchant/{{STRIPE_ACCOUNT_ID}}

```

#### Support for multiple Stripe accounts

If you’re configuring SSO for multiple Stripe accounts, first create an
[organization](https://docs.stripe.com/get-started/account/orgs) to centrally
configure SSO across all of your accounts. You can change the account token at
the end of the SSO URL to authenticate against another account. You can find the
list of account tokens in the **Accounts** section of your
[Profile](https://dashboard.stripe.com/settings/user).

**Multiple IdP connections:** If you have multiple Stripe businesses with
multiple IdP settings (for example, different SAML endpoints or issuer IDs) but
share the same domain, we recommend using login URLs.

## Revoke team member access

You can revoke a team member’s access using either active or passive methods.

### Actively revoke access with an assertion

Send Stripe an assertion from your identity provider to grant a team member
access to specific Stripe accounts. This also lets you revoke a team member’s
access. To revoke access for a team member, assign them a role of `none` for the
Stripe account’s access you want to revoke. For example:

```
<saml2:attribute name="Stripe-Role-STRIPE-ACCOUNT-ID"
NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
 <saml2:attributevalue>none
 </saml2:attributevalue>
</saml2:attribute>
```

#### Caution

You can’t revoke access for the owner of a Stripe account.

### Passively revoke access with enforcement mode

When **enforcement mode** is set to **required**, only team members who can
authenticate with your identity provider can access your Stripe account. In
**required** mode, you can revoke a team member’s access to a Stripe account by
preventing your identity provider from authenticating them. In the Stripe
Dashboard, set SSO to **required** in [User
authentication](https://dashboard.stripe.com/account/user_authentication).

## See also

- [Troubleshoot
SSO](https://docs.stripe.com/get-started/account/sso/troubleshooting)

## Links

- [organization](https://docs.stripe.com/get-started/account/orgs/sso)
- [User
authentication](https://dashboard.stripe.com/settings/security/authentication)
- [organization](https://docs.stripe.com/get-started/account/orgs)
- [Stripe support](https://support.stripe.com/)
- [User roles supported by
Stripe](https://docs.stripe.com/get-started/account/teams/roles)
- [Profile](https://dashboard.stripe.com/settings/user)
- [organization-level
roles](https://docs.stripe.com/get-started/account/orgs/team#organization-level-and-account-level-roles)
- [User
authentication](https://dashboard.stripe.com/account/user_authentication)
- [Troubleshoot
SSO](https://docs.stripe.com/get-started/account/sso/troubleshooting)
- [Stripe sign in page](https://dashboard.stripe.com/login)