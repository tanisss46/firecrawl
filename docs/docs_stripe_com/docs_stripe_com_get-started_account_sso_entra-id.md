# Single sign-on with Entra IDPublic preview

## Learn how to setup single sign-on in the Dashboard with Entra ID.

Use [Microsoft Entra ID](https://entra.microsoft.com/) (formerly known as Azure
Active Directory) to verify domain ownership, create user role groups, configure
single sign-on (SSO), and assign roles to manage access to your Stripe account.

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
ownership](https://docs.stripe.com/get-started/account/sso/entra-id#domain-verification)
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

[Create groups of users in Entra
ID](https://docs.stripe.com/get-started/account/sso/entra-id#assign-roles)
Create groups for Stripe roles and assign your team members (users) to these
groups. Users can belong to only one group per Stripe account. For example, if
you want a user to have an admin role, assign them to the administrator group.
However, if you want a user to have multiple roles, such as view only and
analyst, create a separate group specifically for those combined roles.

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
Analyst`transfer_analyst`View only`view_only`- Log in to the [Entra ID
Dashboard](https://entra.microsoft.com/).
- In the left navigation pane, click **Groups**.
- Click **Add new group**:- For **Group type**, select **Security**.
- For **Group name**, enter the name of the group (for example, View only users
in Stripe).
- Click **No members added**, and add users to the group.
[Create an Entra ID
application](https://docs.stripe.com/get-started/account/sso/entra-id#create-entra-app)
#### Caution

These instructions assume you already have a Directory in your Entra ID account.

To configure Entra ID, create a new application to represent the relationship
between Entra ID and the Stripe Dashboard:

- In the left navigation pane, click **Applications** > **Enterprise
applications**.
- Click **Create your own application**, enter the name your application, select
**Integrate any other application you don’t find in the gallery**, and click
**Create**.
- Under **Getting Started**, click **1. Assign users and groups**.
- Click **Add user/group**, and select the groups you previously created.
- In your app’s left navigation page, click **Overview** > **2. Set up single
sign on**.
- Select **SAML** to open the **SAML-based Sign on** page.
- Click **Basic SAML Configuration**, enter the following values, and click
**Save**.- Identifier: `https://dashboard.stripe.com/saml/metadata`
- Reply URL: `https://dashboard.stripe.com/login/saml/consume`
[Add attributes and
claims](https://docs.stripe.com/get-started/account/sso/entra-id#add-claims)
You must assign attributes and claims to the groups you created.

- On the **SAML-based Sign on** page, click **Attributes and claims**.
- Click **Add new claim**. You must create a new claim for each Stripe account
you’re configuring SSO for.
- Click **Claim conditions** to create the mapping between the group and the
role you want to the group for this Stripe account.- Set the **Name** to
`Stripe-Role-{{STRIPE_ACCOUNT_ID}}`. This identifies which Stripe account you
authenticate your team member to (and is set to whichever Stripe account you’re
signed in to while viewing this page, currently: ****)
- For **Source**, select **Attribute**.
- For **User type**, select **Members**.
- For **Group**, select the group you want.
- For **Source**, select **Attribute**.
- For **Value**, enter the [Dashboard
role](https://docs.stripe.com/get-started/account/teams/roles) you want to
assign (for example, `developer`), and click **Enter**. This means you’ve
assigned this role to any members in this group.
- Assign Stripe roles you want to the groups you created. If you want a user to
have multiple roles (such as view only and analyst), you must create a separate
group that exists specifically for those combined roles.

!
- Click **Save**.
[Verify
certificates](https://docs.stripe.com/get-started/account/sso/entra-id#verify-certificates)
On the **SAML-based Sign on** page, click **SAML certificates** to verify if the
signing algorithm configuration is correct. Ensure the following values match:

- **Signing Option**: `Sign SAML assertion`
- **Signing Algorithm**: `SHA-256`
[Configure
Stripe](https://docs.stripe.com/get-started/account/sso/entra-id#configure-stripe)
To configure Stripe with SSO:

### Retrieve values from Entra ID

Retrieve the values for **Login URL**, **Microsoft Entra Identifier**, and **PEM
SAML Certificate** from your app in Entra ID.

- Open the Entra ID Dashboard.
- In your app’s left navigation pane, click **Single sign-on**.
- On the **SAML-based Sign on** page, navigate to **Set up Stripe**, and
retrieve the following values for:- Login URL
- Microsoft Entra Identifier
- On the **SAML-based Sign on** page, click **SAML Certificates**.
- Next to your certificate, click the overflow button (), and click **PEM
certificate download**
- Open the `.pem` file in a basic text editor. This is your **Identity provider
certificate**.

### Configure your Stripe account to connect to Entra ID

Enter the values you retrieved from your app in Entra ID in Stripe:

- In the Stripe Dashboard, navigate to **Settings** > **Team and security** >
[User authentication](https://dashboard.stripe.com/account/user_authentication).
- Next to the domain name, click the overflow button () > **Manage SSO
settings**.
- Click **Test your configuration** > **Next**.
- Provide info for your identity provider:- For **Issuer ID**, enter the value
for **Microsoft Entra Identifier** in Entra ID.
- For **Identity provider URL**, enter the value for **Login URL** in Entra ID.
- For **Identity provider certificate**, enter the certificate value from the
`.pem` file you downloaded in Entra ID (include the begin certificate and end
certificate text).
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
SSO](https://docs.stripe.com/get-started/account/sso/entra-id#authenticate-sso)
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

## Links

- [Microsoft Entra ID](https://entra.microsoft.com/)
- [organization](https://docs.stripe.com/get-started/account/orgs/sso)
- [User
authentication](https://dashboard.stripe.com/settings/security/authentication)
- [organization](https://docs.stripe.com/get-started/account/orgs)
- [Stripe support](https://support.stripe.com/)
- [User roles supported by
Stripe](https://docs.stripe.com/get-started/account/teams/roles)
- [User
authentication](https://dashboard.stripe.com/account/user_authentication)
- [Troubleshoot
SSO](https://docs.stripe.com/get-started/account/sso/troubleshooting)
- [Stripe sign in page](https://dashboard.stripe.com/login)
- [Profile](https://dashboard.stripe.com/settings/user)