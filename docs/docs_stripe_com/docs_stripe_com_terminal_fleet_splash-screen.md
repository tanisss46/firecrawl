# Configure readers with a custom splash screen

## Customize the default splash screen for your readers.

A splash screen is the default screen that displays when your reader is ready to
accept payments. You can set a custom splash screen for these readers in one of
two ways:

- In the Dashboard
- Using the Configuration API

You can configure an account default splash screen, which applies to all readers
in your fleet. You can also configure a custom splash screen for individual
locations, which overrides the splash screen configured at the account level.
Locations without a custom splash screen inherit the account default splash
screen.

DashboardAPI
To update the splash screen, navigate to the relevant configuration you want to
change and edit it. If adding a new configuration, create a new one first.

- Navigate to the [Manage
locations](https://dashboard.stripe.com/terminal/locations) page.
- Find the specific location you want to change.
- Click the overflow menu () > **Edit configuration**.
- Click **Edit** or **Override** next to the **Splash screen** icon.
- Select the reader type (for example, S700, BBPOS WisePOS E) to indicate which
reader type to apply the splash screen to.- You can’t upload or apply a single
splash screen across every reader type.
- Upload an image to display on your readers. JPG and PNG images must be less
than 2MB. GIF images must be less than 4 MB. Each reader has a specific display
resolution and you must crop your JPG or PNG image to fit those dimensions. GIF
images scale automatically.
- Click **Done**.
- Apply the configuration changes by clicking **Apply changes** on the
configuration drawer.

#### Note

Only Stripe S700 and BBPOS WisePOS E readers can use GIF images for the splash
screen.

#### Caution

GIF files under 4 MB might still fail to upload. If this occurs, reduce the file
size further by manually deleting frames. Try reducing the GIF’s frame count by
50% until the upload succeeds.

ReaderResolution (W x H)Stripe S7001080 x 1920BBPOS WisePOS E720 x 1280Verifone
P400320 x 480
After uploading, save the changes and apply the configuration. The splash screen
updates on the reader within 10 minutes.

## Links

- [Manage locations](https://dashboard.stripe.com/terminal/locations)