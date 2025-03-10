# Using Checkout and Go (legacy)

#### Warning

**This page is for the legacy version of Checkout**

We released a [new version of
Checkout](https://docs.stripe.com/payments/checkout) in April 2019 which
redirects to a Stripe-hosted payments page and supports card payments, Apple
Pay, and Google Pay. You can use the [Checkout Migration
Guide](https://docs.stripe.com/payments/checkout/migration) to move from the
legacy version of Checkout to the new version. If you’d like to embed your
payments form on your site, we recommend using [Stripe
Elements](https://docs.stripe.com/payments/elements).

This tutorial demonstrates how to accept payments with Stripe
[Checkout](https://docs.stripe.com/payments/checkout) in a web application built
with [Go](https://golang.org/). The application uses Checkout to accept credit
cards from the end user and send tokens to a back-end API. The back-end route
uses the [Stripe Go library](https://github.com/stripe/stripe-go) to create a
charge. There are four steps:

- [Install
dependencies](https://docs.stripe.com/legacy-checkout/go#step-1-install-dependencies)
- [Create the view
template](https://docs.stripe.com/legacy-checkout/go#step-2-create-the-view-template)
- [Create the
routes](https://docs.stripe.com/legacy-checkout/go#step-3-create-routes)
- [Run the
application](https://docs.stripe.com/legacy-checkout/go#step-4-run-the-application)
[Install and configure
dependencies](https://docs.stripe.com/legacy-checkout/go#step-1-install-dependencies)
To follow along, you need a working Go environment. Create and enter a new
directory, then make sure your package is using Go Modules:

```
go mod init
```

Create a file named **main.go** and add the necessary imports and configuration
values:

```
package main

import (
 "fmt"
 "html/template"
 "net/http"
 "os"
 "path/filepath"

 "github.com/stripe/stripe-go/v76.0.0"
 "github.com/stripe/stripe-go/v76.0.0/charge"
 "github.com/stripe/stripe-go/v76.0.0/customer"
 "github.com/stripe/stripe-go/v{{GOLANG_MAJOR_VERSION}}"
)

func main() {
 publishableKey := os.Getenv("PUBLISHABLE_KEY")
 stripe.Key = os.Getenv("SECRET_KEY")
}
```

The file includes two values, the secret and publishable keys. These keys
identify your account when you communicate with Stripe. In this example, the
application extracts the values from local environment variables in order to
cleanly separate configuration from code. Avoid hard-coding API access keys and
other sensitive data in your application code.

Assign the secret key to the `Key` property of the `stripe` package. Assign the
publishable key to a new variable called `publishableKey` so that it can be used
later.

[Create the view
template](https://docs.stripe.com/legacy-checkout/go#step-2-create-the-view-template)
This example uses Go’s `html/template` package for server-side templating.
Create a file named **views/index.html** for the index template:

```
<html>
<head>
 <title>Checkout Example</title>
</head>
<body>
<form action="/charge" method="post" class="payment">
 <article>
 <label class="amount">
 <span>Amount: $5.00</span>
 </label>
 </article>

<script src="https://checkout.stripe.com/checkout.js" class="stripe-button"
data-key="{{ .Key }}" data-description="A month's subscription"
data-amount="500" data-locale="auto"></script>
</form>
</body>
</html>
```

To integrate the form, load Checkout in an HTML `<script>` tag. It adds a button
to the form that the user can click to display the credit card overlay. The
overlay automatically performs validation and error handling. The `action`
attribute specifies the path of the **charge** route. In the next step, you will
see how the `.Key` attribute is populated with the publishable key for your
Stripe account.

Add the following code to the `main` function in your **main.go** file so that
it will load the template when the application runs:

```
tmpls, _ := template.ParseFiles(filepath.Join("views", "index.html"))
```

[Create routes](https://docs.stripe.com/legacy-checkout/go#step-3-create-routes)
The server exposes two routes:

- A GET route that displays the payment form
- A POST route that receives the payment token and creates the charge

Add the route handlers to the `main` function of the **main.go** file:

```
http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
 tmpl := tmpls.Lookup("index.html")
 tmpl.Execute(w, map[string]string{"Key": publishableKey})
})

http.HandleFunc("/charge", func(w http.ResponseWriter, r *http.Request) {
 r.ParseForm()

 customerParams := &stripe.CustomerParams{
 Email: stripe.String(r.Form.Get("stripeEmail")),
 }
 customerParams.SetSource(r.Form.Get("stripeToken"))

 newCustomer, err := customer.New(customerParams)

 if err != nil {
 http.Error(w, err.Error(), http.StatusInternalServerError)
 return
 }

 chargeParams := &stripe.ChargeParams{
 Amount: stripe.Int64(500),
 Currency: stripe.String(string(stripe.CurrencyUSD)),
 Description: stripe.String("Sample Charge"),
 Customer: stripe.String(newCustomer.ID),
 }

 if _, err := charge.New(chargeParams); err != nil {
 http.Error(w, err.Error(), http.StatusInternalServerError)
 return
 }

 fmt.Fprintf(w, "Charge completed successfully!")
})

http.ListenAndServe(":4567", nil)
```

The index route renders the Checkout form and displays it to the user. Pass the
publishable key into the render function via a map literal so that the template
can embed it in the Checkout form markup.

The **charge** route retrieves the email address and card token from the POST
request body. It uses those parameters to create a Stripe customer. Next, it
invokes the `charge.New` function, providing the `Customer` ID as an option.

In this example, the application charges the user $5. Stripe expects the
developer to describe charges in cents, so compute the value of the `amount`
parameter by multiplying the desired number of dollars by one hundred. Stripe
charges also take an optional `Desc` parameter, which lets you describe the
charge.

When the charge completes successfully, the application displays a message to
the user. You could optionally use a second template in the **charge** route
instead of a plain string.

That’s it, a complete Stripe integration in about 60 lines of Go code.

[Run the
application](https://docs.stripe.com/legacy-checkout/go#step-4-run-the-application)
Run the application from the command line:

```
PUBLISHABLE_KEY=pk_test_TYooMQauvdEDq54NiTphI7jx
SECRET_KEY=sk_test_BQokikJOvBiI2HlWgH4olfQ2 go run main.go
```

Specify values for the [publishable and secret
key](https://dashboard.stripe.com/apikeys) environment variables. `

Navigate to the running application in your browser and click the button to
launch the payment form. If you’re using Stripe test keys, you can test it with
some dummy data. Enter the test number **4242 4242 4242 4242**, a three digit
CVC, and a future expiry date. Submit the form and see if the application
correctly displays the successful charge page.

## Links

- [new version of Checkout](https://docs.stripe.com/payments/checkout)
- [Checkout Migration
Guide](https://docs.stripe.com/payments/checkout/migration)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Go](https://golang.org/)
- [Stripe Go library](https://github.com/stripe/stripe-go)
- [publishable and secret key](https://dashboard.stripe.com/apikeys)