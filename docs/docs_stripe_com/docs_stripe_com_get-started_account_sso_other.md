# Single sign-on with SAML Identity ProviderPublic preview

## Learn how to setup single sign-on in the Dashboard with SAML Identity Provider.

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
domains](https://docs.stripe.com/get-started/account/sso/other#proving-domain-verification)
that your team will use to sign in to the Dashboard.
- [Configure SAML Identity
Provider](https://docs.stripe.com/get-started/account/sso/other#configuring-your-identity-provider)
to work with Stripe.
- [Configure
Stripe](https://docs.stripe.com/get-started/account/sso/other#configure-stripe)
to work with SAML Identity Provider.
[Proving Domain
Ownership](https://docs.stripe.com/get-started/account/sso/other#proving-domain-verification)
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

[Configuring SAML Identity
Provider](https://docs.stripe.com/get-started/account/sso/other#configuring-your-identity-provider)
#### Caution

Stripe supports SSO with the SAML 2.0 protocol. Any identity provider that
supports SAML 2.0 should work with Stripe.

To configure your identity provider, create an application (wording might vary
by identity provider) to represent the relationship between your identity
provider and Stripe.

Within this application, set the following values.

- **Security settings**: Configure your signature algorithm to `RSA-SHA256`, and
your digest algorithm to `SHA256`. We enforce this for security reasons because
*SHA-256* is the industry-standard hashing algorithm.
- **SSO URL**: This value represents which URL your identity provider redirects
your team back to after they authenticate. Set this to be
`https://dashboard.stripe.com/login/saml/consume`.
- **Audience URI** or **Entity ID**: This value represents an ID for the Stripe
Dashboard within your identity provider. Set this to be
`https://dashboard.stripe.com/saml/metadata`.
- **RelayState**: This value represents where to redirect the team member after
they successfully authenticate. The URL must be relative (for example,
`/payments`) and only set in IdP-initiated login.
- **Name ID**: This value represents the team member that’s authenticating (that
is, the subject of the SAML assertion), and it must be the team member’s email
address.

```
<saml2:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">{{
USER_EMAIL }}</saml2:NameID>
```

- **Attribute statements for team roles**: You can send multiple roles in the
SAML assertion as either a semicolon-separated list in a single SAML attribute
or as a multi-value SAML attribute.

```
<saml2:AttributeStatement>
<saml2:Attribute Name="Stripe-Role-"
NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
 <saml2:AttributeValue>role_id_1; role_id_2</saml2:AttributeValue>
 </saml2:Attribute>
</saml2:AttributeStatement>
```

```
<saml2:AttributeStatement>
<saml2:Attribute Name="Stripe-Role-"
NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
 <saml2:AttributeValue>role_id_1</saml2:AttributeValue>
 <saml2:AttributeValue>role_id_2</saml2:AttributeValue>
 </saml2:Attribute>
</saml2:AttributeStatement>
```

The `Name` attribute of the `saml2:Attribute` element identifies which Stripe
account to authenticate your team member to.

The value of `role_id` represents the [Dashboard
role](https://docs.stripe.com/get-started/account/teams/roles) of the team
member. The team member’s role per account must be included as an attribute
statement in any assertion that you send to Stripe.

Include a `saml2:Attribute` element per Stripe account to authenticate a team
member for multiple Stripe accounts.

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
To support multiple Stripe accounts, add a `saml2:Attribute` element per
account.

```
<saml2:attributestatement>
<saml2:attribute name="Stripe-role-account-token-1"
NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
 <saml2:attributevalue>view_only
 </saml2:attributevalue>
 </saml2:attribute>
<saml2:attribute name="Stripe-role-account-token-2"
NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
 <saml2:attributevalue>view_only
 </saml2:attributevalue>
 </saml2:attribute>
</saml2:attributestatement>
```

The list of account tokens can be found in the *Accounts* section of your
[Profile](https://dashboard.stripe.com/settings/user).

[Configuring
Stripe](https://docs.stripe.com/get-started/account/sso/other#configure-stripe)
### Enter values from your identity provider

Next, you’ll need to configure your Stripe account to connect to your identity
provider from the [User
authentication](https://dashboard.stripe.com/account/user_authentication) page.

To configure Stripe to connect to your identity provider you’ll need:

- **Issuer ID**: An identifier of your identity provider.
- **Identity provider URL**: The URL of your identity provider that your team
members are redirected to, so they can authenticate.
- **Identity provider certificate**: The X.509 certificate that your identity
provider uses to signs assertions.

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
SSO](https://docs.stripe.com/get-started/account/sso/other#authenticate-sso)
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