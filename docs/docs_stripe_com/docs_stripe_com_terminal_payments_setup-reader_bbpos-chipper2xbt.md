# Set up BBPOS Chipper 2X BT

## Learn how to set up the BBPOS Chipper 2X BT.

#### Note

This reader is no longer available for purchase. If you’re getting started with
Stripe Terminal, we recommend [viewing our current reader
offerings](https://docs.stripe.com/terminal/payments/setup-reader).

!

The BBPOS Chipper 2X BT is a handheld reader for use with mobile applications.
It uses Bluetooth Low Energy (LE) or USB (Android only) to
[connect](https://docs.stripe.com/terminal/payments/connect-reader) to the
Stripe Terminal SDK on a mobile device.

This reader is compatible with iOS, Android, and React Native SDKs. To view the
reader’s parts and features, see the [BBPOS Chipper 2X BT product
sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/c2xbt_product_sheet.pdf).

## Turn the reader on and off

You can turn on the BBPOS Chipper 2X BT reader by pressing and releasing the
power button. The status light turns on to indicate power. The reader waits for
a connection for five minutes before turning off.

When the reader [connects to a device running your
app](https://docs.stripe.com/terminal/payments/connect-reader), its status light
shines steady blue. If inactive for more than 30 seconds, it enters standby mode
to conserve power, and the status light begins flashing at 5-second intervals.
The reader stays connected to your iOS or Android device while in standby and
automatically exits standby mode when you resume activity.

The reader automatically turns off after 10 hours of inactivity. You can turn
the reader off manually by pressing and holding the power button until the
status light goes out. You don’t need to turn off the reader to conserve power.

#### Note

With typical usage, you only need to fully [charge the
reader](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-chipper2xbt#charging)
once per day.

## Status light

When you turn on the BBPOS Chipper 2X BT, the LED located beside the power
button shows the reader’s current status.

LightMeaningNoneThe reader is off.Flashing blue every secondThe reader is on and
ready to connect to a device. (Will turn off after 5 min.)Multicolored
flashingThe reader has been discovered using [Bluetooth
Proximity](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#bluetooth-proximity)
or USB (Android only) and is ready to connect.Steady blueThe reader is connected
to a device.Flashing blue every 5 secondsThe reader is in standby mode. (Will
remain in standby indefinitely.)Alternating red and magentaThe reader is
charging.Flashing redThe reader’s battery is low.Rapidly flashing blue and
orangeThe reader has finished installing a software update. If the reader is
unresponsive after the update completes, restart the reader by turning it off
and on.
## Charge the reader

To charge the BBPOS Chipper 2X BT, use the included cable or a micro USB cable.

## See also

- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Chipper 2X BT
reference](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of
BBPOS Limited in the United States and/or other countries. The Verifone® name
and logo are either trademarks or registered trademarks of Verifone in the
United States and/or other countries. Use of the trademarks does not imply any
endorsement by BBPOS or Verifone.

## Links

- [viewing our current reader
offerings](https://docs.stripe.com/terminal/payments/setup-reader)
- [connect](https://docs.stripe.com/terminal/payments/connect-reader)
- [BBPOS Chipper 2X BT product
sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/c2xbt_product_sheet.pdf)
- [Bluetooth
Proximity](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#bluetooth-proximity)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Chipper 2X BT
reference](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt)