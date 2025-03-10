# Configure the reboot time window

## Customize the reboot time window for your readers.

By default, BBPOS WisePOS E and Stripe Reader S700 readers reboot every 24 hours
at midnight. If your business is open or processing payments during this time,
you might want to set a custom reboot window to avoid any interruptions.

You can set a specific time period for the devices to reboot according to their
registered location’s local time. For example, if you register a device in a
location with a local time corresponding to UTC-8:00, but it’s managed from a
location in UTC-5:00, the scheduled reboot time is UTC-8:00.

#### Note

To avoid disruption, not every reader in the same registered location updates
simultaneously. Instead, the readers reboot randomly within the configured time
period.

DashboardAPI
To change the reboot window, navigate to the relevant configuration you want to
change and edit it. Add a new configuration first if you don’t have an existing
one.

- Navigate to the [Manage
locations](https://dashboard.stripe.com/terminal/locations) page.
- Find the specific location you want to change.
- Click the overflow menu () > **Edit configuration**.
- Click **Edit** or **Override** next to the **Reboot time** icon.
- Select a start and end time. If `start_hour` is less than `end_hour`, we
consider them as values for the same day. If `start_hour` is greater than
`end_hour`, we consider the `end_hour` a value for the next day.
- Click **Update**.
- Apply the configuration changes by clicking **Apply changes** on the
configuration drawer.

Stripe sets the new reboot window within 10 minutes. If the reader has already
rebooted for the day, the reboot window takes effect during the next time
period.

## Links

- [Manage locations](https://dashboard.stripe.com/terminal/locations)