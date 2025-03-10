# Set up Stripe Reader S700

## Learn how to set up Stripe Reader S700.

Available in: 

!

Stripe Reader S700 is an Android-based smart reader for countertop and handheld
use. You can customize the on-reader checkout UI using a suite of pre-built and
custom elements.

The [Stripe Terminal SDK connects to the
reader](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet)
over the internet, LAN, or [handoff
mode](https://docs.stripe.com/terminal/features/apps-on-devices/build#discover-and-connect-a-reader).

This reader is compatible with the following integrations:

- JavaScript SDK
- iOS SDK
- Android SDK
- React Native SDK
- Server-driven

For Stripe Reader S700, we recommend the [server-driven
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=server-driven),
which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts
and features, see the [Stripe Reader S700 product
sheet](https://d37ugbyn3rpeym.cloudfront.net/docs/assets/s700_product_sheet.612cfab6b7effea90f2164ba79898a0165675e951faa3378068646c8c8bbc0ee.pdf).

## Turn the reader on and off

Connect the reader to power by plugging the provided USB-C cable into the port
on the left side of your reader. Connect the opposite end of the USB-C cable to
the provided power adapter and plug it into a power outlet. The Stripe Reader
S700 requires a recommended 12W of power to operate properly. Stripe power
adapters and cables are recommended for the charging and operation of the S700
and its accessories. Using alternative power adapters or cables might result in
failure modes including inadequate S700 charging, and might invalidate your
product warranty.

![Side of Stripe Reader
S700](https://b.stripecdn.com/docs-statics-srv/assets/s700-side-view.66affe17a0aeac5999a561f44d67bfbc.png)

Stripe Reader S700

After the reader is fully charged, hold down the power button on the right side
until the screen turns on. After the device powers on, press the power button to
sleep or wake the device. To fully power off the device, hold down the power
button until the power off option appears on the screen, then select it.

In a countertop deployment, leaving the device on for extended periods is
expected. With a full charge, you can expect the battery to last about 15 hours.

Even when not in use, leave Stripe Reader S700 plugged in and powered on to
receive automatic software updates.

## Access settings

To open the settings menu, swipe right from the left edge of the reader screen
to reveal a **Settings** button. Tap the **Settings** button and enter the admin
PIN `07139`. From here, you can update your WiFi settings or generate a pairing
code for device registration. Battery status is displayed at the top right of
this screen. To close the settings menu, click the back arrow in the top left
corner.

!

Settings button

!

Admin PIN screen

!

Settings menu

## Screen timeout

The screen times out when the reader isn’t connected to a power source. The
default timeout of 1 hour improves battery performance. To update this value, go
to the
[settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700#settings),
select **Appearance**, then select a new screen timeout from the dropdown. The
device screen turns on automatically after a device interaction occurs (such as
touching the screen or picking up the device), or when the device enters the
payments flow and a payment is initiated.

!

Settings menu

!

Appearance menu

!

Timeout menu

## Connect the reader to the internet

Because the Stripe Reader S700 is a smart reader, its reader software
communicates directly with Stripe. Your point of sale application communicates
with the reader through either a LAN (using a Terminal SDK) or the internet
(using the [server-driven
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)).
When communicating with the reader through the LAN, the reader must connect to
the same local network as your point of sale application. If you’re running into
issues connecting your reader to the internet, follow the [troubleshooting
steps](https://docs.stripe.com/terminal/readers/stripe-reader-s700#troubleshooting)
to diagnose the issue.

### WiFi

To connect to WiFi or switch networks, go to
[settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700#settings),
then select **WiFi settings** to choose the network and connect. Attempting to
join a new network disconnects the reader from any existing wireless connection.
Learn more about our [network
requirements](https://docs.stripe.com/terminal/network-requirements) and how to
[configure advanced network
settings](https://support.stripe.com/questions/bbpos-wisepos-e-stripe-reader-s700-advanced-network-settings)
for supported WiFi networks.

### Ethernet and USB Peripherals

Ethernet connectivity requires an optional hub, which provides wired 10/100
Ethernet connectivity and allows your smart reader to remain fully charged with
the included charging cable. The hub also provides two USB-A ports to connect
peripherals such as a barcode scanner and printer. The hub is compatible with
the S700 Dock for countertop applications. You can purchase the hub and dock
separately in the [Stripe
Dashboard](https://dashboard.stripe.com/terminal/shop).

To set up the hub:

- Connect the Ethernet cable from your hub to your router.
- Connect the hub to power through the built-in USB-C cable. We recommend using
the power adapter included with your tripe Reader S700 to make sure the
appropriate power is provided to the hub (27W) to power the reader and attached
peripherals.
- Connect the USB-C cable (provided with Stripe Reader S700) to the hub and
reader when both cables are in place. The right-angle USB-C connector connects
to the reader.

To confirm the reader’s Ethernet connectivity, verify that the reader is
charging and check if the Ethernet icon is visible in the status bar.

Charging icon

Ethernet icon

The reader obtains an IP address using DHCP. As soon as the network cable is
plugged in, the reader attempts to establish communication with Stripe.

!

Hub when used with Dock (sold separately)

!

Hub with peripherals. Ethernet connected and power connected to Stripe Reader
S700.

For more information about these accessories, see [Stripe Reader S700
accessories](https://docs.stripe.com/terminal/payments/stripe-reader-s700/accessories).

## Network priority

The Stripe Reader S700 prioritizes connecting through Ethernet if possible. Even
if previously configured for WiFi, the reader switches to using an Ethernet
connection when connected to the dock with a plugged-in Ethernet cable. If you
remove the reader from the dock, it switches back to the WiFi connection.

If you dock the reader, but you don’t have an Ethernet cable plugged in, it uses
WiFi. Regardless of connectivity while docked, you can still connect to WiFi and
manage networks on the device.

## Change the UI appearance

By default, the user interface of your Stripe Reader S700 reader uses a light
theme.

Welcome screen

Payment screen

Processing screen

Approved screen

You can change the appearance of the UI to use a different theme in the settings
menu. Go to
[settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700#settings),
then select **Appearance**, and select a new theme from the dropdown.

!

Settings menu

!

Appearance menu

!

Theme menu

## Change the default reader language

Stripe Reader S700 supports changing the reader language in the [reader
settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700#access-settings)
menu. Swipe right across the screen to access the settings menu, and select your
language.

## Design your own accessories

You can design your own accessories for the Stripe Reader S700. To download the
Stripe Reader S700 mechanical design files (.STP), you must first review and
accept our [Terminal Design File License
Agreement](https://stripe.com/legal/terminal-design). By downloading the file
below, you agree to the terms outlined in the license.

[Download Stripe design
files](https://d37ugbyn3rpeym.cloudfront.net/terminal/Stripe-Reader-S700-and-Accessories-Design-Files.zip)

### Custom mounting attachment

If you’re interested in designing your own custom mounting attachment, see the
[Stripe Reader S700 Accessory Design
Guidelines](https://d37ugbyn3rpeym.cloudfront.net/terminal/Stripe-Reader-S700-Accessories-Design-Files-Mechanical-Usage-Guidelines.pdf).

## See also

- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Stripe Reader S700
reference](https://docs.stripe.com/terminal/readers/stripe-reader-s700)

## Links

- [Dashboard](https://dashboard.stripe.com/terminal/shop/)
- [Stripe Terminal SDK connects to the
reader](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet)
- [handoff
mode](https://docs.stripe.com/terminal/features/apps-on-devices/build#discover-and-connect-a-reader)
- [server-driven
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)
- [Stripe Reader S700 product
sheet](https://d37ugbyn3rpeym.cloudfront.net/docs/assets/s700_product_sheet.612cfab6b7effea90f2164ba79898a0165675e951faa3378068646c8c8bbc0ee.pdf)
- [troubleshooting
steps](https://docs.stripe.com/terminal/readers/stripe-reader-s700#troubleshooting)
- [network requirements](https://docs.stripe.com/terminal/network-requirements)
- [configure advanced network
settings](https://support.stripe.com/questions/bbpos-wisepos-e-stripe-reader-s700-advanced-network-settings)
- [Stripe Dashboard](https://dashboard.stripe.com/terminal/shop)
- [Stripe Reader S700
accessories](https://docs.stripe.com/terminal/payments/stripe-reader-s700/accessories)
- [Terminal Design File License
Agreement](https://stripe.com/legal/terminal-design)
- [Download Stripe design
files](https://d37ugbyn3rpeym.cloudfront.net/terminal/Stripe-Reader-S700-and-Accessories-Design-Files.zip)
- [Stripe Reader S700 Accessory Design
Guidelines](https://d37ugbyn3rpeym.cloudfront.net/terminal/Stripe-Reader-S700-Accessories-Design-Files-Mechanical-Usage-Guidelines.pdf)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Stripe Reader S700
reference](https://docs.stripe.com/terminal/readers/stripe-reader-s700)