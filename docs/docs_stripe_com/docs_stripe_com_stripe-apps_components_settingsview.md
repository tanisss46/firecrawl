# SettingsView component for Stripe Apps

## Let users change details about how the app works with their account.

SDK version8.x9.x
You can define a specialized settings view to let users change specific details
about how the app works with their account. For example, an app that uses a
third-party API like Zendesk could use `SettingsView` to authorize a user with
their Zendesk account. For more details, learn how to [add a settings
page](https://docs.stripe.com/stripe-apps/app-settings) for your app.

!

What SettingsView looks like

`SettingsView` is a view root component, just like `ContextView`, containing all
other UI elements. It’s the only view that isn’t tied to a specific object, but
tied instead to the `settings` viewport. The `settings` viewport maps to
predefined locations in the Dashboard, outside of the app drawer.

`SettingsView` renders on the app settings page in the Dashboard after you
upload an app. While previewing your app locally, you can preview the
`SettingsView` in the Dashboard at
[https://dashboard.stripe.com/apps/settings-preview](https://dashboard.stripe.com/apps/settings-preview).

To use `SettingsView`, you must add a view with the `settings` viewport to your
app manifest. An application with a settings view would have an app manifest
with a `ui_extension` field that would look something like this:

```
{
 ...,
 "ui_extension": {
 "views": [
 ...,
 {
 "viewport": "settings",
 "component": "AppSettings"
 }
 ],
 }
}
```

### SettingsView props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`onSave`

Optional
`((values: { [x: string]: string; }) => void) | undefined`

If provided, a “Save” `Button` will be rendered with the `SettingsView`. This
callback will be called when the `Button` is clicked.

`statusMessage`

Optional
`string | undefined`

A string to display a status such as “Saved” or “Error” in the header of the
view.

## Example

This example shows how to fetch settings from an external API, display them, and
save changes.

```
import React from 'react';
import {ExtensionContextValue} from '@stripe/ui-extension-sdk/context';
import {Box, SettingsView, TextField} from '@stripe/ui-extension-sdk/ui';

type FormStatus = 'initial' | 'saving' | 'saved' | 'error';

const AppSettings = ({userContext}: ExtensionContextValue) => {
 const [storedValue, setStoredValue] = React.useState<string>('');
 const [status, setStatus] = React.useState<FormStatus>('initial');

 // use the current user id to retrieve the stored value from an external api
 const key = userContext.id;

 React.useEffect(() => {
 if (!key) {
 return;
 }

 const fetchSetting = async (key: string) => {
 try {
 const response = await fetch(`https://www.my-api.com/${key}`);
 const storedSettingValue = await response.text();
 if (storedSettingValue) {
 setStoredValue(storedSettingValue);
 }
 } catch (error) {
 console.log('Error fetching setting: ', error);
 }
 };
 fetchSetting(key);
 }, [key]);

 const saveSettings = React.useCallback(async (values) => {
 setStatus('saving');
 try {
 const {greeting} = values;
 const result = await fetch('https://www.my-api.com/', {
 method: 'POST',
 body: JSON.stringify(values),
 });
 await result.text();
 setStatus('saved');
 setStoredValue(greeting);
 } catch (error) {
 console.error(error);
 setStatus('error');
 }
 }, []);

 const getStatusLabel = React.useCallback(() => {
 switch (status) {
 case 'saving':
 return 'Saving...';
 case 'saved':
 return 'Saved!';
 case 'error':
 return 'Error: There was an error saving your settings.';
 case 'initial':
 default:
 return '';
 }
 }, [status]);
 const statusLabel = getStatusLabel();

 return (
 <SettingsView onSave={saveSettings} statusMessage={statusLabel}>
 <Box
 css={{
 padding: 'medium',
 backgroundColor: 'container',
 }}
 >
 <Box
 css={{
 font: 'lead',
 }}
 >
 Please enter a greeting
 </Box>
 <Box
 css={{
 marginBottom: 'medium',
 font: 'caption',
 }}
 >
 Saved value: {storedValue || 'None'}
 </Box>
 <TextField
 name="greeting"
 type="text"
 label="Greeting:"
 size="medium"
 />
 </Box>
 </SettingsView>
 );
};
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [add a settings page](https://docs.stripe.com/stripe-apps/app-settings)
-
[https://dashboard.stripe.com/apps/settings-preview](https://dashboard.stripe.com/apps/settings-preview)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)