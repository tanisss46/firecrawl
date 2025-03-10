# Configure offline mode

## Enable or disable offline mode on your readers.

When you’re operating with intermittent, limited, or no network connectivity,
Stripe Terminal allows you to store payments locally on [your POS
device](https://docs.stripe.com/terminal/features/operate-offline/overview).
When a network connection is restored, the SDK automatically forwards any stored
payments to Stripe.

You can configure offline mode in the Dashboard or in the Configuration API.

DashboardAPI
To enable (or disable) offline mode, navigate to the relevant configuration you
want to change and edit it. If adding a new configuration, create a new one
first.

- Navigate to the [Manage
locations](https://dashboard.stripe.com/terminal/locations) page.
- Find the specific location you want to change.
- Click the overflow menu () > **Edit configuration**.
- Click **Edit** or **Override** next to the **Offline mode** icon.
- Enable (or disable) the toggle depending on your preference.
- Click **Update**.
- Apply the configuration changes by clicking **Apply changes** on the
configuration drawer.

The offline mode setting updates on the reader within 10 minutes.

## Links

- [your POS
device](https://docs.stripe.com/terminal/features/operate-offline/overview)
- [Manage locations](https://dashboard.stripe.com/terminal/locations)