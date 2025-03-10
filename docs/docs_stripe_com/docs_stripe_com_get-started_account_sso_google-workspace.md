# Single sign-on with Google WorkspacePublic preview

## Learn how to setup single sign-on in the Dashboard with Google Workspace.

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
domains](https://docs.stripe.com/get-started/account/sso/google-workspace#proving-domain-verification)
that your team will use to sign in to the Dashboard.
- [Configure Google
Workspace](https://docs.stripe.com/get-started/account/sso/google-workspace#configuring-your-identity-provider)
to work with Stripe.
- [Configure
Stripe](https://docs.stripe.com/get-started/account/sso/google-workspace#configure-stripe)
to work with Google Workspace.
[Proving Domain
Ownership](https://docs.stripe.com/get-started/account/sso/google-workspace#proving-domain-verification)
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

[Configuring Google
Workspace](https://docs.stripe.com/get-started/account/sso/google-workspace#configuring-your-identity-provider)
#### Caution

These instructions require changes in the [Google Workspace Admin
console](https://admin.google.com/).

- To configure Google Workspace, create a new SAML application to represent the
relationship between Google Workspace and the Stripe Dashboard. In the menu
accessible at the top left, select **Apps**, and click **Web and mobile apps**.

![Create a new SAML application in Google
Workspace](https://b.stripecdn.com/docs-statics-srv/assets/google_workspace_saml_apps.db133edbd1c04d8f0190a738ae5631b6.png)

![Create a new SAML application in Google
Workspace](https://b.stripecdn.com/docs-statics-srv/assets/google_workspace_saml_apps.db133edbd1c04d8f0190a738ae5631b6.png)

- Click the **Add app** menu and select **Add custom SAML app**. On the **App
details** screen, set the **App name** and any other parameters you need. Click
**Continue**.

![Custom SAML app
details](https://b.stripecdn.com/docs-statics-srv/assets/step-1.439c06d6540fd6ed1b4dd4fbdcd6aee9.png)

![Custom SAML app
details](https://b.stripecdn.com/docs-statics-srv/assets/step-1.439c06d6540fd6ed1b4dd4fbdcd6aee9.png)

- Save the **SSO URL**, **Entity ID**, and download the certificate. You need
these in [step
3](https://docs.stripe.com/get-started/account/sso/google-workspace#configure-stripe).
Next, click **Continue**.

![Custom SAML Google Identity Provider
detail](https://b.stripecdn.com/docs-statics-srv/assets/step-2.df4f42226695ba60fcad0b2edc588163.png)

![Custom SAML Google Identity Provider
detail](https://b.stripecdn.com/docs-statics-srv/assets/step-2.df4f42226695ba60fcad0b2edc588163.png)

- On the **Service Provider Details** screen, configure the following:

SettingValueACS URL`https://dashboard.stripe.com/login/saml/consume`Entity
ID`https://dashboard.stripe.com/saml/metadata`Name ID`Basic Information` and
`Primary Email`Name ID Format`EMAIL`

![Custom SAML service provider
details](https://b.stripecdn.com/docs-statics-srv/assets/step-3.a57d2f453981a3eef89a5e611da90f69.png)

![Custom SAML service provider
details](https://b.stripecdn.com/docs-statics-srv/assets/step-3.a57d2f453981a3eef89a5e611da90f69.png)

- Click **Continue** and then click **Finish** on next screen to complete the
SAML application set up.

### Create a Google Workspace custom user attribute

To authenticate a team member to Stripe, configure Google Workspace with the
role they have in the Stripe Dashboard per Stripe account. To do this, create an
**Attribute Mapping** from a Google Workspace user property to your SAML
application, then create a custom user property in Google Workspace to store
this information.

- In the admin console main menu at the top left, select **Directory**, and
click **Users**.

![Manage custom
attributes](https://b.stripecdn.com/docs-statics-srv/assets/custom-attributes.d0bf966eca081bddeb7b6b8b75def633.png)

![Manage custom
attributes](https://b.stripecdn.com/docs-statics-srv/assets/custom-attributes.d0bf966eca081bddeb7b6b8b75def633.png)

- In the menu of the user list, click **More options** and select the **Manage
custom attributes** item. In the top right, click **Add custom attribute**.

![Add custom
attribute](https://b.stripecdn.com/docs-statics-srv/assets/add-attribute.83d3279f110085b942ede4a900a47429.png)

![Add custom
attribute](https://b.stripecdn.com/docs-statics-srv/assets/add-attribute.83d3279f110085b942ede4a900a47429.png)

- Enter a **Category**, **Description**, and **Name** as needed. Select an
**Info type** of `Text`, a **Visibility** of your choice, set **No. of values**
to `Single Value`, then click **Add**.

![Add custom
fields](https://b.stripecdn.com/docs-statics-srv/assets/custom-attribute.b318a94afeb67ce894a3db855ae9d436.png)

![Add custom
fields](https://b.stripecdn.com/docs-statics-srv/assets/custom-attribute.b318a94afeb67ce894a3db855ae9d436.png)

### Map user attributes to the Stripe Dashboard

- After you create your custom user property, map that property to an attribute
in the SAML assertions your application sends. To navigate back to your SAML
application in the main menu, click the menu icon in the top left, select
**Apps**, then **Web and mobile apps**.
- Choose your new application from the list, then click **Configure SAML
attribute mapping** in the **SAML attribute mapping** section.

![Configure SAML attribute
mapping](https://b.stripecdn.com/docs-statics-srv/assets/configure-attribute-mapping.04f876bd5c94c52b23d1109624398ccb.png)

![Configure SAML attribute
mapping](https://b.stripecdn.com/docs-statics-srv/assets/configure-attribute-mapping.04f876bd5c94c52b23d1109624398ccb.png)

- Add a row for each Stripe account you want to authenticate your team to, and
click **Save**.- **Google Directory attributes** is the [custom field you
configured](https://docs.stripe.com/get-started/account/sso/google-workspace#goolge-workspace-custom-attribute-values).
- **App attribute** is the Stripe account to connect to. The format is
`Stripe-Role-`. The account ID value is your currently logged in account, such
as: ****.

![Configure SAML attribute mapping
details](https://b.stripecdn.com/docs-statics-srv/assets/configure-attribute-add-attributes.242476cdf7fba4a2ac77c0d70d8d6d88.png)

![Configure SAML attribute mapping
details](https://b.stripecdn.com/docs-statics-srv/assets/configure-attribute-add-attributes.242476cdf7fba4a2ac77c0d70d8d6d88.png)

#### Multiple Stripe accounts support

Add one **Attribute Mapping** per account.

![Configure SAML mulpti attributes
mapping](https://b.stripecdn.com/docs-statics-srv/assets/configure-attribute-mulpti-attributes.e186b3dfffe6f5511eef0544edde4d9b.png)

![Configure SAML mulpti attributes
mapping](https://b.stripecdn.com/docs-statics-srv/assets/configure-attribute-mulpti-attributes.e186b3dfffe6f5511eef0544edde4d9b.png)

You can find the list of account tokens in the *Accounts* section of your
[Profile](https://dashboard.stripe.com/settings/user).

### Assign roles to your team

- After you set up your SAML application, enable it for your users. Click **Edit
service** at the top right of the application details.

![Edit user
access](https://b.stripecdn.com/docs-statics-srv/assets/edit-user-access.5892c2e5c3633e0fcd7e14bda98c4093.png)

![Edit user
access](https://b.stripecdn.com/docs-statics-srv/assets/edit-user-access.5892c2e5c3633e0fcd7e14bda98c4093.png)

- Select `ON for everyone`, and click **Save**.

![Enable Stripe app for
everyone](https://b.stripecdn.com/docs-statics-srv/assets/enble-app-for-everyone.f4c155e872f2d49c644e5ae4af809d5a.png)

![Enable Stripe app for
everyone](https://b.stripecdn.com/docs-statics-srv/assets/enble-app-for-everyone.f4c155e872f2d49c644e5ae4af809d5a.png)

- For each team member, set a Stripe role on their User Information page in the
Directory. Navigate there in the main menu by clicking **Directory**, then
**Users**. Select the user you want to set a role for from the list, click
**User Information**, and scroll down to your new attribute.

![Assign stripe role to
users](https://b.stripecdn.com/docs-statics-srv/assets/users-assign-stripe-role.814b761e530f97eb5d234f7949323a9c.png)

![Assign stripe role to
users](https://b.stripecdn.com/docs-statics-srv/assets/users-assign-stripe-role.814b761e530f97eb5d234f7949323a9c.png)

- To assign **multiple roles** to a user upon login, you can add a semicolon
after each role. For example, you can set the attribute as `analyst; developer`.
In this case, the user obtains the `analyst` and the `developer` role when they
sign in.

Stripe supports distinct Dashboard roles for each Stripe account. This allows
team members to have the appropriate permission for each account they have
access to.

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
Analyst`transfer_analyst`View only`view_only`[Configuring
Stripe](https://docs.stripe.com/get-started/account/sso/google-workspace#configure-stripe)
### Enter values from your identity provider

Configure your Stripe account to connect to your identity provider from the
[User authentication](https://dashboard.stripe.com/account/user_authentication)
page.

To configure Stripe to connect to your identity provider you’ll need:

- **Issuer ID**: An identifier of your identity provider.
- **Identity provider URL**: The URL of your identity provider that your team
members are redirected to, so they can authenticate.
- **Identity provider certificate**: The X.509 certificate that your identity
provider uses to signs assertions.

### Find these values in your identity provider

If you don’t have these values from Step 1, navigate to the [SAML
application](https://docs.stripe.com/get-started/account/sso/google-workspace#configuring-your-identity-provider)
you created earlier, select **Service Provider Details**, and click **Manage
certificates**.

![Manage SAML app
certificates](https://b.stripecdn.com/docs-statics-srv/assets/service-provider-details.198a2158954fa219c95834bbffc901de.png)

![Manage SAML app
certificates](https://b.stripecdn.com/docs-statics-srv/assets/service-provider-details.198a2158954fa219c95834bbffc901de.png)

This opens a new window with the following information:

Name of property in StripeName of property in Google WorkspaceIdentity provider
URLSSO URLIssuer IDEntity IDIdentity provider certificateCertificate 1
Download a copy of Certificate 1 to allow you to copy the certificate to Stripe.

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
SSO](https://docs.stripe.com/get-started/account/sso/google-workspace#authenticate-sso)
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
- [Google Workspace Admin console](https://admin.google.com/)
- [Profile](https://dashboard.stripe.com/settings/user)
- [User roles supported by
Stripe](https://docs.stripe.com/get-started/account/teams/roles)
- [User
authentication](https://dashboard.stripe.com/account/user_authentication)
- [Stripe sign in page](https://dashboard.stripe.com/login)
- [IdP needs to support Service Provider-initiated
login](https://docs.stripe.com/get-started/account/sso/troubleshooting)