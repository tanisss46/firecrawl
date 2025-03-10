# Stripe Connector for Salesforce Platform Installation Guide

## Install and configure the Stripe Connector for Salesforce Platform.

Identify the environment where you want to install your app. We provide separate
installation options for test and production environments.

- To install this Application from the Salesforce AppExchange , follow this
[link](https://appexchange.salesforce.com/appxListingDetail?listingId=4dff0f8e-0b10-47c2-a3a3-f3905e7f7927).
For users in Japan, [AppExchange
Japan](https://appexchangejp.salesforce.com/appxListingDetail?listingId=a0N3u00000RgdoWEAR)
is also available.
- Log into the Salesforce organization where you want to install the package.
- After logging in, you’re directed to the installation page. Click **Continue**
to begin the installation process.
- We recommend installing **Install for Admins Only**. This option allows for
controlling access and permissions after the package has been installed.

!
- **Approve Third-Party Access** check off the box and click **Continue** to
start the package installation when the modal appears. As it states, this is to
allow data to be sent back and forth between your Salesforce org and the Stripe
PBO.

!

## Configure permission sets

The package incorporates both the Stripe Connector Integration User and the
Stripe Connector Data User permission sets. These sets enable different users
within your organization to access specific application features.

## Stripe Connector integration user

The Stripe Connector Integration User permission set must be assigned to any
non-system administrator persona designated to manage setup log cleanup settings
and event subscriptions. However, since system permissions are unable to be
packaged due to limitations with Salesforce AppExchange apps. You must add
additional permissions manually by cloning the permission set, in order for
these users to access setup features.

- **Clone Permission Set** To clone the permission set, navigate to **Setup >
User > Permission Sets**.
- Next to the **Stripe Connector Integration User** permission set, click
**Clone**.

!
- Enter a new unique **Label** and **API Name**, then click **Save**. 

!
- **Modify Permission Set** Navigate to **Setup > User > Permission Sets** and
select your cloned permission set.

!
- Select **System Permissions**. 

!
- Click **Edit** then select the **Download AppExchange Packages** permissions,
and click **Save**.

!
- Click **Save** again to confirm changes. 

!
- **Assign Permission Set** to users by navigating to **Setup > User >
Permission Sets**.
- Select your cloned permission set. 

!
- From the Permission Set Overview page, click **Manage Assignments**. 

!
- Click **Add Assignments**. 

!
- Check the box next to the users to assign permission set to and click **Next**
at the bottom of the page.

#### Stripe Connector data user

The Stripe Connector Data User has the ability to perform operations on the
`Stripe_Event__c` object records, which the Webhook Handler class creates. To
provide non-admin users access to Stripe Event records, you must assign a data
user permission set to their user profile.

- Assign a permission set to a user by navigating to **Setup > User > Permission
Sets**.
- Select the **Stripe Connector Data User** permission set. 

!
- From the **Permission Set Overview** page, click **Manage Assignments**. 

!
- Click **Add Assignments**. 

!
- Check the box next to a user to assign a permission set to them
- Click **Next** at the bottom of the page.

## Stripe for Salesforce Platform setup wizard

When users first access the Stripe Connector for Salesforce app, they must
complete an Initial Setup flow. This guided wizard flow helps users authorize an
org, add a Stripe account, and configure sync preferences. After completing the
initial setup, the Account Management tab becomes the users’ landing page. Here,
they can add more Stripe accounts or navigate to other tabs to edit
configuration settings.

### Add a Stripe account using the setup wizard

- Launch the initial setup wizard, and navigate to **App Launcher > Stripe for
Salesforce Platform**

!
- Click the **Get Started** button. 

!
- Click the **Authorize** button. 

!
- After the new window opens, click **Allow** to grant access for your org.
- Click the **Next** button. 

!
- Input your Stripe API Key, and click **Add Account** button to add the Stripe
account.

!
- After you select an account, click the **Next** button. 

!
- (Optional) Click the **toggle** if you wish to enable the Stripe Events and
Sync Logs cleanup.
- If the cleanup trigger is active, enter the numerical value in the input box
to set the desired amount of records to be retained in the Salesforce org.
- Click the **Next** button. 

!
- Click the **Stripe API Version** dropdown.
- Select the **Stripe API** version to install. If you’re unsure what version to
install, select the latest version.
- Click the **Install Package** button, which launches another window that you
need to use to complete the installation of the extension package.
- Click **Finish** 

!

## See also

- [Enablement
videos](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/videos)
- [Configure
events](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/configure-events)

## Links

-
[link](https://appexchange.salesforce.com/appxListingDetail?listingId=4dff0f8e-0b10-47c2-a3a3-f3905e7f7927)
- [AppExchange
Japan](https://appexchangejp.salesforce.com/appxListingDetail?listingId=a0N3u00000RgdoWEAR)
- [Enablement
videos](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/videos)
- [Configure
events](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/configure-events)