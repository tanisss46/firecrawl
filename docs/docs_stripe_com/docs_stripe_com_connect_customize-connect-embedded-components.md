# Customize Connect embedded components

[View the text-based
guide](https://docs.stripe.com/connect/get-started-connect-embedded-components#customize-the-look-of-connect-embedded-components)
The [embedded components Figma UI
toolkit](https://www.figma.com/community/file/1438614134095442934) contains
every component, common patterns, and an example application. You can use it to
visualize and design embedded UIs in your website.

To customize the appearance of Connect embedded components, use the `appearance`
options when you initialize `StripeConnectInstance`. Connect embedded components
already inherit the font-family of their parent HTML element, but you can also
make them match with the rest of your site by modifying colors, fonts, borders,
padding, and so on.

#### Note

These options are the only way to change styles in Connect embedded components.
You can’t override their styles with CSS selectors or other mechanisms. You also
can’t eliminate an embedded component’s use of popups in some flows, such as
user authentication.

PreviewPaymentsSizeDesktopLocale (United States)[Learn more about the
Payments component
→](https://docs.stripe.com/connect/supported-embedded-components/payments)This
demo is read-only with limited functionality. Visit
[furever.dev](https://furever.dev/) for a fully functional demo.
```
import {loadConnect} from '@stripe/connect-js';

const stripeConnect = await loadConnect();
const stripeConnectInstance = stripeConnect.initialize({
 publishableKey: "PUBLISHABLE_KEY",
 clientSecret: 'CLIENT_SECRET',
})
```

## Links

- [text version of this
guide](https://docs.stripe.com/connect/get-started-connect-embedded-components#customize-the-look-of-connect-embedded-components)
- [embedded components Figma UI
toolkit](https://www.figma.com/community/file/1438614134095442934)
- [Learn more about the Payments component
→](https://docs.stripe.com/connect/supported-embedded-components/payments)
- [furever.dev](https://furever.dev)