# Error codes

## Learn more about error codes and how to resolve them.

Some [Errors](https://docs.stripe.com/api/errors) include an [error
code](https://docs.stripe.com/api/errors#errors-code)—a short string with a
brief explanation. These codes play a role in [our recommended error handling
techniques](https://docs.stripe.com/error-handling). See the documentation on
[payment errors](https://docs.stripe.com/error-handling#payment-errors) for an
example.

Below is a list of possible error codes, along with additional information about
how to resolve them. For convenience, every Error object links to this list in
its [doc_url](https://docs.stripe.com/api/errors#errors-doc_url) attribute.

You can also [trigger some specific error
codes](https://docs.stripe.com/testing#declined-payments) for test purposes.

### `account_closed`

The customer’s bank account has been closed.

### `account_country_invalid_address`

The country of the business address provided does not match the country of the
account. Businesses must be located in the same country as the account.

### `account_error_country_change_requires_additional_steps`

Your account has already onboarded as a Connect platform. Changing your country
requires additional steps. Please reach out to Stripe support for more
information.

### `account_information_mismatch`

Some account information mismatches with one another. For example, some banks
might require that the business_profile.name must match the account holder name.

### `account_invalid`

The account ID provided as a value for the `Stripe-Account` header is invalid.
Check that your requests are specifying a valid account ID.

### `account_number_invalid`

The bank account number provided is invalid (e.g., missing digits). Bank account
information varies from country to country. We recommend creating validations in
your entry forms based on the [bank account
formats](https://docs.stripe.com/connect/payouts-bank-accounts) we provide.

### `acss_debit_session_incomplete`

The ACSS debit session is not ready to transition to complete status yet. Please
try again the request later.

### `alipay_upgrade_required`

This method for creating Alipay payments is not supported anymore. Please
upgrade your integration to use
[Sources](https://stripe.com/docs/sources/alipay) instead.

### `amount_too_large`

The specified amount is greater than the maximum amount allowed. Use a lower
amount and try again.

### `amount_too_small`

The specified amount is less than the minimum amount allowed. Use a higher
amount and try again.

### `api_key_expired`

The API key provided has expired. Obtain your current API keys from the
[Dashboard](https://dashboard.stripe.com/account/apikeys) and update your
integration to use them.

### `application_fees_not_allowed`

The proposed money movement could not be completed due to regulatory reasons.

### `authentication_required`

The payment requires authentication to proceed. If your customer is [off
session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session),
notify your customer to return to your application and complete the payment. If
you provided the
[error_on_requires_action](https://docs.stripe.com/payments/without-card-authentication)
parameter, then your customer should try another card that does not require
authentication.

### `balance_insufficient`

The transfer or payout could not be completed because the associated account
does not have a sufficient balance available. Create a new transfer or payout
using an amount less than or equal to the account’s available balance.

### `balance_invalid_parameter`

Invalid parameter was provided in the balance method object. Check our API
documentation or the returned error message for more context.

### `bank_account_bad_routing_numbers`

The bank account is known to not support the currency in question.

### `bank_account_declined`

The bank account provided can not be used to charge, either because it is not
verified yet or it is not supported.

### `bank_account_exists`

The bank account provided already exists on the specified
[Customer](https://docs.stripe.com/api#update_customer-source) object. If the
bank account should also be attached to a different customer, include the
correct customer ID when making the request again.

### `bank_account_restricted`

The customer’s account cannot be used with the payment method.

### `bank_account_unusable`

The bank account provided cannot be used. A different bank account must be used.

### `bank_account_unverified`

Your Connect platform is attempting to share an unverified bank account with a
connected account.

### `bank_account_verification_failed`

The bank account cannot be verified, either because the microdeposit amounts
provided do not match the actual amounts, or because verification has failed too
many times.

### `billing_invalid_mandate`

The Subscription or Invoice attempted payment on a PaymentMethod without an
active mandate. In order to create Subscription or Invoice payments with this
PaymentMethod, it must be confirmed on-session with a PaymentIntent or
SetupIntent first.

### `bitcoin_upgrade_required`

This method for creating Bitcoin payments is not supported anymore. Please
upgrade your integration to use [Sources](https://stripe.com/docs/sources)
instead.

### `capture_charge_authorization_expired`

The charge cannot be [captured](https://docs.stripe.com/charges/placing-a-hold)
as the authorization has expired. Refer to the payment method’s documentation to
learn more.

### `capture_unauthorized_payment`

The charge you’re attempting to
[capture](https://docs.stripe.com/charges/placing-a-hold) has not been
authorized for capturing payment.

### `card_decline_rate_limit_exceeded`

This card has been declined too many times. You can try to charge this card
again after 24 hours. We suggest reaching out to your customer to make sure they
have entered all of their information correctly and that there are no issues
with their card.

### `card_declined`

The card has been declined. When a card is declined, the error returned also
includes the `decline_code` attribute with the reason why the card was declined.
Refer to our [decline codes](https://docs.stripe.com/declines/codes)
documentation to learn more.

### `cardholder_phone_number_required`

You must have a `phone_number` on file for Issuing Cardholders who will be
creating EU cards. You cannot create EU cards without a `phone_number` on file
for the cardholder. See the [3D Secure
Documenation](https://docs.stripe.com/issuing/3d-secure) for more details.

### `charge_already_captured`

The charge you’re attempting to
[capture](https://docs.stripe.com/charges/placing-a-hold) has already been
captured. Update the request with an uncaptured charge ID.

### `charge_already_refunded`

The charge you’re attempting to [refund](https://docs.stripe.com/refunds) has
already been refunded. Update the request to use the ID of a charge that has not
been refunded.

### `charge_disputed`

The charge you’re attempting to [refund](https://docs.stripe.com/refunds) has
been charged back. Check the [disputes
documentation](https://docs.stripe.com/disputes) to learn how to respond to the
dispute.

### `charge_exceeds_source_limit`

This charge would cause you to exceed your rolling-window processing limit for
this source type. Please retry the charge later, or [contact
us](https://support.stripe.com/email) to request a higher processing limit.

### `charge_exceeds_transaction_limit`

This charge would cause you to exceed your processing limit for this payment
type. Please [contact us](https://support.stripe.com/contact/login) to request a
higher processing limit.

### `charge_expired_for_capture`

The charge cannot be captured as the authorization has expired. Auth and capture
charges must be [captured within a set number of
days](https://docs.stripe.com/charges/placing-a-hold) (7 by default).

### `charge_invalid_parameter`

One or more provided parameters was not allowed for the given operation on the
Charge. Check our [API reference](https://docs.stripe.com/api/charges) or the
returned error message to see which values were not correct for that Charge.

### `charge_not_refundable`

Attempt to refund a charge was unsuccessful because the charge is no longer
refundable.

### `clearing_code_unsupported`

The clearing code provided is not supported.

### `country_code_invalid`

The country code provided was invalid.

### `country_unsupported`

Your platform attempted to create a custom account in a country that is not yet
supported. Make sure that users can only sign up in [countries supported by
custom accounts](https://docs.stripe.com/connect/custom-accounts#country).

### `coupon_expired`

The [coupon](https://docs.stripe.com/api#coupons) provided for a
[subscription](https://docs.stripe.com/api#subscriptions) or
[order](https://docs.stripe.com/api#orders) has expired. Either create a new
coupon, or use an existing one that is valid.

### `customer_max_payment_methods`

The maximum number of
[PaymentMethods](https://docs.stripe.com/api/payment_methods) for this
[Customer](https://docs.stripe.com/api/customers) has been reached. Either
[detach](https://docs.stripe.com/api/payment_methods/detach) some PaymentMethods
from this Customer or proceed with a different Customer.

### `customer_max_subscriptions`

The maximum number of subscriptions for a customer has been reached. [Contact
us](https://support.stripe.com/email) if you are receiving this error.

### `customer_tax_location_invalid`

The customer address is missing or not valid for tax purposes. Make sure to
provide a
[country](https://docs.stripe.com/api/customers/object#customer_object-address-country)
as a two-letter [ISO code](https://en.wikipedia.org/wiki/ISO_3166-1) and also a
[postal_code](https://docs.stripe.com/api/customers/object#customer_object-address-postal_code),
at minimum. See how to [collect customer
addresses](https://docs.stripe.com/tax/customer-locations).

### `debit_not_authorized`

The customer has notified their bank that this payment was unauthorized.

### `email_invalid`

The email address is invalid (e.g., not properly formatted). Check that the
email address is properly formatted and only includes [allowed
characters](https://en.wikipedia.org/wiki/Email_address#Local-part).

### `expired_card`

The card has expired. Check the expiration date or use a different card.

### `financial_connections_account_inactive`

Data cannot be refreshed on inactive Financial Connections accounts.

### `financial_connections_no_successful_transaction_refresh`

Transaction data can only be retrieved for accounts that have at least one
successful transaction refresh.

### `forwarding_api_inactive`

The vault and forward API is currently not accessible with this account and/or
config. Please [contact us](https://support.stripe.com/contact) if you are
receiving this error.

### `forwarding_api_invalid_parameter`

Invalid parameter was provided in the vault and forward API. Check our API
documentation or the returned error message for more context.

### `forwarding_api_upstream_connection_error`

Stripe did not receive a response from the destination endpoint. This typically
indicates a problem with the destination endpoint, rather than with Stripe.

### `forwarding_api_upstream_connection_timeout`

The request to the destination endpoint timed out. This typically indicates a
problem with the destination endpoint, rather than with Stripe.

### `idempotency_key_in_use`

The idempotency key provided is currently being used in another request. This
occurs if your integration is making duplicate requests simultaneously.

### `incorrect_address`

The card’s address is incorrect. Check the card’s address or use a different
card.

### `incorrect_cvc`

The card’s security code is incorrect. Check the card’s security code or use a
different card.

### `incorrect_number`

The card number is incorrect. Check the card’s number or use a different card.

### `incorrect_zip`

The card’s postal code is incorrect. Check the card’s postal code or use a
different card.

### `instant_payouts_config_disabled`

This connected account is not eligible for Instant Payouts. Ask the platform to
enable Instant Payouts.

### `instant_payouts_currency_disabled`

This connected account is not eligible for Instant Payouts in this currency. Ask
the platform to enable Instant Payouts in this currency.

### `instant_payouts_limit_exceeded`

You have reached your daily processing limits for Instant Payouts.

### `instant_payouts_unsupported`

Instant Payouts are not available for this request. Please review our [Instant
Payouts documentation](https://support.stripe.com/topics/instant-payouts) for
detailed requirements and supported configurations.

### `insufficient_funds`

The customer’s account has insufficient funds to cover this payment.

### `intent_invalid_state`

Intent is not in the state that is required to perform the operation.

### `intent_verification_method_missing`

Intent does not have verification method specified in its PaymentMethodOptions
object.

### `invalid_card_type`

The card provided as an [external
account](https://stripe.com/docs/api#external_accounts) is not supported for
payouts. Provide a non-prepaid debit card instead.

### `invalid_characters`

This value provided to the field contains characters that are unsupported by the
field.

### `invalid_charge_amount`

The specified amount is invalid. The [charge
amount](https://docs.stripe.com/api#create_charge-amount) must be a positive
integer in the smallest currency unit, and not exceed the [minimum or maximum
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).

### `invalid_cvc`

The card’s security code is invalid. Check the card’s security code or use a
different card.

### `invalid_expiry_month`

The card’s expiration month is incorrect. Check the expiration date or use a
different card.

### `invalid_expiry_year`

The card’s expiration year is incorrect. Check the expiration date or use a
different card.

### `invalid_mandate_reference_prefix_format`

The provided prefix used to generate the mandate reference is invalid.

### `invalid_number`

The card number is invalid. Check the card details or use a different card.

### `invalid_source_usage`

The source cannot be used because it is not in the correct state (e.g., a charge
request is trying to use a source with a `pending`, `failed`, or `consumed`
source). Check the [status](https://docs.stripe.com/api#source_object-status) of
the source you are attempting to use.

### `invalid_tax_location`

The specified location is invalid. Check the [Supported address
formats](https://docs.stripe.com/tax/customer-locations#supported-formats) for
the address formats supported when calculating tax.

### `invoice_no_customer_line_items`

An invoice cannot be generated for the specified customer as there are no
pending invoice items. Check that the correct customer is being specified or
create any necessary invoice items first.

### `invoice_no_payment_method_types`

An invoice cannot be finalized because there are no payment method types
available to process the payment. Your [invoice template
settings](https://dashboard.stripe.com/settings/billing/invoice) or the
invoice’s
[payment_settings](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings)
might be restricting which payment methods are available, or you might need to
activate more [payment methods](https://dashboard.stripe.com/settings/payments)
in the Dashboard.

### `invoice_no_subscription_line_items`

An invoice cannot be generated for the specified subscription as there are no
pending invoice items. Check that the correct subscription is being specified or
create any necessary invoice items first.

### `invoice_not_editable`

The specified invoice can no longer be edited. Instead, consider creating
additional [invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
that will be applied to the next invoice. You can either [manually
generate](https://docs.stripe.com/billing/invoices/subscription#generating-invoices)
the next invoice or wait for it to be automatically generated at the end of the
billing cycle.

### `invoice_on_behalf_of_not_editable`

You cannot update the `on_behalf_of` property of an invoice after the invoice
has been assigned a number.

### `invoice_payment_intent_requires_action`

This payment requires additional user action before it can be completed
successfully. Payment can be completed using the PaymentIntent associated with
the invoice. See [this
page](https://stripe.com/docs/billing/subscriptions/payment#handling-action-required)
for more details.

### `invoice_upcoming_none`

There is no upcoming invoice on the specified customer to preview. Only
customers with active subscriptions or pending invoice items have invoices that
can be previewed.

### `livemode_mismatch`

Test and live mode API keys, requests, and objects are only available within the
mode they are in.

### `lock_timeout`

This object cannot be accessed right now because another API request or Stripe
process is currently accessing it. If you see this error intermittently, retry
the request. If you see this error frequently and are making multiple concurrent
requests to a single object, make your requests serially or at a lower rate. See
the [rate limit
documentation](https://docs.stripe.com/rate-limits#object-lock-timeouts) for
more details.

### `missing`

Both a customer and source ID have been provided, but the source has not been
saved to the customer. To create a charge for a customer with a specified
source, you must first [save the card
details](https://docs.stripe.com/saving-cards).

### `no_account`

The bank account could not be located.

### `not_allowed_on_standard_account`

Transfers and payouts on behalf of a Standard connected account are not allowed.

### `out_of_inventory`

One or more line item(s) are out of stock. If more stock is available, update
the inventory’s orderable quantity and try again.

### `ownership_declaration_not_allowed`

Company ownership declaration is allowed only during account updates and
accounts created via account tokens.

### `parameter_invalid_empty`

One or more required values were not provided. Make sure requests include all
required parameters.

### `parameter_invalid_integer`

One or more of the parameters requires an integer, but the values provided were
a different type. Make sure that only supported values are provided for each
attribute. Refer to our [API documentation](https://stripe.com/docs/api) to look
up the type of data each attribute supports.

### `parameter_invalid_string_blank`

One or more values provided only included whitespace. Check the values in your
request and update any that contain only whitespace.

### `parameter_invalid_string_empty`

One or more required string values is empty. Make sure that string values
contain at least one character.

### `parameter_missing`

One or more required values are missing. Check our [API
documentation](https://docs.stripe.com/api) to see which values are required to
create or modify the specified resource.

### `parameter_unknown`

The request contains one or more unexpected parameters. Remove these and try
again.

### `parameters_exclusive`

Two or more mutually exclusive parameters were provided. Check our [API
documentation](https://docs.stripe.com/api) or the returned error message to see
which values are permitted when creating or modifying the specified resource.

### `payment_intent_action_required`

The provided payment method requires customer actions to complete, but
`error_on_requires_action` was set. If you’d like to add this payment method to
your integration, we recommend that you first [upgrade your integration to
handle
actions](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions).

### `payment_intent_authentication_failure`

The provided payment method has failed authentication. Provide a new payment
method to attempt to fulfill this PaymentIntent again.

### `payment_intent_incompatible_payment_method`

The PaymentIntent expected a payment method with different properties than what
was provided.

### `payment_intent_invalid_parameter`

One or more provided parameters was not allowed for the given operation on the
PaymentIntent. Check our [API
reference](https://docs.stripe.com/api/payment_intents) or the returned error
message to see which values were not correct for that PaymentIntent.

### `payment_intent_konbini_rejected_confirmation_number`

The `confirmation_number` provided in `payment_method_options[konbini]` was
rejected by the processing partner at time of PaymentIntent confirmation.

### `payment_intent_mandate_invalid`

The provided mandate is invalid and can not be used for the payment intent.

### `payment_intent_payment_attempt_expired`

The latest payment attempt for the PaymentIntent has expired. Check the
[last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
property on the PaymentIntent for more details, and provide a new payment method
to attempt to fulfill this PaymentIntent again.

### `payment_intent_payment_attempt_failed`

The latest payment attempt for the PaymentIntent has failed. Check the
[last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
property on the PaymentIntent for more details, and provide a new payment method
to attempt to fulfill this PaymentIntent again.

### `payment_intent_unexpected_state`

The PaymentIntent’s state was incompatible with the operation you were trying to
perform.

### `payment_method_bank_account_already_verified`

This bank account has already been verified.

### `payment_method_bank_account_blocked`

This bank account has failed verification in the past and can not be used.
[Contact us](https://support.stripe.com/email) if you wish to attempt to use
these bank account credentials.

### `payment_method_billing_details_address_missing`

The PaymentMethod’s billing details is missing address details. Please update
the missing fields and try again.

### `payment_method_configuration_failures`

Attempt to create or modify Payment Method Configuration was unsuccessful.

### `payment_method_currency_mismatch`

The currency specified does not match the currency for the attached payment
method. A payment can only be created for the same currency as the corresponding
payment method.

### `payment_method_customer_decline`

The customer did not approve the payment. Please provide a new payment method to
attempt to fulfill this intent again.

### `payment_method_invalid_parameter`

Invalid parameter was provided in the payment method object. Check our [API
documentation](https://docs.stripe.com/api) or the returned error message for
more context.

### `payment_method_invalid_parameter_testmode`

The parameter provided for payment method is not allowed to be used in testmode.
Check our [API documentation](https://docs.stripe.com/api) or the returned error
message for more context.

### `payment_method_microdeposit_failed`

Microdeposits were failed to be deposited into the customer’s bank account.
Please check the account, institution and transit numbers as well as the
currency type.

### `payment_method_microdeposit_verification_amounts_invalid`

You must provide exactly two microdeposit amounts.

### `payment_method_microdeposit_verification_amounts_mismatch`

The amounts provided do not match the amounts that were sent to the bank
account.

### `payment_method_microdeposit_verification_attempts_exceeded`

You have exceeded the number of allowed verification attempts.

### `payment_method_microdeposit_verification_descriptor_code_mismatch`

The verification code provided does not match the one sent to the bank account.

### `payment_method_microdeposit_verification_timeout`

Payment method should be verified with microdeposits within the required period.

### `payment_method_not_available`

The payment processor for the provided payment method is temporarily
unavailable. Please try a different payment method or retry later with the same
payment method.

### `payment_method_provider_decline`

The payment or setup attempt was declined by the issuer or customer. Check the
[last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
or
[last_setup_error](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-last_setup_error)
property on the PaymentIntent or SetupIntent respectively for more details, and
provide a new payment method to attempt to fulfill this intent again.

### `payment_method_provider_timeout`

The payment method failed due to a timeout. Check the
[last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
or
[last_setup_error](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-last_setup_error)
property on the PaymentIntent or SetupIntent respectively for more details, and
provide a new payment method to attempt to fulfill this intent again.

### `payment_method_unactivated`

The operation cannot be performed as the payment method used has not been
activated. Activate the payment method in the
[Dashboard](https://dashboard.stripe.com/account/payments/settings), then try
again.

### `payment_method_unexpected_state`

The provided payment method’s state was incompatible with the operation you were
trying to perform. Confirm that the payment method is in an allowed state for
the given operation before attempting to perform it.

### `payment_method_unsupported_type`

The API only supports payment methods of certain types.

### `payout_reconciliation_not_ready`

Reconciliation for this payout is still in progress.

### `payouts_limit_exceeded`

You have reached your daily processing limits for this payout type.

### `payouts_not_allowed`

Payouts have been disabled on the connected account. Check the connected
account’s status to see if any [additional
information](https://docs.stripe.com/connect/identity-verification) needs to be
provided, or if payouts have been disabled for [another
reason](https://docs.stripe.com/connect/handling-api-verification#determining-if-identity-verification-is-needed).

### `platform_account_required`

Only Stripe Connect platforms can work with other accounts. If you need to setup
a Stripe Connect platform, you can do so [in the
dashboard](https://dashboard.stripe.com/account/applications/settings).

### `platform_api_key_expired`

The API key provided by your Connect platform has expired. This occurs if your
platform has either generated a new key or the connected account has been
disconnected from the platform. Obtain your current API keys from the
[Dashboard](https://dashboard.stripe.com/account/apikeys) and update your
integration, or reach out to the user and reconnect the account.

### `postal_code_invalid`

The postal code provided was incorrect.

### `processing_error`

An error occurred while processing the card. Try again later or with a different
payment method.

### `product_inactive`

The product this SKU belongs to is no longer available for purchase.

### `progressive_onboarding_limit_exceeded`

Progressive onboarding limit has been reached for the platform.

### `rate_limit`

Too many requests hit the API too quickly. We recommend an exponential backoff
of your requests.

### `refer_to_customer`

The customer has stopped the payment with their bank. Contact them for details
and to arrange payment.

### `refund_disputed_payment`

You cannot refund a disputed payment.

### `resource_already_exists`

A resource with a user-specified ID (e.g., plan or coupon) already exists. Use a
different, unique value for `id` and try again.

### `resource_missing`

The ID provided is not valid. Either the resource does not exist, or an ID for a
different resource has been provided.

### `return_intent_already_processed`

You cannot confirm this refund as it is already processed.

### `routing_number_invalid`

The bank routing number provided is invalid.

### `secret_key_required`

The API key provided is a publishable key, but a secret key is required. Obtain
your current API keys from the
[Dashboard](https://dashboard.stripe.com/account/apikeys) and update your
integration to use them.

### `sepa_unsupported_account`

Your account does not support [SEPA](https://docs.stripe.com/sources/sepa-debit)
payments.

### `setup_attempt_failed`

The latest setup attempt for the SetupIntent has failed. Check the
`last_setup_error` property on the SetupIntent for more details, and provide a
new payment method to attempt to set it up again.

### `setup_intent_authentication_failure`

The provided payment method has failed authentication. Provide a new payment
method to attempt to fulfill this SetupIntent again.

### `setup_intent_invalid_parameter`

One or more provided parameters was not allowed for the given operation on the
SetupIntent. Check our [API
reference](https://docs.stripe.com/api/setup_intents) or the returned error
message to see which values were not correct for that SetupIntent.

### `setup_intent_mandate_invalid`

The provided mandate is invalid and can not be used for the setup intent.

### `setup_intent_mobile_wallet_unsupported`

Card Present and Interac Present SetupIntents can only be created with physical
cards, not with mobile wallets.

### `setup_intent_setup_attempt_expired`

The latest setup attempt for the SetupIntent has expired. Check the
[last_setup_error](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-last_setup_error)
property on the SetupIntent for more details, and provide a new payment method
to attempt to complete this SetupIntent again.

### `setup_intent_unexpected_state`

The SetupIntent’s state was incompatible with the operation you were trying to
perform.

### `shipping_address_invalid`

The shipping address information cannot be used to accurately determine tax
rates. Verify that address fields such as zip code, state, or province have been
added correctly.

### `shipping_calculation_failed`

Shipping calculation failed as the information provided was either incorrect or
could not be verified.

### `sku_inactive`

The SKU is inactive and no longer available for purchase. Use a different SKU,
or make the current SKU active again.

### `state_unsupported`

Occurs when providing the `legal_entity` information for a U.S. custom account,
if the provided state is not supported. (This is mostly associated states and
territories.)

### `status_transition_invalid`

The requested status transition is not valid.

### `stripe_tax_inactive`

Stripe Tax has not been activated on your account. Check the [setup
documentation](https://docs.stripe.com/tax/set-up) to get started.

### `tax_id_invalid`

The tax ID number provided is invalid (e.g., missing digits). Tax ID information
varies from country to country, but must be at least nine digits.

### `taxes_calculation_failed`

Tax calculation for the order failed.

### `terminal_location_country_unsupported`

Terminal is currently only available in some countries. Locations in your
country cannot be created in livemode.

### `terminal_reader_busy`

Reader is currently busy processing another request. Please reference the
[integration
guide](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#handle-errors)
for details on how to handle this error.

### `terminal_reader_hardware_fault`

Reader can no longer accept payments as an unrecoverable hardware fault has been
detected. Please reach out to Stripe support at
https://support.stripe.com/contact/email and provide your reader’s serial number
for replacement.

### `terminal_reader_invalid_location_for_activation`

Reader can’t be activated in the currently registered Location. Please register
the reader to a new Location. See [Manage
locations](https://stripe.com/docs/terminal/fleet/locations) for more
information.

### `terminal_reader_invalid_location_for_payment`

Reader can’t take payments in the currently registered Location. Please register
the reader to a new Location. See [Manage
locations](https://stripe.com/docs/terminal/fleet/locations) for more
information.

### `terminal_reader_offline`

Reader is currently offline, please ensure the reader is powered on and
connected to the internet before retrying your request. Reference the
[integration
guide](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#handle-errors)
for details on how to handle this error.

### `terminal_reader_timeout`

There was a timeout when sending this command to the reader. Please reference
the [integration
guide](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#handle-errors)
for details on how to handle this error.

### `testmode_charges_only`

Your account has not been activated and can only make test charges. [Activate
your account](https://dashboard.stripe.com/account/onboarding) in the Dashboard
to begin processing live charges.

### `tls_version_unsupported`

Your integration is using an older version of
[TLS](https://docs.stripe.com/security#tls) that is unsupported. You must be
using TLS 1.2 or above.

### `token_already_used`

The token provided has already been used. You must create a new token before you
can retry this request.

### `token_card_network_invalid`

Invalid card network parameter was provided in the card token object. Check our
[API documentation](https://docs.stripe.com/api) or the returned error message
for more context.

### `token_in_use`

The token provided is currently being used in another request. This occurs if
your integration is making duplicate requests simultaneously.

### `transfer_source_balance_parameters_mismatch`

When creating a Transfer, the `payments` parameter in `source_balance` should
not be passed in when balance `type` is set to `issuing`.

### `transfers_not_allowed`

The requested transfer cannot be created. [Contact
us](https://support.stripe.com/email) if you are receiving this error.

### `url_invalid`

The URL provided is invalid.

## Links

- [Workbench](https://dashboard.stripe.com/workbench)
- [Errors](https://docs.stripe.com/api/errors)
- [error code](https://docs.stripe.com/api/errors#errors-code)
- [our recommended error handling
techniques](https://docs.stripe.com/error-handling)
- [payment errors](https://docs.stripe.com/error-handling#payment-errors)
- [doc_url](https://docs.stripe.com/api/errors#errors-doc_url)
- [trigger some specific error
codes](https://docs.stripe.com/testing#declined-payments)
- [bank account formats](https://docs.stripe.com/connect/payouts-bank-accounts)
- [Sources](https://stripe.com/docs/sources/alipay)
- [Dashboard](https://dashboard.stripe.com/account/apikeys)
- [off
session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
-
[error_on_requires_action](https://docs.stripe.com/payments/without-card-authentication)
- [Customer](https://docs.stripe.com/api#update_customer-source)
- [Sources](https://stripe.com/docs/sources)
- [captured](https://docs.stripe.com/charges/placing-a-hold)
- [decline codes](https://docs.stripe.com/declines/codes)
- [3D Secure Documenation](https://docs.stripe.com/issuing/3d-secure)
- [refund](https://docs.stripe.com/refunds)
- [disputes documentation](https://docs.stripe.com/disputes)
- [contact us](https://support.stripe.com/email)
- [contact us](https://support.stripe.com/contact/login)
- [API reference](https://docs.stripe.com/api/charges)
- [countries supported by custom
accounts](https://docs.stripe.com/connect/custom-accounts#country)
- [coupon](https://docs.stripe.com/api#coupons)
- [subscription](https://docs.stripe.com/api#subscriptions)
- [order](https://docs.stripe.com/api#orders)
- [PaymentMethods](https://docs.stripe.com/api/payment_methods)
- [Customer](https://docs.stripe.com/api/customers)
- [detach](https://docs.stripe.com/api/payment_methods/detach)
-
[country](https://docs.stripe.com/api/customers/object#customer_object-address-country)
- [ISO code](https://en.wikipedia.org/wiki/ISO_3166-1)
-
[postal_code](https://docs.stripe.com/api/customers/object#customer_object-address-postal_code)
- [collect customer addresses](https://docs.stripe.com/tax/customer-locations)
- [allowed characters](https://en.wikipedia.org/wiki/Email_address#Local-part)
- [contact us](https://support.stripe.com/contact)
- [Instant Payouts
documentation](https://support.stripe.com/topics/instant-payouts)
- [external account](https://stripe.com/docs/api#external_accounts)
- [charge amount](https://docs.stripe.com/api#create_charge-amount)
- [minimum or maximum
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
- [status](https://docs.stripe.com/api#source_object-status)
- [Supported address
formats](https://docs.stripe.com/tax/customer-locations#supported-formats)
- [invoice template
settings](https://dashboard.stripe.com/settings/billing/invoice)
-
[payment_settings](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings)
- [payment methods](https://dashboard.stripe.com/settings/payments)
- [invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
- [manually
generate](https://docs.stripe.com/billing/invoices/subscription#generating-invoices)
- [this
page](https://stripe.com/docs/billing/subscriptions/payment#handling-action-required)
- [rate limit
documentation](https://docs.stripe.com/rate-limits#object-lock-timeouts)
- [save the card details](https://docs.stripe.com/saving-cards)
- [API documentation](https://stripe.com/docs/api)
- [API documentation](https://docs.stripe.com/api)
- [upgrade your integration to handle
actions](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions)
- [API reference](https://docs.stripe.com/api/payment_intents)
-
[last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
-
[last_setup_error](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-last_setup_error)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [additional
information](https://docs.stripe.com/connect/identity-verification)
- [another
reason](https://docs.stripe.com/connect/handling-api-verification#determining-if-identity-verification-is-needed)
- [in the dashboard](https://dashboard.stripe.com/account/applications/settings)
- [SEPA](https://docs.stripe.com/sources/sepa-debit)
- [API reference](https://docs.stripe.com/api/setup_intents)
- [setup documentation](https://docs.stripe.com/tax/set-up)
- [integration
guide](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#handle-errors)
- [Manage locations](https://stripe.com/docs/terminal/fleet/locations)
- [Activate your account](https://dashboard.stripe.com/account/onboarding)
- [TLS](https://docs.stripe.com/security#tls)