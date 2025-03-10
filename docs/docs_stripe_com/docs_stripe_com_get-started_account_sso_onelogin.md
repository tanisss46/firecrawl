# Single sign-on with OneLoginPublic preview

## Learn how to setup single sign-on in the Dashboard with OneLogin.

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

## Set up SSO

To integrate your Stripe account with your IdP, you’ll need to complete three
steps:

- [Prove ownership of the
domains](https://docs.stripe.com/get-started/account/sso/onelogin#proving-domain-verification)
that your team will use to sign in to the Dashboard.
- [Configure
OneLogin](https://docs.stripe.com/get-started/account/sso/onelogin#configuring-your-identity-provider)
to work with Stripe.
- [Configure
Stripe](https://docs.stripe.com/get-started/account/sso/onelogin#configure-stripe)
to work with OneLogin.
[Proving Domain
Ownership](https://docs.stripe.com/get-started/account/sso/onelogin#proving-domain-verification)
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

[Configuring
OneLogin](https://docs.stripe.com/get-started/account/sso/onelogin#configuring-your-identity-provider)
#### Caution

There isn’t an official Stripe SAML connector in OneLogin yet. The only
available Stripe app is for password-based authentication. Don’t use the
password-based authentication for SAML.

- Create a new application to represent the relationship between OneLogin and
the Stripe Dashboard. To do so, navigate to the **Applications** page, and
select **Add App**.
- Find the **SAML Test Connector (IdP w/ attr w/ sign response)** app.
- Select **Save**, and navigate to the **Configuration** section. Then, enter
the following values:- **Audience**:
`https://dashboard.stripe.com/saml/metadata`
- **Recipient**: `https://dashboard.stripe.com/login/saml/consume`
- **Consumer URL Validator**: `https://dashboard.stripe.com/login/saml/consume`
- **Consumer URL**: `https://dashboard.stripe.com/login/saml/consume`
- Select **SSO** on the side panel, and set the **Signature Algorithm** to
`SHA-256`.
- Save your configuration changes by selecting **Save**.

### Assign roles to your team

To authenticate a team member to Stripe and assign them roles, configure
OneLogin to send the roles in the SAML assertions.

- Navigate to the **Parameters** section, and create a new **Field**- Set the
**Field name** to ` Stripe-Role- `. This identifies which account you sign in
to.
- Select **Include in SAML assertion**.
- In the next form, select the [Dashboard
role](https://docs.stripe.com/get-started/account/teams/roles) you want your
users to have by default. Select **Macro**, and input the desired default role
in the field below

!

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
#### Support for multiple Stripe accounts

Repeat the previous step and add a **parameter** for each additional Stripe
account. Select **Add parameter**, use the current account’s token for the
**Field name** and choose the role you want your users to have by default.

The list of account tokens can be found in the **Accounts** section of your
[Profile](https://dashboard.stripe.com/settings/user).

!

- Navigate to the **Users** tab. Here, you can assign team members to your
application. You can also configure which Roles a user obtains upon log in.
- Select the **User** you want to edit. Then, navigate to **Applications** on
the side panel.
- In the next modal that opens, you can configure the roles that a user obtains
when they log in. To use multiple roles, add a semicolon after each role. In the
following example, the user obtains the `analyst` and the `developer` role when
they sign in.

!

[Configuring
Stripe](https://docs.stripe.com/get-started/account/sso/onelogin#configure-stripe)
### Enter values from your identity provider

Next, configure your Stripe account to connect to your identity provider from
the [User
authentication](https://dashboard.stripe.com/account/user_authentication) page.

To configure Stripe to connect to your identity provider you need:

- **Issuer ID**: An identifier of your identity provider.
- **Identity provider URL**: The URL of your identity provider that your team
members are redirected to, so they can authenticate.
- **Identity provider certificate**: The X.509 certificate that your identity
provider signs assertions with.

### How to find these values in your identity provider

In OneLogin, you can find these values by navigating to the **SSO** tab of [your
application](https://docs.stripe.com/get-started/account/sso/onelogin#configuring_your_identity_provider).

Name of property in StripeName of property in OneLoginIssuer IDIssuer
URLIdentity provider URLSAML 2.0 Endpoint (HTTP)Identity provider
certificateX.509 certificate (click View Details)

!

#### Test your configuration

Before saving your settings, a test runs to validate your SSO integration. After
you click the **Test** button, a window opens in your browser that redirects to
your identity provider to sign in. After you sign in, the window automatically
closes and test results display on the original page.

If the test succeeds, you can save the settings, and select an enforcement mode.
If the test fails, modify your configuration to address the issues reported and
test the integration again.

#### Select an enforcement mode for SSO

When using SSO, there are three separate enforcement modes that you can choose
from. These affect which methods of authentication your team members can use.

ModeSSO authentication allowedRegular authentication
allowedOffNoYesOptionalYesYesRequired[Authenticate with
SSO](https://docs.stripe.com/get-started/account/sso/onelogin#authenticate-sso)
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

- [organization](https://docs.stripe.com/get-started/account/orgs/sso)
- [User
authentication](https://dashboard.stripe.com/settings/security/authentication)
- [organization](https://docs.stripe.com/get-started/account/orgs)
- [Stripe support](https://support.stripe.com/)
- [Dashboard role](https://docs.stripe.com/get-started/account/teams/roles)
- [Profile](https://dashboard.stripe.com/settings/user)
- [User
authentication](https://dashboard.stripe.com/account/user_authentication)
- [Stripe sign in page](https://dashboard.stripe.com/login)
- [IdP needs to support Service Provider-initiated
login](https://docs.stripe.com/get-started/account/sso/troubleshooting)