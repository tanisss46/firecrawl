# Toast component for Stripe AppsDashboard only

## Inform users of temporary status.

SDK version8.x9.x
To add the Toast component to your app:

```
import { showToast } from "@stripe/ui-extension-sdk/utils";
```

```
const App = () => {
 React.useEffect(() => {
 showToast('Changes saved', {type: 'success'});
 }, []);
};
```

Render a toast at the bottom of your view to inform the user about the status of
an action. For example, a toast can show a user whether an API call succeeded or
failed.

```
import {showToast} from '@stripe/ui-extension-sdk/utils';

const App = () => {
 const handleClick = () => {
 fetch(...)
 .then((response) => {
 showToast("Invoice updated", {type: "success"})
 return response.json()
 })
 .catch(() => {
 showToast("Invoice could not be updated", {type: "caution"})
 })
 }

 // Use the `handleClick`...
}
```

The `showToast()` function takes two arguments, a `message` and `options`. The
function is defined as follows:

```
type ToastType = "success" | "caution" | "pending" | undefined;
type ToastOptions = { type?: ToastType; action?: string; onAction: () => void; }
(message: string, options?: ToastOptions) => Promise<{
 update: (updateMessage: string, updateOptions?: ToastOptions) => void;
 dismiss: () => void;
}>;
```

Toast messages can’t exceed 30 characters in length or be empty. If a message is
too long or empty, the console logs an error.

Unless they’re of type `pending`, toasts dismiss automatically.

Is PendingHas
ActionTimeout`false``false`4s`false``true`6s`true``false`None`true``true`None
```
import {showToast} from '@stripe/ui-extension-sdk/utils';

const App = () => {
 const handleClick = async () => {
 const { dismiss, update } = await showToast("Refreshing data", {
 type: "pending",
 });
 try {
 await refreshData();
 dismiss();
 } catch (error) {
 update("Data could not be refreshed", { type: "caution" });
 }
 }

 // Use the `handleClick`...
}
```

Toasts can also prompt the user to take an action. Clicking the action button
automatically dismisses the toast.

```
import {showToast} from '@stripe/ui-extension-sdk/utils';

const App = () => {
 const handleClick = async () => {
 let timeout;
 const { dismiss } = await showToast('Message "sent"', {
 action: "Undo",
 onAction: () => {
 clearTimeout(timeout);
 showToast('Message "unsent"');
 },
 });
 timeout = setTimeout(() => {
 sendMessage();
 dismiss();
 }, 3000);
 }

 // Use the `handleClick`...
}
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)