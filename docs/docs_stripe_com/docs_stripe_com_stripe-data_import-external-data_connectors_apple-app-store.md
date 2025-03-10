# Stripe connector for Apple App Store®*

## Automate recurring file imports from Apple App Store to Stripe.

To set up an automated job for importing data and make sure that your Stripe
products remain up-to-date, you can import files from the Apple App Store into
Stripe’s data management platform.

## Before you begin

Before you integrate, make sure that you have:

- An active Apple Developer and App Store Connect account with access to the
application files.
- Admin account access to the Stripe Dashboard.
- An App Store Connect API key with at least the access level of Admin, Finance,
or Sales.
- The `.p8` key file that’s saved securely. You need to upload this key to
Stripe.
- The Issuer ID associated with the API key.
- The Vendor Number located in the App Store Connect under **Payments and
Financial Reports**.

#### Disclaimer

Note: By using this Stripe Connector you warrant that you’ve obtained the
requisite permissions, and provided the necessary notices and consents required,
in order for you to use the Stripe Connector and to enable Stripe to provide you
the Services.

[Generate an App Store Connect API
key](https://docs.stripe.com/stripe-data/import-external-data/connectors/apple-app-store#generate-an-app-store-connect-api-key)
To create a new App Store Connect API key:

- Navigate to **Users and Access** > **Integrations** in your [App Store Connect
Dashboard](https://appstoreconnect.apple.com/access/api).
- Select the **Team Keys** sub-tab.
- Click the plus icon () next to the heading of active keys table.
- Enter a name, then select **Finance role** to create an API Key.
- Hover over the API key to access additional options, then click **Download API
Key** to download the key.

Locate the **Key ID** in the third column of the **Active keys** table and
identify the **Issuer ID** directly above the same table.

To locate your **Vendor number**:

- Navigate to [App Store Connect Dashboard](https://appstoreconnect.apple.com/).
- Click **Payments and Financial Reports**, then access the **Vendor number**
under **Legal entity name**.
[Configure the Stripe connector for Apple App
Store](https://docs.stripe.com/stripe-data/import-external-data/connectors/apple-app-store#upload-api-key)
To upload the App Store Connect API key to Stripe:

- Click the [Connectors tab on the Data management
page](https://dashboard.stripe.com/data-management/connectors) or the [Data
import tab on the Revenue recognition
page](https://dashboard.stripe.com/revenue-recognition/data-import).
- Click **+ Set up connector** > **Stripe Connector for Apple App Store**.
- Enter a name, then click **Next**.
- Upload your `.p8` file in the **Private Key** section.
- Enter the **Key ID**, **Issuer ID**, and **Vendor number** that you generated.
[Maintain your Apple App Store
connection](https://docs.stripe.com/stripe-data/import-external-data/connectors/apple-app-store#maintain-connection)
After Stripe establishes your connection, we fetch your data once a day. To
monitor the health of your connection:

- View the status and the latest sync details of your established connections on
the [Data management
page](https://dashboard.stripe.com/data-management/connectors).
- Click the connector to manage an individual connection. You can edit the name,
re-authenticate a broken connection, and delete a connection.

### Data syncing requirements

Stripe can only sync reports if you have agreed to the Apple Developer
Agreement. Stripe can’t sync data if the agreement has expired or the latest
agreement has not been accepted. In these cases, Stripe sends a notification
email to the merchant’s primary email.

Go to [Apple App Store Connect](https://appstoreconnect.apple.com/login) to
review and either accept the latest version of the Developer Agreement or renew
your existing agreement. Learn more about [signing and updating
agreements](https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements).

*Apple and App Store are trademarks of Apple Inc., registered in the U.S. and
other countries and regions.

## Have questions about Stripe Connector for Apple App Store?

Please provide your email address below and our team will be in touch.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [App Store Connect Dashboard](https://appstoreconnect.apple.com/access/api)
- [App Store Connect Dashboard](https://appstoreconnect.apple.com/)
- [Connectors tab on the Data management
page](https://dashboard.stripe.com/data-management/connectors)
- [Data import tab on the Revenue recognition
page](https://dashboard.stripe.com/revenue-recognition/data-import)
- [Apple App Store Connect](https://appstoreconnect.apple.com/login)
- [signing and updating
agreements](https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements)
- [privacy policy](https://stripe.com/privacy)