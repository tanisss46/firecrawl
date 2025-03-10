# Configure the WiFi networkPublic preview

## Remotely configure a WiFi network for your readers.

#### Public preview

This preview feature is available for [BBPOS WisePOS
E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e) and [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700) readers.

You can remotely configure and manage WiFi networks for our sPOS readers. We
support the following network security types:

- WPA/WPA2 Personal (PSK)
- WPA/WPA2 Enterprise (EAP-PEAP)
- WPA/WPA2 Enterprise (EAP-TLS)

To fetch the remotely configured network from the server, the reader must first
connect to a local WiFi network.

After you set the WiFi configuration, it displays as a `Configured network` on
the reader. You can then select this network to connect automatically, without
requiring the end user to enter any additional information.

If you update the WiFi profile, Stripe sends these updates to the reader, which
stays connected to the network as long as the credentials are accurate.

#### Caution

Stripe doesn’t perform validation checks when you configure the WiFi profile. If
you enter an incorrect password, expired EAP-TLS certificate, or other invalid
credentials, the reader won’t connect to the network.

DashboardAPI
To configure WiFi settings in the Dashboard:

- Navigate to the [Manage
locations](https://dashboard.stripe.com/terminal/locations/) page.
- Find the specific location you want to change.
- Click the overflow menu () > **Edit configuration**.
- Click **Edit** or **Override** next to the **WiFi** icon.
- Use the **Security** dropdown to select a security type.
- Enter the relevant credentials.
- Click **Done**.
- Click **Apply changes**.

After registering to the location, readers display a prompt to connect to the
configured network. For readers that are already registered, the WiFi network
might take up to 10 minutes to appear under `Configured networks` in the
reader’s network settings screen.

## Links

- [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e)
- [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [Manage locations](https://dashboard.stripe.com/terminal/locations/)