# Verifone P400

## Learn about the Verifone P400 reader.

#### Note

This reader is no longer available for purchase. If you’re getting started with
Stripe Terminal, we recommend [viewing our current reader
offerings](https://docs.stripe.com/terminal/payments/setup-reader).

!

The [Verifone
P400](https://docs.stripe.com/terminal/payments/setup-reader/verifone-p400) is a
countertop reader for Stripe Terminal apps. It
[connects](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet)
to the Stripe Terminal SDK over the internet.

This reader is compatible with JavaScript, iOS, Android, and React Native SDKs.
To view the reader’s parts and features, see the [product
sheet](https://www.verifone.com/sites/default/files/2018-01/p400_datasheet_ltr_013018.pdf).

## Troubleshoot the reader

Make sure your network meets all of our [network
requirements](https://docs.stripe.com/terminal/network-requirements), and try
the steps in the [network
troubleshooting](https://docs.stripe.com/terminal/network-requirements#troubleshooting)
section.

To begin troubleshooting, use the following common scenarios to help diagnose
what’s broken.

### Reader is unable to connect

Stripe provides two debug screens on the reader. Use these screens to help
diagnose common connectivity and network issues. To access a debug screen, enter
the following key sequences while on the splash screen:

Key SequenceDebug ScreenDescription0-4-2-6-8Device StatusShows the device’s IP
address, account ID, location, gateway, network mask, and connectivity
status.0-8-6-2-4ConnectivityStarts a network test, by attempting to connect to
the required endpoints.
To exit a debug screen, press **0** on the keypad. You can also program your app
to re-render the screen by calling any of these functions:

- `connectReader()`
- `collectPayment()`
- `setReaderDisplay()`

#### Note

Debug screens overlay the reader’s normal screen display, and can trigger only
while on the [reader
screens](https://docs.stripe.com/terminal/readers/verifone-p400#reader-screens)
shown above.

### Reader is unable to update

If your reader isn’t updating, it’s possible that it can’t connect to Stripe.
Make sure the network it’s connected to meets our [network
requirements](https://docs.stripe.com/terminal/network-requirements).

### Reader doesn’t have IP address

The **Device Status** [debug
screen](https://docs.stripe.com/terminal/readers/verifone-p400#checking-connectivity)
shows the reader’s IP address, or **No ETH** if the device doesn’t have an IP
address. Use the following steps to debug a **No ETH** condition.

**Other IP-address**

If the above steps don’t reveal an IP address on the reader, try these
additional steps:

- Unplug and reconnect the Ethernet connection to the network source (that is,
the modem for router networking, or your computer for bridged networking).
- Restart the reader with the network source attached to it. You can restart the
reader by unplugging and reconnecting the power cable from the connector cable.
- Check the connectors for any broken hardware (such as bent pins).

#### Note

Remember to connect *production* deployments to the merchant network through
router networking.

### Reader has IP address, but is unable to communicate with Stripe

The **Connectivity** [debug
screen](https://docs.stripe.com/terminal/readers/verifone-p400#checking-connectivity)
indicates the connection status between the P400 and Stripe. Refer to our
[network requirements](https://docs.stripe.com/terminal/network-requirements)
for details and further troubleshooting steps.

## Stripe reader software

Stripe maintains the software that controls the Verifone P400. The reader
receives updates automatically from Stripe when not in use. Read about [reader
software
updates](https://docs.stripe.com/terminal/payments/setup-reader#reader-software-updates)
for details. These can include improvements and required security updates from
Stripe and our hardware partners. As reader software updates are made available,
update your readers to the latest available version to continue using Stripe
Terminal. Failing to install a required update can prevent a reader from
accepting payments.

The reader restarts every day at midnight for PCI compliance, and disconnects
from the POS app every morning. Leave your reader connected to power to receive
automatic software updates. This ensures that updates happen at midnight (in the
timezone of the [assigned
location](https://docs.stripe.com/terminal/fleet/locations-and-zones)) to avoid
interruption to sales. If you unplug the reader at night, an update could start
when you turn it back on. To manually check for an update, reboot the reader.

You can always check the current reader version by pressing **0-4-2-6-8**.

### Verifone P400 software releases

VersionDescription`3.0.2.5`Bug fixes and performance improvements.`3.0.2.3`Fixed
`cardholder_name` for contactless transactions.`3.0.2.1`Updated server on-device
to now host a unique PQDN per device.`3.0.1.18`Improved reader
reliability.`3.0.1.16`Updated messaging to more strongly advocate for the use of
contactless payment methods.`3.0.1.15`Added automatic handling of soft
declines.`3.0.1.14`Added support for `cardholder_name` in payment method
details.`3.0.1.13`Added support for additional integration methods, fixed some
localization issues.`3.0.1.12`Fixed some international refunds issues, improved
WiFi disconnection handling and retries.`3.0.1.10`Added regional support for
Canadian merchants.`3.0.1.8`Added improved triaging tools, bug fixes, and
prerequisite work for future features.`3.0.1.6`Implemented WiFi upgrades
improving re-connection of cached networks, bug fixes.`3.0.1.5`Added support for
regional EMV configurations, bug fixes.`3.0.1.2`Changed red `X` button behavior
in testmode (now clears a transaction’s payment method instead of canceling that
transaction; this mirrors livemode behavior), added MAC address to Device Status
debug screen, bug fixes.`3.0.1.0`Added new reader screens for better UX,
disabled contactless sources during `readReusableCard`, fixed bugs.
For additional instruction on maintaining [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
when installing updates to your Verifone P400 device, refer to the reader PCI
[implementation
guide](https://d37ugbyn3rpeym.cloudfront.net/docs/files/terminal/terminal_implementation_guide.pdf).

## See also

- [Set up Verifone
P400](https://docs.stripe.com/terminal/payments/setup-reader/verifone-p400)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Connect to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)
- [Collect
payments](https://docs.stripe.com/terminal/payments/collect-card-payment)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of
BBPOS Limited in the United States and/or other countries. The Verifone® name
and logo are either trademarks or registered trademarks of Verifone in the
United States and/or other countries. Use of the trademarks does not imply any
endorsement by BBPOS or Verifone.

## Links

- [viewing our current reader
offerings](https://docs.stripe.com/terminal/payments/setup-reader)
- [Verifone
P400](https://docs.stripe.com/terminal/payments/setup-reader/verifone-p400)
-
[connects](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet)
- [product
sheet](https://www.verifone.com/sites/default/files/2018-01/p400_datasheet_ltr_013018.pdf)
- [network requirements](https://docs.stripe.com/terminal/network-requirements)
- [network
troubleshooting](https://docs.stripe.com/terminal/network-requirements#troubleshooting)
- [reader software
updates](https://docs.stripe.com/terminal/payments/setup-reader#reader-software-updates)
- [assigned
location](https://docs.stripe.com/terminal/fleet/locations-and-zones)
- [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [implementation
guide](https://d37ugbyn3rpeym.cloudfront.net/docs/files/terminal/terminal_implementation_guide.pdf)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Connect to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)
- [Collect
payments](https://docs.stripe.com/terminal/payments/collect-card-payment)