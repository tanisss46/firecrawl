# Deploy your app with the API

## Learn how to deploy your Android app to your devices through a webhook.

After Stripe reviews and approves your app for deployment, we [notify
you](https://docs.stripe.com/terminal/features/apps-on-devices/submit#monitor-status)
by email through a webhook. You can then follow the instructions below to deploy
your app.

During deployment, your app is immediately sent and downloaded to your device.
The device reboots to install the app. Devices reboot every 24 hours and apply
any updates automatically. To check for and apply updates immediately, you can
manually reboot your device.

You can deploy new and updated apps for Terminal devices in the Dashboard.

## Add or edit a deploy group

Before you can add or edit a deploy group, you must create a Terminal
[location](https://docs.stripe.com/terminal/fleet/locations-and-zones) and add
[readers](https://docs.stripe.com/api/terminal/readers/object) to that location.
You can then assign locations to a deploy group, meaning all readers in the
location receive updates from that deploy group.

After you create a deploy group, you can edit it at any time by selecting it.

### Add a deploy group

- On the [Terminal
apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps) tab, click
**Manage deploy groups**.
- Click **Add deploy group**.
- Complete the following steps in the **Add deploy group** drawer:- Enter a
group name.
- Choose your Terminal device type.
- If desired, select the **Default deploy group** checkbox to create a default
deploy group. A default deploy group automatically contains all locations that
aren’t explicitly assigned to a different deploy group. You can create one
default deploy group per device type.
- Click **Done**.

### Manage deploy groups with destination charges

- On the [Terminal
apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps) tab, click
**Manage deploy groups**.
- Select the deploy group from the list.
- Click **Add locations**.
- Choose the locations to add.
- Click **Done**.

### Manage deploy groups with direct charges

- On the [Terminal
apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps) tab, click
**Manage deploy groups**.
- Select the deploy group from the list.
- Click **Add locations**.
- Select the account that you want to add locations from in the account
dropdown. You must select an account before adding locations.
- Choose the locations to add.
- Click **Done**.

## Deploy an app version

You can deploy your app after a [Stripe reviewer
approves](https://docs.stripe.com/terminal/features/apps-on-devices/app-review)
it.

- On the [Terminal
apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps) tab, choose
the app that you want to deploy.
- On the app details page, click **Deploy version**.
- Choose a version of the approved app, and then click **Next**. You can’t
deploy an earlier version of an app—the app version must be newer than the
currently deployed app.
- Choose the deploy group, then click **Next**.
- Choose your preferred kiosk app, then click **Next**. This is the default app
that launches when the Stripe reader turns on. If you only have one app to
deploy, choose that app instead.
- Confirm the deployment details, then click **Deploy**. The app deploys
immediately.

## Share apps across multiple accounts

Use this feature if you have multiple Stripe accounts and want to deploy the
same app across accounts. Sharing one app across accounts avoids constraints
with package name uniqueness and duplicate app reviews.

Designate one account to create and manage the app. Only the account that owns
the app can upload new app versions, but other accounts can view and deploy the
app by searching for the app ID.

- On the [Terminal
apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps) tab, click the
overflow menu ().
- Click **Search for app**.
- Enter the app ID and click **View app details**.
- Click **Deploy version** and enter the deployment details.

Deploy your app to devices by creating a device deploy group and associating it
with a [location](https://docs.stripe.com/api/terminal/locations).

## Create a device deploy group

[Create](https://docs.stripe.com/api/terminal/device_deploy_groups/create) a
device deploy group with a given `name` and `device_type`.

```
curl https://api.stripe.com/v1/terminal/device_deploy_groups \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_deploy_api_beta=v1" \
 -d name=my_toy_store_ddg \
 -d device_type=stripe_s700
```

The following response shows a `tmddg_...` identifier that you used to create
the deployment plan.

```
{
 "id": "tmddg_EuEMSgeudJ0Zyw",
 "object": "terminal.device_deploy_group",
 "current_device_asset_versions": [],
 "device_type": "stripe_s700",
 "is_default": false,
 "livemode": false,
 "name": "my_toy_store_ddg"
}
```

## Add readers to the device deploy group

Use the [location](https://docs.stripe.com/api/terminal/locations) API to add
devices to a device deploy group. You can set the `device_deploy_groups` field
on a location to map a `device_type` to the device deploy group.

The Deploy API supports the `stripe_s700` device type (used by production Stripe
S700 devices) and the `stripe_s700_devkit` device type (used by DevKit devices).

```
curl https://api.stripe.com/v1/terminal/locations/tml_EUmKfAsUh3 \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_deploy_api_beta=v1" \
 -d "device_deploy_groups[stripe_s700]"=tmddg_EuEMSgeudJ0Zyw
```

When you deploy a device asset version to a deploy group, the API validates that
the
[compatible_device_types](https://docs.stripe.com/api/terminal/device_asset_versions/object#terminal_device_asset_version_object-compatible_device_types)
parameter matches the deploy group’s `device_type`.

## Set the default app

Use the
[preferred_kiosk_app](https://docs.stripe.com/api/terminal/deploy_plans/object#terminal_deploy_plan_object-preferred_kiosk_app)
parameter to set the default app that launches on your devices.

```
curl https://api.stripe.com/v1/terminal/deploy_plans \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_deploy_api_beta=v1" \
 -d device_deploy_group=tmddg_EuEMSgeudJ0Zyw \
-d "device_asset_versions_to_install[]"=tmdav_5300BozlU0005TThQ5411LAZYXcVxtG \
-d "device_asset_versions_to_install[]"=tmdav_5300QO3Ea0005SSea9p11HdL2OHx9Vf \
 -d preferred_kiosk_app=tmda_5300slhdm0005YeJakU11De7w9i9cLi
```

## Update your app

Use the
[device_asset_versions_to_install](https://docs.stripe.com/api/terminal/deploy_plans/create#create_terminal_deploy_plan-device_asset_versions_to_install)
parameter to update the device asset version on your devices.

```
curl https://api.stripe.com/v1/terminal/deploy_plans \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_deploy_api_beta=v1" \
 -d device_deploy_group=tmddg_EuEMSgeudJ0Zyw \
-d "device_asset_versions_to_install[]"=tmdav_5300BozlU0005TThQ5411LAZYXcVxtG \
-d "device_asset_versions_to_install[]"=tmdav_5300QO3Ea0005SSea9p11HdL2OHx9Vf \
-d "device_asset_versions_to_install[]"=tmdav_5300d2sWI0015SS1YVA11HdL2OHx9Vf \
 -d preferred_kiosk_app=tmda_5300slhdm0005YeJakU11De7w9i9cLi
```

After you deploy your app, you can [monitor its
progress](https://docs.stripe.com/terminal/features/apps-on-devices/monitor).

## Uninstall your app

Use the
[device_assets_to_uninstall](https://docs.stripe.com/api/terminal/deploy_plans/create#create_terminal_deploy_plan-device_assets_to_uninstall)
parameter to uninstall your app from your devices.

```
curl https://api.stripe.com/v1/terminal/deploy_plans \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_deploy_api_beta=v1" \
 -d device_deploy_group=tmddg_EuEMSgeudJ0Zyw \
-d "device_asset_versions_to_install[]"=tmdav_5300BozlU0005TThQ5411LAZYXcVxtG \
-d "device_asset_versions_to_install[]"=tmdav_5300QO3Ea0005SSea9p11HdL2OHx9Vf \
 -d "device_assets_to_uninstall[]"=tmda_5300slhdm0005YeJakU11De7w9i9cLi \
 -d preferred_kiosk_app=tmda_5300OPKai0005SiSmpV11HdL2OHx9Vf
```

## Launch the Stripe Reader app

You can revert your device deploy group to launch the Stripe Reader app instead
of your preferred kiosk app.

In a single request, use the
[device_assets_to_uninstall](https://docs.stripe.com/api/terminal/deploy_plans/create#create_terminal_deploy_plan-device_assets_to_uninstall)
parameter to uninstall your app, then set the
[preferred_kiosk_app](https://docs.stripe.com/api/terminal/deploy_plans/create#create_terminal_deploy_plan-preferred_kiosk_app)
parameter to `STRIPE_APP` (case sensitive). Make sure there are no third-party
apps in the device deploy group.

```
curl https://api.stripe.com/v1/terminal/deploy_plans \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_deploy_api_beta=v1" \
 -d device_deploy_group=tmddg_EuEMSgeudJ0Zyw \
 -d "device_assets_to_uninstall[]"=tmda_5300slhdm0005YeJakU11De7w9i9cLi \
 -d preferred_kiosk_app=STRIPE_APP
```

## Remove readers from a device deploy group

To remove readers from a device deploy group, set the `device_deploy_groups`
parameter on a [location](https://docs.stripe.com/api/terminal/locations) to map
a `device_type` to an empty string.

```
curl https://api.stripe.com/v1/terminal/locations/tml_EUmKfAsUh3 \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_deploy_api_beta=v1" \
 -d "device_deploy_groups[stripe_s700]"=
```

## Deploy group best practices

You can sort devices into different deploy groups to roll out software
independently and isolate fault in case of any issues. You might have fewer or
more deploy groups based on tooling, risk tolerance, and specific business
needs.

We recommend the following deploy group setup:

- **Alpha** - Contains locations that correspond to your internal devkits or
internal production devices.
- **Beta** - Contains a small number of actual user locations. You can randomly
choose these locations, select them based on meaningful criteria (for example,
less risky locations), or have users opt in to the Beta deploy group based on
their risk tolerance.
- **General** - Contains all remaining actual user locations, except those in
the `Alpha` or `Beta` groups. You can use a default deploy group to avoid
manually assigning each remaining location.

When your app is ready for deployment, promote deploy groups from least to most
risky:

1AlphaFirst, deploy to the Alpha deploy group to test your app in a way that
minimizes risk to users. Discovering a bug or undesirable behavior at this stage
only affects a small number of internal devices, rather than actual users and
real payments.2BetaSecond, deploy to the Beta deploy group. This balances
exposing your app to real users and not exposing all users to potential
issues.3GeneralFinally, deploy to the General deploy group after addressing any
issues or confirming that no issues existed for the Beta deploy group.
## Next step

- [Monitor your
deployment](https://docs.stripe.com/terminal/features/apps-on-devices/monitor)

## Links

- [notify
you](https://docs.stripe.com/terminal/features/apps-on-devices/submit#monitor-status)
- [location](https://docs.stripe.com/terminal/fleet/locations-and-zones)
- [readers](https://docs.stripe.com/api/terminal/readers/object)
- [Terminal apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps)
- [Stripe reviewer
approves](https://docs.stripe.com/terminal/features/apps-on-devices/app-review)
- [Contact your sales representative](https://stripe.com/contact/sales)
- [location](https://docs.stripe.com/api/terminal/locations)
- [Create](https://docs.stripe.com/api/terminal/device_deploy_groups/create)
-
[compatible_device_types](https://docs.stripe.com/api/terminal/device_asset_versions/object#terminal_device_asset_version_object-compatible_device_types)
-
[preferred_kiosk_app](https://docs.stripe.com/api/terminal/deploy_plans/object#terminal_deploy_plan_object-preferred_kiosk_app)
-
[device_asset_versions_to_install](https://docs.stripe.com/api/terminal/deploy_plans/create#create_terminal_deploy_plan-device_asset_versions_to_install)
- [monitor its
progress](https://docs.stripe.com/terminal/features/apps-on-devices/monitor)
-
[device_assets_to_uninstall](https://docs.stripe.com/api/terminal/deploy_plans/create#create_terminal_deploy_plan-device_assets_to_uninstall)
-
[preferred_kiosk_app](https://docs.stripe.com/api/terminal/deploy_plans/create#create_terminal_deploy_plan-preferred_kiosk_app)