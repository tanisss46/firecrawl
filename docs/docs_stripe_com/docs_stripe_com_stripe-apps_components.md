# UI components

## Use Stripe’s library of components to quickly build your user interface.

If your app needs a frontend, use this reference documentation to compose a UI.
Stripe’s library of prebuilt components has customizable properties to help you
quickly build apps aligned to Stripe best practices. Use components to structure
layouts and create graphical or interactive experiences in your apps.

All components are available in Figma at
[@stripedesign](https://www.figma.com/community/file/1105918844720321397) on
Figma Community.

## Views

Every [view you add](https://docs.stripe.com/stripe-apps/build-ui) needs a view
component. These determine which view of your app the user sees at different
moments, similar to different HTML pages of a website.

The most common view is `ContextView`. When a user begins a workflow or task in
your app, their view should switch to `FocusView` to hide the background
details. To design your app settings page, use `SettingsView`. To design a sign
in screen, use `SignInView`.

Some views are root components. `ContextView`, `SettingsView`, and `SignInView`
are view roots—the foundational components that contain all other UI
elements—whereas `FocusView` is a child component of `ContextView`.

Component
Description[ContextView](https://docs.stripe.com/stripe-apps/components/contextview)ContextView
allows apps to render next to Stripe content in a drawer so users can look at
them side by side and share
context.[SettingsView](https://docs.stripe.com/stripe-apps/components/settingsview)Use
SettingsView to let users to change details about how the app works with their
account.[SignInView](https://docs.stripe.com/stripe-apps/components/signinview)Use
SignInView to display a sign in screen to users.
## Layout

Use layout components to create the structure of your pages and elements.

Component
Description[Box](https://docs.stripe.com/stripe-apps/components/box)Use boxes to
wrap other components and add custom styles and
layouts.[Divider](https://docs.stripe.com/stripe-apps/components/divider)Render
a simple horizontal rule with the divider component.
## 

Use navigation components to help users wayfind and interact with your app.

Component
Description[Button](https://docs.stripe.com/stripe-apps/components/button)Buttons
allow users to take actions in Stripe products, and you can use them to direct
users’ attention or warn them of
outcomes.[ButtonGroup](https://docs.stripe.com/stripe-apps/components/buttongroup)Use
ButtonGroup to handle the layout for multiple buttons and collapse them into an
overflow menu when space is
limited.[Link](https://docs.stripe.com/stripe-apps/components/link)Links are
used for navigating users from one page to another, and for actions that need
more subtlety than a button
provides.[Menu](https://docs.stripe.com/stripe-apps/components/menu)A menu
presents a group of actions that a user can choose from, often related to a
particular object or
context.[Tabs](https://docs.stripe.com/stripe-apps/components/tabs)Use tabs to
display sections of content.
## Content

Use content components to organize and place information within your app.

Component
Description[Accordion](https://docs.stripe.com/stripe-apps/components/accordion)Use
accordions to split long or complex content into collapsible
chunks.[Badge](https://docs.stripe.com/stripe-apps/components/badge)Use badges
to indicate states that an item or object might move through or change
to.[Banner](https://docs.stripe.com/stripe-apps/components/banner)Use the Banner
to show a variety of alerts or messages you want to make explicit to the
user.[Chip](https://docs.stripe.com/stripe-apps/components/chip)Use chips to
display and allow users to manipulate
values.[FocusView](https://docs.stripe.com/stripe-apps/components/focusview)Use
FocusView to open a dedicated space for the end user to complete a specific
task.[Icon](https://docs.stripe.com/stripe-apps/components/icon)Display an icon
graphic in a compatible
format.[Img](https://docs.stripe.com/stripe-apps/components/img)Display images
with the Img UI
component.[Inline](https://docs.stripe.com/stripe-apps/components/inline)Use the
inline component to style inline content such as
text.[List](https://docs.stripe.com/stripe-apps/components/list)Display a list
of information in a variety of preconfigured
formats.[Spinner](https://docs.stripe.com/stripe-apps/components/spinner)Use the
Spinner component to indicate something is
loading.[Table](https://docs.stripe.com/stripe-apps/components/table)Display
rows and columns of
data.[Toast](https://docs.stripe.com/stripe-apps/components/toast)Inform users
of temporary
status.[Tooltip](https://docs.stripe.com/stripe-apps/components/tooltip)Use
Tooltips to provide additional contextual information about a particular element
or subject.
## Forms

Use form components to compose input fields and controls that require user
input. For example, use them to create checklists or to enable users to select
settings.

Component
Description[Checkbox](https://docs.stripe.com/stripe-apps/components/checkbox)Use
checkboxes to indicate or control boolean
values.[DateField](https://docs.stripe.com/stripe-apps/components/datefield)Use
DateField to create a date input
field.[FormFieldGroup](https://docs.stripe.com/stripe-apps/components/formfieldgroup)Group
form fields with the FormFieldGroup
component.[Radio](https://docs.stripe.com/stripe-apps/components/radio)Use
Radios to make a selection from a mutually exclusive set of
options.[Select](https://docs.stripe.com/stripe-apps/components/select)Use
Select to pick from a set of options in a
dropdown.[Switch](https://docs.stripe.com/stripe-apps/components/switch)Similar
to Checkboxes, you can use Switches to indicate or control boolean
values.[TextArea](https://docs.stripe.com/stripe-apps/components/textarea)Use
TextArea to create an input field for multiple lines of
text.[TextField](https://docs.stripe.com/stripe-apps/components/textfield)Use
TextField to create a text input field.
## Charts

Use chart components to map data points visually. For example, use a chart in
your app to help users track payments data or compare progress over time.

Component
Description[BarChart](https://docs.stripe.com/stripe-apps/components/barchart)A
bar chart visualizes data as a series of data points using
bars.[LineChart](https://docs.stripe.com/stripe-apps/components/linechart)A line
chart visualizes data as a series of data points connected into a
line.[Sparkline](https://docs.stripe.com/stripe-apps/components/sparkline)A type
of line chart to display data succinctly as a simple line.
## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [@stripedesign](https://www.figma.com/community/file/1105918844720321397)
- [view you add](https://docs.stripe.com/stripe-apps/build-ui)
- [ContextView](https://docs.stripe.com/stripe-apps/components/contextview)
- [SettingsView](https://docs.stripe.com/stripe-apps/components/settingsview)
- [SignInView](https://docs.stripe.com/stripe-apps/components/signinview)
- [Box](https://docs.stripe.com/stripe-apps/components/box)
- [Divider](https://docs.stripe.com/stripe-apps/components/divider)
- [Button](https://docs.stripe.com/stripe-apps/components/button)
- [ButtonGroup](https://docs.stripe.com/stripe-apps/components/buttongroup)
- [Link](https://docs.stripe.com/stripe-apps/components/link)
- [Menu](https://docs.stripe.com/stripe-apps/components/menu)
- [Tabs](https://docs.stripe.com/stripe-apps/components/tabs)
- [Accordion](https://docs.stripe.com/stripe-apps/components/accordion)
- [Badge](https://docs.stripe.com/stripe-apps/components/badge)
- [Banner](https://docs.stripe.com/stripe-apps/components/banner)
- [Chip](https://docs.stripe.com/stripe-apps/components/chip)
- [FocusView](https://docs.stripe.com/stripe-apps/components/focusview)
- [Icon](https://docs.stripe.com/stripe-apps/components/icon)
- [Img](https://docs.stripe.com/stripe-apps/components/img)
- [Inline](https://docs.stripe.com/stripe-apps/components/inline)
- [List](https://docs.stripe.com/stripe-apps/components/list)
- [Spinner](https://docs.stripe.com/stripe-apps/components/spinner)
- [Table](https://docs.stripe.com/stripe-apps/components/table)
- [Toast](https://docs.stripe.com/stripe-apps/components/toast)
- [Tooltip](https://docs.stripe.com/stripe-apps/components/tooltip)
- [Checkbox](https://docs.stripe.com/stripe-apps/components/checkbox)
- [DateField](https://docs.stripe.com/stripe-apps/components/datefield)
-
[FormFieldGroup](https://docs.stripe.com/stripe-apps/components/formfieldgroup)
- [Radio](https://docs.stripe.com/stripe-apps/components/radio)
- [Select](https://docs.stripe.com/stripe-apps/components/select)
- [Switch](https://docs.stripe.com/stripe-apps/components/switch)
- [TextArea](https://docs.stripe.com/stripe-apps/components/textarea)
- [TextField](https://docs.stripe.com/stripe-apps/components/textfield)
- [BarChart](https://docs.stripe.com/stripe-apps/components/barchart)
- [LineChart](https://docs.stripe.com/stripe-apps/components/linechart)
- [Sparkline](https://docs.stripe.com/stripe-apps/components/sparkline)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)