# Stripe connector for Google Play Store*

## Automate recurring file imports from Google Play Store to Stripe.

To set up an automated job for importing data and make sure that your Stripe
products remain up-to-date, you can import files from the Google Play Store into
the Stripe Data Management Platform.

## Before you begin

Before you integrate, make sure that you have:

- An active Google Cloud and Play Console account with access to the application
files.
- Admin account access to the Stripe Dashboard.
- Enabled the APIs for Google Cloud Storage and Google Play Android Developer.
- A service account on Google Cloud platform. The Data Connector uses this
account to access your application’s financial reports.
- The private key of your service account that’s saved securely.
- The service account added under **Users and permissions** in Play Console.
- The application’s package name (the URL below the app name in Play Console)
and Google Cloud Storage URI.

#### Disclaimer

Note: By using this Stripe Connector you warrant that you’ve obtained the
requisite permissions, and provided the necessary notices and consents required,
in order for you to use the Stripe Connector and to enable Stripe to provide you
the Services.

[Enable the
APIs](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#enable-apis)
To enable the necessary APIs:

- Sign in to the [Google Cloud Console](https://console.cloud.google.com/), then
select your project for the application in the top left corner.
- Click **API and Services** > **Enabled APIs & services** in the left pane.
- If the list on this page contains the **Cloud Storage API** and the **Google
Play Android Developer API**, skip this step and [create a service account
key](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#generate-keys)
instead. Otherwise, click **Enable APIs and Service**.
- Search for **Play Store**, then select **Google Play Android Developer API**.
- Click the **Enable** button.
[Set up a service
account](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#create-service-account)
To create a service account:

- Click **Credentials** under **APIs & Services** in the left pane.
- Click **+ Create credentials** > **Service account**.
- Enter a name and description for the service account. The Data Connector uses
this account to access your application’s financial reports.
- Add the **Storage Object Viewer** role from the **Role** dropdown, then click
**Done**.
[Create service account
keys](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#generate-keys)
After you create the service account, Google Cloud redirects you to the
Credentials page. From this page:

- Click the service account that you created.
- On the Keys page, click **Add key** > **Create new key**.
- Select **JSON**, then click **Create** to download a private key on your
device. Make sure that you secure this private key. If you lose it, you must
generate a new one because it’s the only copy of the private key.
[Integrate the service account in Play
Console](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#add-service-account)
To integrate the service account on Play Console:

- On the [Play Console page](https://play.google.com/console/), click **Users
and permissions** in the left pane.
- Click **Invite new user**.
- Enter the email address of the service account you created.
- Under **App permissions**, click **Add app**.
- Select the app that you want to integrate with, then click **Apply**.
- Select **View app information (read-only)**, **View financial data**, and
**Manage orders and subscriptions**, then click **Apply**.
- Click **Invite user** > **Send Invite**.
[Submit the service account credentials and app package
name](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#submit-service-account)
To submit the service account credentials and your app package name:

- In the Google Play Store Console Dashboard, click ** Cloud Storage URI**
to copy your Google Cloud Storage URI. The URI begins with `pubsite_prod_rev`
(for example, `pubsite_prod_rev_01234567890987654321`).
- Enter your App Package Name. This is the URL that appears under the app name
in the Play Console.
- Use the secure link that we provide to upload the Service Account Credentials
JSON file.
[Configure the Stripe connector for Google Play
Store](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#upload-api-key)
To configure the Stripe connector for Google Play Store using Stripe:

- Click **+ Set up connector** > **Google Play Store** in the [Connectors tab on
the Data management
page](https://dashboard.stripe.com/data-management/connectors).
- Enter a name, then click **Next**.
- Review the permissions, then click **Next**.
- Upload your private key file to the **Private key** section. Then, enter the
**App package name** and **Google Cloud Storage Bucket ID** [that you created
for the service
account](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#generate-keys).
- Click **Authenticate** to establish a connection.
[Maintain your Google Play Store
connection](https://docs.stripe.com/stripe-data/import-external-data/connectors/google-play#maintain-connection)
After Stripe establishes your connection, it takes up to 24 hours for the first
sync to begin showing your data in the Dashboard. After that, we fetch your data
once a day. To monitor the health of your connection:

- View the status and the latest sync details of your established connections in
the [Data Management Connector
Dashboard](https://dashboard.stripe.com/data-management/connectors).
- Click the connector to manage an individual connection. You can edit the name,
re-authenticate a broken connection, and delete a connection.

*Google Play is a trademark of Google LLC.

## Links

- [Google Cloud Console](https://console.cloud.google.com/)
- [Play Console page](https://play.google.com/console/)
- [Connectors tab on the Data management
page](https://dashboard.stripe.com/data-management/connectors)