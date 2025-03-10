# Supported appearance options

## Review the appearance options available for Embedded Components.

The [embedded components Figma UI
toolkit](https://www.figma.com/community/file/1438614134095442934) contains
every component, common patterns, and an example application. You can use it to
visualize and design embedded UIs in your website.

The `variables` object includes the following optional properties, which apply
to all Connect embedded components in your application. You can test the
variables on [the customization
page](https://docs.stripe.com/connect/customize-connect-embedded-components).

## Commonly used variables

NameTypeExample Value`fontFamily`string`sans-serif`The [font
family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) value used
throughout embedded components. If an embedded component inherits a
`font-family` value from an element on your site in which it’s placed, this
setting overrides that inheritance.`fontSizeBase`string`16px`The baseline font
size set on the embedded component root. This scales the value of other font
size variables. This supports pixel values only.`spacingUnit`string`8px`The base
spacing unit that derives all spacing values. Increase or decrease this value to
make your layout more or less spacious. This supports pixel values
only.`borderRadius`string`15px`The general border radius used in embedded
components. This sets the default border radius for all components. This
supports pixel values only.`colorPrimary`string`#0074D4`The primary color used
throughout embedded components. Set this to your primary brand color. This
accepts hex values or RGB/HSL strings.`colorBackground`string`#FFFFFF`The
background color for embedded components, including overlays, tooltips, and
popovers. This accepts hex values or RGB/HSL
strings.`colorText`string`#444444`The color used for regular text. This accepts
hex values or RGB/HSL strings.`colorDanger`string`#DF1B41`The color used to
indicate errors or destructive actions. This accepts hex values or RGB/HSL
strings.
## Less commonly used variables

NameTypeExample Value`buttonPrimaryColorBackground`string`#0074D4`The color used
as a background for primary buttons. This accepts hex values or RGB/HSL
strings.`buttonPrimaryColorBorder`string`#0074D4`The border color used for
primary buttons. This accepts hex values or RGB/HSL
strings.`buttonPrimaryColorText`string`#FFFFFF`The text color used for primary
buttons. This accepts hex values or RGB/HSL
strings.`buttonSecondaryColorBackground`string`#EBEEF1`The color used as a
background for secondary buttons. This accepts hex values or RGB/HSL
strings.`buttonSecondaryColorBorder`string`#EBEEF1`The color used as a border
for secondary buttons. This accepts hex values or RGB/HSL
strings.`buttonSecondaryColorText`string`#393B3E`The text color used for
secondary buttons. This accepts hex values or RGB/HSL
strings.`colorSecondaryText`string`#717171`The color used for secondary text.
This accepts hex values or RGB/RGBA/HSL
strings.`actionPrimaryColorText`string`#0074D4`The color used for primary
actions and links. This accepts hex values or RGB/HSL
strings.`actionPrimaryTextDecorationLine`string`underline`The line type used for
text decoration of primary actions and links. This accepts a valid [text
decoration
line](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-line)
value.`actionPrimaryTextDecorationColor`string`#0074D4`The color used for text
decoration of primary actions and links. This accepts hex values or RGB/HSL
strings.`actionPrimaryTextDecorationStyle`string`solid`The style of text
decoration of primary actions and links. This accepts a valid [text decoration
style](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-style)
value.`actionPrimaryTextDecorationThickness`string`1px`The thickness of text
decoration of primary actions and links. This accepts a valid [text decoration
thickness](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-thickness)
value.`actionSecondaryColorText`string`#444444`The color used for secondary
actions and links. This accepts hex values or RGB/HSL
strings.`actionSecondaryTextDecorationLine`string`underline`The line type used
for text decoration of secondary actions and links. This accepts a valid [text
decoration
line](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-line)
value.`actionSecondaryTextDecorationColor`string`#0074D4`The color used for text
decoration of secondary actions and links. This accepts hex values or RGB/HSL
strings.`actionSecondaryTextDecorationStyle`string`solid`The style of text
decoration of secondary actions and links. This accepts a valid [text decoration
style](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-style)
value.`actionSecondaryTextDecorationThickness`string`1px`The thickness of text
decoration of secondary actions and links. This accepts a valid [text decoration
thickness](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-thickness)
value.`badgeNeutralColorBackground`string`#E4ECEC`The background color used to
represent neutral state or lack of state in status badges. This accepts hex
values or RGB/HSL strings.`badgeNeutralColorText`string`#545969`The text color
used to represent neutral state or lack of state in status badges. This accepts
hex values or RGB/HSL strings.`badgeNeutralColorBorder`string`#CBD5D6`The border
color used to represent neutral state or lack of state in status badges. This
accepts hex values or RGB/RGBA/HSL
strings.`badgeSuccessColorBackground`string`#CEF6BB`The background color used to
reinforce a successful outcome in status badges. This accepts hex values or
RGB/HSL strings.`badgeSuccessColorText`string`#05690D`The text color used to
reinforce a successful outcome in status badges. This accepts hex values or
RGB/HSL strings.`badgeSuccessColorBorder`string`#B4E1A2`The border color used to
reinforce a successful outcome in status badges. This accepts hex values or
RGB/RGBA/HSL strings.`badgeWarningColorBackground`string`#FCEEBA`The background
color used in status badges to highlight things that might require action, but
are optional to resolve. This accepts hex values or RGB/HSL
strings.`badgeWarningColorText`string`#A82C00`The text color used in status
badges to highlight things that might require action, but are optional to
resolve. This accepts hex values or RGB/HSL
strings.`badgeWarningColorBorder`string`#F5DA80`The border color used in status
badges to highlight things that might require action, but are optional to
resolve. This accepts hex values or RGB/RGBA/HSL
strings.`badgeDangerColorBackground`string`#F9E4F1`The background color used in
status badges for high-priority, critical situations that the user must address
immediately, and to indicate failed or unsuccessful outcomes. This accepts hex
values or RGB/HSL strings.`badgeDangerColorText`string`#B3063D`The text color
used in status badges for high-priority, critical situations that the user must
address immediately, and to indicate failed or unsuccessful outcomes. This
accepts hex values or RGB/HSL strings.`badgeDangerColorBorder`string`#F2C9E3`The
border color used in status badges for high-priority, critical situations that
the user must address immediately, and to indicate failed or unsuccessful
outcomes. This accepts hex values or RGB/RGBA/HSL
strings.`offsetBackgroundColor`string`#FFFFFF`The background color used when
highlighting information, like the selected row on a table or particular piece
of UI. This accepts hex values or RGB/HSL
strings.`formBackgroundColor`string`#FFFFFF`The background color used for form
items. This accepts hex values or RGB/HSL
strings.`colorBorder`string`#D7D7D7`The color used for borders throughout the
component. This accepts hex values or RGB/RGBA/HSL
strings.`formHighlightColorBorder`string`#D7D7D7`The color used to highlight
form items when focused. This accepts hex values or RGB/RGBA/HSL
strings.`formAccentColor`string`#0074D4`The color used for to fill in form items
like checkboxes, radio buttons and switches. This accepts hex values or RGB/HSL
strings.`buttonBorderRadius`string`4px`The border radius used for buttons. This
supports pixel values only.`formBorderRadius`string`6px`The border radius used
for form elements. This supports pixel values
only.`badgeBorderRadius`string`4px`The border radius used for badges. This
supports pixel values only.`overlayBorderRadius`string`8px`The border radius
used for overlays. This supports pixel values only.`overlayZIndex`number`1000`A
[z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index) to use for
the overlay throughout embedded components. Set this number to control the
z-order of the overlay.`overlayBackdropColor`string`#F9E4F1`The backdrop color
when an overlay is opened. This accepts hex values or RGB/RGBA/HSL
strings.`bodyMdFontSize`string`16px`The font size for the medium body
typography. Body typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`bodyMdFontWeight`string`400`The font weight for the medium body
typography. Body typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`bodySmFontSize`string`14px`The font size for the small body typography.
Body typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`bodySmFontWeight`string`400`The font weight for the small body
typography. Body typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`headingXlFontSize`string`28px`The font size for the extra large heading
typography. Heading typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`headingXlFontWeight`string`700`The font weight for the extra large
heading typography. Heading typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`headingXlTextTransform`string`uppercase`The text transform for the extra
large heading typography. Heading typography variables accept a valid [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
value.`headingLgFontSize`string`24px`The font size for the large heading
typography. Heading typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`headingLgFontWeight`string`700`The font weight for the large heading
typography. Heading typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`headingLgTextTransform`string`uppercase`The text transform for the large
heading typography. Heading typography variables accept a valid [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
value.`headingMdFontSize`string`20px`The font size for the medium heading
typography. Heading typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`headingMdFontWeight`string`700`The font weight for the medium heading
typography. Heading typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`headingMdTextTransform`string`uppercase`The text transform for the medium
heading typography. Heading typography variables accept a valid [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
value.`headingSmFontSize`string`16px`The font size for the small heading
typography. Heading typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`headingSmFontWeight`string`700`The font weight for the small heading
typography. Heading typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`headingSmTextTransform`string`uppercase`The text transform for the small
heading typography. Heading typography variables accept a valid [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
value.`headingXsFontSize`string`12px`The font size for the extra small heading
typography. Heading typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`headingXsFontWeight`string`700`The font weight for the extra small
heading typography. Heading typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`headingXsTextTransform`string`uppercase`The text transform for the extra
small heading typography. Heading typography variables accept a valid [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
value.`labelMdFontSize`string`14px`The font size for the medium label
typography. Label typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`labelMdFontWeight`string`400`The font weight for the medium label
typography. Label typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`labelMdTextTransform`string`uppercase`The text transform for the medium
label typography. Label typography variables accept a valid [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
value.`labelSmFontSize`string`12px`The font size for the small label typography.
Label typography variables accept a valid [font
size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
value.`labelSmFontWeight`string`400`The font weight for the small label
typography. Label typography variables accept a valid [font
weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
value.`labelSmTextTransform`string`uppercase`The text transform for the small
label typography. Label typography variables accept a valid [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
value.

## Links

- [embedded components Figma UI
toolkit](https://www.figma.com/community/file/1438614134095442934)
- [the customization
page](https://docs.stripe.com/connect/customize-connect-embedded-components)
- [font family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)
- [text decoration
line](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-line)
- [text decoration
style](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-style)
- [text decoration
thickness](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-thickness)
- [z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index)
- [font size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
- [font weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
- [text
transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)