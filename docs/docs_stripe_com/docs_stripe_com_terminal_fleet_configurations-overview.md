# Terminal configurations

## Use the Terminal Configurations object to apply configurations to your readers.

The Terminal [Configuration](https://docs.stripe.com/api/terminal/configuration)
object contains all relevant configurations for a reader, such as the splash
screen, tipping settings, offline mode, and so on. Because these settings are
hierarchical, you can apply a configuration at either the account level or at
the individual location level. You can set configurations in the following ways:

- On individual [Locations](https://docs.stripe.com/api/terminal/locations):
Applies to all readers registered to that Location
- At the account level: Applies to all readers in your fleet

You can override account-level settings with location-level settings. If you
don’t configure settings at the location level, they inherit the account-level
settings.

#### Note

We don’t support assigning or adding configurations to zones.

For example, you can model your `Configuration` objects as follows:

![Configuration
Hierarchy](https://b.stripecdn.com/docs-statics-srv/assets/configuration-object-tree.5ec745ad57500a800c4f34f0a970224e.png)

In this scenario, Location 3 inherits the configurations from the account
“Default configuration”, while Locations 1 and 2 have their own configuration.

#### Note

If you don’t set a configuration on the location-level, the Location inherits
the default configuration on the account. For example, if you don’t set the
splash screen on the Location, it inherits it from the default configuration set
at the account level.

Any configuration changes made with the API or Dashboard can take up to 10
minutes to reflect on the target readers.

DashboardAPI
You can view and manage your configurations in the Stripe Dashboard. To manage
your configurations, click **Manage locations** on the Readers tab. Stripe
displays a list of configurations on the right hand side of the page. To view
additional configurations, click **View more** at the bottom of the list.

## Update the default configuration for the account

- Select the overflow menu () on the **All locations** list item (top).
- Click **Edit configuration**.
- Click **Override** for each configuration type you want to update.
- Click **Apply changes**.

All readers across all locations inherit the configuration settings that you
set, unless there’s an override set on the configuration for the location. The
reader updates within 10 minutes after you add the configuration.

## Create a new configuration for a location

- Select the overflow menu () on the location item.
- Click **Add configuration**.
- Enter a name for the configuration. You can use this name more than once.
- Click **Override** for each configuration type you want to update.
- Click **Apply changes**.

All readers in the location inherit the configuration settings that you set. The
reader updates within 10 minutes after you add the configuration.

## Update an existing configuration

- Select the overflow menu () on either the location list item (left side) or
the configuration itself (right side).
- Click **Edit configuration**.
- Click **Override** for each configuration type you want to update.
- Click **Apply changes**.

All the readers in the location update within 10 minutes.

## Delete an existing configuration

- Select the overflow menu () on either the location list item (left side) or
the configuration itself (right side).
- Click **Delete configuration**.

After you delete the configuration, the readers in the location default back to
the account’s default configuration within 10 minutes.

## Links

- [Configuration](https://docs.stripe.com/api/terminal/configuration)
- [Locations](https://docs.stripe.com/api/terminal/locations)