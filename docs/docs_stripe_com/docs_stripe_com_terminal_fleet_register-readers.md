# Register readers

## Register your readers to a location.

You must register your reader to a location to accept payments. The process for
registering your reader to a location differs based on whether it’s a [smart
reader](https://docs.stripe.com/terminal/smart-readers) or a [mobile
reader](https://docs.stripe.com/terminal/mobile-readers).

Any [user role](https://docs.stripe.com/get-started/account/teams/roles) with
write permissions can register readers.

## Smart readers

You can register smart readers in one of three ways:

- Registration code
- Serial number
- Order number

### Registration code

For this method, you must generate a pairing code (also known as a registration
code) on the reader. If a reader isn’t registered, a pairing code automatically
appears on the screen when you unbox it. If it isn’t, or if you need to
re-register a reader, you can generate a new pairing code using the [admin
settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700#settings).
After generating the pairing code, you can enter it in the Dashboard or API to
register the reader.

DashboardAPI- On the **Readers** tab on the [Terminal
Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register
Reader**.
- Enter the pairing code on the reader and click **Next**.
- Provide a name for the reader.
- Assign to a location or create a new one.
- Confirm the details and click **Register**.

### Serial number

You can register readers using their serial number. This method doesn’t require
someone to physically have the reader to register it, so you can use it
immediately after you unbox it. This method also allows you to re-register the
reader without the need to physically have the reader to generate a pairing
code.

You can find the serial number in four ways:

- From the hardware order on the [Hardware
Orders](https://dashboard.stripe.com/terminal/hardware_orders) tab
- From the [Hardware Order Devices
API](https://docs.stripe.com/api/terminal/hardware_order_devices)
- On the reader itself (on the box and the back of the reader)
- If the reader is already registered, from the reader details page in the
Dashboard or the [Reader API](https://docs.stripe.com/api/terminal/readers)

#### Note

This method only works for readers that were ordered by the account. For
Platforms, the platform or the sub-account must have placed the order to
register it to a sub-account.

#### Note

This method allows you to register up to 10 readers at a time.

DashboardAPI
After you find the serial number, you can register the reader through the
registration flow in the Dashboard.

- On the [Terminal Readers](https://dashboard.stripe.com/terminal/readers) page,
click **Register reader**.
- Enter the serial number and click **Next**. To register multiple devices at
once, you can enter multiple serial numbers, separated by commas.
- Optionally, choose a name for the reader.
- If you already created a location, select the reader’s new location.
Otherwise, create a location by clicking **+ Add new**.
- Click **Register** to finish registering your reader.

### Order number

#### Note

This method only works for readers that were ordered by the account (or one of
their sub-accounts). If the reader isn’t associated with an order with that
account, this method won’t work.

DashboardAPI
In the Dashboard, you can register readers by the order number in one of two
ways:

- From the order itself
- Entering the order number during the registration flow

#### From the order

- On the [Hardware
orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an
order with a status of either `shipped` or `delivered`. Click the overflow menu
() at the end of the row, then click **Register**.
- On the Register Readers page, select one or more readers from the hardware
order to register, then click **Register**.
- Optionally, choose a name for the reader. If you selected multiple readers,
the name serves as a prefix and we name the readers sequentially (for example,
for a given input of “Test reader”, we name the readers “Test reader 1”, “Test
reader 2”, and so on).
- If you already created a location, select the reader’s new Location.
Otherwise, create a Location by clicking **+ Add new**.
- Click **Register** to finish registering your readers.

#### Registration flow

- On the [Terminal Readers](https://dashboard.stripe.com/terminal/readers) page,
click **Register reader**.
- Enter the order number and click **Next**. If there are registerable readers
in the order, continue by clicking **Register**.
- On the **Register Readers** page, select one or more readers from the hardware
order to register, then click **Register**.
- Optionally, choose a name for the reader. If you selected multiple readers,
the name serves as a prefix and we name the readers sequentially (for example,
for a given input of “Test reader,” we name the readers “Test reader 1,” “Test
reader 2,” and so on).
- If you already created a location, select the reader’s new location.
Otherwise, create a location by clicking **+ Add new**.
- Click **Register** to finish registering your readers.

## Mobile readers

iOSAndroidReact Native
Register mobile readers ([Stripe Reader
M2](https://docs.stripe.com/terminal/readers/stripe-m2), [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=bluetooth#connect-reader),
and [BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=bluetooth#connect-reader))
to a location while connecting to the reader by specifying the `locationId` in
your `BluetoothConnectionConfiguration`. If you prefer, you can register the
reader to the last used location by passing in the `reader.locationId` from a
discovered reader.

```
// Call `connectReader` with the selected reader and a connection config
// to register to a location as set by your app.
let connectionConfig: BluetoothConnectionConfiguration
do {
connectionConfig = try BluetoothConnectionConfigurationBuilder(delegate:
yourMobileReaderDelegate, locationId: "{{LOCATION_ID}}")
 .build()
} catch {
 // Handle the error building the connection configuration
 return
}
Terminal.shared.connectReader(selectedReader, connectionConfig:
connectionConfig) { reader, error in
 if let reader = reader {
 print("Successfully connected to reader: \(reader)")
 } else if let error = error {
 print("connectReader failed: \(error)")
 }
}
```

## Links

- [smart reader](https://docs.stripe.com/terminal/smart-readers)
- [mobile reader](https://docs.stripe.com/terminal/mobile-readers)
- [user role](https://docs.stripe.com/get-started/account/teams/roles)
- [admin
settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700#settings)
- [Terminal Readers](https://dashboard.stripe.com/terminal/readers)
- [Hardware Orders](https://dashboard.stripe.com/terminal/hardware_orders)
- [Hardware Order Devices
API](https://docs.stripe.com/api/terminal/hardware_order_devices)
- [Reader API](https://docs.stripe.com/api/terminal/readers)
- [Stripe Reader M2](https://docs.stripe.com/terminal/readers/stripe-m2)
- [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=bluetooth#connect-reader)