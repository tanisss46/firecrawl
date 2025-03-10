# Manage your teamPublic preview

## Learn how to invite and interact with team members in your organization.

You can manage your team from the
[Team](https://dashboard.stripe.com/settings/team) page. Administrators can
update the team by adding or removing members, and changing the roles assigned
to members. You can view all team members, and filter their activity in the
security history. You can also manage two-factor authentication settings for an
individual or the whole team.

## Two-factor authentication controls

Stripe supports two-factor authentication (2FA) through TouchID, security key,
SMS, and authenticator apps, such as Google Authenticator. As an additional
security measure, we recommend that all users register for 2FA.

### Require 2FA for all users in an organization

To require 2FA for Organization users, you must assign the Administrator or
Super Administrator roles:

- Navigate to the [User
Authentication](https://dashboard.stripe.com/org/settings/security/authentication)
page.
- Enable **Require two-step authentication for all team members**.

After you enable this option, all users must register a 2FA device during their
next login, which requires them to complete a 2FA challenge during all
subsequent login attempts.

### Reset 2FA for a single user

If a single user loses access to their 2FA devices, an Administrator or Super
Administrator must reset the compromised user’s 2FA settings from the
account-level:

- Navigate to the [Team](https://dashboard.stripe.com/settings/team) page of an
account.
- Click the compromised user’s name.
- Click **Reset two-factor authentication**.

Stripe sends an email to the compromised user’s registered email address with
instructions on how they can reset their 2FA devices. This can’t be done on the
organization-level management user detail’s page.

## View and filter your security history

To view your security-related events, navigate to the [Security
history](https://dashboard.stripe.com/settings/security_history) page. You can
filter your security filter by date, user, action type, and so on. Your
user-based security history filters include:

- IP Address
- User
- API Key
- Device

**Action filters** categorize hundreds of different actions based on product
areas (for example, Billing, Radar, or Checkout). You can export your security
history as a **CSV** file.

## Team management

### Organization-level and account-level roles

For every account you have access to, you must assign users either an
organization-level or account-level role. Organization-level roles grant users
access to all accounts within the organization, including the organization
itself. Account-level roles allow users to access a specific assigned account
with the assigned role.

Say your organization contains three accounts: Banking, Finance, and Consulting.
In this scenario, you can assign the following roles:

- **Organization-level role**: If you assign a user the “IAM Administrator”
role, they possess that role in all three accounts, as well as within the
organization itself. This grants them access to team management for all three
accounts, in addition to organization-level team management.
- **Account-level role**: If you assign a user the “IAM Administrator” role in
the Banking account, their access is limited solely to the IAM role within the
Banking account. They can manage account-level teams exclusively within that
account. However, this role doesn’t grant access to other accounts or
organization-level team management.

## Differences in team management with Organizations

Use Stripe Organizations to manage your team either at the organization-level
*or* at the account-level.

- **Manage your team for an account**: Add, remove, and edit team members of an
account, and update the roles of users associated with that account, on the
[Team and security](https://dashboard.stripe.com/settings/team) page.
- **Manage your team for an organization**: Manage user access and roles for
specific accounts on the [Team](https://dashboard.stripe.com/org/settings/team)
page. From here, you can also manage team members by granting access to multiple
accounts simultaneously or providing access to the entire organization. You can
only access this page if you have an organization-level role.
Organization-level managementAccount-level management
You can view all of the team members within your organization in the
[Team](https://dashboard.stripe.com/org/settings/team) page. Additionally, you
can:

- Invite new members directly.
- Edit members.
- Grant members access to additional accounts.
- Select the specific accounts that you want to grant access to.
- Remove members from your organization.

### Add a team member

To add a new team member:

- Navigate to the [Team](https://dashboard.stripe.com/org/settings/team) page.
- Click **Add Member**.
- Add the email address of the user you want to invite. To invite multiple team
members with the same role and access, enter the first email address, follow it
with a space or a comma, then enter the next email, and continue this pattern
for all required email addresses.
- Select the [User
Roles](https://docs.stripe.com/get-started/account/teams/roles) that you want to
give to this team member. You can give multiple roles to a single user within
the same account.
- Select the accounts that you want to give this user access to. You can select
individual accounts, or grant access to the entire organization. Org-level
access gives users access to all accounts within the organization, and access to
the organization itself.
- Click **Send Invites** to send the email with the steps for creating their
Stripe Account.

### Remove a team member

To remove an existing team member:

- Navigate to the [Team](https://dashboard.stripe.com/settings/team) page.
- Click the user’s profile from the list of team members.
- Click the overflow menu ().
- Click **Remove member** to cancel this users’ access to this Stripe account
immediately. This won’t cancel this user’s access to other accounts they have
access to.

### Edit a team member’s access

To edit an existing team member’s access:

- Navigate to the [Team](https://dashboard.stripe.com/settings/team) page.
- Click the user’s profile from the list of team members.
- Click **Manage roles**.
- Choose at least one role that you want to assign to this user.
- (Optional) To remove the user, click **Remove member**.
- Choose the accounts you want to assign roles in. You can add new accounts,
remove accounts, or grant organization-level access.

### View all users in the Dashboard

To view all team members within an organization, navigate to the
[Team](https://dashboard.stripe.com/org/settings/team) page. You can filter by:

- Role
- Name
- Email
- Status

You can export this information as a **CSV** file.

## Links

- [Team](https://dashboard.stripe.com/settings/team)
- [User
Authentication](https://dashboard.stripe.com/org/settings/security/authentication)
- [Security history](https://dashboard.stripe.com/settings/security_history)
- [Team](https://dashboard.stripe.com/org/settings/team)
- [User Roles](https://docs.stripe.com/get-started/account/teams/roles)