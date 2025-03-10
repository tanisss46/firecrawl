# Stripe Connector for Salesforce Platform invocations

This guide hands you actionable code examples, that walk you through essential
tasks like creating Stripe customers, initiating checkout sessions, and listing
existing customers—all directly from Salesforce. Geared toward Salesforce
administrators, developers, and anyone interested in seamless Stripe-Salesforce
integrations, these examples utilize custom Apex classes for class based
invocations using Stripe API calls. Whether you’re building a new e-commerce
solution or upgrading your payment workflows, this guide equips you with the
tools you need for efficient Stripe operations in Salesforce.

## Create a Customer in Stripe

The following code example creates a Stripe
[Customer](https://docs.stripe.com/api/customers) with a `name`, `email`, and
`metadata` set.

```
// Step 1: Initialize an instance of the stripeGC.v01_CreateCustomers.V1 class
stripeGC.CreateCustomers.V1 params = new stripeGC.CreateCustomers.V1();
List<stripeGC.CreateCustomers.V1> paramsCollection = new
List<stripeGC.CreateCustomers.V1>{
 params
 };
// Step 2: Set the accountRecordId parameter to the record ID of the Stripe
Account you wish to connect to
params.accountRecordId = 'a028B0000029RhlQAE';

// Step 3: Set the metadata field
stripeGC.Metadata metadata = new stripeGC.Metadata();
metadata.listAdditionalStringField = new List<stripeGC.AdditionalString>{
 new stripeGC.AdditionalString('AccountID', 'abc123')
};
params.metadata = metadata;

// Step 4: Set the name field
params.name = 'Tim Smith';

// Step 5: Set the email field
params.email = 'example@example.com';

// Step 6: Call the stripeGC.v01_PostCustomers.postCustomers_2022_11_15 method
List<stripeGC.Customer> customers =
stripeGC.v01_CreateCustomers.createCustomers_2022_11_15(paramsCollection);
```

## Create a Checkout Session

The following code example creates a Checkout session in Stripe:

```
// Step 1: Initialize an instance of the stripeGC.v01_CreateCheckoutSessions.V1
class
stripeGC.CreateCheckoutSessions.V1 params = new
stripeGC.CreateCheckoutSessions.V1();
List<stripeGC.CreateCheckoutSessions.V1> paramsCollection = new
List<stripeGC.CreateCheckoutSessions.V1>{
 params
 };
// Step 2: Set the accountRecordId parameter to the record ID of the Stripe
Account you wish to connect to
params.accountRecordId = 'a028B0000029RhlQAE';

// Step 3: Set the checkout line items
stripeGC.CreateCheckoutSessionsReqLineItem cliparams = new
stripeGC.CreateCheckoutSessionsReqLineItem();
cliparams.price = 'price_1NhcVkBSPQ8HL343ZNsBp'; //price id from Stripe.
cliparams.quantity = 1;
List<stripeGC.CreateCheckoutSessionsReqLineItem> cliparamlist = new
List<stripeGC.CreateCheckoutSessionsReqLineItem>();
cliparamlist.add(cliparams);
params.lineItems = cliparamlist;

// Step 4: Set mode,successurl,client ref fields
params.mode = 'payment';
params.successUrl = 'https://stripe.com';
params.clientReferenceId = 'abcd123';

// Step 5: Call the
stripeGC.v01_CreateCheckoutSessions.CreateCheckoutSessions_2022_11_15 method
List<stripeGC.CheckoutSession> results =
stripeGC.v01_CreateCheckoutSessions.createCheckoutSessions_2022_11_15(paramsCollection);
```

### List Customers

The following code example lists all of your customers that are stored in
Stripe:

```
// Step 1: Initialize an instance of the stripeGC.v01_ListCustomers.V1 class
stripeGC.ListCustomers.V1 params = new stripeGC.ListCustomers.V1();
List<stripeGC.ListCustomers.V1> paramsCollection = new
List<stripeGC.ListCustomers.V1>{
 params
};

// Step 2: Set the accountRecordId parameter to the record ID of the Stripe
Account you wish to connect to
params.accountRecordId = 'a028B0000029RhlQAE';

// Step 3: Call the stripeGC.v01_ListCustomers.listCustomers_2022_11_15 method
List<stripeGC.CustomerResourceCustomerList > results =
stripeGC.v01_ListCustomers.listCustomers_2022_11_15(paramsCollection);
System.debug(results[0]);
```

## See also

- [Installation
Guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)
- [Enablement
Videos](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/videos)
- [Configure
Events](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/configure-events)

## Links

- [Customer](https://docs.stripe.com/api/customers)
- [https://stripe.com](https://stripe.com)
- [Installation
Guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)
- [Enablement
Videos](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/videos)
- [Configure
Events](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/configure-events)