# Build a UI

## Build, test, and edit a custom UI that extends the functionality of the Stripe Dashboard.

Give your app a user interface by using TypeScript, React, and Stripe’s [UI
Extensions
SDK](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api) and [UI
toolkit](https://docs.stripe.com/stripe-apps/design) to extend the Stripe
Dashboard. This guide explains how to build a simple UI by creating and removing
views.

For a more technical overview, [learn how UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work).

## Add a view

Use views to develop your app UI. A view is a pairing of a React component and a
specified viewport. The React component is composed of UI components from our UI
toolkit. The viewport is the page or section of the Stripe Dashboard where you
want to display it.

- Use the `add` command from your project root directory:

```
stripe apps add view
```
- Follow the prompts:

- Select the viewport for your view to appear in. See a list of [available
viewports](https://docs.stripe.com/stripe-apps/reference/viewports).
- Name your view (for example, MyComponentName). The CLI suggests names based on
your viewport selection.

Stripe automatically adds your view to the `views` array in your [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest), creates a
new React component file in the `src/views` directory, and creates a unit test
file alongside it.

## Preview the application

You can run your app locally, make updates, and preview your changes in the
Dashboard.

- From your project root directory, start the development server:

```
stripe apps start
```
- Press **Enter** to open your browser.
- Click **Continue** to preview your app in your Stripe account:
- To stop the development server, type **Ctrl+C** from your command line.

When the development server is running, you can make changes to your app and see
them automatically in the Dashboard without refreshing the page. Until you
resolve them, any errors automatically show up in the Stripe Dashboard, your
browser’s dev tools, and the Stripe CLI.

### Switch previews

You can disable previewing the local version of your app to preview a recently
[installed version of your app in test
mode](https://docs.stripe.com/stripe-apps/upload-install-app). If you’ve never
installed any version of your app in test mode, you can’t switch previews.

To preview the most recently installed version of your app in test mode, run
your development server and follow these steps:

- In your app, click the overflow menu in the top right of your app.
- Click **Turn off app preview**, then **Continue**.

## Access Stripe objects in the Dashboard

When you assign a component to a viewport, the component can receive context
about the Stripe object on that page using the `environment.objectContext`
object.

For example, if you create a view that uses the
`stripe.dashboard.customer.detail` viewport, the `environment.objectContext`
object returns a `customer` object type and the current customer’s ID. You can
then use those values to get more information about the
[Customer](https://docs.stripe.com/api/customers?lang=node) object and modify
attributes like their address, description, and so on.

For an index of the objects that a viewport gives, see [viewports reference
documentation](https://docs.stripe.com/stripe-apps/reference/viewports).

### Example: Update customer name

The following code updates the customer name by using the [Stripe Node.js API
client](https://docs.stripe.com/api?lang=node) and the viewport’s
`environment.objectContext` ID:

- Add the `customer_write` permission to your app:

```
stripe apps grant permission "customer_write" "Allows the app to update the name
of the customer."
```
- Use the Stripe API in your app to update the customer’s name:

```
import {createHttpClient, STRIPE_API_KEY} from
'@stripe/ui-extension-sdk/http_client';
import Stripe from 'stripe';

// Initiate communication with the stripe client.
const stripe = new Stripe(STRIPE_API_KEY, {
 httpClient: createHttpClient(),
 apiVersion: '2022-08-01',
})

const App = ({environment, userContext}) => {
 // Call the Stripe API to make updates to customer details.
 const updateCurrentCustomer = async (newCustomerName) => {
 try {
 // If the user has permission to update customers, this should succeed.
 const updatedCustomer = await stripe.customers.update(
 // We can use the current objectContext to get the customer ID.
 environment.objectContext.id,
 {name: newCustomerName}
 );

 console.log(updatedCustomer.name);
 } catch (error) {}
 };
}
```

### Example: Update Dashboard data

If your app changes data in the Dashboard, use the
[useRefreshDashboardData](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#useRefreshDashboardData)
function to generate a callback that refreshes the data:

```
import {useCallback} from 'react';
import {useRefreshDashboardData} from '@stripe/ui-extension-sdk/context';

const App = () => {
 // Get the callback used to refresh the dashboard data
 const refreshDashboardData = useRefreshDashboardData();

 // Stripe API call
 const updateCustomer = useCallback(async () => {
 try {
 await updateCurrentCustomer();

 // Call to refresh the data in the Dashboard
 refreshDashboardData();
 } catch (error) {}
 }, [refreshDashboardData]);
}
```

## Use third-party APIs

Your UI extension can call third-party APIs (your own API or any public API) to
have your app request or send data.

- Use the `grant url` command to add the third-party API URL:

```
stripe apps grant url "https://*.api.example.com/path/" "Send data to example
service..."
```

Connect-src URL must meet the following requirements:

- Use secure HTTPS protocol (example: `https://www.example.com/api/users/`).
- Contain a path (example: `https://www.example.com/api/users/` URL is valid,
not `https://www.example.com/`). Adding a base path with a trailing slash covers
all paths after it (example: `https://www.example.com/api/` enables calls to
`https://www.example.com/api/users/abc123/address`).
- Can’t be a call to a Stripe API.
- If using a wildcard (`*`), it must be in the left-most DNS label (example:
`https://*.example.com/api/users/`).

Stripe Apps adds the URL in the `connect-src` array of your project’s [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest):

```
"ui_extension": {
 "views": [],
 "actions": [],
 "content_security_policy": {
 "connect-src": [
 "https://*.api.example.com/",
 "https://o0.ingest.example.io/api/",
 ],
"purpose": "Send data to example service. The Example app sends data to the
Example service to provide its functionality and sends anonymous error reports
to our partner Example for debugging purposes"
 }
 }
```

To remove a connect-src URL, you can also use the Stripe CLI:

```
stripe apps revoke connect-src "https://*.api.example.com/path/"
```
- To preview your app in the browser, start your development server and follow
the CLI prompts:

```
stripe apps start
```
- Add the `fetch` call with the URL of your third-party API in your app.

For example, if you add the `https://www.example.com/api/users` connect-src URL
to your [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest), you could
use this fetch call:

```
const makeRequestToService = (endpoint, requestData) => {
 return fetch(`https://www.example.com/api/${endpoint}/`, {
 'POST',
 headers: {
 'Content-Type': 'application/json',
 },
 body: requestData,
 });
};
```
- To use different [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest) values in
local development and production, [load an extended manifest
file](https://docs.stripe.com/stripe-apps/reference/app-manifest#extended-manifest).
- If the third-party API has a JavaScript client library, you can add the
dependency to your app using the `npm add` command.

## Debug the application

While developing your app, you can use your browser’s dev tools console as a
debugging tool.

To isolate the messages related to your app:

- Find your app ID in the [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest).
- On the **Console** panel of your dev tools browser, enter `[Stripe App <your
app ID>]` in the **Filter** box. It should look something like `[Stripe App
com.example.helloworld]`.

## Write tests for your view

We recommend writing tests for your views. In addition to verifying that your
view behaves as intended, unit tests also make it safer to make changes to code
in the future.

When you create your view, the test file ending in `.test.tsx` contains a test
of the default view:

```
import {render, getMockContextProps} from "@stripe/ui-extension-sdk/testing";
import {ContextView} from "@stripe/ui-extension-sdk/ui";

import App from "./App";

describe("App", () => {
 it("renders ContextView", () => {
 const {wrapper} = render(<App {...getMockContextProps()} />);

 expect(wrapper.find(ContextView)).toContainText("save to reload this view");
 });
});
```

You can run all your tests using the included [Jest](https://jestjs.io/) test
runner with the `npm run test` or `yarn test` command. If you’ve used popular
React testing tools like [Testing
Library](https://testing-library.com/docs/react-testing-library/intro) and
[Enzyme](https://enzymejs.github.io/enzyme), the test package included in
`@stripe/ui-extension-sdk/testing` is most familiar.

A typical test follows this pattern:

- Render your view.
- Make an assertion about the initial state, such as text existing.
- Interact with the view.
- Make an assertion about the new state, such as new text appearing.

For more methods and features of the test package, see [UI testing
reference](https://docs.stripe.com/stripe-apps/ui-testing).

[OptionalRemove a
view](https://docs.stripe.com/stripe-apps/build-ui#remove-a-view)
## See also

- [UI components](https://docs.stripe.com/stripe-apps/components)
- [Add an app settings page](https://docs.stripe.com/stripe-apps/app-settings)

## Links

- [UI Extensions
SDK](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)
- [UI toolkit](https://docs.stripe.com/stripe-apps/design)
- [learn how UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [available viewports](https://docs.stripe.com/stripe-apps/reference/viewports)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [installed version of your app in test
mode](https://docs.stripe.com/stripe-apps/upload-install-app)
- [Customer](https://docs.stripe.com/api/customers?lang=node)
- [Stripe Node.js API client](https://docs.stripe.com/api?lang=node)
-
[useRefreshDashboardData](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#useRefreshDashboardData)
- [https://*.api.example.com/path/](https://*.api.example.com/path/)
- [https://*.api.example.com/](https://*.api.example.com/)
- [https://o0.ingest.example.io/api/](https://o0.ingest.example.io/api/)
-
[https://www.example.com/api/${endpoint}/`,](https://www.example.com/api/${endpoint}/`,)
- [load an extended manifest
file](https://docs.stripe.com/stripe-apps/reference/app-manifest#extended-manifest)
- [Jest](https://jestjs.io/)
- [Testing
Library](https://testing-library.com/docs/react-testing-library/intro)
- [Enzyme](https://enzymejs.github.io/enzyme)
- [UI testing reference](https://docs.stripe.com/stripe-apps/ui-testing)
- [UI components](https://docs.stripe.com/stripe-apps/components)
- [Add an app settings page](https://docs.stripe.com/stripe-apps/app-settings)