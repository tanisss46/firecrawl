# Stripe Connector for Salesforce Platform AgnosticInvocable Example

This guide hands you actionable code examples, showing you step-by-step how to
create Stripe customers and payment intents directly within Salesforce. If
you’re a Salesforce administrator, a developer, or simply someone aiming to link
Stripe and Salesforce for smooth data flow and transaction handling, you’ve come
to the right place.

The examples here leverage custom Apex classes to enable generic, agnostic calls
to Stripe’s RESTful API. These examples come in handy if you aim to establish a
layer of abstraction between your Salesforce platform and the Stripe API, making
your system more flexible and easier to manage.

## Create a Customer in Stripe

The following code example creates a Stripe
[Customer](https://docs.stripe.com/api/customers) with a `name`, `email`, and
`metadata` set.

```
// Step 1: Create an instance of the stripeGC.RawInvocableParameters class. This
class is used to set the parameters for the Stripe API call.
stripeGC.RawInvocableParameters parameters = new
stripeGC.RawInvocableParameters();

// Step 2: Set the HTTP method to 'POST' as you are creating a new customer.
parameters.method = 'POST';

// Step 3: Set the endpoint to '/v1/customers'. This is the Stripe API endpoint
for creating a new customer.
parameters.endpoint = '/v1/customers';

//Step 4: Set the Stripe Account ID from Salesforce and set it to the accountId
field of the parameters object.
parameters.accountId = 'a028B0000029RhlQAE';

//Step 5: Set the request body with the customer details.
List<String> postCustomerParameters = new List<String>{
 'email=' + 'customerEmail@example.com',
 'name=' + 'Tim Smith',
 'metadata[AccountId]=' + 'abc123'
};
parameters.requestBody = String.join(postCustomerParameters, '&');

//Step 6: Add the parameters object to a list and call the callStripeEndpoint
method of the stripeGC.AgnosticInvocable class.
List<stripeGC.RawInvocableParameters> paramsCollection = new
List<stripeGC.RawInvocableParameters>{
 parameters
};
List<String> results =
stripeGC.AgnosticInvocable.callStripeEndpoint(paramsCollection);

//Step 7: The callStripeEndpoint method will return a list of strings. If the
customer was created successfully, the first string in the list will be the ID
of the new customer.
System.debug(results[0]);
```

### Create a PaymentIntent

This code example creates a paymentIntent in Stripe.

```
public class stripePayment {
 @AuraEnabled(cacheable=true)
public static String paymentIntent(String StripeAccountID, String amount, String
stripecurrency, String orderID, String onBehalfOf, String customerId) {
 // Create Call for invocable
stripeGC.RawInvocableParameters parameters = new
stripeGC.RawInvocableParameters();
 // Add HTTP Method
 parameters.method = 'POST';

 // Add endpoint
 parameters.endpoint = '/v1/payment_intents';

 // Get the Stripe Account ID from Salesforce
// This assumes you already have the Stripe Account ID and will pass it in as a
parameter
// Alternately, you could use a SOQL query to obtain the Stripe Account ID as
per previous examples
 parameters.accountId = StripeAccountID;
 parameters.connectAccount = onBehalfOf;

 // Prepare the request body
 List<String> postPaymentIntentParameters = new List<String>{
'amount=' + amount, // Pass in the amount to be charged for this payment intent
in the minimum currency unit (for example, cents for USD)
'currency=' + stripecurrency, // Pass in the currency for this payment intent
(for example, 'usd' for USD)
 'customer=' + customerId, // Pass in customer to payment intent
'automatic_payment_methods[enabled]=true', //Turning on automatic payment
methods
 'metadata[order_id]=' + orderID
 };

 parameters.requestBody = String.join(postPaymentIntentParameters, '&');

List<stripeGC.RawInvocableParameters> paramsCollection = new
List<stripeGC.RawInvocableParameters>{ parameters };

List<String> results =
stripeGC.AgnosticInvocable.callStripeEndpoint(paramsCollection);

 return (results != null && results.size() > 0) ? results[0] : null;
 }
}
```

## See also

- [Installation
guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)
- [Enablement
videos](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/videos)
- [Configure
events](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/configure-events)

## Links

- [Customer](https://docs.stripe.com/api/customers)
- [Installation
guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)
- [Enablement
videos](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/videos)
- [Configure
events](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/configure-events)