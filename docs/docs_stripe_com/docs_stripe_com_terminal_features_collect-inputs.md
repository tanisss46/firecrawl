# Collect on-screen inputsPrivate preview

## Use Terminal to collect inputs from your customers.

**Available in:** All supported countries for [Stripe
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700) and [BBPOS
WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e) using
[server-driven integration and client Terminal
SDKs](https://docs.stripe.com/terminal/payments/setup-integration).

#### Private preview

This feature was previously called On-Reader Forms. To request access to the
Collect Inputs private preview for server-driven or client Terminal SDKs, [email
us](mailto:stripe-terminal-betas@stripe.com).

Server-drivenJavascriptiOSAndroidReact Native[Collect
inputs](https://docs.stripe.com/terminal/features/collect-inputs#collect-inputs)
In addition to collecting payments, Terminal smart readers allow you to display
forms and collect information from customers. You make requests to the Stripe
API, and the API communicates with the reader to display a prebuilt UI to
collect customer input. Stripe notifies your backend of the customer’s responses
using [webhooks](https://docs.stripe.com/webhooks).

To collect inputs using Terminal’s smart readers, use the
[collect_inputs](https://docs.stripe.com/api/terminal/readers/collect_inputs)
command. You can specify up to 5 inputs at a time, and the reader collects them
in sequence. Stripe smart readers currently support six input types:

- The `selection` input type allows you to display up to 4 choices for a
customer to select from.
- The `signature` input type allows you to collect a signature using the
reader’s touchscreen.
- The `email` input type allows you to collect an email address from a customer.
- The `phone` input type allows you to collect a phone number from a customer.
- The `text` input type allows you to collect additional information from
customers.
- The `numeric` input type allows you to collect additional information from
customers.

![Supported input
types.](https://b.stripecdn.com/docs-statics-srv/assets/collect-inputs-form-types.9715c2bbc0105378c9c4a5e8e1c4eb59.png)

Supported input types.

You can customize the appearance and behavior of all input types:

- Set important inputs as
[required](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-required)
to make sure they’re collected. For required inputs, the skip button is hidden.
- Provide context to your customer by specifying the text you want to display on
the reader screen for each input using
[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text).
- Use line breaks in your text for better formatting.
- Add up to 4
[toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles)
that customers can enable or disable for Boolean options, agreements, or
opt-ins.
Field nameField locationMaximum
characters`title`[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-title)40`description`[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-description)500when
used with the `selection`
form`description`[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-description)100when
used with any other form
type`submit_button`[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-submit_button)30`skip_button`[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-skip_button)14`title`[toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles-title)50`description`[toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles-description)50

![Toggles in email and selection
form](https://b.stripecdn.com/docs-statics-srv/assets/collect-inputs-toggle.3183c0c14cc916374d588ba54ad34639.png)

Email and selection form with toggle

Additional customization is available for
[selection](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection)
inputs. When specifying the
[choices](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection-choices)
you want to display to the customer, you can emphasize or de-emphasize choices
using the
[style](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection-choices-style)
parameter.

![Selection choice
styles](https://b.stripecdn.com/docs-statics-srv/assets/collect-inputs-choice-style.dc4d2fcb98ee649a29bc43df806c114a.png)

Primary and secondary selection choice styles

In addition to the list of inputs, you might want to include
[metadata](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-metadata)
in your request. The request payload includes the specified metadata, which
appears in both the synchronous response and the success or failure webhooks. By
including a unique identifier such as a customer ID or order ID, you can more
easily identify and handle the incoming webhook.

```
curl https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/collect_inputs \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; terminal_collect_inputs_beta=v1;" \
 -d "inputs[0][type]"=signature \
 -d "inputs[0][custom_text][title]"="Rental Agreement" \
-d "inputs[0][custom_text][description]"="Please sign below to indicate that you
agree to the rental agreement." \
 -d "inputs[0][custom_text][submit_button]"=Submit \
 -d "inputs[0][required]"=true \
 -d "inputs[1][type]"=selection \
 -d "inputs[1][selection][choices][0][style]"=primary \
 -d "inputs[1][selection][choices][0][value]"=Email \
 -d "inputs[1][selection][choices][1][style]"=primary \
 -d "inputs[1][selection][choices][1][value]"=Printed \
 -d "inputs[1][selection][choices][2][style]"=secondary \
 -d "inputs[1][selection][choices][2][value]"="No thanks" \
 -d "inputs[1][custom_text][title]"=Receipt \
--data-urlencode "inputs[1][custom_text][description]"="How would you like your
receipt?" \
 -d "inputs[1][required]"=true \
 -d "inputs[2][type]"=email \
 -d "inputs[2][custom_text][title]"="Enter your email" \
--data-urlencode "inputs[2][custom_text][description]"="We'll send updates on
your order and occasional deals" \
 -d "inputs[2][required]"=true \
 -d "inputs[2][toggles][0][title]"="Opt-in for marketing emails" \
 -d "inputs[2][toggles][0][default_value]"=enabled \
 -d "metadata[order_number]"=12345
```

#### Private preview

You must include the `terminal_collect_inputs_beta=v1` header to use the
`collect_inputs` preview feature. The
[reader](https://docs.stripe.com/api/terminal/readers/object) object won’t
include the
[collect_inputs](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs)
object in API responses if you omit the header.

#### Note

Don’t use `collect_inputs` to collect sensitive data (including protected health
information and customer payment card information), or any information
restricted by law.

[Customer
interaction](https://docs.stripe.com/terminal/features/collect-inputs#customer-interaction)
When the reader begins collecting inputs, it displays the first input from the
list you specified to the customer. The customer must make a selection, provide
a signature, or use the keyboard to proceed with required inputs. However, for
optional inputs, the customer has the option to skip to the next requested
input.

After the customer has either submitted or skipped all inputs, Stripe updates
the reader object and sends out the `terminal.reader.action_succeeded` webhook.
The reader transitions to an interstitial state for 3 seconds, where it’s able
to navigate to a subsequent request. After the 3 seconds, the reader transitions
back to the splash screen.

#### Note

You are fully responsible for being aware of, and complying with all applicable
laws and regulations governing your use of this feature, and must in relation to
such use, obtain, as applicable, all necessary consents, authorizations,
licenses, rights, and permissions. If you use input collected by, or output
displayed from a Terminal smart reader to enter into contracts with, or provide
notices to your customers, you are fully responsible for ensuring the legal
validity and enforceability of such contracts or notices.

[Receive input
data](https://docs.stripe.com/terminal/features/collect-inputs#receive-input-data)
Use the curl command below as an example to create a webhook endpoint to receive
the collected inputs.

```
curl https://api.stripe.com/v1/webhook_endpoints \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 --header "Stripe-Version: 2023-10-16; terminal_collect_inputs_beta=v1" \
 --data-urlencode "url"="https://example.com/webhook/endpoint" \
 --data-urlencode "api_version"="2023-10-16;terminal_collect_inputs_beta=v1" \
 --data-urlencode "enabled_events[]"="terminal.reader.action_succeeded" \
 --data-urlencode "enabled_events[]"="terminal.reader.action_failed"
```

#### Caution

You must create the webhook endpoint directly with Stripe’s
[/v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/create)
API. The [collect_inputs
object](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs)
doesn’t return complete results if you create the webhook endpoint with Stripe
CLI or Stripe server-side SDKs. To make sure that the `collect_inputs` object is
present in the webhook payload, include `terminal_collect_inputs_beta=v1` in the
request header and set the `api_version` property when you [create the webhook
endpoint](https://docs.stripe.com/api/webhook_endpoints/create).

You won’t be able to update an existing webhook to start listening to collected
inputs, you must create a new one.

When all inputs have been collected or skipped, Stripe sends a request to your
webhook endpoint. The request payload is identical to the response when calling
[collect_inputs](https://docs.stripe.com/api/terminal/readers/collect_inputs),
but adds a few additional parameters:

- The `value` parameter is populated for each collected input.- For signature
type inputs, the
[value](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-signature-value)
is a [file ID](https://docs.stripe.com/api/files/object#file_object-id) that
[retrieves](https://docs.stripe.com/api/files/retrieve) the signature image as
an SVG.
- For selection type inputs, the
[value](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-selection-value)
is the string of the selected choice’s `value`.
- For phone, email, text, and numeric inputs, the value is the string of the
customer’s response.
- If an optional input is skipped by the customer, the
[skipped](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-skipped)
parameter is set to `true`.
- The `value` of each toggle is populated with `enabled` or `disabled`.

Subscribe to webhooks to receive collected inputs as soon as they’re available.
You can [retrieve the
reader](https://docs.stripe.com/api/terminal/readers/retrieve) with the
`terminal_collect_inputs_beta=v1` request header as a backup if your backend
fails to consume the webhook.

Stripe sends two webhooks to notify your backend of the reader’s status:

- `terminal.reader.action_succeeded`: Sent when a `collect_inputs` action
succeeds.
- `terminal.reader.action_failed`: Sent when a `collect_inputs` action fails.
This includes timeouts, which occur after the reader screen isn’t touched for 2
minutes.
[Download signature
images](https://docs.stripe.com/terminal/features/collect-inputs#download-signature-images)
To receive the collected signature image, [retrieve the
file](https://docs.stripe.com/api/files/retrieve) and use your secret key to
access its [URL](https://docs.stripe.com/api/files/object#file_object-url).

#### Note

Stripe stores the signature images you collect for 7 days. If you need to use
signature images more than 7 days after collecting them, download the file and
store it. You are fully responsible for being aware of and complying with all
laws that apply to your use, storage, and disclosure of your customers’
signatures.

## Test your integration

After you’re approved and enabled for the private preview, you can test your
integration using a simulated reader.

## Beta SDK

If you use one of Stripe’s [server-side SDKs](https://docs.stripe.com/sdks), you
must install a beta version. For installation instructions, refer to the
relevant GitHub page for the server SDK you want to use.

You also need to configure your SDK’s API version to include the beta header
mentioned above. View [language-specific examples of how to accomplish
this](https://docs.stripe.com/api/versioning).

## Links

- [Stripe S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e)
- [server-driven integration and client Terminal
SDKs](https://docs.stripe.com/terminal/payments/setup-integration)
- [webhooks](https://docs.stripe.com/webhooks)
- [collect_inputs](https://docs.stripe.com/api/terminal/readers/collect_inputs)
-
[required](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-required)
-
[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text)
-
[toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles)
-
[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-title)
-
[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-description)
-
[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-submit_button)
-
[custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text-skip_button)
-
[toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles-title)
-
[toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles-description)
-
[selection](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection)
-
[choices](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection-choices)
-
[style](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection-choices-style)
-
[metadata](https://docs.stripe.com/api/terminal/readers/collect_inputs#collect_inputs-metadata)
- [reader](https://docs.stripe.com/api/terminal/readers/object)
-
[collect_inputs](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs)
- [https://example.com/webhook/endpoint](https://example.com/webhook/endpoint)
- [/v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/create)
-
[value](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-signature-value)
- [file ID](https://docs.stripe.com/api/files/object#file_object-id)
- [retrieves](https://docs.stripe.com/api/files/retrieve)
-
[value](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-selection-value)
-
[skipped](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-skipped)
- [retrieve the reader](https://docs.stripe.com/api/terminal/readers/retrieve)
- [URL](https://docs.stripe.com/api/files/object#file_object-url)
- [server-side SDKs](https://docs.stripe.com/sdks)
- [language-specific examples of how to accomplish
this](https://docs.stripe.com/api/versioning)