# Single sign-on (SSO)Public preview

## Configure authentication for access to the Stripe Dashboard with an Identity Provider.

Single Sign-On (SSO) allows your team to sign in through an Identity Provider
(IdP) using one set of credentials and access multiple applications, such as
Stripe. Enabling SSO for your team increases security and makes it easier for
them to sign in to Stripe. Stripe specifically supports Security Assertion
Markup Language (SAML) 2.0, so your IdP can manage the creation of user accounts
(team members) as well as authentication and authorization during sign-in. Any
identity provider that supports SAML 2.0 works with Stripe.

#### Security incidents

If your Identity Provider (IdP) is compromised, unauthorized parties could
access your Stripe account. You’re responsible for mitigating your exposure to
security incidents by evaluating your security needs and implementing the
necessary security protocols and controls.

## Setup SSO with an Identity Provider

[Auth0Learn how to setup single sign-on in the Dashboard with
Auth0.](https://docs.stripe.com/get-started/account/sso/v2/auth0)[Entra IDLearn
how to setup single sign-on in the Dashboard with Entra ID (formerly known as
Azure AD).](https://docs.stripe.com/get-started/account/sso/entra-id)[Google
WorkspaceLearn how to setup single sign-on in the Dashboard with Google
Workspace.](https://docs.stripe.com/get-started/account/sso/google-workspace)[OktaLearn
how to setup single sign-on in the Dashboard with
Okta.](https://docs.stripe.com/get-started/account/sso/okta)[OneLoginLearn how
to setup single sign-on in the Dashboard with
OneLogin.](https://docs.stripe.com/get-started/account/sso/onelogin)[OtherLearn
how to setup single sign-on in the Dashboard with a different identity
provider.](https://docs.stripe.com/get-started/account/sso/other)
## Additional resources

[Consolidate SSOLearn how to consolidate single sign-on (SSO) settings across
multiple
accounts.](https://docs.stripe.com/get-started/account/orgs/sso-consolidation)[Troubleshoot
SSOLearn how to resolve failed configuration checks when setting up
SSO.](https://docs.stripe.com/get-started/account/sso/troubleshooting)
## Supported features

Stripe supports the following SSO features:

- SSO configuration options: Configure Stripe accounts to either mandate SSO for
all users or allow sign-in using SSO or email and password.
- Just-In-Time account creation: Automatically create new Stripe accounts for
users without existing access upon their first SSO sign-in.
- Granular Dashboard roles: Assign granular [user
roles](https://docs.stripe.com/get-started/account/teams/roles) through your
IdP.
- IdP-initiated SSO: Authenticate directly from an IdP’s website or browser
extension.
- Service Provider-initiated SSO: Initiate SSO login directly from Stripe’s
[login page](https://dashboard.stripe.com/login).

### Limitations

Stripe doesn’t support the following SSO features:

- **User Deletion in SAML**: Due to the limitations of SAML, Stripe doesn’t get
notified if user access is revoked in IdP. If users try to log in again through
SSO after their current session expires, Stripe revokes their access. If you
need to remove access instantly, you can delete the users in your [Team
settings](https://dashboard.stripe.com/settings/team).
- **System for Cross-domain Identity Management (SCIM)**: SCIM is a protocol
that an IdP can use to synchronize user identity lifecycle processes (for
example, provisioning and deprovisioning access, and populating user details)
with the service provider, such as Stripe.

## Links

- [Auth0Learn how to setup single sign-on in the Dashboard with
Auth0.](https://docs.stripe.com/get-started/account/sso/v2/auth0)
- [Entra IDLearn how to setup single sign-on in the Dashboard with Entra ID
(formerly known as Azure
AD).](https://docs.stripe.com/get-started/account/sso/entra-id)
- [Google WorkspaceLearn how to setup single sign-on in the Dashboard with
Google
Workspace.](https://docs.stripe.com/get-started/account/sso/google-workspace)
- [OktaLearn how to setup single sign-on in the Dashboard with
Okta.](https://docs.stripe.com/get-started/account/sso/okta)
- [OneLoginLearn how to setup single sign-on in the Dashboard with
OneLogin.](https://docs.stripe.com/get-started/account/sso/onelogin)
- [OtherLearn how to setup single sign-on in the Dashboard with a different
identity provider.](https://docs.stripe.com/get-started/account/sso/other)
- [Consolidate SSOLearn how to consolidate single sign-on (SSO) settings across
multiple
accounts.](https://docs.stripe.com/get-started/account/orgs/sso-consolidation)
- [Troubleshoot SSOLearn how to resolve failed configuration checks when setting
up SSO.](https://docs.stripe.com/get-started/account/sso/troubleshooting)
- [user roles](https://docs.stripe.com/get-started/account/teams/roles)
- [login page](https://dashboard.stripe.com/login)
- [Team settings](https://dashboard.stripe.com/settings/team)