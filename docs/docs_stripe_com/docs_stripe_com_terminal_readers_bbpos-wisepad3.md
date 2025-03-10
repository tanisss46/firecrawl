# BBPOS WisePad 3

## Learn about the BBPOS WisePad 3 reader.

Available in: 

!

The [BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3) is a
handheld reader for use with mobile applications. It uses [Bluetooth Low Energy
(LE)](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=bluetooth)
or
[USB](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=usb)
(Android only) to connect to the Stripe Terminal SDK on a mobile device. The
WisePad 3 features a display and PIN pad, which facilitates usage in countries
where PIN-authenticated transactions are more common.

This reader is compatible with our iOS, Android, and React Native SDKs. To view
the reader’s parts and features, see the [BBPOS WisePad 3 product
sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/wp3_product_sheet.pdf).

## Reader software releases

The software on the BBPOS Wisepad 3 consists of a firmware version,
configuration name, and key identifier. The reader **software version** joins
these three components with underscores into a single string.

CountriesLatest VersionAustraliaMalaysiaNew
Zealand`4.01.00.41.szzz.07_Prod_APAC1_on_v23_490001`Singapore`4.01.00.41.szzz.07_Prod_APAC1_off_v12_490001`AustriaBelgiumFranceGermanyItalyLuxembourgNetherlandsSwitzerland`4.01.00.41.szzz.07_Prod_EU_W1_on_v23_510001`DenmarkNorwaySweden`4.01.00.41.szzz.07_Prod_EU_W2_on_v16_510001`SpainPortugal`4.01.00.41.szzz.07_Prod_EU_W3_on_v9_510001`Czech
Republic`4.01.00.41.szzz.07_Prod_EU_E1_on_v4_51001`IrelandUnited
KingdomFinland`4.01.00.41.szzz.07_Prod_EU_W1_off_v23_510001`Canada`4.01.00.41.szzz.07_Prod_NA_off_v23_480001`
### Firmware versions

#### Note

In PCI listings, the firmware identifier is in the format `WPC3x.<batch>-xxxxx`,
where `xxxxx` is a placeholder for all firmware versions. All firmware versions
are PCI compliant.

Specifically, a PCI firmware ID `ABCDD` maps to firmware version `AA.BB.CC.DD`.
For example, `WPC3x.01-41041` maps to firmware version `4.01.00.41`.

VersionRelease Date Description`4.01.00.41.szzz.07`3/3/2025- Fixed a bug that
prevented devices from properly waking up from standby mode.
- Fixed a bug that sometimes caused issues with debit transactions.
`4.01.00.41.szzz.01`11/14/2024- Bug fixes and improvements.
`4.01.00.41`8/26/2024- Updated the transaction counter increment for the
Girocard SCA flow.
- Updated Domestic Debit Priority option OFF to be applied to a card with one
AID.
- Fixed an issue where canceling NFC card detection wasn’t allowed when the
reader presents “Try another card.”
`4.01.00.39`7/25/2024- Added code improvements.
- Added six additional CAPK key slots.
- Fixed an edge case scenario where the reader screen occasionally goes blank
when canceling power off.
- Added Tag DFDE48 for Inerac SCA PIN Request.
`4.01.00.38`5/28/2024- Added support for Girocard.
- Added support for DCPOS certification configuration.
- Fixed an error with JCB L3 Test Case 212-01 and 213-01.
- Fixed the Unknown ICC card removed error.
- Fixed the Discover DPAS L3 Test Case DGN CL 030.
- Fixed an incorrect readTerminalSetting that impacted multiple tags.
- Added a new key forcePinEntry at startEmv.
`4.01.00.37`5/1/2024- Fixed an issue where repeatedly pressing the power button
caused a Bluetooth disconnect.
- Fixed an issue with incorrect ICC Rx length checking that caused ICC
Transaction Terminated.
- Fixed an issue with the missing UI for MSR and Manual PAN Entry.
- Fixed an issue with the incorrect USB attached/detached state during device
restart.
- Fixed a Bluetooth initialization error that could cause Bluetooth connection
timeout.
- Updated the YiChip Bluetooth library to fix the Bluetooth response to an empty
packet causing a timeout and disconnection issue.
- Modified the JCB CDA Signature Verification requirement according to EMV
Bulletin No. 290.
- Increased the temperature to stop or resume charging from 40℃ to 42℃.
`4.01.00.33.SZZZ.01`1/16/2024Contains fix for an edge case scenario that
resulted reader battery level decreasing.`4.01.00.33`12/3/2023Routine firmware
maintenance updates and security updates.`4.01.00.32`4/10/2023Routine firmware
maintenance updates and security updates.`4.01.00.28`10/19/2022Routine firmware
maintenance updates and security updates.`4.01.00.27`8/30/2022Routine firmware
maintenance updates and security updates.`4.01.00.25.SZZZ.01`7/27/2022Improves
transaction processing time.Routine firmware maintenance updates and security
updates.`4.01.00.24`4/27/2022Routine firmware maintenance updates and security
updates.`4.01.00.23.szzz.01`2022-04-05Routine firmware maintenance
updates.`4.01.00.18.szzz.02`2022-02-08Fix for missing payments data that
resulted in failed collection.`4.01.00.18`2022-01-18Routine firmware maintenance
updates.`4.01.00.17.SZZZ.01`2021-09-15Contains an additional fix for an edge
case scenario that resulted in slower reader response time during PIN
entry.`4.01.00.16`2021-08-05Contains a fix for an edge case scenario that
resulted in slower reader response time during PIN
entry.`4.01.00.15.beta4`2021-05-25Contains a fix for an edge case scenario that
resulted in readers freezing during card
presentment.`4.01.00.13`2021-04-21Routine firmware maintenance
updates.`4.01.00.12.beta5`2021-02-22Contains fixes for Interac
payments.`4.01.00.11`2021-01-27Routine firmware maintenance
updates.`4.01.00.08.beta2`2020-10-14Improves reliability of transaction
processing.`4.01.00.07`2020-09-02Allows language to be selected in the settings
menu.`4.01.00.07.beta5 `2020-08-31Improves reliability of reader
events.`4.01.00.06.beta10 `2020-06-30The initial firmware version available for
this device.
### Configurations

Region (PIN type) NameRelease Date DescriptionAPAC (Online PIN)
AustraliaMalaysiaNew Zealand`Prod_APAC1_on_v23`2024-04-16Updated config for
Online PIN Asia Pacific countries.`Prod_APAC1_on_v21`2023-05-16Updated config
for Online PIN Asia Pacific countries.`Prod_APAC1_on_v8`2021-05-19Updated config
for Online PIN Asia Pacific countries.`Prod_APAC1_on_v7`2021-04-21Updated config
for Online PIN Asia Pacific countries.`Prod_APAC1_on_v6`2020-11-06Updated config
for Online PIN Asia Pacific countries.`Prod_APAC1_on_v5`2020-10-14Updated config
for Online PIN Asia Pacific countries.`Prod_APAC1_on_v4`2020-08-28Initial config
for Online PIN Asia Pacific countries.APAC (Offline PIN)
Singapore`Prod_APAC1_off_v12`2024-04-24Updated config for Offline PIN Asia
Pacific countries.`Prod_APAC1_off_v10`2023-05-09Updated config for Offline PIN
Asia Pacific countries.`Prod_APAC1_off_v7`2021-05-19Updated config for Offline
PIN Asia Pacific countries.`Prod_APAC1_off_v6`2021-04-21Updated config for
Offline PIN Asia Pacific countries.`Prod_APAC1_off_v5`2020-10-14Updated config
for Offline PIN Asia Pacific countries.`Prod_APAC1_off_v4`2020-08-28Initial
config for Offline PIN Asia Pacific countries.EMEA (Online PIN 1)
AustriaBelgiumFranceGermanyNetherlandsSwitzerland`Prod_EU_W1_on_v22`2024-05-07Updated
config for Online PIN Western European
countries.`Prod_EU_W1_on_v21`2023-06-01Updated display
brightness.`Prod_EU_W1_on_v16`2021-10-17Updated config for Online PIN Western
European countries.`Prod_EU_W1_on_v14`2021-10-06Added support for additional
languages.`Prod_EU_W1_on_v13`2021-05-19Updated config for Online PIN Western
European countries.`Prod_EU_W1_on_v9`2021-04-21Updated config for Online PIN
Western European countries.`Prod_EU_W1_on_v8`2020-11-06Updated config for Online
PIN Western European countries.`Prod_EU_W1_on_v7`2020-10-14Updated config for
Online PIN Western European countries.EMEA (Online PIN 2)
DenmarkNorwaySweden`Prod_EU_W2_on_v14`2024-04-22Updated config for Online PIN
Western European countries, sub-region 2.`Prod_EU_W2_on_v12`2023-04-19Updated
config for Online PIN Western European countries, sub-region
2.`Prod_EU_W2_on_v2`2021-10-17Initial config for Online PIN Western European
countries, sub-region 2.EMEA (Online PIN 3)
Spain`Prod_EU_W3_on_v8`2024-04-29Updated config for Online PIN Western European
countries, sub-region 3.`Prod_EU_W3_on_v6`2022-10-04Updated config for Online
PIN Western European countries, sub-region 3.`Prod_EU_W3_on_v2`2021-10-17Initial
config for Online PIN Western European countries, sub-region 3.EMEA (Offline
PIN) United KingdomIreland`Prod_EU_W1_off_v20`2024-04-22Updated config for
Offline PIN Western European countries.`Prod_EU_W1_off_v18`2023-06-01Updated
display brightness.`Prod_EU_W1_off_v12`2021-11-09Updated config for Offline PIN
Western European countries.`Prod_EU_W1_off_v10`2021-10-06Added support for
additional languages.`Prod_EU_W1_off_v9`2021-05-19Updated config for Offline PIN
Western European countries.`Prod_EU_W1_off_v6`2021-04-21Updated config for
Offline PIN Western European countries.`Prod_EU_W1_off_v5`2020-10-14Updated
config for additional Offline PIN Western European
countries.`Prod_EU_W1_off_v2`2020-08-28Initial config for Offline PIN Western
European countries.NA (Offline PIN) Canada`Prod_NA_off_v21`2024-04-22Updated
config for North American countries.`Prod_NA_off_v19`2023-06-01Updated display
brightness.`Prod_NA_off_v7`2021-05-19Updated config for North American
countries.`Prod_NA_off_v6`2021-04-21Updated config for North American
countries.`Prod_NA_off_v5`2021-02-22Initial North American config.
### Key identifiers

IdentifierCountries Description`490001`AustraliaMalaysiaNew ZealandSingaporeThe
initial key identifier available for the Asia Pacific region on this
device.`510001`AustriaBelgiumDenmarkFranceGermanyIrelandNetherlandsNorwaySwedenSpainSwitzerlandUnited
KingdomThe initial key identifier available for the European region on this
device.`480001`CanadaThe initial key identifier available for the North American
region on this device.
## Accessories for the reader

You can design your own accessories for the BBPOS WisePad 3. To download the
BBPOS WisePad 3 mechanical design files (.STP), you must first review and accept
our [Terminal Design File License
Agreement](https://stripe.com/legal/terminal-design). By downloading the file
below, you agree to the terms outlined in the license.

[Download Stripe design
files](https://d37ugbyn3rpeym.cloudfront.net/terminal/bbpos_wp3_mechanical_design_files_and_guidelines.zip)

## See also

- [Set up BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)
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

- [BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)
- [Bluetooth Low Energy
(LE)](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=bluetooth)
-
[USB](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=usb)
- [BBPOS WisePad 3 product
sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/wp3_product_sheet.pdf)
- [deviceSoftwareVersion
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReader.html#/c:objc(cs)SCPReader(py)deviceSoftwareVersion)
- [softwareVersion
(Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-reader/software-version.html)
- [Terminal Design File License
Agreement](https://stripe.com/legal/terminal-design)
- [Download Stripe design
files](https://d37ugbyn3rpeym.cloudfront.net/terminal/bbpos_wp3_mechanical_design_files_and_guidelines.zip)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [Connect to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)
- [Collect
payments](https://docs.stripe.com/terminal/payments/collect-card-payment)