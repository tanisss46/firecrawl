# Configure on-reader tips

## Customize the tipping options displayed on your readers.

You can use [on-reader
tips](https://docs.stripe.com/terminal/features/collecting-tips/overview) to
display suggested tip amounts on the reader before customers present their
payment method. We support the following on-reader tip types:

- **Suggest smart tips**: The reader dynamically displays three percentages or
amounts, depending on the size of the pre-tip amount.
- **Suggest percentages**: The reader displays three percentage-based tip
amounts.
- **Suggest amounts**: The reader displays three tip amounts.
DashboardAPI
To configure on-reader tips:

- Navigate to the [Manage
locations](https://dashboard.stripe.com/terminal/locations/) page.
- Find the specific location you want to change.
- Click the overflow menu () > **Edit configuration** to display the
configuration drawer.
- Click **Edit** or **Override** next to the **Tipping** icon.
- Choose the **Tipping mode**.
- Choose the **Currency**.
- Enter the desired tipping options (for example, you can enter 10%, 15%, and
20% for percentage-based tipping), and repeat this process for different tipping
modes and currencies.
- Click **Review** to view your changes, then click **Confirm**.
- Click **Apply changes**.

Stripe applies the tipping configurations on the reader within 10 minutes.

## Links

- [on-reader
tips](https://docs.stripe.com/terminal/features/collecting-tips/overview)
- [Manage locations](https://dashboard.stripe.com/terminal/locations/)