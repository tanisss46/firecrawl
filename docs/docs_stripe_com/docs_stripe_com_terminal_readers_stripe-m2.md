# Stripe Reader M2

## Learn about the Stripe Reader M2 Bluetooth reader.

Available in: 
The [Stripe Reader
M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2) is a
small, robust reader for use with mobile applications. It uses [Bluetooth Low
Energy
(LE)](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=bluetooth)
or
[USB](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=usb)
(Android only) to connect to the Stripe Terminal SDK on a mobile device.

This reader is compatible with our iOS, Android, and React Native SDKs. To view
the reader’s parts and features, see the [Stripe Reader M2 product
sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/m2_product_sheet_20250221.pdf).

## LED status lights

The LEDs on top of the reader show the current status.

### LED icon meanings

Use this table to understand what the icons in the subsequent tables indicate.

IconMeaningThe light is on.The light is flashing.The light is off.
### Battery and charging status

When the Stripe Reader M2 is on, you can press and release the power button once
to check the battery level. Learn more about [Stripe M2 battery
life](https://docs.stripe.com/terminal/payments/setup-reader#device-specs-and-accessories).

LEDsMeaningFull charge75% charge50% charge25% charge(flashing) Charging
### Connectivity and reader status

When you connect to the Stripe Reader M2, you can check the LEDs for the reader
status.

LEDsMeaning(flashing, three times) Reader is connected to Bluetooth or USBReader
is in bootloader modeReader is in standby mode(flashing, every 0.1 seconds for
30 seconds) Reader tampered(30 seconds) Reader integrity check failed
## Reader software releases

The software on the Stripe Reader M2 consists of a firmware version,
configuration name, and key identifier. The reader **software version** joins
these three components with underscores into a single string.

Latest Version`2.01.00.21.szzz.01-SZZZ_Prod_US_v10-480001`
#### Firmware versions

#### Note

In PCI listings, the firmware identifier is in the format `CHB3x.<batch>-xxxxx`,
where `xxxxx` is a placeholder for all firmware versions. All firmware versions
are PCI compliant.

Specifically, a PCI firmware ID `ABCDD` maps to firmware version `AA.BB.CC.DD`.
For example, `CHB3x.01-21021` maps to firmware version `2.01.00.21`.

VersionRelease DateDescription`2.01.00.21.szzz.01``2024-11-04`Bug fixes and
improvements.`2.01.00.21``2024-05-22`- Fixed an issue where repeatedly pressing
the power button causes a Bluetooth disconnect.
- Fixed a Bluetooth initialization error that can cause Bluetooth connection
timeout.
- Fixed a bug that prevented Tag DF841A from disabling the Clear Bluetooth link
key feature.
- Modified the YiChip Bluetooth library to fix a problem that occurs when
Bluetooth continuously communicates for a long time, resulting in timeouts and
disconnects.
- Modified JCB CDA Signature Verification requirement according to EMV Bulletin
No. 290.
- Fixed an issue where ICC transactions can terminate due to incorrect ICC Rx
length checking.
- Updated the MH1901H crypto library.
`2.01.00.20``2023-10-24`Bug fixes and improvements.`2.01.00.17``2023-04-17`Bug
fixes and improvements.`2.01.00.16``2022-10-17`Bug fixes and
improvements.`2.01.00.15``2022-03-17`Bug fixes and
improvements.`2.01.00.05``2021-07-01`The initial firmware version available for
this device.
#### Configurations

NameRelease DateDescription`SZZZ_Prod_US_v10``2024-02-29`Updates production
configuration for this device.`SZZZ_Prod_US_v5``2023-04-17`Updates production
configuration for this device.`SZZZ_Prod_US_v1``2021-11-03`Updates production
configuration for this device.`SZZZ_Test_US_v6``2021-07-01`The initial
configuration available for this device.
#### Key identifiers

IdentifierRelease DateDescription`480001``2021-07-01`The initial key identifier
available for this device.
## Accessories for the reader

You can use the [Stripe Reader M2](https://dashboard.stripe.com/terminal/shop)
with an optional
[dock](https://dashboard.stripe.com/terminal/shop/thsku_JokGg2oA2nariI) for
countertop checkout, or an optional
[mount](https://dashboard.stripe.com/terminal/shop/thsku_KFGV5dfkxwiGMW) for
roaming checkout.

You can also design your own accessories for the Stripe Reader M2. To download
the Stripe Reader M2 mechanical design files (.STP), you must first review and
accept our [Terminal Design File License
Agreement](https://stripe.com/legal/terminal-design). By downloading the file
below, you agree to the terms outlined in the license.

[Download Stripe design
files](https://d37ugbyn3rpeym.cloudfront.net/terminal/stripe_reader_M2_mechanical_design_files_and_guidelines.zip)

## See also

- [Set up Stripe Reader
M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Connect to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)
- [Collect
payments](https://docs.stripe.com/terminal/payments/collect-card-payment)

## Links

- [Stripe Reader
M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2)
- [Bluetooth Low Energy
(LE)](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=bluetooth)
-
[USB](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=usb)
- [Stripe Reader M2 product
sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/m2_product_sheet_20250221.pdf)
- [Stripe M2 battery
life](https://docs.stripe.com/terminal/payments/setup-reader#device-specs-and-accessories)
- [deviceSoftwareVersion
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReader.html#/c:objc(cs)SCPReader(py)deviceSoftwareVersion)
- [softwareVersion
(Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-reader/software-version.html)
- [Stripe Reader M2](https://dashboard.stripe.com/terminal/shop)
- [dock](https://dashboard.stripe.com/terminal/shop/thsku_JokGg2oA2nariI)
- [mount](https://dashboard.stripe.com/terminal/shop/thsku_KFGV5dfkxwiGMW)
- [Terminal Design File License
Agreement](https://stripe.com/legal/terminal-design)
- [Download Stripe design
files](https://d37ugbyn3rpeym.cloudfront.net/terminal/stripe_reader_M2_mechanical_design_files_and_guidelines.zip)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Connect to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)
- [Collect
payments](https://docs.stripe.com/terminal/payments/collect-card-payment)