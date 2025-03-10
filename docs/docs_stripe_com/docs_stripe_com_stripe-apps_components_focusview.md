# FocusView component for Stripe AppsDashboard only

## Use FocusView to open a dedicated space for the end user to complete a specific task.

SDK version8.x9.x
A `FocusView` component can be opened from other `View` components and allows
the developer to open a dedicated space for the end user to complete a specific
task. Examples include:

- Enter details to create a new entry in a database
- Go through a wizard to decide on next steps
- Confirm that the user wants to take the action they indicated

!

What FocusView looks like

`FocusView` must be a child of `ContextView`. Don’t wrap the `FocusView` in a
conditional, instead use the `shown` property to control its visible state. For
more information, see
[ContextView](https://docs.stripe.com/stripe-apps/components/contextview).

To add the `FocusView` component to your app:

```
import {FocusView} from '@stripe/ui-extension-sdk/ui';
```

### FocusView props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`title`

Required
`string`

The title of the `FocusView`. This will be displayed at the top of the drawer
under your app’s name.

`confirmCloseMessages`

Optional
`ConfirmCloseMessages | undefined`

If provided, confirmCloseMessages will be displayed when the user closes the
`FocusView`.

Related types:
[ConfirmCloseMessages](https://docs.stripe.com/stripe-apps/components/focusview#confirmclosemessages).

`footerContent`

Optional
`React.ReactNode`

React node adjacent to any actions in the footer.

`primaryAction`

Optional
`React.ReactElement | undefined`

A primary call to action (“Save” or “Continue”) `Button` placed in the footer.

`secondaryAction`

Optional
`React.ReactElement | undefined`

A secondary call to action (“Cancel”) `Button` placed in the footer.

`setShown`

Optional
`((shown: boolean) => void) | undefined`

Allows the `FocusView` to manage shown state if a user requests to close the
window, or if it needs to stay open because of the close confirmation dialog.

`shown`

Optional
`boolean | undefined`

Whether the `FocusView` should be shown or not. This property is maintained by a
parent view.

`onClose`

OptionalDeprecated
Use `setShown` instead. If the user clicks out of the `FocusView` or presses the
escape button, this informs the extension that the user has closed the view.

`(() => void) | undefined`

### ConfirmCloseMessages

PropertyType
`cancelAction`

Required
`string`

`description`

Required
`string`

`exitAction`

Required
`string`

`title`

Required
`string`

## Close Confirmation Dialog

When passing `confirmCloseMessages`, in order for the close confirmation dialog
to work properly in every close scenario, pass the `setShown` prop so the
`FocusView` can manage its `shown` state. To control when the close confirmation
dialog displays, you can use state to conditionally pass `confirmCloseMessages`
to the `FocusView`, like in the following example:

## Example

```
import React from 'react';
import {
 Box,
 Button,
 ContextView,
 FocusView,
 Select,
} from '@stripe/ui-extension-sdk/ui';

type Mood = 'Happy' | 'Sad';

const confirmCloseMessages = {
 title: 'Your mood will not be saved',
 description: 'Are you sure you want to exit?',
 cancelAction: 'Cancel',
 exitAction: 'Exit',
};

const MoodView = () => {
 const [mood, setMood] = React.useState<Mood>('Happy');
 const [shown, setShown] = React.useState<boolean>(false);
 const [confirmClose, setConfirmClose] = React.useState<boolean>(false);

 const open = () => {
 setConfirmClose(true);
 setShown(true);
 };

 const closeWithoutConfirm = () => {
 setConfirmClose(false);
 setShown(false);
 };

 const closeWithConfirm = () => {
 setShown(false);
 };

 const updateMood = (newMood: Mood) => {
 setMood(newMood);
 closeWithoutConfirm();
 };

 return (
 <ContextView
 title="Mood picker"
 description="This section communicates my extension's feelings"
 >
 <FocusView
 title="Pick your mood"
 shown={shown}
 setShown={setShown}
 confirmCloseMessages={confirmClose ? confirmCloseMessages : undefined}
 secondaryAction={<Button onPress={closeWithConfirm}>Cancel</Button>}
 >
 <Select onChange={(e) => updateMood(e.target.value as Mood)}>
 <option label="">Select mood</option>
 <option label="Happy">Happy</option>
 <option label="Sad">Sad</option>
 </Select>
 </FocusView>
 <Box css={{stack: 'x', gap: 'medium'}}>
 <Box
 css={{
 font: 'subheading',
 color: mood === 'Happy' ? 'success' : 'info',
 }}
 >
 {mood}
 </Box>
 <Button onPress={open}>Change mood</Button>
 </Box>
 </ContextView>
 );
};
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [ContextView](https://docs.stripe.com/stripe-apps/components/contextview)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)