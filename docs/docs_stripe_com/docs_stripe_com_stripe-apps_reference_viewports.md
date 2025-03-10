# Viewports reference

## A list of available viewports for Stripe Apps and how your end users see them.

A viewport specifies the page in the Dashboard where your view can appear. A
viewport can provide an `environment.objectContext` object that allows you to
receive context on a current page’s Stripe object. For more information, see
[Access Stripe objects in the
Dashboard](https://docs.stripe.com/stripe-apps/build-ui#access-stripe-objects).

Available viewports for your UI extension:

Viewport IDPageURLsObject type`stripe.dashboard.payment.list`Payments
page`dashboard.stripe.com/payments``null``stripe.dashboard.payment.detail`Payment
details page`dashboard.stripe.com/payments/:id``charge`,
`payment_intent``stripe.dashboard.customer.list`Customers
page`dashboard.stripe.com/customers``null``stripe.dashboard.customer.detail`Customer
details
page`dashboard.stripe.com/customers/:id``customer``stripe.dashboard.invoice.list`Invoices
page`dashboard.stripe.com/invoices``null``stripe.dashboard.invoice.detail`Invoice
details
page`dashboard.stripe.com/invoices/:id``invoice``stripe.dashboard.product.list`Products
page`dashboard.stripe.com/products/``null``stripe.dashboard.product.detail`Product
details
page`dashboard.stripe.com/products/:id``product``stripe.dashboard.subscription.list`Subscriptions
page`dashboard.stripe.com/subscriptions``null``stripe.dashboard.subscription.detail`Subscription
details
page`dashboard.stripe.com/subscriptions/:id``subscription``stripe.dashboard.payment-link.list`Payment
Links
page`dashboard.stripe.com/payment-links``null``stripe.dashboard.payment-link.detail`Payment
Link details
page`dashboard.stripe.com/payment-links/:id``payment_link``stripe.dashboard.home.overview`Dashboard
homepage`dashboard.stripe.com/dashboard``null``stripe.dashboard.balance.overview`Balance
page`dashboard.stripe.com/balance/overview``null``stripe.dashboard.billing.overview`Billing
page`dashboard.stripe.com/billing``null``stripe.dashboard.report.overview`Reports
> Overview
page`dashboard.stripe.com/reports/hub``null``stripe.dashboard.revenue-recognition.overview`Revenue
Recognition
page`dashboard.stripe.com/revenue-recognition``null``stripe.dashboard.shipping-rates.list`Shipping
Rates
page`dashboard.stripe.com/shipping-rates``null``stripe.dashboard.shipping-rates.detail`Shipping
Rate details
page`dashboard.stripe.com/shipping-rates/:id``shipping_rate``stripe.dashboard.tax-report.overview`Reports
> Tax
page`dashboard.stripe.com/tax/reporting``null``stripe.dashboard.drawer.default`Available
across all pages (For more information, see [Dashboard-wide
availability](https://docs.stripe.com/stripe-apps/reference/viewports#dashboard-wide-availability))
`null``settings`App settings page (For more information, learn how to [add an
app settings page](https://docs.stripe.com/stripe-apps/app-settings).) `null`
## Application availability

You can make your application available across all pages or specific to a single
page in the Dashboard.

### Dashboard-wide availability

If your app specifies a view for the `stripe.dashboard.drawer.default` viewport,
this view appears on every page in the Dashboard except for where you have
defined page-specific views.

For example, if the `ui_extension.views` field in your app’s `stripe-app.json`
manifest is as follows:

```
{
 "id": "com.example.app",
 "version": "1.2.3",
 "name": "Example App",
 "icon": "./example_icon_32.png",
 "permissions": [
 {
 "permission": "customer_read",
 "purpose": "Receive access to the customer information"
 }
 ],
 "ui_extension": {
 "views": [
 {
 "viewport": "stripe.dashboard.customer.detail",
 "component": "CustomerView"
 },
 {
 "viewport": "stripe.dashboard.drawer.default",
 "component": "EverywhereElseView"
 }
 ]
 }
}
```

“CustomerView” would appear when the application is open on the Customer details
page, and “EverywhereElseView” would appear on every other page in the
Dashboard.

The `stripe.dashboard.drawer.default` view doesn’t receive `objectContext` data
the way that a page-specific view does. If your app needs to access information
like the `id` of an invoice shown on an “Invoice details” page, you need to
create a view that uses the `stripe.dashboard.invoice.detail` viewport. For more
information, see [Page-specific
availability](https://docs.stripe.com/stripe-apps/reference/viewports#page-specific-availability).

### Page-specific availability

Page-specific views relate to the current page the user is viewing, and allow
apps to receive additional context about the page through the `environment`
property. For more information, see [Access Stripe objects in the
Dashboard](https://docs.stripe.com/stripe-apps/build-ui#access-stripe-objects).

For example, if your app has a view for the `stripe.dashboard.product.detail`
viewport, when a user opens your app on the Product details page, that view
appears in the app.

If your app doesn’t have either a page-specific view for the current page or an
app-specific default view, the drawer displays a generic default view that shows
the user how to access the app.

For example, if your app has two views on page-specific viewports, shown in the
app manifest below:

```
{
 "id": "com.example.app",
 "version": "1.2.3",
 "name": "Example App",
 "icon": "./example_icon_32.png",
 "permissions": [
 {
 "permission": "customer_read",
 "purpose": "Receive access to the customer information"
 }
 ],
 "ui_extension": {
 "views": [
 {
 "viewport": "stripe.dashboard.customer.detail",
 "component": "CustomerView"
 },
 {
 "viewport": "stripe.dashboard.product.detail",
 "component": "ProductView"
 }
 ]
 }
}
```

When the end user opens your app on the Dashboard homepage, the application
displays links to the Customers and Products pages. If the user then navigates
to the Customers page, the app displays a message prompting them to select a
customer to see related information in your app.

## See also

- [Design your app](https://docs.stripe.com/stripe-apps/design)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [Permissions
reference](https://docs.stripe.com/stripe-apps/reference/permissions)
- [UI extension SDK
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)

## Links

- [Access Stripe objects in the
Dashboard](https://docs.stripe.com/stripe-apps/build-ui#access-stripe-objects)
- [add an app settings page](https://docs.stripe.com/stripe-apps/app-settings)
- [Page-specific
availability](https://docs.stripe.com/stripe-apps/reference/viewports#page-specific-availability)
- [Design your app](https://docs.stripe.com/stripe-apps/design)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [Permissions
reference](https://docs.stripe.com/stripe-apps/reference/permissions)
- [UI extension SDK
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)