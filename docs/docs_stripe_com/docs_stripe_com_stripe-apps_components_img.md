# Img component for Stripe Apps

## Display images with the Img UI component.

SDK version8.x9.x
To add an image to your app:

- Import the `Img` component:

```
import {Img} from '@stripe/ui-extension-sdk/ui';
```

- Include the base URLs of any images you include in the `image-src` section of
the `content_security_policy` in your [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest).

The following shows a preview of an image with the respective `Img` tag below:

```
<Img
 src="https://images.example.com/gross-volume.svg"
 width="484"
 height="207"
 alt="Gross volume"
/>
```

### Img props

PropertyType
`alt`

Optional
`string | undefined`

The alternative text of the image.

`crossOrigin`

Optional
`"anonymous" | undefined`

Cross-origin support for the image.

`height`

Optional
`(string | number) | undefined`

The height of the image.

`sizes`

Optional
`string | undefined`

The sizes of the image (for use with srcSet).

`src`

Optional
`string | undefined`

The source of the image.

`srcSet`

Optional
`string | undefined`

The source set of the image.

`width`

Optional
`(string | number) | undefined`

The width of the image.

## SrcSet

You can use `srcSet` for [responsive
images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images).

The example below uses the `size` attribute to define the maximum width of the
specified image:

```
<Img
srcSet="https://images.example.com/daily-sales.jpg 480w,
https://images.example.com/daily-sales-large.jpg 800w"
 sizes="(max-width: 600px) 480px, 800px"
 width="484"
 height="207"
 alt="Daily sales"
/>
```

## Data URLs

You can co-locate images with your UI extension code and load them directly into
the `Img` component. Supported formats are GIF, JPEG, SVG, PNG, and WEBP.

We recommend using SVG for most common use-cases like icons and other way
finding illustrations. You must include the suffix of the image in the `require`
or `import` statement.

```
import {Img} from '@stripe/ui-extension-sdk/ui';
import CommunityIcon from './community-icon.svg';

const DataURl = () => (
 <Img width="75" height="75" src={CommunityIcon} alt="Community" />
)
```

## Styling

You can achieve certain styling effects for `Img` components by wrapping them
with a styled [Box](https://docs.stripe.com/stripe-apps/components/box)
component.

### Borders

To add a [border](https://docs.stripe.com/stripe-apps/style#borders) to an
`Img`, use the CSS `keyline` property, along with `width` and `display` to
contain the image:

```
<Box
 css={{
 keyline: 'critical',
 width: 'fit',
 stack: 'x',
 }}
>
 <Img
 src="https://images.example.com/gross-margin.svg"
 width="484"
 height="207"
 alt="Gross margin"
 />
</Box>
```

### Rounded corners

To add rounded corners to an `Img`, use the CSS `borderRadius` property, along
with `overflow`, `width`, and `display` to contain the image:

```
<Box
 css={{
 borderRadius: 'rounded',
 overflow: 'hidden',
 width: 'fit',
 stack: 'x',
 }}
>
 <Img
 src="https://images.example.com/gross-margin.svg"
 width="484"
 height="207"
 alt="Gross margin"
 />
</Box>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
-
[https://images.example.com/gross-volume.svg](https://images.example.com/gross-volume.svg)
- [responsive
images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
-
[https://images.example.com/daily-sales.jpg](https://images.example.com/daily-sales.jpg)
-
[https://images.example.com/daily-sales-large.jpg](https://images.example.com/daily-sales-large.jpg)
- [Box](https://docs.stripe.com/stripe-apps/components/box)
- [border](https://docs.stripe.com/stripe-apps/style#borders)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)