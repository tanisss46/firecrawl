# Daily changelog

#### Caution

This page is no longer being updated. To learn about updates to the Stripe API,
visit the new [Changelog](https://docs.stripe.com/changelog).

This changelog lists historical additions and updates to the Stripe API, in
chronological order.

For breaking changes and steps for upgrading your Stripe API version, view the
[upgrade guide](https://docs.stripe.com/upgrades).

### September 18, 2024

- Add support for new value `international_transaction` on enum
`Treasury.ReceivedDebit.failure_code`
- Add support for `automatically_finalizes_at` on `Invoice`

### September 17, 2024

- Add support for `amazon_pay` on `Dispute.payment_method_details`
- Add support for new value `amazon_pay` on enum
`Dispute.payment_method_details.type`

### September 16, 2024

- Add support for new value `verification_supportability` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`BankAccount.future_requirements.errors[].code`, and
`BankAccount.requirements.errors[].code`
- Add support for new value `terminal_reader_invalid_location_for_activation` on
enums `Invoice.last_finalization_error.code`,
`PaymentIntent.last_payment_error.code`, `SetupAttempt.setup_error.code`,
`SetupIntent.last_setup_error.code`, and `StripeError.code`
- Add support for `payer_details` on `Charge.payment_method_details.klarna`
- Add support for `state_sales_tax` on
`Tax.Registration#create.country_options.us` and
`Tax.Registration.country_options.us`

### September 10, 2024

- Change `TestHelpers.TestClock.status_details` to be required
- Add support for new value `submitted` on enum `Issuing.Card.shipping.status`
- Add support for `required` on `Checkout.Session#create.tax_id_collection`,
`Checkout.Session.tax_id_collection`, `PaymentLink#create.tax_id_collection`,
`PaymentLink#update.tax_id_collection`, and `PaymentLink.tax_id_collection`

### September 9, 2024

- Add support for new resource `InvoiceRenderingTemplate`
- Add support for `archive`, `list`, `retrieve`, and `unarchive` methods on
resource `InvoiceRenderingTemplate`
- Add support for `template` on
`Customer#create.invoice_settings.rendering_options`,
`Customer#update.invoice_settings.rendering_options`,
`Customer.invoice_settings.rendering_options`, `Invoice#create.rendering`,
`Invoice#update.rendering`, and `Invoice.rendering`
- Add support for `template_version` on `Invoice#create.rendering`,
`Invoice#update.rendering`, and `Invoice.rendering`

### September 5, 2024

- Remove support for resource `Billing.MeterErrorReport`

### September 4, 2024

- Add support for `subscription_item` and `subscription` on
`Billing.Alert#create.filter`
- Change type of `Billing.Alert#create.alert_type`,
`Billing.Alert#list.alert_type`, and `Billing.Alert.alert_type` from
`enum('spend_threshold'|'usage_threshold')` to `literal('usage_threshold')`
- Remove support for `spend_threshold_config` on `Billing.Alert#create` and
`Billing.Alert`
- Change `Terminal.Reader#process_setup_intent.customer_consent_collected` to be
optional

### August 30, 2024

- Change type of `Billing.Alert#create.alert_type`,
`Billing.Alert#list.alert_type`, and `Billing.Alert.alert_type` from
`literal('usage_threshold')` to `enum('spend_threshold'|'usage_threshold')`
- Add support for `spend_threshold_config` on `Billing.Alert#create` and
`Billing.Alert`

### August 29, 2024

- Add support for new resource `Billing.MeterErrorReport`

### August 28, 2024

- Change `AccountLink#create.collection_options.fields` to be optional
- Change `LineItem.description` to be optional
- Add support for `status_details` on `TestHelpers.TestClock`

### August 26, 2024

- Change `Issuing.Card.shipping.address_validation` to be required
- Add support for new value `issuing_regulatory_reporting` on enums
`File#list.purpose` and `File.purpose`
- Add support for new value `issuing_regulatory_reporting` on enum
`File#create.purpose`

### August 21, 2024

- Add support for new value `hr_oib` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`,
`Tax.Calculation.customer_details.tax_ids[].type`,
`Tax.Transaction.customer_details.tax_ids[].type`, and `TaxId.type`
- Add support for new value `hr_oib` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#create_preview.customer_details.tax_ids[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Tax.Calculation#create.customer_details.tax_ids[].type`, and
`TaxId#create.type`

### August 16, 2024

- Remove support for resource `Issuing.DisputeSettlementDetail`
- Remove support for `retrieve` method on resource `DisputeSettlementDetail`

### August 15, 2024

- Add support for new resource `Issuing.DisputeSettlementDetail`
- Add support for `retrieve` method on resource `DisputeSettlementDetail`
- Add support for `wallet` on `Charge.payment_method_details.card_present`,
`ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present`,
`ConfirmationToken.payment_method_preview.card_present`,
`PaymentMethod.card.generated_from.payment_method_details.card_present`, and
`PaymentMethod.card_present`

### August 12, 2024

- Add support for `authorization_code` on `Charge.payment_method_details.card`

### August 9, 2024

- Add support for `chips` on
`Treasury.OutboundPayment.testHelpers#update.tracking_details.us_domestic_wire`,
`Treasury.OutboundPayment.tracking_details.us_domestic_wire`,
`Treasury.OutboundTransfer.testHelpers#update.tracking_details.us_domestic_wire`,
and `Treasury.OutboundTransfer.tracking_details.us_domestic_wire`
- Change type of
`Treasury.OutboundPayment.tracking_details.us_domestic_wire.imad` and
`Treasury.OutboundTransfer.tracking_details.us_domestic_wire.imad` from `string`
to `nullable(string)`
- Add support for `mandate_options` on
`PaymentIntent#confirm.payment_method_options.bacs_debit`,
`PaymentIntent#create.payment_method_options.bacs_debit`,
`PaymentIntent#update.payment_method_options.bacs_debit`, and
`PaymentIntent.payment_method_options.bacs_debit`
- Add support for `bacs_debit` on `SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_options`, and
`SetupIntent.payment_method_options`

### August 8, 2024

- Add support for `type` on
`Charge.payment_method_details.card_present.offline`,
`ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present.offline`,
`ConfirmationToken.payment_method_preview.card_present.offline`,
`PaymentMethod.card.generated_from.payment_method_details.card_present.offline`,
`PaymentMethod.card_present.offline`, and
`SetupAttempt.payment_method_details.card_present.offline`

### August 7, 2024

- Add support for `activate`, `archive`, `create`, `deactivate`, `list`, and
`retrieve` methods on resource `Billing.Alert`
- Add support for new value `invalid_mandate_reference_prefix_format` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Change
`Invoice#create.payment_settings.payment_method_options.card.installments.plan.count`,
`Invoice#create.payment_settings.payment_method_options.card.installments.plan.interval`,
`Invoice#update.payment_settings.payment_method_options.card.installments.plan.count`,
`Invoice#update.payment_settings.payment_method_options.card.installments.plan.interval`,
`PaymentIntent#confirm.payment_method_options.card.installments.plan.count`,
`PaymentIntent#confirm.payment_method_options.card.installments.plan.interval`,
`PaymentIntent#create.payment_method_options.card.installments.plan.count`,
`PaymentIntent#create.payment_method_options.card.installments.plan.interval`,
`PaymentIntent#update.payment_method_options.card.installments.plan.count`, and
`PaymentIntent#update.payment_method_options.card.installments.plan.interval` to
be optional

### August 6, 2024

- Add support for new value `financial_addresses.aba.forwarding` on enums
`Treasury.FinancialAccount.active_features[]`,
`Treasury.FinancialAccount.pending_features[]`, and
`Treasury.FinancialAccount.restricted_features[]`
- Remove support for value `finanical_addresses.aba.forwarding` from enums
`Treasury.FinancialAccount.active_features[]`,
`Treasury.FinancialAccount.pending_features[]`, and
`Treasury.FinancialAccount.restricted_features[]`

### August 5, 2024

- Add support for `offline` on
`ConfirmationToken.payment_method_preview.card_present` and
`PaymentMethod.card_present`
- Add support for new value `finanical_addresses.aba.forwarding` on enums
`Treasury.FinancialAccount.active_features[]`,
`Treasury.FinancialAccount.pending_features[]`, and
`Treasury.FinancialAccount.restricted_features[]`
- Add support for new value `girocard` on enums
`PaymentIntent#confirm.payment_method_options.card.network`,
`PaymentIntent#create.payment_method_options.card.network`,
`PaymentIntent#update.payment_method_options.card.network`,
`PaymentIntent.payment_method_options.card.network`,
`SetupIntent#confirm.payment_method_options.card.network`,
`SetupIntent#create.payment_method_options.card.network`,
`SetupIntent#update.payment_method_options.card.network`,
`SetupIntent.payment_method_options.card.network`,
`Subscription#create.payment_settings.payment_method_options.card.network`,
`Subscription#update.payment_settings.payment_method_options.card.network`, and
`Subscription.payment_settings.payment_method_options.card.network`

### August 2, 2024

- Add support for `related_customer` on `Identity.VerificationSession#create`,
`Identity.VerificationSession#list`, and `Identity.VerificationSession`
- Add support for `retrieve` method on resource `Tax.Calculation`

### July 31, 2024

- Add support for new value `charge_exceeds_transaction_limit` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### July 29, 2024

- Add support for new resources `Billing.AlertTriggered` and `Billing.Alert`
- Add support for new value `billing.alert.triggered` on enum `Event.type`
- Add support for new value `billing.alert.triggered` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### July 25, 2024

- Remove support for `authorization_code` on
`Charge.payment_method_details.card`
- Add support for `tax_registrations` and `tax_settings` on
`AccountSession#create.components` and `AccountSession.components`
- Add support for `update` method on resource `Checkout.Session`

### July 24, 2024

- Add support for `brand_product` on
`Charge.payment_method_details.card_present`,
`ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present`,
`ConfirmationToken.payment_method_preview.card_present`,
`PaymentMethod.card.generated_from.payment_method_details.card_present`, and
`PaymentMethod.card_present`
- Add support for `network_transaction_id` on
`Charge.payment_method_details.card_present`,
`Charge.payment_method_details.interac_present`,
`ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present`,
and `PaymentMethod.card.generated_from.payment_method_details.card_present`

### July 23, 2024

- Add support for `transaction_id` on `Charge.payment_method_details.affirm`
- Add support for `twint` on `PaymentMethodConfiguration#create`,
`PaymentMethodConfiguration#update`, and `PaymentMethodConfiguration`
- Add support for `authorization_code` on `Charge.payment_method_details.card`

### July 22, 2024

- Add support for new values `invoice.overdue` and `invoice.will_be_due` on enum
`Event.type`
- Add support for new values `invoice.overdue` and `invoice.will_be_due` on
enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Add support for `buyer_id` on `Charge.payment_method_details.blik`
- Add support for `case_type` on `Dispute.payment_method_details.card`

### July 17, 2024

- Add support for new value `issuing_dispute.funds_rescinded` on enum
`Event.type`
- Add support for new value `issuing_dispute.funds_rescinded` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Add support for new value `stripe_s700` on enums
`Terminal.Reader#list.device_type` and `Terminal.Reader.device_type`
- Add support for new value `multibanco` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`

### July 12, 2024

- Add support for `customer` on `ConfirmationToken.payment_method_preview`

### July 11, 2024

- Add support for `payment_method_options` on `ConfirmationToken`

### July 9, 2024

- Add support for `payment_element` on `CustomerSession#create.components` and
`CustomerSession.components`
- Change `Plan.meter` and `Price.recurring.meter` to be required

### July 8, 2024

- Remove support for value `payment_intent_fx_quote_invalid` from enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Add support for `address_validation` on `Issuing.Card#create.shipping` and
`Issuing.Card.shipping`
- Add support for `shipping` on `Issuing.Card#update`
- Remove support for values `billing_policy_remote_function_response_invalid`,
`billing_policy_remote_function_timeout`,
`billing_policy_remote_function_unexpected_status_code`, and
`billing_policy_remote_function_unreachable` from enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### July 5, 2024

- Add support for `posted_at` on `Tax.Transaction#create_from_calculation` and
`Tax.Transaction`

### July 3, 2024

- Add support for new value `payment_intent_fx_quote_invalid` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### July 2, 2024

- Add support for `add_lines`, `remove_lines`, and `update_lines` methods on
resource `Invoice`

### June 27, 2024

- Add support for `filters` on
`Checkout.Session.payment_method_options.us_bank_account.financial_connections`,
`Invoice#create.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`Invoice#update.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`Invoice.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent#confirm.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent#create.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent#update.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent#confirm.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent#create.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent#update.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent.payment_method_options.us_bank_account.financial_connections`,
`Subscription#create.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`Subscription#update.payment_settings.payment_method_options.us_bank_account.financial_connections`,
and
`Subscription.payment_settings.payment_method_options.us_bank_account.financial_connections`
- Add support for `account_subcategories` on
`FinancialConnections.Session#create.filters` and
`FinancialConnections.Session.filters`

### June 26, 2024

- Add support for new values `multibanco` and `twint` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`

### June 25, 2024

- Add support for `email_type` on `CreditNote#create`,
`CreditNote#preview_lines`, and `CreditNote#preview`
- Add support for `reboot_window` on `Terminal.Configuration#create`,
`Terminal.Configuration#update`, and `Terminal.Configuration`
- Add support for new value `zip` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`

### June 24, 2024

- Add support for new value `ch_uid` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`,
`Tax.Calculation.customer_details.tax_ids[].type`,
`Tax.Transaction.customer_details.tax_ids[].type`, and `TaxId.type`
- Add support for new value `ch_uid` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#create_preview.customer_details.tax_ids[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Tax.Calculation#create.customer_details.tax_ids[].type`, and
`TaxId#create.type`

### June 21, 2024

- Add support for `finalize_amount` test helper method on resource
`Issuing.Authorization`
- Add support for `fleet` on
`Issuing.Authorization.testHelpers#capture.purchase_details`,
`Issuing.Authorization.testHelpers#create`, `Issuing.Authorization`,
`Issuing.Transaction.purchase_details`,
`Issuing.Transaction.testHelpers#create_force_capture.purchase_details`, and
`Issuing.Transaction.testHelpers#create_unlinked_refund.purchase_details`
- Add support for `fuel` on `Issuing.Authorization.testHelpers#create` and
`Issuing.Authorization`
- Add support for `industry_product_code` on
`Issuing.Authorization.testHelpers#capture.purchase_details.fuel`,
`Issuing.Transaction.purchase_details.fuel`,
`Issuing.Transaction.testHelpers#create_force_capture.purchase_details.fuel`,
and
`Issuing.Transaction.testHelpers#create_unlinked_refund.purchase_details.fuel`
- Add support for new values `card_canceled`, `card_expired`,
`cardholder_blocked`, `insecure_authorization_method`, and `pin_blocked` on enum
`Issuing.Authorization.request_history[].reason`

### June 18, 2024

- Add support for new value `2024-06-20` on enum
`WebhookEndpoint#create.api_version`
- Add support for new values `charging_minute`, `imperial_gallon`, `kilogram`,
`kilowatt_hour`, and `pound` on enums
`Issuing.Authorization.testHelpers#capture.purchase_details.fuel.unit`,
`Issuing.Transaction.testHelpers#create_force_capture.purchase_details.fuel.unit`,
and
`Issuing.Transaction.testHelpers#create_unlinked_refund.purchase_details.fuel.unit`
- Add support for `quantity_decimal` on
`Issuing.Authorization.testHelpers#capture.purchase_details.fuel`,
`Issuing.Transaction.purchase_details.fuel`,
`Issuing.Transaction.testHelpers#create_force_capture.purchase_details.fuel`,
and
`Issuing.Transaction.testHelpers#create_unlinked_refund.purchase_details.fuel`
- Remove support for `volume_decimal` on
`Issuing.Authorization.testHelpers#capture.purchase_details.fuel`,
`Issuing.Transaction.purchase_details.fuel`,
`Issuing.Transaction.testHelpers#create_force_capture.purchase_details.fuel`,
and
`Issuing.Transaction.testHelpers#create_unlinked_refund.purchase_details.fuel`

### June 15, 2024

- Add support for new value `mobilepay` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`

### June 14, 2024

- Add support for `tax_id_collection` on `PaymentLink#update`

### June 11, 2024

- Add support for `twint_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `twint` on `Charge.payment_method_details`,
`ConfirmationToken.payment_method_preview`,
`ConfirmationToken.testHelpers#create.payment_method_data`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `twint` on enums
`Checkout.Session#create.payment_method_types[]`,
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`
- Add support for new value `twint` on enums
`ConfirmationToken.testHelpers#create.payment_method_data.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `twint` on enums
`ConfirmationToken.payment_method_preview.type` and `PaymentMethod.type`

### June 10, 2024

- Add support for `multibanco_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `multibanco` on
`Checkout.Session#create.payment_method_options`,
`Checkout.Session.payment_method_options`,
`ConfirmationToken.payment_method_preview`,
`ConfirmationToken.testHelpers#create.payment_method_data`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethodConfiguration#create`, `PaymentMethodConfiguration#update`,
`PaymentMethodConfiguration`, `PaymentMethod`, `Refund.destination_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `multibanco` on enums
`Checkout.Session#create.payment_method_types[]`,
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`
- Add support for new value `multibanco` on enums
`ConfirmationToken.testHelpers#create.payment_method_data.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `multibanco` on enums
`ConfirmationToken.payment_method_preview.type` and `PaymentMethod.type`
- Add support for `multibanco_display_details` on `PaymentIntent.next_action`

### June 7, 2024

- Add support for new value `de_stn` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`,
`Tax.Calculation.customer_details.tax_ids[].type`,
`Tax.Transaction.customer_details.tax_ids[].type`, and `TaxId.type`
- Add support for new value `de_stn` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#create_preview.customer_details.tax_ids[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Tax.Calculation#create.customer_details.tax_ids[].type`, and
`TaxId#create.type`

### June 6, 2024

- Add support for new value `swish` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for `invoice_settings` on `Subscription`

### June 4, 2024

- Remove support for resource `PlatformTaxFee`

### June 3, 2024

- Add support for `gb_bank_transfer_payments`, `jp_bank_transfer_payments`,
`mx_bank_transfer_payments`, `sepa_bank_transfer_payments`, and
`us_bank_transfer_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`

### May 30, 2024

- Add support for `generated_from` on
`ConfirmationToken.payment_method_preview.card` and `PaymentMethod.card`
- Add support for new value
`verification_requires_additional_proof_of_registration` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`BankAccount.future_requirements.errors[].code`, and
`BankAccount.requirements.errors[].code`

### May 29, 2024

- Add support for new values `issuing_personalization_design.activated`,
`issuing_personalization_design.deactivated`,
`issuing_personalization_design.rejected`, and
`issuing_personalization_design.updated` on enum `Event.type`
- Change `Issuing.Card.personalization_design` and
`Issuing.PhysicalBundle.features` to be required
- Add support for new values `issuing_personalization_design.activated`,
`issuing_personalization_design.deactivated`,
`issuing_personalization_design.rejected`, and
`issuing_personalization_design.updated` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### May 28, 2024

- Add support for `default_value` on
`Checkout.Session#create.custom_fields[].dropdown`,
`Checkout.Session#create.custom_fields[].numeric`,
`Checkout.Session#create.custom_fields[].text`,
`Checkout.Session.custom_fields[].dropdown`,
`Checkout.Session.custom_fields[].numeric`, and
`Checkout.Session.custom_fields[].text`

### May 25, 2024

- Add support for new values `en-RO` and `ro-RO` on enums
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`

### May 22, 2024

- Add support for `external_account_collection` on
`AccountSession#create.components.balances.features`,
`AccountSession#create.components.payouts.features`,
`AccountSession.components.balances.features`, and
`AccountSession.components.payouts.features`
- Add support for `payment_method_remove` on
`Checkout.Session.saved_payment_method_options`

### May 17, 2024

- Add support for new value `terminal_reader_invalid_location_for_payment` on
enums `Invoice.last_finalization_error.code`,
`PaymentIntent.last_payment_error.code`, `SetupAttempt.setup_error.code`,
`SetupIntent.last_setup_error.code`, and `StripeError.code`

### May 15, 2024

- Add support for `routing` on
`PaymentIntent#confirm.payment_method_options.card_present`,
`PaymentIntent#create.payment_method_options.card_present`,
`PaymentIntent#update.payment_method_options.card_present`, and
`PaymentIntent.payment_method_options.card_present`

### May 14, 2024

- Add support for `stripe_s700` on `Terminal.Configuration#create`,
`Terminal.Configuration#update`, and `Terminal.Configuration`
- Add support for `loss_reason` on `Issuing.Dispute`
- Add support for `fee_source` on `ApplicationFee`
- Add support for `net_available` on `Balance.instant_available[]`
- Add support for `application_fee_amount` and `application_fee` on `Payout`

### May 13, 2024

- Add support for `klarna` on `Dispute.payment_method_details`
- Add support for new value `klarna` on enum
`Dispute.payment_method_details.type`
- Remove support for `kr_market` on `Charge.payment_method_details`,
`ConfirmationToken.payment_method_preview`,
`ConfirmationToken.testHelpers#create.payment_method_data`,
`Mandate.payment_method_details`, `PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`, `SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Remove support for value `kr_market` from enums
`ConfirmationToken.testHelpers#create.payment_method_data.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Remove support for value `kr_market` from enums
`ConfirmationToken.payment_method_preview.type` and `PaymentMethod.type`
- Remove support for value `kr_market` from enums
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`
- Add support for `kr_market` on `Charge.payment_method_details`,
`ConfirmationToken.payment_method_preview`,
`ConfirmationToken.testHelpers#create.payment_method_data`,
`Mandate.payment_method_details`, `PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`, `SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `kr_market` on enums
`ConfirmationToken.testHelpers#create.payment_method_data.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `kr_market` on enums
`ConfirmationToken.payment_method_preview.type` and `PaymentMethod.type`
- Add support for new value `kr_market` on enums
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`

### May 10, 2024

- Add support for `archived` and `lookup_key` on `Entitlements.Feature#list`
- Change `Treasury.OutboundPayment.tracking_details` and
`Treasury.OutboundTransfer.tracking_details` to be required

### May 9, 2024

- Add support for `preferred_locales` on
`Charge.payment_method_details.card_present`,
`ConfirmationToken.payment_method_preview.card_present`, and
`PaymentMethod.card_present`
- Add support for `no_valid_authorization` on `Issuing.Dispute#create.evidence`,
`Issuing.Dispute#update.evidence`, and `Issuing.Dispute.evidence`
- Add support for new value `no_valid_authorization` on enums
`Issuing.Dispute#create.evidence.reason`,
`Issuing.Dispute#update.evidence.reason`, and `Issuing.Dispute.evidence.reason`
- Change `FinancialConnections.Session#create.filters.countries` to be optional
- Remove support for `pending_invoice_items_behavior` on `Subscription#create`

### May 8, 2024

- Add support for `preview_mode` on `Invoice#create_preview`,
`Invoice#upcomingLines`, and `Invoice#upcoming`

### May 7, 2024

- Add support for `pending_invoice_items_behavior` on `Subscription#create`

### May 6, 2024

- Add support for `allow_redisplay` on
`ConfirmationToken.payment_method_preview` and `PaymentMethod`
- Add support for `update` test helper method on resources
`Treasury.OutboundPayment` and `Treasury.OutboundTransfer`
- Add support for new values
`treasury.outbound_payment.tracking_details_updated` and
`treasury.outbound_transfer.tracking_details_updated` on enum `Event.type`
- Add support for `tracking_details` on `Treasury.OutboundPayment` and
`Treasury.OutboundTransfer`
- Add support for new values
`treasury.outbound_payment.tracking_details_updated` and
`treasury.outbound_transfer.tracking_details_updated` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### May 2, 2024

- Change type of `Entitlements.Feature#update.metadata` from `map(string:
string)` to `emptyable(map(string: string))`
- Add support for `paypal` on `Dispute.payment_method_details`
- Change type of `Dispute.payment_method_details.type` from `literal('card')` to
`enum('card'|'paypal')`

### May 1, 2024

- Add support for `bh`, `eg`, `ge`, `ke`, `kz`, `ng`, and `om` on
`Tax.Registration#create.country_options` and `Tax.Registration.country_options`

### April 29, 2024

- Add support for `payment_method_types` on `PaymentIntent#confirm`

### April 26, 2024

- Change `Apps.Secret.payload`,
`BillingPortal.Configuration.features.subscription_update.products`,
`Charge.refunds`, `ConfirmationToken.payment_method_preview.klarna.dob`,
`Identity.VerificationReport.document.dob`,
`Identity.VerificationReport.document.expiration_date`,
`Identity.VerificationReport.document.number`,
`Identity.VerificationReport.id_number.dob`,
`Identity.VerificationReport.id_number.id_number`,
`Identity.VerificationSession.provided_details`,
`Identity.VerificationSession.verified_outputs.dob`,
`Identity.VerificationSession.verified_outputs.id_number`,
`Identity.VerificationSession.verified_outputs`,
`Issuing.Dispute.balance_transactions`, `Issuing.Transaction.purchase_details`,
`PaymentMethod.klarna.dob`, `Tax.Calculation.line_items`,
`Tax.CalculationLineItem.tax_breakdown`, `Tax.Transaction.line_items`,
`Treasury.FinancialAccount.financial_addresses[].aba.account_number`,
`Treasury.ReceivedCredit.linked_flows.source_flow_details`,
`Treasury.Transaction.entries`, `Treasury.Transaction.flow_details`, and
`Treasury.TransactionEntry.flow_details` to be optional
- Add support for new value `shipping_address_invalid` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Add support for `ship_from_details` on `Tax.Calculation#create`,
`Tax.Calculation`, and `Tax.Transaction`

### April 25, 2024

- Add support for `mobilepay` on `PaymentMethodConfiguration#create`,
`PaymentMethodConfiguration#update`, and `PaymentMethodConfiguration`

### April 24, 2024

- Add support for `setup_future_usage` on
`Checkout.Session.payment_method_options.amazon_pay`,
`Checkout.Session.payment_method_options.revolut_pay`,
`PaymentIntent.payment_method_options.amazon_pay`, and
`PaymentIntent.payment_method_options.revolut_pay`
- Add support for new values `amazon_pay` and `revolut_pay` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for `amazon_pay` and `revolut_pay` on
`Mandate.payment_method_details` and `SetupAttempt.payment_method_details`

### April 23, 2024

- Change type of `Entitlements.ActiveEntitlement.feature` from `string` to
`expandable($Entitlements.Feature)`

### April 22, 2024

- Remove support for `email` and `phone` on
`Identity.VerificationSession#create.options` and
`Identity.VerificationSession#update.options`
- Change `Identity.VerificationSession.provided_details`,
`Identity.VerificationSession.verified_outputs.email`, and
`Identity.VerificationSession.verified_outputs.phone` to be required

### April 19, 2024

- Add support for `ending_before`, `limit`, and `starting_after` on
`PaymentMethodConfiguration#list`

### April 18, 2024

- Add support for `mobilepay` on
`Checkout.Session#create.payment_method_options` and
`Checkout.Session.payment_method_options`
- Add support for new value `mobilepay` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for `create_preview` method on resource `Invoice`
- Add support for `schedule_details` and `subscription_details` on
`Invoice#upcomingLines` and `Invoice#upcoming`

### April 17, 2024

- Add support for new value `other` on enums
`Issuing.Authorization.testHelpers#capture.purchase_details.fuel.unit`,
`Issuing.Transaction.testHelpers#create_force_capture.purchase_details.fuel.unit`,
and
`Issuing.Transaction.testHelpers#create_unlinked_refund.purchase_details.fuel.unit`
- Add support for `payment_method_data` on `Checkout.Session#create`
- Add support for `saved_payment_method_options` on `Checkout.Session#create`
and `Checkout.Session`
- Add support for `allow_redisplay` on
`ConfirmationToken.testHelpers#create.payment_method_data`,
`Customer#list_payment_methods`, `PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#update.payment_method_data`, `PaymentMethod#create`,
`PaymentMethod#update`, `SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`

### April 15, 2024

- Remove support for `config` on `Forwarding.Request#create` and
`Forwarding.Request`
- Add support for `balances` and `payouts_list` on
`AccountSession#create.components` and `AccountSession.components`
- Change
`AccountSession.components.payment_details.features.destination_on_behalf_of_charge_management`
and
`AccountSession.components.payments.features.destination_on_behalf_of_charge_management`
to be required
- Add support for `swish` on `PaymentMethodConfiguration#create`,
`PaymentMethodConfiguration#update`, and `PaymentMethodConfiguration`
- Change type of `Dispute.payment_method_details.card` from
`nullable(DisputePaymentMethodDetailsCard)` to `DisputePaymentMethodDetailsCard`
- Change `Dispute.payment_method_details.card` to be optional

### April 13, 2024

- Change `Billing.MeterEvent#create.timestamp` to be optional
- Add support for new resource `Entitlements.ActiveEntitlementSummary`
- Add support for new value `entitlements.active_entitlement_summary.updated` on
enum `Event.type`
- Add support for new value `entitlements.active_entitlement_summary.updated` on
enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### April 11, 2024

- Add support for `capture_method` on
`PaymentIntent#confirm.payment_method_options.revolut_pay`,
`PaymentIntent#create.payment_method_options.revolut_pay`,
`PaymentIntent#update.payment_method_options.revolut_pay`, and
`PaymentIntent.payment_method_options.revolut_pay`
- Add support for `account_management` and `notification_banner` on
`AccountSession#create.components` and `AccountSession.components`
- Add support for `amazon_pay` on `Charge.payment_method_details`,
`Checkout.Session#create.payment_method_options`,
`Checkout.Session.payment_method_options`,
`ConfirmationToken.payment_method_preview`,
`ConfirmationToken.testHelpers#create.payment_method_data`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethodConfiguration#create`, `PaymentMethodConfiguration#update`,
`PaymentMethodConfiguration`, `PaymentMethod`, `Refund.destination_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_data`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_data`,
`SetupIntent#update.payment_method_options`, and
`SetupIntent.payment_method_options`
- Add support for new value `amazon_pay` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for new value `amazon_pay` on enums
`ConfirmationToken.testHelpers#create.payment_method_data.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `amazon_pay` on enums
`ConfirmationToken.payment_method_preview.type` and `PaymentMethod.type`
- Add support for new value `amazon_pay` on enums
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`
- Add support for new value `ownership` on enums
`Checkout.Session#create.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Checkout.Session.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Invoice#create.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Invoice#update.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Invoice.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent#confirm.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent#create.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent#update.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent#confirm.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent#create.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent#update.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Subscription#create.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Subscription#update.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
and
`Subscription.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`
- Add support for `next_refresh_available_at` on
`FinancialConnections.Account.ownership_refresh`
- Add support for new value `ownership` on enums
`Invoice.payment_settings.payment_method_options.us_bank_account.financial_connections.permissions[]`
and
`Subscription.payment_settings.payment_method_options.us_bank_account.financial_connections.permissions[]`
- Change `Billing.MeterEventAdjustment#create.cancel.identifier` and
`Billing.MeterEventAdjustment#create.cancel` to be optional
- Change `Billing.MeterEventAdjustment#create.type` to be required
- Change type of `Billing.MeterEventAdjustment.cancel` from
`BillingMeterResourceBillingMeterEventAdjustmentCancel` to
`nullable(BillingMeterResourceBillingMeterEventAdjustmentCancel)`
- Add support for new values `billing_policy_remote_function_response_invalid`,
`billing_policy_remote_function_timeout`,
`billing_policy_remote_function_unexpected_status_code`, and
`billing_policy_remote_function_unreachable` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Add support for `external_account_collection` on
`AccountSession#create.components.account_onboarding.features` and
`AccountSession.components.account_onboarding.features`
- Add support for new values `bh_vat`, `kz_bin`, `ng_tin`, and `om_vat` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`,
`Tax.Calculation.customer_details.tax_ids[].type`,
`Tax.Transaction.customer_details.tax_ids[].type`, and `TaxId.type`
- Add support for new values `bh_vat`, `kz_bin`, `ng_tin`, and `om_vat` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Tax.Calculation#create.customer_details.tax_ids[].type`, and
`TaxId#create.type`

### April 9, 2024

- Add support for `marketing_features` on `Product#create`, `Product#update`,
and `Product`
- Remove support for `features` on `Product#create`, `Product#update`, and
`Product`
- Add support for new resources `Entitlements.ActiveEntitlement` and
`Entitlements.Feature`
- Add support for `list` and `retrieve` methods on resource `ActiveEntitlement`
- Add support for `create`, `list`, `retrieve`, and `update` methods on resource
`Feature`

### April 8, 2024

- Remove support for `rendering_options` on `Invoice#create`, `Invoice#update`,
and `Invoice`
- Add support for `controller` on `Account#create`
- Add support for `fees`, `losses`, `requirement_collection`, and
`stripe_dashboard` on `Account.controller`
- Add support for new value `none` on enum `Account.type`

### April 5, 2024

- Add support for new value `2024-04-10` on enum
`WebhookEndpoint#create.api_version`
- Add support for `event_name` on `Billing.MeterEventAdjustment#create` and
`Billing.MeterEventAdjustment`
- Add support for `cancel` and `type` on `Billing.MeterEventAdjustment`

### April 4, 2024

- Add support for new value `mobile_phone_reader` on enums
`Terminal.Reader#list.device_type` and `Terminal.Reader.device_type`
- Add support for `promotion_code` on `Quote#create.discounts[]`,
`Quote#create.line_items[].discounts[]`, `Quote#update.discounts[]`, and
`Quote#update.line_items[].discounts[]`

### April 3, 2024

- Add support for `offline` on
`SetupAttempt.payment_method_details.card_present`
- Add support for `card_present` on
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_options`, and
`SetupIntent.payment_method_options`
- Add support for `email` and `phone` on `Identity.VerificationReport`,
`Identity.VerificationSession#create.options`,
`Identity.VerificationSession#update.options`,
`Identity.VerificationSession.options`, and
`Identity.VerificationSession.verified_outputs`
- Add support for `verification_flow` on `Identity.VerificationReport`,
`Identity.VerificationSession#create`, and `Identity.VerificationSession`
- Add support for new value `verification_flow` on enums
`Identity.VerificationReport.type` and `Identity.VerificationSession.type`
- Add support for `provided_details` on `Identity.VerificationSession#create`,
`Identity.VerificationSession#update`, and `Identity.VerificationSession`
- Change `Identity.VerificationSession#create.type` to be optional
- Add support for new values `email_unverified_other`,
`email_verification_declined`, `phone_unverified_other`, and
`phone_verification_declined` on enum
`Identity.VerificationSession.last_error.code`
- Add support for `zip` on `PaymentMethodConfiguration#create`,
`PaymentMethodConfiguration#update`, and `PaymentMethodConfiguration`
- Add support for `subscription_item` on `Discount`
- Add support for `discounts` on `Invoice#upcoming.subscription_items[]`,
`Invoice#upcomingLines.subscription_items[]`, `Quote#create.line_items[]`,
`Quote#update.line_items[]`, `Subscription#create.add_invoice_items[]`,
`Subscription#create.items[]`, `Subscription#create`,
`Subscription#update.add_invoice_items[]`, `Subscription#update.items[]`,
`Subscription#update`, `SubscriptionItem#create`, `SubscriptionItem#update`,
`SubscriptionItem`, `SubscriptionSchedule#create.phases[].add_invoice_items[]`,
`SubscriptionSchedule#create.phases[].items[]`,
`SubscriptionSchedule#create.phases[]`,
`SubscriptionSchedule#update.phases[].add_invoice_items[]`,
`SubscriptionSchedule#update.phases[].items[]`,
`SubscriptionSchedule#update.phases[]`,
`SubscriptionSchedule.phases[].add_invoice_items[]`,
`SubscriptionSchedule.phases[].items[]`, `SubscriptionSchedule.phases[]`, and
`Subscription`
- Change type of `Invoice.discounts` from
`nullable(array(expandable(deletable($Discount))))` to
`array(expandable(deletable($Discount)))`

### April 2, 2024

- Remove support for value `2024-04-03` from enum
`WebhookEndpoint#create.api_version`
- Add support for `promotion_code` on `Invoice#create.discounts[]`,
`Invoice#update.discounts[]`, `InvoiceItem#create.discounts[]`, and
`InvoiceItem#update.discounts[]`
- Change type of
`Checkout.Session#create.payment_method_options.swish.reference` from
`emptyStringable(string)` to `string`
- Change
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.hosted_instructions_url`,
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.mobile_auth_url`,
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code.data`,
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code.image_url_png`,
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code.image_url_svg`,
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code`,
and `PaymentIntent.payment_method_options.swish.reference` to be required

### April 1, 2024

- Add support for `allowed_merchant_countries` and `blocked_merchant_countries`
on `Issuing.Card#create.spending_controls`,
`Issuing.Card#update.spending_controls`, `Issuing.Card.spending_controls`,
`Issuing.Cardholder#create.spending_controls`,
`Issuing.Cardholder#update.spending_controls`, and
`Issuing.Cardholder.spending_controls`

### March 29, 2024

- Remove support for `subscription_pause` on
`BillingPortal.Configuration#create.features`,
`BillingPortal.Configuration#update.features`, and
`BillingPortal.Configuration.features`
- Change `Charge.payment_method_details.us_bank_account.payment_reference` to be
required

### March 28, 2024

- Add support for new value `2024-04-03` on enum
`WebhookEndpoint#create.api_version`
- Add support for new value `verification_failed_representative_authority` on
enums `Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`BankAccount.future_requirements.errors[].code`, and
`BankAccount.requirements.errors[].code`

### March 26, 2024

- Add support for new resources `Billing.MeterEventAdjustment`,
`Billing.MeterEvent`, and `Billing.Meter`
- Add support for `create`, `deactivate`, `list`, `reactivate`, `retrieve`, and
`update` methods on resource `Meter`
- Add support for `create` method on resources `MeterEventAdjustment` and
`MeterEvent`
- Add support for `meter` on `Plan#create`, `Plan`, `Price#create.recurring`,
`Price#list.recurring`, and `Price.recurring`

### March 25, 2024

- Add support for `amazon_pay_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `destination_on_behalf_of_charge_management` on
`AccountSession#create.components.payment_details.features`,
`AccountSession#create.components.payments.features`,
`AccountSession.components.payment_details.features`, and
`AccountSession.components.payments.features`
- Add support for `second_line` on `Issuing.Card#create`

### March 21, 2024

- Add support for `mandate` on `Charge.payment_method_details.us_bank_account`,
`Treasury.InboundTransfer.origin_payment_method_details.us_bank_account`,
`Treasury.OutboundPayment.destination_payment_method_details.us_bank_account`,
and
`Treasury.OutboundTransfer.destination_payment_method_details.us_bank_account`
- Add support for `mobilepay` on `Charge.payment_method_details`,
`ConfirmationToken.payment_method_preview`,
`ConfirmationToken.testHelpers#create.payment_method_data`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `mobilepay` on enums
`ConfirmationToken.testHelpers#create.payment_method_data.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `mobilepay` on enums
`ConfirmationToken.payment_method_preview.type` and `PaymentMethod.type`
- Add support for new value `mobilepay` on enums
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`
- Add support for new values `forwarding_api_inactive`,
`forwarding_api_invalid_parameter`, `forwarding_api_upstream_connection_error`,
and `forwarding_api_upstream_connection_timeout` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### March 20, 2024

- Add support for `payment_reference` on
`Charge.payment_method_details.us_bank_account`
- Add support for new resource `Forwarding.Request`
- Add support for `create`, `list`, and `retrieve` methods on resource `Request`
- Add support for new resource `ConfirmationToken`
- Add support for `retrieve` method on resource `ConfirmationToken`
- Add support for `confirmation_token` on `PaymentIntent#confirm`,
`PaymentIntent#create`, `SetupIntent#confirm`, and `SetupIntent#create`
- Add support for `mobilepay_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`

### March 18, 2024

- Add support for `name` on `Terminal.Configuration#create`,
`Terminal.Configuration#update`, and `Terminal.Configuration`
- Add support for `payout` on `Treasury.ReceivedDebit.linked_flows`

### March 13, 2024

- Add support for `sepa_debit` on
`Subscription#create.payment_settings.payment_method_options`,
`Subscription#update.payment_settings.payment_method_options`, and
`Subscription.payment_settings.payment_method_options`
- Add support for `second_line` on `Issuing.PhysicalBundle.features`

### March 12, 2024

- Change type of `Subscription#create.application_fee_percent` and
`Subscription#update.application_fee_percent` from `number` to
`emptyStringable(number)`

### March 8, 2024

- Add support for new resources `Issuing.PersonalizationDesign` and
`Issuing.PhysicalBundle`
- Add support for `create`, `list`, `retrieve`, and `update` methods on resource
`PersonalizationDesign`
- Add support for `list` and `retrieve` methods on resource `PhysicalBundle`
- Add support for `personalization_design` on `Issuing.Card#create`,
`Issuing.Card#list`, `Issuing.Card#update`, and `Issuing.Card`

### March 7, 2024

- Add support for `documents` on `AccountSession.components`
- Add support for `sepa_debit` on
`Invoice#create.payment_settings.payment_method_options`,
`Invoice#update.payment_settings.payment_method_options`, and
`Invoice.payment_settings.payment_method_options`

### March 5, 2024

- Add support for `documents` on `AccountSession#create.components`

### March 4, 2024

- Add support for `created` on `CreditNote#list`
- Add support for `request_three_d_secure` on
`Checkout.Session#create.payment_method_options.card` and
`Checkout.Session.payment_method_options.card`

### February 29, 2024

- Add support for `payment_method` on `Token#create.bank_account`

### February 27, 2024

- Change `Identity.VerificationReport.type` to be required
- Change type of `Identity.VerificationSession.type` from
`nullable(enum('document'|'id_number'))` to `enum('document'|'id_number')`
- Add support for `enable_customer_cancellation` on
`Terminal.Reader#process_payment_intent.process_config`,
`Terminal.Reader#process_setup_intent.process_config`,
`Terminal.Reader.action.process_payment_intent.process_config`, and
`Terminal.Reader.action.process_setup_intent.process_config`
- Add support for `refund_payment_config` on `Terminal.Reader#refund_payment`
and `Terminal.Reader.action.refund_payment`

### February 26, 2024

- Change
`SubscriptionSchedule.default_settings.invoice_settings.account_tax_ids`,
`SubscriptionSchedule.phases[].invoice_settings.account_tax_ids`, and
`TaxId.owner` to be required
- Add support for `number` on `Invoice#create` and `Invoice#update`

### February 22, 2024

- Add support for `client_reference_id` on `Identity.VerificationReport#list`,
`Identity.VerificationReport`, `Identity.VerificationSession#create`,
`Identity.VerificationSession#list`, and `Identity.VerificationSession`

### February 21, 2024

- Add support for `created` on `Treasury.OutboundPayment#list`
- Remove support for value `include_and_require` from enum
`Invoice#create.pending_invoice_items_behavior`

### February 16, 2024

- Remove support for value `service_tax` from enums `TaxRate#create.tax_type`,
`TaxRate#update.tax_type`, and `TaxRate.tax_type`

### February 14, 2024

- Change `PaymentMethod.card.display_brand` to be required
- Add support for new value `no_voec` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`,
`Tax.Calculation.customer_details.tax_ids[].type`,
`Tax.Transaction.customer_details.tax_ids[].type`, and `TaxId.type`
- Add support for new value `no_voec` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Tax.Calculation#create.customer_details.tax_ids[].type`, and
`TaxId#create.type`

### February 13, 2024

- Add support for `networks` on `Card`, `PaymentMethod#create.card[0]`,
`PaymentMethod#update.card`, and `Token#create.card[0]`
- Add support for `display_brand` on `PaymentMethod.card`

### February 9, 2024

- Add support for new value `financial_connections.account.refreshed_ownership`
on enum `Event.type`
- Add support for new value `financial_connections.account.refreshed_ownership`
on enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Add support for `mobile_auth_url` on
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code`
- Remove support for `mobile_auth_url` on
`PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code`

### February 8, 2024

- Add support for new value `velobank` on enums
`Charge.payment_method_details.p24.bank`,
`PaymentIntent#confirm.payment_method_data.p24.bank`,
`PaymentIntent#create.payment_method_data.p24.bank`,
`PaymentIntent#update.payment_method_data.p24.bank`,
`PaymentMethod#create.p24.bank`, `PaymentMethod.p24.bank`,
`SetupIntent#confirm.payment_method_data.p24.bank`,
`SetupIntent#create.payment_method_data.p24.bank`, and
`SetupIntent#update.payment_method_data.p24.bank`

### February 7, 2024

- Add support for `setup_future_usage` on
`PaymentIntent#confirm.payment_method_options.blik`,
`PaymentIntent#create.payment_method_options.blik`,
`PaymentIntent#update.payment_method_options.blik`, and
`PaymentIntent.payment_method_options.blik`

### February 6, 2024

- Add support for `require_cvc_recollection` on
`PaymentIntent#confirm.payment_method_options.card`,
`PaymentIntent#create.payment_method_options.card`,
`PaymentIntent#update.payment_method_options.card`, and
`PaymentIntent.payment_method_options.card`

### February 1, 2024

- Add support for new resource `TaxId`
- Add support for `create`, `delete`, `list`, and `retrieve` methods on resource
`TaxId`
- Add support for `invoices` on `Account#update.settings` and `Account.settings`
- Add support for `account_tax_ids` on `Subscription#create.invoice_settings`,
`Subscription#update.invoice_settings`,
`SubscriptionSchedule#create.default_settings.invoice_settings`,
`SubscriptionSchedule#create.phases[].invoice_settings`,
`SubscriptionSchedule#update.default_settings.invoice_settings`,
`SubscriptionSchedule#update.phases[].invoice_settings`,
`SubscriptionSchedule.default_settings.invoice_settings`, and
`SubscriptionSchedule.phases[].invoice_settings`
- Add support for `swish_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `swish` on `Charge.payment_method_details`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`Refund.destination_details`, `SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `swish` on enums
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`
- Add support for new value `swish` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for `swish_handle_redirect_or_display_qr_code` on
`PaymentIntent.next_action`
- Add support for new value `swish` on enum `PaymentMethod.type`
- Add support for `relationship` on `Account#create.individual`,
`Account#update.individual`, and `Token#create.account.individual`

### January 31, 2024

- Change type of `Terminal.Reader.status` from `string` to
`enum('offline'|'online')`

### January 30, 2024

- Add support for `swish` on `Checkout.Session#create.payment_method_options`
and `Checkout.Session.payment_method_options`
- Add support for new value `swish` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for new value `swish` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`

### January 29, 2024

- Add support for `jurisdiction_level` on `TaxRate`

### January 24, 2024

- Add support for `liability` on `Quote#create.automatic_tax`,
`Quote#update.automatic_tax`, and `Quote.automatic_tax`
- Add support for `issuer` on `Quote#create.invoice_settings`,
`Quote#update.invoice_settings`, and `Quote.invoice_settings`
- Add support for `liability` on `PaymentLink#create.automatic_tax`,
`PaymentLink#update.automatic_tax`, and `PaymentLink.automatic_tax`
- Add support for `issuer` on
`PaymentLink#create.invoice_creation.invoice_data`,
`PaymentLink#update.invoice_creation.invoice_data`, and
`PaymentLink.invoice_creation.invoice_data`
- Add support for `invoice_settings` on `PaymentLink#create.subscription_data`,
`PaymentLink#update.subscription_data`, and `PaymentLink.subscription_data`

### January 23, 2024

- Add support for `account_type` on `PaymentMethod#update.us_bank_account`
- Add support for `annual_revenue` and `estimated_worker_count` on
`Account#create.business_profile`, `Account#update.business_profile`, and
`Account.business_profile`
- Add support for `liability` on
`SubscriptionSchedule#create.default_settings.automatic_tax`,
`SubscriptionSchedule#create.phases[].automatic_tax`,
`SubscriptionSchedule#update.default_settings.automatic_tax`,
`SubscriptionSchedule#update.phases[].automatic_tax`,
`SubscriptionSchedule.default_settings.automatic_tax`, and
`SubscriptionSchedule.phases[].automatic_tax`
- Add support for `issuer` on
`SubscriptionSchedule#create.default_settings.invoice_settings`,
`SubscriptionSchedule#create.phases[].invoice_settings`,
`SubscriptionSchedule#update.default_settings.invoice_settings`,
`SubscriptionSchedule#update.phases[].invoice_settings`,
`SubscriptionSchedule.default_settings.invoice_settings`, and
`SubscriptionSchedule.phases[].invoice_settings`
- Add support for `liability` on `Checkout.Session#create.automatic_tax` and
`Checkout.Session.automatic_tax`
- Add support for `issuer` on
`Checkout.Session#create.invoice_creation.invoice_data` and
`Checkout.Session.invoice_creation.invoice_data`
- Add support for `invoice_settings` on
`Checkout.Session#create.subscription_data`
- Add support for new value `registered_charity` on enums
`Account#create.company.structure`, `Account#update.company.structure`,
`Account.company.structure`, and `Token#create.account.company.structure`

### January 22, 2024

- Add support for `collection_options` on `AccountLink#create`
- Add support for new value `challenge` on enums
`Invoice#create.payment_settings.payment_method_options.card.request_three_d_secure`,
`Invoice#update.payment_settings.payment_method_options.card.request_three_d_secure`,
`Invoice.payment_settings.payment_method_options.card.request_three_d_secure`,
`Subscription#create.payment_settings.payment_method_options.card.request_three_d_secure`,
`Subscription#update.payment_settings.payment_method_options.card.request_three_d_secure`,
and
`Subscription.payment_settings.payment_method_options.card.request_three_d_secure`
- Add support for `promotion_code` on `Invoice#upcoming.discounts[]`,
`Invoice#upcoming.invoice_items[].discounts[]`,
`Invoice#upcomingLines.discounts[]`, and
`Invoice#upcomingLines.invoice_items[].discounts[]`

### January 18, 2024

- Change `CustomerSession.components.buy_button` and
`CustomerSession.components.pricing_table` to be required
- Add support for `invoice_settings` on `Subscription#create` and
`Subscription#update`
- Add support for `liability` on `Subscription#create.automatic_tax`,
`Subscription#update.automatic_tax`, and `Subscription.automatic_tax`

### January 17, 2024

- Add support for `customer_balance` on `PaymentMethodConfiguration#create`,
`PaymentMethodConfiguration#update`, and `PaymentMethodConfiguration`
- Add support for `revocation_reason` on
`Mandate.payment_method_details.bacs_debit`
- Add support for new value `nn` on enums
`Charge.payment_method_details.ideal.bank`,
`PaymentIntent#confirm.payment_method_data.ideal.bank`,
`PaymentIntent#create.payment_method_data.ideal.bank`,
`PaymentIntent#update.payment_method_data.ideal.bank`,
`PaymentMethod#create.ideal.bank`, `PaymentMethod.ideal.bank`,
`SetupAttempt.payment_method_details.ideal.bank`,
`SetupIntent#confirm.payment_method_data.ideal.bank`,
`SetupIntent#create.payment_method_data.ideal.bank`, and
`SetupIntent#update.payment_method_data.ideal.bank`
- Add support for new value `NNBANL2G` on enums
`Charge.payment_method_details.ideal.bic`, `PaymentMethod.ideal.bic`, and
`SetupAttempt.payment_method_details.ideal.bic`
- Add support for `pin` on `Issuing.Card#create`

### January 16, 2024

- Change `Subscription.billing_cycle_anchor_config` to be required
- Add support for `issuer` and `on_behalf_of` on `Invoice#upcomingLines` and
`Invoice#upcoming`
- Add support for `issuer` on `Invoice#create`, `Invoice#update`, and `Invoice`
- Add support for `liability` on `Invoice#create.automatic_tax`,
`Invoice#upcoming.automatic_tax`, `Invoice#upcomingLines.automatic_tax`,
`Invoice#update.automatic_tax`, and `Invoice.automatic_tax`

### January 12, 2024

- Remove support for `expand` on `BankAccount#delete` and `Card#delete`
- Add support for `account_type`, `default_for_currency`, and `documents` on
`BankAccount#update` and `Card#update`
- Remove support for `owner` on `BankAccount#update` and `Card#update`
- Change type of `BankAccount#update.account_holder_type` and
`Card#update.account_holder_type` from `enum('company'|'individual')` to
`emptyStringable(enum('company'|'individual'))`

### January 11, 2024

- Add support for new resource `CustomerSession`
- Add support for `create` method on resource `CustomerSession`

### January 10, 2024

- Remove support for values `obligation_inbound`, `obligation_payout_failure`,
`obligation_payout`, and `obligation_reversal_outbound` from enum
`BalanceTransaction.type`
- Remove support for value `obligation` from enum
`Reporting.ReportRun#create.parameters.reporting_category`

### January 9, 2024

- Add support for `billing_cycle_anchor_config` on `Subscription#create` and
`Subscription`

### January 8, 2024

- Add support for new values `eps` and `p24` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`

### January 3, 2024

- Change `AccountSession.components.payment_details.features`,
`AccountSession.components.payment_details`,
`AccountSession.components.payments.features`,
`AccountSession.components.payments`,
`AccountSession.components.payouts.features`, and
`AccountSession.components.payouts` to be required

### January 2, 2024

- Change `PaymentLink.inactive_message` and `PaymentLink.restrictions` to be
required
- Add support for `retrieve` method on resource `Tax.Registration`
- Change type of `SubscriptionSchedule.default_settings.invoice_settings` from
`nullable(InvoiceSettingSubscriptionScheduleSetting)` to
`InvoiceSettingSubscriptionScheduleSetting`

### December 21, 2023

- Add support for `collection_method` on
`Mandate.payment_method_details.us_bank_account`
- Add support for `mandate_options` on
`PaymentIntent#confirm.payment_method_options.us_bank_account`,
`PaymentIntent#create.payment_method_options.us_bank_account`,
`PaymentIntent#update.payment_method_options.us_bank_account`,
`PaymentIntent.payment_method_options.us_bank_account`,
`SetupIntent#confirm.payment_method_options.us_bank_account`,
`SetupIntent#create.payment_method_options.us_bank_account`,
`SetupIntent#update.payment_method_options.us_bank_account`, and
`SetupIntent.payment_method_options.us_bank_account`

### December 20, 2023

- Add support for new resource `FinancialConnections.Transaction`
- Add support for `list` and `retrieve` methods on resource `Transaction`
- Add support for `subscribe` and `unsubscribe` methods on resource
`FinancialConnections.Account`
- Change type of
`Checkout.Session#create.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Checkout.Session.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Invoice#create.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Invoice#update.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Invoice.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent#confirm.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent#create.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent#update.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`PaymentIntent.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent#confirm.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent#create.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent#update.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`SetupIntent.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Subscription#create.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
`Subscription#update.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`,
and
`Subscription.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`
from `literal('balances')` to `enum('balances'|'transactions')`
- Add support for new value
`financial_connections.account.refreshed_transactions` on enum `Event.type`
- Add support for new value `transactions` on enum
`FinancialConnections.Account#refresh.features[]`
- Add support for `subscriptions` and `transaction_refresh` on
`FinancialConnections.Account`
- Add support for new value `transactions` on enums
`FinancialConnections.Session#create.prefetch[]` and
`FinancialConnections.Session.prefetch[]`
- Add support for new value
`financial_connections.account.refreshed_transactions` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Add support for new value `challenge` on enums
`PaymentIntent#confirm.payment_method_options.card.request_three_d_secure`,
`PaymentIntent#create.payment_method_options.card.request_three_d_secure`,
`PaymentIntent#update.payment_method_options.card.request_three_d_secure`,
`PaymentIntent.payment_method_options.card.request_three_d_secure`,
`SetupIntent#confirm.payment_method_options.card.request_three_d_secure`,
`SetupIntent#create.payment_method_options.card.request_three_d_secure`,
`SetupIntent#update.payment_method_options.card.request_three_d_secure`, and
`SetupIntent.payment_method_options.card.request_three_d_secure`
- Add support for new value `unknown` on enums
`Issuing.Authorization.testHelpers#create.verification_data.authentication_exemption.type`
and `Issuing.Authorization.verification_data.authentication_exemption.type`
- Add support for `features` on `AccountSession#create.components.payouts`
- Add support for `edit_payout_schedule`, `instant_payouts`, and
`standard_payouts` on `AccountSession.components.payouts.features`

### December 19, 2023

- Add support for `next_refresh_available_at` on
`FinancialConnections.Account.balance_refresh`
- Change type of `Quote.invoice_settings` from
`nullable(InvoiceSettingQuoteSetting)` to `InvoiceSettingQuoteSetting`

### December 18, 2023

- Add support for `revolut_pay` on `PaymentMethodConfiguration#create`,
`PaymentMethodConfiguration#update`, and `PaymentMethodConfiguration`

### December 15, 2023

- Add support for `destination_details` on `Refund`

### December 14, 2023

- Remove support for `features` on `AccountSession#create.components.payouts`

### December 13, 2023

- Add support for `created` on `Radar.EarlyFraudWarning#list`

### December 8, 2023

- Remove support for `id_bank_transfer`, `multibanco`, `netbanking`,
`pay_by_bank`, and `upi` on `PaymentMethodConfiguration`
- Add support for `payment_method_reuse_agreement` on
`Checkout.Session#create.consent_collection`,
`Checkout.Session.consent_collection`, `PaymentLink#create.consent_collection`,
and `PaymentLink.consent_collection`
- Add support for `after_submit` on `Checkout.Session#create.custom_text`,
`Checkout.Session.custom_text`, `PaymentLink#create.custom_text`,
`PaymentLink#update.custom_text`, and `PaymentLink.custom_text`
- Remove support for values `challenge_only` and `challenge` from enum
`SetupIntent.payment_method_options.card.request_three_d_secure`

### December 7, 2023

- Add support for new value
`financial_connections_no_successful_transaction_refresh` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Remove support for values `challenge_only` and `challenge` from enum
`PaymentIntent.payment_method_options.card.request_three_d_secure`
- Add support for `transfer_group` on `PaymentLink#create.payment_intent_data`,
`PaymentLink#update.payment_intent_data`, and `PaymentLink.payment_intent_data`

### December 6, 2023

- Remove support for value `various` from enum
`Climate.Supplier.removal_pathway`
- Add support for new value `customer_tax_location_invalid` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### December 5, 2023

- Add support for `payment_details`, `payments`, and `payouts` on
`AccountSession#create.components` and `AccountSession.components`
- Add support for `features` on
`AccountSession#create.components.account_onboarding` and
`AccountSession.components.account_onboarding`

### December 4, 2023

- Add support for `trial_settings` on `PaymentLink#create.subscription_data`,
`PaymentLink#update.subscription_data`, and `PaymentLink.subscription_data`
- Add support for `inactive_message` and `restrictions` on `PaymentLink#create`,
`PaymentLink#update`, and `PaymentLink`

### December 1, 2023

- Change `Climate.Product.metric_tons_available` to be required
- Add support for new values `payment_network_reserve_hold` and
`payment_network_reserve_release` on enum `BalanceTransaction.type`

### November 30, 2023

- Add support for new value `challenge` on enums
`PaymentIntent.payment_method_options.card.request_three_d_secure` and
`SetupIntent.payment_method_options.card.request_three_d_secure`
- Add support for `created` on `Checkout.Session#list`
- Add support for new value `enhanced_weathering` on enum
`Climate.Supplier.removal_pathway`

### November 29, 2023

- Add support for new values `climate_order_purchase` and `climate_order_refund`
on enum `BalanceTransaction.type`
- Add support for new values `climate_order_purchase` and `climate_order_refund`
on enum `Reporting.ReportRun#create.parameters.reporting_category`
- Change type of `Climate.Order.expected_delivery_year` from
`nullable(longInteger)` to `longInteger`
- Add support for new values `climate.order.canceled`, `climate.order.created`,
`climate.order.delayed`, `climate.order.delivered`,
`climate.order.product_substituted`, `climate.product.created`, and
`climate.product.pricing_updated` on enum `Event.type`
- Add support for new values `climate.order.canceled`, `climate.order.created`,
`climate.order.delayed`, `climate.order.delivered`,
`climate.order.product_substituted`, `climate.product.created`, and
`climate.product.pricing_updated` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Add support for `validate_location` on `Customer#create.tax` and
`Customer#update.tax`

### November 22, 2023

- Add support for new resources `Climate.Order`, `Climate.Product`, and
`Climate.Supplier`
- Add support for `cancel`, `create`, `list`, `retrieve`, and `update` methods
on resource `Order`
- Add support for `list` and `retrieve` methods on resources `Product` and
`Supplier`

### November 21, 2023

- Add support for new value `financial_connections_account_inactive` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### November 20, 2023

- Add support for `electronic_commerce_indicator` and `transaction_id` on
`Charge.payment_method_details.card.three_d_secure` and
`SetupAttempt.payment_method_details.card.three_d_secure`
- Add support for `exemption_indicator_applied` and `exemption_indicator` on
`Charge.payment_method_details.card.three_d_secure`
- Add support for `three_d_secure` on
`PaymentIntent#confirm.payment_method_options.card`,
`PaymentIntent#create.payment_method_options.card`,
`PaymentIntent#update.payment_method_options.card`,
`SetupIntent#confirm.payment_method_options.card`,
`SetupIntent#create.payment_method_options.card`, and
`SetupIntent#update.payment_method_options.card`

### November 18, 2023

- Add support for `system_trace_audit_number` on
`Issuing.Authorization.network_data`
- Add support for `transaction_id` on `Issuing.Authorization.network_data` and
`Issuing.Transaction.network_data`
- Add support for `network_risk_score` on
`Issuing.Authorization.pending_request` and
`Issuing.Authorization.request_history[]`
- Add support for `requested_at` on `Issuing.Authorization.request_history[]`
- Add support for `authorization_code` on `Issuing.Transaction.network_data`

### November 17, 2023

- Add support for `offline` on `Charge.payment_method_details.card_present`

### November 16, 2023

- Add support for `status` on `Checkout.Session#list`
- Add support for `bacs_debit_payments` on `Account#create.settings` and
`Account#update.settings`
- Add support for `service_user_number` on
`Account.settings.bacs_debit_payments`
- Change type of `Account.settings.bacs_debit_payments.display_name` from
`string` to `nullable(string)`
- Change `Account.settings.bacs_debit_payments.display_name` to be required

### November 15, 2023

- Change type of `SubscriptionSchedule#create.start_date[0]`,
`SubscriptionSchedule#update.phases[].end_date[0]`,
`SubscriptionSchedule#update.phases[].start_date[0]`, and
`SubscriptionSchedule#update.phases[].trial_end[0]` from `longInteger` to
`DateTime`
- Add support for `tax_amounts` on `CreditNote#create.lines[]`,
`CreditNote#preview.lines[]`, and `CreditNote#preview_lines.lines[]`
- Add support for `capture_before` on `Charge.payment_method_details.card`
- Add support for `network_data` on `Issuing.Transaction`

### November 14, 2023

- Add support for `paypal` on `Checkout.Session.payment_method_options`

### November 8, 2023

- Add support for new value `terminal_reader_hardware_fault` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Change `Charge.payment_method_details.card.amount_authorized` to be required

### November 7, 2023

- Change `PaymentIntent.latest_charge` to be required
- Change `Product.features[].name` to be optional

### November 3, 2023

- Change `Checkout.Session.payment_method_configuration_details`,
`PaymentIntent.payment_method_configuration_details`, and
`SetupIntent.payment_method_configuration_details` to be required
- Add support for `metadata` on `Quote#create.subscription_data`,
`Quote#update.subscription_data`, and `Quote.subscription_data`

### November 2, 2023

- Add support for new value `payment_unreconciled` on enum
`BalanceTransaction.type`
- Add support for new value `unreconciled_customer_funds` on enum
`Reporting.ReportRun#create.parameters.reporting_category`
- Add support for `url` on `Issuing.Authorization.merchant_data`,
`Issuing.Authorization.testHelpers#create.merchant_data`,
`Issuing.Transaction.merchant_data`,
`Issuing.Transaction.testHelpers#create_force_capture.merchant_data`, and
`Issuing.Transaction.testHelpers#create_unlinked_refund.merchant_data`
- Add support for `authentication_exemption` and `three_d_secure` on
`Issuing.Authorization.testHelpers#create.verification_data` and
`Issuing.Authorization.verification_data`
- Add support for new value `token_card_network_invalid` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Add support for `description` on `PaymentLink#create.payment_intent_data`,
`PaymentLink#update.payment_intent_data`, and `PaymentLink.payment_intent_data`

### November 1, 2023

- Add support for `revolut_pay_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `revolut_pay` on `Charge.payment_method_details`,
`Checkout.Session#create.payment_method_options`,
`Checkout.Session.payment_method_options`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `revolut_pay` on enums
`Checkout.Session#create.payment_method_types[]`,
`Customer#list_payment_methods.type`, `PaymentMethod#create.type`, and
`PaymentMethod#list.type`
- Add support for new value `revolut_pay` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `revolut_pay` on enum `PaymentMethod.type`

### October 31, 2023

- Add support for new resource `Tax.Registration`
- Add support for `create`, `list`, and `update` methods on resource
`Registration`
- Change `Charge.payment_method_details.paypal.payer_email`,
`Charge.payment_method_details.paypal.payer_id`,
`Charge.payment_method_details.paypal.payer_name`,
`Charge.payment_method_details.paypal.seller_protection`,
`Charge.payment_method_details.paypal.transaction_id`,
`Mandate.payment_method_details.paypal.payer_id`,
`PaymentIntent.payment_method_options.paypal.reference`,
`PaymentMethod.paypal.payer_email`, and `PaymentMethod.paypal.payer_id` to be
required

### October 26, 2023

- Add support for `aba` and `swift` on
`FundingInstructions.bank_transfer.financial_addresses[]` and
`PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[]`
- Add support for new values `ach`, `domestic_wire_us`, and `swift` on enums
`FundingInstructions.bank_transfer.financial_addresses[].supported_networks[]`
and
`PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].supported_networks[]`
- Add support for new values `aba` and `swift` on enums
`FundingInstructions.bank_transfer.financial_addresses[].type` and
`PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].type`

### October 25, 2023

- Add support for new value `balance_invalid_parameter` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### October 24, 2023

- Change `Issuing.Cardholder.individual.card_issuing` to be optional

### October 18, 2023

- Remove support for `request_incremental_authorization` on
`PaymentIntent#confirm.payment_method_options.card_present`,
`PaymentIntent#create.payment_method_options.card_present`, and
`PaymentIntent#update.payment_method_options.card_present`

### October 17, 2023

- Add support for new value `invalid_dob_age_under_minimum` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`BankAccount.future_requirements.errors[].code`, and
`BankAccount.requirements.errors[].code`

### October 16, 2023

- Change `Checkout.Session.client_secret` and `Checkout.Session.ui_mode` to be
required
- Add support for `legal_guardian` on `Account#persons.relationship` and
`Token#create.person.relationship`
- Add support for new values `invalid_address_highway_contract_box`,
`invalid_address_private_mailbox`, `invalid_business_profile_name_denylisted`,
`invalid_business_profile_name`, `invalid_company_name_denylisted`,
`invalid_dob_age_over_maximum`, `invalid_product_description_length`,
`invalid_product_description_url_match`,
`invalid_statement_descriptor_business_mismatch`,
`invalid_statement_descriptor_denylisted`,
`invalid_statement_descriptor_length`,
`invalid_statement_descriptor_prefix_denylisted`,
`invalid_statement_descriptor_prefix_mismatch`, `invalid_tax_id_format`,
`invalid_tax_id`, `invalid_url_denylisted`, `invalid_url_format`,
`invalid_url_length`, `invalid_url_web_presence_detected`,
`invalid_url_website_business_information_mismatch`,
`invalid_url_website_empty`, `invalid_url_website_inaccessible_geoblocked`,
`invalid_url_website_inaccessible_password_protected`,
`invalid_url_website_inaccessible`,
`invalid_url_website_incomplete_cancellation_policy`,
`invalid_url_website_incomplete_customer_service_details`,
`invalid_url_website_incomplete_legal_restrictions`,
`invalid_url_website_incomplete_refund_policy`,
`invalid_url_website_incomplete_return_policy`,
`invalid_url_website_incomplete_terms_and_conditions`,
`invalid_url_website_incomplete_under_construction`,
`invalid_url_website_incomplete`, and `invalid_url_website_other` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`BankAccount.future_requirements.errors[].code`, and
`BankAccount.requirements.errors[].code`
- Add support for `additional_tos_acceptances` on `Token#create.person`
- Add support for new value `2023-10-16` on enum
`WebhookEndpoint#create.api_version`

### October 12, 2023

- Add support for new values `issuing_token.created` and `issuing_token.updated`
on enum `Event.type`
- Add support for new values `issuing_token.created` and `issuing_token.updated`
on enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### October 10, 2023

- Add support for `offline` on `Terminal.Configuration#create`,
`Terminal.Configuration#update`, and `Terminal.Configuration`
- Change type of `Checkout.Session.custom_fields[].dropdown` from
`nullable(PaymentPagesCheckoutSessionCustomFieldsDropdown)` to
`PaymentPagesCheckoutSessionCustomFieldsDropdown`
- Change type of `Checkout.Session.custom_fields[].numeric` and
`Checkout.Session.custom_fields[].text` from
`nullable(PaymentPagesCheckoutSessionCustomFieldsNumeric)` to
`PaymentPagesCheckoutSessionCustomFieldsNumeric`
- Change `Checkout.Session.custom_fields[].dropdown`,
`Checkout.Session.custom_fields[].numeric`,
`Checkout.Session.custom_fields[].text`, `PaymentLink.custom_fields[].dropdown`,
`PaymentLink.custom_fields[].numeric`, and `PaymentLink.custom_fields[].text` to
be optional
- Change type of `PaymentLink.custom_fields[].dropdown` from
`nullable(PaymentLinksResourceCustomFieldsDropdown)` to
`PaymentLinksResourceCustomFieldsDropdown`
- Change type of `PaymentLink.custom_fields[].numeric` and
`PaymentLink.custom_fields[].text` from
`nullable(PaymentLinksResourceCustomFieldsNumeric)` to
`PaymentLinksResourceCustomFieldsNumeric`

### October 6, 2023

- Add support for `postal_code` on `Issuing.Authorization.verification_data`
- Add support for `redirect_on_completion`, `return_url`, and `ui_mode` on
`Checkout.Session#create` and `Checkout.Session`
- Change `Checkout.Session#create.success_url` to be optional
- Add support for `client_secret` on `Checkout.Session`

### October 4, 2023

- Remove support for resource `Margin`
- Add support for `statement_descriptor_suffix` and `statement_descriptor` on
`PaymentLink#create.payment_intent_data`,
`PaymentLink#update.payment_intent_data`, and `PaymentLink.payment_intent_data`

### October 3, 2023

- Change `PaymentLink.payment_intent_data.metadata` and
`PaymentLink.subscription_data.metadata` to be required
- Add support for new resources `Issuing.Token` and `Margin`
- Add support for `list`, `retrieve`, and `update` methods on resource `Token`
- Add support for `amount_authorized`, `extended_authorization`,
`incremental_authorization`, `multicapture`, and `overcapture` on
`Charge.payment_method_details.card`
- Add support for `token` on `Issuing.Authorization` and `Issuing.Transaction`
- Add support for `request_extended_authorization`, `request_multicapture`, and
`request_overcapture` on `PaymentIntent#confirm.payment_method_options.card`,
`PaymentIntent#create.payment_method_options.card`,
`PaymentIntent#update.payment_method_options.card`, and
`PaymentIntent.payment_method_options.card`
- Add support for `request_incremental_authorization` on
`PaymentIntent#confirm.payment_method_options.card_present`,
`PaymentIntent#confirm.payment_method_options.card`,
`PaymentIntent#create.payment_method_options.card_present`,
`PaymentIntent#create.payment_method_options.card`,
`PaymentIntent#update.payment_method_options.card_present`,
`PaymentIntent#update.payment_method_options.card`, and
`PaymentIntent.payment_method_options.card`
- Add support for `final_capture` on `PaymentIntent#capture`
- Add support for `metadata` on `PaymentLink#create.payment_intent_data`,
`PaymentLink#create.subscription_data`, `PaymentLink.payment_intent_data`, and
`PaymentLink.subscription_data`
- Add support for `payment_intent_data` and `subscription_data` on
`PaymentLink#update`

### September 29, 2023

- Add support for `authorization_code` on
`Issuing.Authorization.request_history[]`

### September 27, 2023

- Change `PaymentMethod.us_bank_account.financial_connections_account` to be
required

### September 26, 2023

- Change `PaymentMethod.us_bank_account.status_details` to be required

### September 22, 2023

- Remove support for values `order.created`, `recipient.created`,
`recipient.deleted`, `recipient.updated`, `sku.created`, `sku.deleted`, and
`sku.updated` from enum `Event.type`
- Remove support for values `order.created`, `recipient.created`,
`recipient.deleted`, `recipient.updated`, `sku.created`, `sku.deleted`, and
`sku.updated` from enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Add support for `rendering` on `Invoice#create`, `Invoice#update`, and
`Invoice`

### September 21, 2023

- Change `Charge.payment_method_details.paypal.payer_email`,
`Charge.payment_method_details.paypal.payer_id`,
`Charge.payment_method_details.paypal.payer_name`,
`Charge.payment_method_details.paypal.seller_protection`,
`Charge.payment_method_details.paypal.transaction_id`,
`Mandate.payment_method_details.paypal.payer_id`,
`PaymentIntent.payment_method_options.paypal.reference`,
`PaymentMethod.paypal.payer_email`, and `PaymentMethod.paypal.payer_id` to be
optional
- Change `Charge.payment_method_details.paypal.payer_email`,
`Charge.payment_method_details.paypal.payer_id`,
`Charge.payment_method_details.paypal.payer_name`,
`Charge.payment_method_details.paypal.seller_protection`,
`Charge.payment_method_details.paypal.transaction_id`,
`Mandate.payment_method_details.paypal.payer_id`,
`PaymentIntent.payment_method_options.paypal.reference`,
`PaymentMethod.paypal.payer_email`, and `PaymentMethod.paypal.payer_id` to be
required

### September 19, 2023

- Add support for `terms_of_service_acceptance` on
`Checkout.Session#create.custom_text`, `Checkout.Session.custom_text`,
`PaymentLink#create.custom_text`, `PaymentLink#update.custom_text`, and
`PaymentLink.custom_text`

### September 14, 2023

- Add support for new resource `PaymentMethodConfiguration`
- Add support for `create`, `list`, `retrieve`, and `update` methods on resource
`PaymentMethodConfiguration`
- Add support for `payment_method_configuration` on `Checkout.Session#create`,
`PaymentIntent#create`, `PaymentIntent#update`, `SetupIntent#create`, and
`SetupIntent#update`
- Add support for `payment_method_configuration_details` on `Checkout.Session`,
`PaymentIntent`, and `SetupIntent`

### September 12, 2023

- Add support for `nonce` on `EphemeralKey#create`

### September 11, 2023

- Add support for `cashback_amount` on `Issuing.Authorization.amount_details`,
`Issuing.Authorization.pending_request.amount_details`,
`Issuing.Authorization.request_history[].amount_details`,
`Issuing.Authorization.testHelpers#create.amount_details`, and
`Issuing.Transaction.amount_details`
- Add support for `capture`, `create`, `expire`, `increment`, and `reverse` test
helper methods on resource `Issuing.Authorization`
- Add support for `create_force_capture`, `create_unlinked_refund`, and `refund`
test helper methods on resource `Issuing.Transaction`

### September 8, 2023

- Add support for new value `stripe_tax_inactive` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`

### September 7, 2023

- Add support for `serial_number` on `Terminal.Reader#list`

### September 5, 2023

- Add support for new resource `PaymentMethodDomain`
- Add support for `create`, `list`, `retrieve`, `update`, and `validate` methods
on resource `PaymentMethodDomain`
- Add support for new value `n26` on enums
`Charge.payment_method_details.ideal.bank`,
`PaymentIntent#confirm.payment_method_data.ideal.bank`,
`PaymentIntent#create.payment_method_data.ideal.bank`,
`PaymentIntent#update.payment_method_data.ideal.bank`,
`PaymentMethod#create.ideal.bank`, `PaymentMethod.ideal.bank`,
`SetupAttempt.payment_method_details.ideal.bank`,
`SetupIntent#confirm.payment_method_data.ideal.bank`,
`SetupIntent#create.payment_method_data.ideal.bank`, and
`SetupIntent#update.payment_method_data.ideal.bank`
- Add support for new value `NTSBDEB1` on enums
`Charge.payment_method_details.ideal.bic`, `PaymentMethod.ideal.bic`, and
`SetupAttempt.payment_method_details.ideal.bic`

### September 4, 2023

- Remove support for value `invoiceitem.updated` from enum `Event.type`
- Remove support for value `invoiceitem.updated` from enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### September 1, 2023

- Add support for new values `treasury.credit_reversal.created`,
`treasury.credit_reversal.posted`, `treasury.debit_reversal.completed`,
`treasury.debit_reversal.created`,
`treasury.debit_reversal.initial_credit_granted`,
`treasury.financial_account.closed`, `treasury.financial_account.created`,
`treasury.financial_account.features_status_updated`,
`treasury.inbound_transfer.canceled`, `treasury.inbound_transfer.created`,
`treasury.inbound_transfer.failed`, `treasury.inbound_transfer.succeeded`,
`treasury.outbound_payment.canceled`, `treasury.outbound_payment.created`,
`treasury.outbound_payment.expected_arrival_date_updated`,
`treasury.outbound_payment.failed`, `treasury.outbound_payment.posted`,
`treasury.outbound_payment.returned`, `treasury.outbound_transfer.canceled`,
`treasury.outbound_transfer.created`,
`treasury.outbound_transfer.expected_arrival_date_updated`,
`treasury.outbound_transfer.failed`, `treasury.outbound_transfer.posted`,
`treasury.outbound_transfer.returned`, `treasury.received_credit.created`,
`treasury.received_credit.failed`, `treasury.received_credit.succeeded`, and
`treasury.received_debit.created` on enum `Event.type`

### August 31, 2023

- Add support for `features` on `Product#create`, `Product#update`, and
`Product`

### August 30, 2023

- Add support for new resource `AccountSession`
- Add support for `create` method on resource `AccountSession`

### August 29, 2023

- Add support for new values `obligation_inbound`, `obligation_outbound`,
`obligation_payout_failure`, `obligation_payout`, `obligation_reversal_inbound`,
and `obligation_reversal_outbound` on enum `BalanceTransaction.type`
- Add support for new value `obligation` on enum
`Reporting.ReportRun#create.parameters.reporting_category`

### August 28, 2023

- Remove support for values `obligation_inbound`, `obligation_outbound`,
`obligation_payout_failure`, `obligation_payout`, `obligation_reversal_inbound`,
and `obligation_reversal_outbound` from enum `BalanceTransaction.type`
- Remove support for value `obligation` from enum
`Reporting.ReportRun#create.parameters.reporting_category`
- Add support for `application` on `PaymentLink`
- Change type of `Event.type` from `string` to `enum`
- Add support for new values `obligation_inbound`, `obligation_outbound`,
`obligation_payout_failure`, `obligation_payout`, `obligation_reversal_inbound`,
and `obligation_reversal_outbound` on enum `BalanceTransaction.type`
- Add support for new value `obligation` on enum
`Reporting.ReportRun#create.parameters.reporting_category`

### August 22, 2023

- Add support for `retention` on
`BillingPortal.Session#create.flow_data.subscription_cancel` and
`BillingPortal.Session.flow.subscription_cancel`

### August 21, 2023

- Add support for `prefetch` on
`Checkout.Session#create.payment_method_options.us_bank_account.financial_connections`,
`Checkout.Session.payment_method_options.us_bank_account.financial_connections`,
`FinancialConnections.Session#create`, `FinancialConnections.Session`,
`Invoice#create.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`Invoice#update.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`Invoice.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent#confirm.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent#create.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent#update.payment_method_options.us_bank_account.financial_connections`,
`PaymentIntent.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent#confirm.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent#create.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent#update.payment_method_options.us_bank_account.financial_connections`,
`SetupIntent.payment_method_options.us_bank_account.financial_connections`,
`Subscription#create.payment_settings.payment_method_options.us_bank_account.financial_connections`,
`Subscription#update.payment_settings.payment_method_options.us_bank_account.financial_connections`,
and
`Subscription.payment_settings.payment_method_options.us_bank_account.financial_connections`
- Change type of `SetupIntent#create.mandate_data` from `secret_key_param` to
`emptyStringable(secret_key_param)`
- Change type of `SetupIntent#confirm.mandate_data` from `secret_key_param |
client_key_param` to `emptyStringable(secret_key_param | client_key_param)`

### August 20, 2023

- Change type of `PaymentIntent#create.mandate_data` from `secret_key_param` to
`emptyStringable(secret_key_param)`
- Change type of `PaymentIntent#confirm.mandate_data` from `secret_key_param |
client_key_param` to `emptyStringable(secret_key_param | client_key_param)`

### August 18, 2023

- Add support for `payment_method_details` on `Dispute`

### August 17, 2023

- Add support for `flat_amount` on `Tax.Transaction#create_reversal`

### August 16, 2023

- Remove support for values `custom_account_update` and
`custom_account_verification` from enum `AccountLink#create.type`
- Remove support for `available_on` on `BalanceTransaction#list`
- Remove support for `alternate_statement_descriptors`, `destination`, and
`dispute` on `Charge`
- Remove support for `shipping_rates` on `Checkout.Session#create`
- Remove support for `coupon` and `trial_from_plan` on
`Checkout.Session#create.subscription_data`
- Remove support for value `card_present` from enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Remove support for value `charge_refunded` from enum `Dispute.status`
- Remove support for `blik` on `Mandate.payment_method_details`,
`PaymentMethod#update`, `SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_options`, and
`SetupIntent.payment_method_options`
- Remove support for `acss_debit`, `affirm`, `au_becs_debit`, `bacs_debit`,
`cashapp`, `sepa_debit`, and `zip` on `PaymentMethod#update`
- Remove support for `country` on `PaymentMethod.link`
- Remove support for `recurring` on `Price#update`
- Remove support for `attributes`, `caption`, and `deactivate_on` on
`Product#create`, `Product#update`, and `Product`
- Add support for new values `verification_directors_mismatch`,
`verification_document_directors_mismatch`, `verification_extraneous_directors`,
and `verification_missing_directors` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`BankAccount.future_requirements.errors[].code`, and
`BankAccount.requirements.errors[].code`

### August 14, 2023

- Add support for new value `2023-08-16` on enum
`WebhookEndpoint#create.api_version`

### August 11, 2023

- Add support for `process_config` on `Terminal.Reader#process_setup_intent` and
`Terminal.Reader.action.process_setup_intent`
- Remove support for `rendering` on `Invoice#create`, `Invoice#update`, and
`Invoice`

### August 10, 2023

- Add support for `rendering` on `Invoice#create`, `Invoice#update`, and
`Invoice`
- Add support for new values `incorporated_partnership` and
`unincorporated_partnership` on enums `Account#create.company.structure`,
`Account#update.company.structure`, `Account.company.structure`, and
`Token#create.account.company.structure`

### August 7, 2023

- Add support for new value `payment_reversal` on enum `BalanceTransaction.type`

### August 4, 2023

- Change `Invoice.subscription_details.metadata` and
`Invoice.subscription_details` to be required

### August 3, 2023

- Add support for `preferred_settlement_speed` on
`PaymentIntent#confirm.payment_method_options.us_bank_account`,
`PaymentIntent#create.payment_method_options.us_bank_account`,
`PaymentIntent#update.payment_method_options.us_bank_account`, and
`PaymentIntent.payment_method_options.us_bank_account`

### August 2, 2023

- Add support for new values `sepa_debit_fingerprint` and
`us_bank_account_fingerprint` on enums `Radar.ValueList#create.item_type` and
`Radar.ValueList.item_type`

### August 1, 2023

- Change type of
`Account#create.settings.card_issuing.tos_acceptance.user_agent`,
`Account#create.settings.treasury.tos_acceptance.user_agent`,
`Account#update.settings.card_issuing.tos_acceptance.user_agent`,
`Account#update.settings.treasury.tos_acceptance.user_agent`,
`BillingPortal.Configuration#create.business_profile.headline`,
`BillingPortal.Configuration#update.business_profile.headline`,
`Invoice#create.payment_settings.default_mandate`,
`Invoice#create.shipping_details.phone`, `Invoice#pay.mandate`,
`Invoice#update.default_source`,
`Invoice#update.payment_settings.default_mandate`,
`Invoice#update.shipping_details.phone`,
`Issuing.Cardholder#create.individual.card_issuing.user_terms_acceptance.user_agent`,
`Issuing.Cardholder#update.individual.card_issuing.user_terms_acceptance.user_agent`,
`Issuing.Dispute#create.evidence.canceled.cancellation_reason`,
`Issuing.Dispute#create.evidence.canceled.explanation`,
`Issuing.Dispute#create.evidence.canceled.product_description`,
`Issuing.Dispute#create.evidence.duplicate.explanation`,
`Issuing.Dispute#create.evidence.fraudulent.explanation`,
`Issuing.Dispute#create.evidence.merchandise_not_as_described.explanation`,
`Issuing.Dispute#create.evidence.merchandise_not_as_described.return_description`,
`Issuing.Dispute#create.evidence.not_received.explanation`,
`Issuing.Dispute#create.evidence.not_received.product_description`,
`Issuing.Dispute#create.evidence.other.explanation`,
`Issuing.Dispute#create.evidence.other.product_description`,
`Issuing.Dispute#create.evidence.service_not_as_described.cancellation_reason`,
`Issuing.Dispute#create.evidence.service_not_as_described.explanation`,
`Issuing.Dispute#update.evidence.canceled.cancellation_reason`,
`Issuing.Dispute#update.evidence.canceled.explanation`,
`Issuing.Dispute#update.evidence.canceled.product_description`,
`Issuing.Dispute#update.evidence.duplicate.explanation`,
`Issuing.Dispute#update.evidence.fraudulent.explanation`,
`Issuing.Dispute#update.evidence.merchandise_not_as_described.explanation`,
`Issuing.Dispute#update.evidence.merchandise_not_as_described.return_description`,
`Issuing.Dispute#update.evidence.not_received.explanation`,
`Issuing.Dispute#update.evidence.not_received.product_description`,
`Issuing.Dispute#update.evidence.other.explanation`,
`Issuing.Dispute#update.evidence.other.product_description`,
`Issuing.Dispute#update.evidence.service_not_as_described.cancellation_reason`,
`Issuing.Dispute#update.evidence.service_not_as_described.explanation`,
`PaymentIntent#confirm.payment_method_data.billing_details.name`,
`PaymentIntent#confirm.payment_method_data.billing_details.phone`,
`PaymentIntent#confirm.payment_method_options.konbini.confirmation_number`,
`PaymentIntent#confirm.payment_method_options.konbini.product_description`,
`PaymentIntent#create.payment_method_data.billing_details.name`,
`PaymentIntent#create.payment_method_data.billing_details.phone`,
`PaymentIntent#create.payment_method_options.konbini.confirmation_number`,
`PaymentIntent#create.payment_method_options.konbini.product_description`,
`PaymentIntent#update.payment_method_data.billing_details.name`,
`PaymentIntent#update.payment_method_data.billing_details.phone`,
`PaymentIntent#update.payment_method_options.konbini.confirmation_number`,
`PaymentIntent#update.payment_method_options.konbini.product_description`,
`PaymentMethod#create.billing_details.name`,
`PaymentMethod#create.billing_details.phone`,
`PaymentMethod#update.billing_details.name`,
`PaymentMethod#update.billing_details.phone`, `Product#update.caption`,
`Product#update.description`, `Product#update.unit_label`,
`Quote#create.description`, `Quote#create.footer`, `Quote#create.header`,
`Quote#update.description`, `Quote#update.footer`, `Quote#update.header`,
`Quote#update.subscription_data.description`,
`SetupIntent#confirm.payment_method_data.billing_details.name`,
`SetupIntent#confirm.payment_method_data.billing_details.phone`,
`SetupIntent#create.payment_method_data.billing_details.name`,
`SetupIntent#create.payment_method_data.billing_details.phone`,
`SetupIntent#update.payment_method_data.billing_details.name`,
`SetupIntent#update.payment_method_data.billing_details.phone`,
`Subscription#cancel.cancellation_details.comment`,
`Subscription#update.cancellation_details.comment`,
`Subscription#update.default_source`, `Subscription#update.description`,
`SubscriptionSchedule#create.default_settings.description`,
`SubscriptionSchedule#create.phases[].description`,
`SubscriptionSchedule#update.default_settings.description`,
`SubscriptionSchedule#update.phases[].description`,
`Tax.Calculation#create.customer_details.address.city`,
`Tax.Calculation#create.customer_details.address.line1`,
`Tax.Calculation#create.customer_details.address.line2`,
`Tax.Calculation#create.customer_details.address.postal_code`,
`Tax.Calculation#create.customer_details.address.state`,
`Terminal.Location#update.configuration_overrides`,
`Terminal.Reader#update.label`,
`Token#create.person.documents.company_authorization.files[]`,
`Token#create.person.documents.passport.files[]`,
`Token#create.person.documents.visa.files[]`,
`Treasury.OutboundPayment#create.destination_payment_method_data.billing_details.name`,
`Treasury.OutboundPayment#create.destination_payment_method_data.billing_details.phone`,
`WebhookEndpoint#create.description`, and `WebhookEndpoint#update.description`
from `string` to `emptyStringable(string)`

### July 28, 2023

- Add support for `subscription_details` on `Invoice`

### July 25, 2023

- Add support for `monthly_estimated_revenue` on
`Account#create.business_profile`, `Account#update.business_profile`, and
`Account.business_profile`

### July 18, 2023

- Remove support for values `excluded_territory`, `jurisdiction_unsupported`,
and `vat_exempt` from enums
`Checkout.Session.shipping_cost.taxes[].taxability_reason`,
`Checkout.Session.total_details.breakdown.taxes[].taxability_reason`,
`CreditNote.shipping_cost.taxes[].taxability_reason`,
`Invoice.shipping_cost.taxes[].taxability_reason`,
`LineItem.taxes[].taxability_reason`,
`Quote.computed.recurring.total_details.breakdown.taxes[].taxability_reason`,
`Quote.computed.upfront.total_details.breakdown.taxes[].taxability_reason`, and
`Quote.total_details.breakdown.taxes[].taxability_reason`

### July 17, 2023

- Add support for `use_stripe_sdk` on `SetupIntent#confirm` and
`SetupIntent#create`
- Add support for new value `service_tax` on enums `TaxRate#create.tax_type`,
`TaxRate#update.tax_type`, and `TaxRate.tax_type`

### July 14, 2023

- Add support for new value `ro_tin` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`,
`Tax.Calculation.customer_details.tax_ids[].type`, and
`Tax.Transaction.customer_details.tax_ids[].type`
- Add support for new value `ro_tin` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`, and
`Tax.Calculation#create.customer_details.tax_ids[].type`

### July 12, 2023

- Add support for `allow_redirects` on
`PaymentIntent#create.automatic_payment_methods`,
`PaymentIntent.automatic_payment_methods`,
`SetupIntent#create.automatic_payment_methods`, and
`SetupIntent.automatic_payment_methods`
- Add support for `order_id` on
`Charge.payment_method_details.afterpay_clearpay`
- Add support for new values `amusement_tax` and `communications_tax` on enums
`Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type`,
`Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type`,
`Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type`, and
`Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type`

### July 11, 2023

- Add support for new resource `Tax.Settings`
- Add support for `retrieve` and `update` methods on resource `Settings`
- Add support for new value `invalid_tax_location` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Add support for new value `tax.settings.updated` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Add support for `product` on `Tax.TransactionLineItem`

### July 3, 2023

- Add support for `automatic_tax` on `Subscription#list`
- Add support for `numeric` and `text` on `PaymentLink.custom_fields[]`

### June 28, 2023

- Add support for `effective_at` on `CreditNote#create`,
`CreditNote#preview_lines`, `CreditNote#preview`, `CreditNote`,
`Invoice#create`, `Invoice#update`, and `Invoice`

### June 27, 2023

- Add support for new value `application_fees_not_allowed` on enums
`Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`,
`SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and
`StripeError.code`
- Add support for new values `ad_nrt`, `ar_cuit`, `bo_tin`, `cn_tin`, `co_nit`,
`cr_tin`, `do_rcn`, `ec_ruc`, `pe_ruc`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`,
and `vn_tin` on enums `Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`,
`Tax.Calculation.customer_details.tax_ids[].type`, and
`Tax.Transaction.customer_details.tax_ids[].type`
- Add support for new values `ad_nrt`, `ar_cuit`, `bo_tin`, `cn_tin`, `co_nit`,
`cr_tin`, `do_rcn`, `ec_ruc`, `pe_ruc`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`,
and `vn_tin` on enums `Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`, and
`Tax.Calculation#create.customer_details.tax_ids[].type`

### June 22, 2023

- Add support for `on_behalf_of` on `Mandate`

### June 9, 2023

- Change type of `Checkout.Session.success_url` from `string` to
`nullable(string)`

### June 6, 2023

- Add support for `taxability_reason` on `Tax.Calculation.tax_breakdown[]`

### June 2, 2023

- Change `Charge.payment_method_details.cashapp.buyer_id`,
`Charge.payment_method_details.cashapp.cashtag`,
`PaymentMethod.cashapp.buyer_id`, and `PaymentMethod.cashapp.cashtag` to be
required

### June 1, 2023

- Add support for `numeric` and `text` on
`Checkout.Session#create.custom_fields[]`, `PaymentLink#create.custom_fields[]`,
and `PaymentLink#update.custom_fields[]`
- Add support for `maximum_length` and `minimum_length` on
`Checkout.Session.custom_fields[].numeric` and
`Checkout.Session.custom_fields[].text`
- Add support for `payer_email` on `PaymentMethod.paypal`
- Add support for new values `aba` and `swift` on enums
`Checkout.Session#create.payment_method_options.customer_balance.bank_transfer.requested_address_types[]`,
`Checkout.Session.payment_method_options.customer_balance.bank_transfer.requested_address_types[]`,
`PaymentIntent#confirm.payment_method_options.customer_balance.bank_transfer.requested_address_types[]`,
`PaymentIntent#create.payment_method_options.customer_balance.bank_transfer.requested_address_types[]`,
`PaymentIntent#update.payment_method_options.customer_balance.bank_transfer.requested_address_types[]`,
and
`PaymentIntent.payment_method_options.customer_balance.bank_transfer.requested_address_types[]`
- Add support for new value `us_bank_transfer` on enums
`Checkout.Session#create.payment_method_options.customer_balance.bank_transfer.type`,
`Checkout.Session.payment_method_options.customer_balance.bank_transfer.type`,
`Customer#create_funding_instructions.bank_transfer.type`,
`PaymentIntent#confirm.payment_method_options.customer_balance.bank_transfer.type`,
`PaymentIntent#create.payment_method_options.customer_balance.bank_transfer.type`,
`PaymentIntent#update.payment_method_options.customer_balance.bank_transfer.type`,
`PaymentIntent.next_action.display_bank_transfer_instructions.type`, and
`PaymentIntent.payment_method_options.customer_balance.bank_transfer.type`

### May 31, 2023

- Add support for `preferred_locales` on `Issuing.Cardholder#create`,
`Issuing.Cardholder#update`, and `Issuing.Cardholder`

### May 30, 2023

- Remove support for `taxability_reason` on `Tax.Calculation.tax_breakdown[]`
- Add support for `taxability_reason` on `Tax.Calculation.tax_breakdown[]`

### May 26, 2023

- Add support for `description`, `iin`, and `issuer` on
`PaymentMethod.card_present` and `PaymentMethod.interac_present`

### May 23, 2023

- Add support for `zip_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `zip` on `Charge.payment_method_details`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `zip` on enums
`Checkout.Session#create.payment_method_types[]` and `PaymentMethod#create.type`
- Add support for new value `zip` on enums `Customer#list_payment_methods.type`
and `PaymentMethod#list.type`
- Add support for new value `zip` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `zip` on enum `PaymentMethod.type`

### May 22, 2023

- Change type of `Invoice.last_finalization_error.code`,
`PaymentIntent.last_payment_error.code`, `SetupAttempt.setup_error.code`,
`SetupIntent.last_setup_error.code`, and `StripeError.code` from `string` to
`enum`

### May 18, 2023

- Remove support for `mandate_options` on
`PaymentIntent#confirm.payment_method_options.blik`,
`PaymentIntent#create.payment_method_options.blik`,
`PaymentIntent#update.payment_method_options.blik`,
`PaymentIntent.payment_method_options.blik`,
`SetupIntent#confirm.payment_method_options.blik`,
`SetupIntent#create.payment_method_options.blik`, and
`SetupIntent#update.payment_method_options.blik`
- Add support for `mandate_options` on
`PaymentIntent#confirm.payment_method_options.blik`,
`PaymentIntent#create.payment_method_options.blik`,
`PaymentIntent#update.payment_method_options.blik`,
`PaymentIntent.payment_method_options.blik`,
`SetupIntent#confirm.payment_method_options.blik`,
`SetupIntent#create.payment_method_options.blik`, and
`SetupIntent#update.payment_method_options.blik`

### May 16, 2023

- Add support for new values `amusement_tax` and `communications_tax` on enums
`TaxRate#create.tax_type`, `TaxRate#update.tax_type`, and `TaxRate.tax_type`

### May 15, 2023

- Add support for `subscription_update_confirm` and `subscription_update` on
`BillingPortal.Session#create.flow_data` and `BillingPortal.Session.flow`
- Add support for new values `subscription_update_confirm` and
`subscription_update` on enums `BillingPortal.Session#create.flow_data.type` and
`BillingPortal.Session.flow.type`
- Add support for `link` on `Charge.payment_method_details.card.wallet` and
`PaymentMethod.card.wallet`

### May 12, 2023

- Add support for `buyer_id` and `cashtag` on
`Charge.payment_method_details.cashapp` and `PaymentMethod.cashapp`

### May 11, 2023

- Add support for `taxability_reason` and `taxable_amount` on
`Checkout.Session.shipping_cost.taxes[]`,
`Checkout.Session.total_details.breakdown.taxes[]`,
`CreditNote.shipping_cost.taxes[]`, `CreditNote.tax_amounts[]`,
`Invoice.shipping_cost.taxes[]`, `Invoice.total_tax_amounts[]`,
`LineItem.taxes[]`, `Quote.computed.recurring.total_details.breakdown.taxes[]`,
`Quote.computed.upfront.total_details.breakdown.taxes[]`, and
`Quote.total_details.breakdown.taxes[]`
- Add support for `effective_percentage` on `TaxRate`

### May 10, 2023

- Add support for `brand`, `cardholder_name`, `country`, `exp_month`,
`exp_year`, `fingerprint`, `funding`, `last4`, `networks`, and `read_method` on
`PaymentMethod.card_present` and `PaymentMethod.interac_present`
- Add support for `preferred_locales` on `PaymentMethod.interac_present`
- Add support for `network_token` on `Charge.payment_method_details.card`

### May 9, 2023

- Add support for `paypal` on `Charge.payment_method_details`,
`Checkout.Session#create.payment_method_options`,
`Mandate.payment_method_details`, `PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_data`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_data`,
`SetupIntent#update.payment_method_options`, and
`SetupIntent.payment_method_options`
- Add support for new value `paypal` on enums
`Checkout.Session#create.payment_method_types[]` and `PaymentMethod#create.type`
- Add support for new value `paypal` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for new value `paypal` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for new value `paypal` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `paypal` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`
- Add support for new value `paypal` on enum `PaymentMethod.type`

### May 8, 2023

- Add support for new value `eftpos_au` on enums
`PaymentIntent#confirm.payment_method_options.card.network`,
`PaymentIntent#create.payment_method_options.card.network`,
`PaymentIntent#update.payment_method_options.card.network`,
`PaymentIntent.payment_method_options.card.network`,
`SetupIntent#confirm.payment_method_options.card.network`,
`SetupIntent#create.payment_method_options.card.network`,
`SetupIntent#update.payment_method_options.card.network`,
`SetupIntent.payment_method_options.card.network`,
`Subscription#create.payment_settings.payment_method_options.card.network`,
`Subscription#update.payment_settings.payment_method_options.card.network`, and
`Subscription.payment_settings.payment_method_options.card.network`

### May 2, 2023

- Add support for `link` on `Checkout.Session#create.payment_method_options` and
`Checkout.Session.payment_method_options`

### May 1, 2023

- Add support for `brand`, `country`, `description`, `exp_month`, `exp_year`,
`fingerprint`, `funding`, `iin`, `issuer`, `last4`, `network`, and `wallet` on
`SetupAttempt.payment_method_details.card`

### April 27, 2023

- Add support for `tax_breakdown` on `Tax.Calculation.shipping_cost` and
`Tax.Transaction.shipping_cost`

### April 26, 2023

- Add support for `billing_cycle_anchor` and `proration_behavior` on
`Checkout.Session#create.subscription_data`

### April 24, 2023

- Add support for `terminal_id` on `Issuing.Authorization.merchant_data` and
`Issuing.Transaction.merchant_data`

### April 22, 2023

- Add support for `checks` on `SetupAttempt.payment_method_details.card`

### April 21, 2023

- Add support for `metadata` on `PaymentIntent#capture`

### April 17, 2023

- Change `Identity.VerificationReport.options` and
`Identity.VerificationReport.type` to be optional
- Change type of `Identity.VerificationSession.options` from
`GelatoVerificationSessionOptions` to
`nullable(GelatoVerificationSessionOptions)`
- Change type of `Identity.VerificationSession.type` from
`enum('document'|'id_number')` to `nullable(enum('document'|'id_number'))`

### April 13, 2023

- Change `Checkout.Session.currency_conversion` to be required
- Add support for new value `REVOIE23` on enums
`Charge.payment_method_details.ideal.bic`, `PaymentMethod.ideal.bic`, and
`SetupAttempt.payment_method_details.ideal.bic`

### April 6, 2023

- Add support for new value `link` on enums
`Charge.payment_method_details.card.wallet.type` and
`PaymentMethod.card.wallet.type`
- Change `Issuing.Cardholder#create.type` to be optional
- Add support for `status_details` on `PaymentMethod.us_bank_account`

### March 31, 2023

- Add support for `country` on `PaymentMethod.link`

### March 30, 2023

- Remove support for `create` method on resource `Tax.Transaction`
- Add support for `export_license_id` and `export_purpose_code` on
`Account#create.company`, `Account#update.company`, `Account.company`, and
`Token#create.account.company`

### March 29, 2023

- Add support for `amount_tip` on
`Terminal.Reader.testHelpers#present_payment_method`

### March 27, 2023

- Remove support for value `deleted` from enum `Invoice.status`

### March 23, 2023

- Add support for new resources `Tax.CalculationLineItem`, `Tax.Calculation`,
`Tax.TransactionLineItem`, and `Tax.Transaction`
- Add support for `create` and `list_line_items` methods on resource
`Calculation`
- Add support for `create_from_calculation`, `create_reversal`, `create`,
`list_line_items`, and `retrieve` methods on resource `Transaction`

### March 22, 2023

- Add support for `currency_conversion` on `Checkout.Session`

### March 20, 2023

- Add support for new value `link` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`

### March 17, 2023

- Add support for `automatic_payment_methods` on `SetupIntent#create` and
`SetupIntent`
- Add support for new value `link` on enum
`Checkout.Session#create.payment_method_types[]`

### March 16, 2023

- Add support for `country` on `Charge.payment_method_details.link`
- Add support for new value `automatic_async` on enums
`Checkout.Session#create.payment_intent_data.capture_method`,
`PaymentIntent#confirm.capture_method`, `PaymentIntent#create.capture_method`,
`PaymentIntent#update.capture_method`, `PaymentIntent.capture_method`,
`PaymentLink#create.payment_intent_data.capture_method`, and
`PaymentLink.payment_intent_data.capture_method`
- Add support for `future_requirements` and `requirements` on `BankAccount`

### March 15, 2023

- Add support for `preferred_locale` on
`PaymentIntent#confirm.payment_method_options.affirm`,
`PaymentIntent#create.payment_method_options.affirm`,
`PaymentIntent#update.payment_method_options.affirm`, and
`PaymentIntent.payment_method_options.affirm`

### March 14, 2023

- Add support for `cashapp_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `cashapp` on `Charge.payment_method_details`,
`Mandate.payment_method_details`, `PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`, `SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `cashapp` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for new value `cashapp` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for new value `cashapp` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for `cashapp_handle_redirect_or_display_qr_code` on
`PaymentIntent.next_action` and `SetupIntent.next_action`
- Add support for new value `cashapp` on enum `PaymentMethod#create.type`
- Add support for new value `cashapp` on enum `PaymentMethod.type`

### March 10, 2023

- Add support for `cashapp` on `Checkout.Session#create.payment_method_options`
and `Checkout.Session.payment_method_options`
- Add support for new value `cashapp` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for new value `cashapp` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`

### March 9, 2023

- Add support for new value `payout.reconciliation_completed` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### March 7, 2023

- Add support for `card_issuing` on `Issuing.Cardholder#create.individual` and
`Issuing.Cardholder#update.individual`
- Add support for new value `requirements.past_due` on enum
`Issuing.Cardholder.requirements.disabled_reason`
- Add support for new values
`individual.card_issuing.user_terms_acceptance.date` and
`individual.card_issuing.user_terms_acceptance.ip` on enum
`Issuing.Cardholder.requirements.past_due[]`

### March 3, 2023

- Add support for `cancellation_details` on `Subscription#cancel`,
`Subscription#update`, and `Subscription`

### March 2, 2023

- Add support for new value `lease_tax` on enums `TaxRate#create.tax_type`,
`TaxRate#update.tax_type`, and `TaxRate.tax_type`
- Add support for `reconciliation_status` on `Payout`

### March 1, 2023

- Add support for new values `electric_vehicle_charging`,
`emergency_services_gcas_visa_use_only`,
`government_licensed_horse_dog_racing_us_region_only`,
`government_licensed_online_casions_online_gambling_us_region_only`,
`government_owned_lotteries_non_us_region`,
`government_owned_lotteries_us_region_only`, and `marketplaces` on enums
`Issuing.Card#create.spending_controls.allowed_categories[]`,
`Issuing.Card#create.spending_controls.blocked_categories[]`,
`Issuing.Card#create.spending_controls.spending_limits[].categories[]`,
`Issuing.Card#update.spending_controls.allowed_categories[]`,
`Issuing.Card#update.spending_controls.blocked_categories[]`,
`Issuing.Card#update.spending_controls.spending_limits[].categories[]`,
`Issuing.Card.spending_controls.allowed_categories[]`,
`Issuing.Card.spending_controls.blocked_categories[]`,
`Issuing.Card.spending_controls.spending_limits[].categories[]`,
`Issuing.Cardholder#create.spending_controls.allowed_categories[]`,
`Issuing.Cardholder#create.spending_controls.blocked_categories[]`,
`Issuing.Cardholder#create.spending_controls.spending_limits[].categories[]`,
`Issuing.Cardholder#update.spending_controls.allowed_categories[]`,
`Issuing.Cardholder#update.spending_controls.blocked_categories[]`,
`Issuing.Cardholder#update.spending_controls.spending_limits[].categories[]`,
`Issuing.Cardholder.spending_controls.allowed_categories[]`,
`Issuing.Cardholder.spending_controls.blocked_categories[]`, and
`Issuing.Cardholder.spending_controls.spending_limits[].categories[]`

### February 22, 2023

- Add support for new value `igst` on enums `TaxRate#create.tax_type`,
`TaxRate#update.tax_type`, and `TaxRate.tax_type`

### February 21, 2023

- Add support for new value `yoursafe` on enums
`Charge.payment_method_details.ideal.bank`,
`PaymentIntent#confirm.payment_method_data.ideal.bank`,
`PaymentIntent#create.payment_method_data.ideal.bank`,
`PaymentIntent#update.payment_method_data.ideal.bank`,
`PaymentMethod#create.ideal.bank`, `PaymentMethod.ideal.bank`,
`SetupAttempt.payment_method_details.ideal.bank`,
`SetupIntent#confirm.payment_method_data.ideal.bank`,
`SetupIntent#create.payment_method_data.ideal.bank`, and
`SetupIntent#update.payment_method_data.ideal.bank`
- Add support for new value `BITSNL2A` on enums
`Charge.payment_method_details.ideal.bic`, `PaymentMethod.ideal.bic`, and
`SetupAttempt.payment_method_details.ideal.bic`

### February 16, 2023

- Add support for new value `name` on enums
`BillingPortal.Configuration#create.features.customer_update.allowed_updates[]`,
`BillingPortal.Configuration#update.features.customer_update.allowed_updates[]`,
and `BillingPortal.Configuration.features.customer_update.allowed_updates[]`
- Add support for `refund_payment` method on resource `Terminal.Reader`
- Add support for `custom_fields` on `Checkout.Session#create`,
`Checkout.Session`, `PaymentLink#create`, `PaymentLink#update`, and
`PaymentLink`
- Add support for `interac_present` on
`Terminal.Reader.testHelpers#present_payment_method`
- Change type of `Terminal.Reader.testHelpers#present_payment_method.type` from
`literal('card_present')` to `enum('card_present'|'interac_present')`
- Add support for `refund_payment` on `Terminal.Reader.action`
- Add support for new value `refund_payment` on enum
`Terminal.Reader.action.type`

### February 13, 2023

- Change `Subscription.trial_settings.end_behavior` and
`Subscription.trial_settings` to be required

### February 2, 2023

- Add support for `payment_link` on `Checkout.Session#list`
- Add support for `shipping_cost` on `CreditNote#create`,
`CreditNote#preview_lines`, `CreditNote#preview`, `CreditNote`,
`Invoice#create`, `Invoice#update`, and `Invoice`
- Add support for `amount_shipping` on `CreditNote` and `Invoice`
- Add support for `shipping_details` on `Invoice#create`, `Invoice#update`, and
`Invoice`
- Change `PaymentLink.invoice_creation` to be required
- Add support for new value `America/Ciudad_Juarez` on enum
`Reporting.ReportRun#create.parameters.timezone`

### February 1, 2023

- Add support for `resume` method on resource `Subscription`
- Add support for `trial_settings` on
`CheckoutSessionCreateParams.subscription_data`, `SubscriptionCreateParams`,
`SubscriptionUpdateParams`, and `Subscription`
- Add support for `subscription_resume_at` on `InvoiceUpcomingLinesParams` and
`InvoiceUpcomingParams`
- Change `IssuingCardholderCreateParams.individual.first_name`,
`IssuingCardholderCreateParams.individual.last_name`,
`IssuingCardholderUpdateParams.individual.first_name`, and
`IssuingCardholderUpdateParams.individual.last_name` to be optional
- Change type of `Issuing.Cardholder.individual.first_name` and
`Issuing.Cardholder.individual.last_name` from `string` to `string | null`
- Add support for `invoice_creation` on `PaymentLinkCreateParams`,
`PaymentLinkUpdateParams`, and `PaymentLink`
- Add support for new value `paused` on enum `SubscriptionListParams.status`
- Add support for new value `paused` on enum `Subscription.status`
- Add support for new values `customer.subscription.paused` and
`customer.subscription.resumed` on enums
`WebhookEndpointCreateParams.enabled_events[]` and
`WebhookEndpointUpdateParams.enabled_events[]`

### January 26, 2023

- Add support for new value `BE` on enums
`Checkout.Session.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country`,
`Invoice.payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country`,
`PaymentIntent.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country`,
and
`Subscription.payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country`
- Add support for new values `cs-CZ`, `el-GR`, `en-CZ`, and `en-GR` on enums
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`

### January 18, 2023

- Add support for `verification_session` on `EphemeralKey#create`
- Add support for new values `refund.created` and `refund.updated` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### January 5, 2023

- Add support for `card_issuing` on `Issuing.Cardholder.individual`

### December 22, 2022

- Add support for new value `merchant_default` on enums
`CashBalance#update.settings.reconciliation_mode`,
`Customer#create.cash_balance.settings.reconciliation_mode`, and
`Customer#update.cash_balance.settings.reconciliation_mode`
- Add support for `using_merchant_default` on `CashBalance.settings`
- Change `Checkout.Session#create.cancel_url` to be optional
- Change type of `Checkout.Session.cancel_url` from `string` to
`nullable(string)`

### December 15, 2022

- Add support for new value `invoice_overpaid` on enum
`CustomerBalanceTransaction.type`

### December 8, 2022

- Change `Customer#list_payment_methods.type` and `PaymentMethod#list.type` to
be optional

### December 6, 2022

- Add support for `flow_data` on `BillingPortal.Session#create`
- Add support for `flow` on `BillingPortal.Session`
- Add support for `india_international_payments` on
`Account#create.capabilities`, `Account#update.capabilities`, and
`Account.capabilities`
- Add support for `invoice_creation` on `Checkout.Session#create` and
`Checkout.Session`
- Add support for `invoice` on `Checkout.Session`
- Add support for `metadata` on `SubscriptionSchedule#create.phases[].items[]`,
`SubscriptionSchedule#update.phases[].items[]`, and
`SubscriptionSchedule.phases[].items[]`

### November 17, 2022

- Add support for `hosted_instructions_url` on
`PaymentIntent.next_action.wechat_pay_display_qr_code`

### November 16, 2022

- Add support for `custom_text` on `Checkout.Session#create`,
`Checkout.Session`, `PaymentLink#create`, `PaymentLink#update`, and
`PaymentLink`
- Add support for `hosted_instructions_url` on
`PaymentIntent.next_action.paynow_display_qr_code`
- Remove support for resources `Order` and `Sku`
- Remove support for `cancel`, `create`, `list_line_items`, `list`, `reopen`,
`retrieve`, `submit`, and `update` methods on resource `Order`
- Remove support for `create`, `delete`, `list`, `retrieve`, and `update`
methods on resource `Sku`
- Change type of `Charge.refunds` from `apiList($Refund)` to
`nullable(apiList($Refund))`
- Change `Charge.refunds` to be required
- Remove support for `amount`, `currency`, `description`, `images`, and `name`
on `Checkout.Session#create.line_items[]`
- Remove support for `items` on `Checkout.Session#create.subscription_data`
- Remove support for `product` on `LineItem`
- Add support for `latest_charge` on `PaymentIntent`
- Remove support for `charges` on `PaymentIntent`
- Add support for new value `2022-11-15` on enum
`WebhookEndpoint#create.api_version`

### November 10, 2022

- Remove support for `tos_shown_and_accepted` on
`Checkout.Session#create.payment_method_options.paynow`

### November 7, 2022

- Add support for `reason_message` on `Issuing.Authorization.request_history[]`
- Add support for new value `webhook_error` on enum
`Issuing.Authorization.request_history[].reason`

### November 1, 2022

- Add support for new values `eg_tin`, `ph_tin`, and `tr_tin` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`, `Order.tax_details.tax_ids[].type`, and
`TaxId.type`
- Add support for new values `eg_tin`, `ph_tin`, and `tr_tin` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Order#create.tax_details.tax_ids[].type`,
`Order#update.tax_details.tax_ids[].type`, and `TaxId#create.type`

### October 31, 2022

- Add support for `on_behalf_of` on `Checkout.Session#create.subscription_data`,
`Subscription#create`, `Subscription#update`,
`SubscriptionSchedule#create.default_settings`,
`SubscriptionSchedule#create.phases[]`,
`SubscriptionSchedule#update.default_settings`,
`SubscriptionSchedule#update.phases[]`, `SubscriptionSchedule.default_settings`,
`SubscriptionSchedule.phases[]`, and `Subscription`
- Add support for `tax_behavior` and `tax_code` on
`Invoice#upcoming.invoice_items[]`, `Invoice#upcomingLines.invoice_items[]`,
`InvoiceItem#create`, and `InvoiceItem#update`

### October 20, 2022

- Add support for new values `jp_trn` and `ke_pin` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`, `Order.tax_details.tax_ids[].type`, and
`TaxId.type`
- Add support for new values `jp_trn` and `ke_pin` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Order#create.tax_details.tax_ids[].type`,
`Order#update.tax_details.tax_ids[].type`, and `TaxId#create.type`
- Add support for `tipping` on
`Terminal.Reader#process_payment_intent.process_config` and
`Terminal.Reader.action.process_payment_intent.process_config`

### October 13, 2022

- Add support for new values `invalid_representative_country` and
`verification_failed_residential_address` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`Capability.future_requirements.errors[].code`,
`Capability.requirements.errors[].code`,
`Person.future_requirements.errors[].code`, and
`Person.requirements.errors[].code`
- Add support for `request_log_url` on `Invoice.last_finalization_error`,
`PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`,
`SetupIntent.last_setup_error`, `StripeErrorResponse.error`, and `StripeError`
- Add support for `network_data` on `Issuing.Authorization`

### October 4, 2022

- Add support for new value `invalid_dob_age_under_18` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`Capability.future_requirements.errors[].code`,
`Capability.requirements.errors[].code`,
`Person.future_requirements.errors[].code`, and
`Person.requirements.errors[].code`
- Add support for new values `America/Nuuk`, `Europe/Kyiv`, and `Pacific/Kanton`
on enum `Reporting.ReportRun#create.parameters.timezone`
- Add support for `klarna` on `SetupAttempt.payment_method_details`

### September 28, 2022

- Change type of
`Charge.payment_method_details.card_present.incremental_authorization_supported`
and `Charge.payment_method_details.card_present.overcapture_supported` from
`nullable(boolean)` to `boolean`
- Add support for `created` on `Checkout.Session`
- Add support for `setup_future_usage` on
`PaymentIntent#confirm.payment_method_options.pix`,
`PaymentIntent#create.payment_method_options.pix`,
`PaymentIntent#update.payment_method_options.pix`, and
`PaymentIntent.payment_method_options.pix`

### September 22, 2022

- Add support for `statement_descriptor` on
`PaymentIntent#increment_authorization`

### September 20, 2022

- Add support for `terms_of_service` on
`Checkout.Session#create.consent_collection`,
`Checkout.Session.consent_collection`, `Checkout.Session.consent`,
`PaymentLink#create.consent_collection`, and `PaymentLink.consent_collection`
- Remove support for `plan` on
`Checkout.Session#create.payment_method_options.card.installments`
- Change `SubscriptionSchedule.phases[].currency` to be required

### September 15, 2022

- Add support for `amount` on `Issuing.Dispute#create` and
`Issuing.Dispute#update`

### September 14, 2022

- Add support for `pix` on `Charge.payment_method_details`,
`Checkout.Session#create.payment_method_options`,
`Checkout.Session.payment_method_options`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `pix` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for new value `pix` on enums `Customer#list_payment_methods.type`
and `PaymentMethod#list.type`
- Add support for `from_invoice` on `Invoice#create` and `Invoice`
- Add support for `latest_revision` on `Invoice`
- Add support for new value `pix` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for `pix_display_qr_code` on `PaymentIntent.next_action`
- Add support for new value `pix` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`
- Add support for new value `pix` on enum `PaymentMethod#create.type`
- Add support for new value `pix` on enum `PaymentMethod.type`
- Add support for `created` on `Treasury.DebitReversal`

### September 8, 2022

- Add support for `require_signature` on `Issuing.Card#create.shipping` and
`Issuing.Card.shipping`
- Add support for `proration_behavior=always_invoice` when creating a
Subscription Schedule.

### September 6, 2022

- Add support for new value `terminal_reader_splashscreen` on enums
`File#list.purpose` and `File.purpose`

### August 31, 2022

- Add support for new values `de-CH`, `en-CH`, `en-PL`, `en-PT`, `fr-CH`,
`it-CH`, `pl-PL`, and `pt-PT` on enums
`Order#create.payment.settings.payment_method_options.klarna.preferred_locale`,
`Order#update.payment.settings.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`
- Add support for `description` on `PaymentLink#create.subscription_data` and
`PaymentLink.subscription_data`

### August 26, 2022

- Change `Account.company.name`, `Charge.refunds`, `PaymentIntent.charges`,
`Product.caption`, `Product.statement_descriptor`, `Product.unit_label`,
`Terminal.Configuration.tipping.aud.fixed_amounts`,
`Terminal.Configuration.tipping.aud.percentages`,
`Terminal.Configuration.tipping.cad.fixed_amounts`,
`Terminal.Configuration.tipping.cad.percentages`,
`Terminal.Configuration.tipping.chf.fixed_amounts`,
`Terminal.Configuration.tipping.chf.percentages`,
`Terminal.Configuration.tipping.czk.fixed_amounts`,
`Terminal.Configuration.tipping.czk.percentages`,
`Terminal.Configuration.tipping.dkk.fixed_amounts`,
`Terminal.Configuration.tipping.dkk.percentages`,
`Terminal.Configuration.tipping.eur.fixed_amounts`,
`Terminal.Configuration.tipping.eur.percentages`,
`Terminal.Configuration.tipping.gbp.fixed_amounts`,
`Terminal.Configuration.tipping.gbp.percentages`,
`Terminal.Configuration.tipping.hkd.fixed_amounts`,
`Terminal.Configuration.tipping.hkd.percentages`,
`Terminal.Configuration.tipping.myr.fixed_amounts`,
`Terminal.Configuration.tipping.myr.percentages`,
`Terminal.Configuration.tipping.nok.fixed_amounts`,
`Terminal.Configuration.tipping.nok.percentages`,
`Terminal.Configuration.tipping.nzd.fixed_amounts`,
`Terminal.Configuration.tipping.nzd.percentages`,
`Terminal.Configuration.tipping.sek.fixed_amounts`,
`Terminal.Configuration.tipping.sek.percentages`,
`Terminal.Configuration.tipping.sgd.fixed_amounts`,
`Terminal.Configuration.tipping.sgd.percentages`,
`Terminal.Configuration.tipping.usd.fixed_amounts`,
`Terminal.Configuration.tipping.usd.percentages`,
`Treasury.FinancialAccount.active_features`,
`Treasury.FinancialAccount.pending_features`,
`Treasury.FinancialAccount.platform_restrictions`, and
`Treasury.FinancialAccount.restricted_features` to be optional
- Add support for `login_page` on `BillingPortal.Configuration#create`,
`BillingPortal.Configuration#update`, and `BillingPortal.Configuration`
- Add support for new value `deutsche_bank_ag` on enums
`Charge.payment_method_details.eps.bank`,
`PaymentIntent#confirm.payment_method_data.eps.bank`,
`PaymentIntent#create.payment_method_data.eps.bank`,
`PaymentIntent#update.payment_method_data.eps.bank`,
`PaymentMethod#create.eps.bank`, `PaymentMethod.eps.bank`,
`SetupIntent#confirm.payment_method_data.eps.bank`,
`SetupIntent#create.payment_method_data.eps.bank`, and
`SetupIntent#update.payment_method_data.eps.bank`
- Add support for `description` on `Quote#create.subscription_data`,
`Quote#update.subscription_data`, `Quote.subscription_data`,
`SubscriptionSchedule#create.default_settings`,
`SubscriptionSchedule#create.phases[]`,
`SubscriptionSchedule#update.default_settings`,
`SubscriptionSchedule#update.phases[]`, `SubscriptionSchedule.default_settings`,
and `SubscriptionSchedule.phases[]`

### August 24, 2022

- Add support for `customs` and `phone_number` on `Issuing.Card#create.shipping`
and `Issuing.Card.shipping`

### August 23, 2022

- Change `Terminal.Reader.action` to be required
- Change `Treasury.OutboundTransfer#create.destination_payment_method` to be
optional
- Change type of `Treasury.OutboundTransfer.destination_payment_method` from
`string` to `nullable(string)`

### August 18, 2022

- Add support for new resource `CustomerCashBalanceTransaction`
- Remove support for value `paypal` from enums
`Order#create.payment.settings.payment_method_types[]`,
`Order#update.payment.settings.payment_method_types[]`, and
`Order.payment.settings.payment_method_types[]`
- Add support for `network` on
`SetupIntent#confirm.payment_method_options.card`,
`SetupIntent#create.payment_method_options.card`,
`SetupIntent#update.payment_method_options.card`,
`Subscription#create.payment_settings.payment_method_options.card`,
`Subscription#update.payment_settings.payment_method_options.card`, and
`Subscription.payment_settings.payment_method_options.card`
- Add support for new value `customer_cash_balance_transaction.created` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### August 11, 2022

- Add support for `payment_method_collection` on `Checkout.Session#create`,
`Checkout.Session`, `PaymentLink#create`, `PaymentLink#update`, and
`PaymentLink`

### August 9, 2022

- Add support for `process_config` on
`Terminal.Reader.action.process_payment_intent`

### August 5, 2022

- Add support for `expires_at` on `Apps.Secret#create` and `Apps.Secret`

### August 1, 2022

- Remove support for deprecated resources `AlipayAccount`, `BitcoinReceiver`,
`BitcoinTransaction`, `IssuerFraudRecord`, `Recipient`, and `ThreeDSecure`
- Remove support for deprecated values `order.payment_failed`,
`order.payment_succeeded`, `order.updated`, `order_return.created`,
`transfer.failed`, and `transfer.paid` from enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Remove support for `default_currency` on `Customer`
- Remove support for `list` method on resource `LineItem`
- Remove support for `recipient` on `Card`
- Remove support for `redirect_url` on `LoginLink#create`
- Remove support for `shipping_rate` and `shipping` on `Checkout.Session`
- Remove support for `trial_end` on `Customer#update`
- Add support for `list_line_items` method on resource `Checkout.Session`
- Add support for `shipping_cost` and `shipping_details` on `Checkout.Session`
- Add support for `validate` on `Customer#create`, `Customer#update`, and
`PaymentSource#create`
- Add support for new value `2022-08-01` on enum
`WebhookEndpoint#create.api_version`
- Add support for new value `design_rejected` on enum
`Issuing.Card.cancellation_reason`
- Add support for new value `invalid_tos_acceptance` on enums
`Account.future_requirements.errors[].code`,
`Account.requirements.errors[].code`,
`Capability.future_requirements.errors[].code`,
`Capability.requirements.errors[].code`,
`Person.future_requirements.errors[].code`, and
`Person.requirements.errors[].code`

### July 26, 2022

- Add support for new value `exempted` on enums
`Charge.payment_method_details.card.three_d_secure.result` and
`SetupAttempt.payment_method_details.card.three_d_secure.result`
- Add support for `customer_balance` on
`Checkout.Session#create.payment_method_options` and
`Checkout.Session.payment_method_options`
- Add support for new value `customer_balance` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for new values `en-CA` and `fr-CA` on enums
`Order#create.payment.settings.payment_method_options.klarna.preferred_locale`,
`Order#update.payment.settings.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`

### July 22, 2022

- Remove support for resource `InstallmentsOptions`
- Add support for `installments` on
`Invoice.payment_settings.payment_method_options.card`
- Add support for new resource `InstallmentsOptions`
- Add support for `installments` on
`Checkout.Session#create.payment_method_options.card`,
`Checkout.Session.payment_method_options.card`,
`Invoice#create.payment_settings.payment_method_options.card`,
`Invoice#update.payment_settings.payment_method_options.card`, and
`PaymentIntentTypeSpecificPaymentMethodOptionsClient`
- Add support for `product_data` on `Order#create.line_items[]` and
`Order#update.line_items[]`

### July 21, 2022

- Add support for `default_mandate` on `Invoice#create.payment_settings`,
`Invoice#update.payment_settings`, and `Invoice.payment_settings`
- Add support for `mandate` on `Invoice#pay`

### July 20, 2022

- Add support for `default_currency` and `invoice_credit_balance` on `Customer`
- Add support for `currency` on `Invoice#create`

### July 18, 2022

- Add support for `blik_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `blik` on `Charge.payment_method_details`,
`Mandate.payment_method_details`, `PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`, `SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_data`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_data`,
`SetupIntent#update.payment_method_options`, and
`SetupIntent.payment_method_options`
- Change type of `Checkout.Session#create.consent_collection.promotions`,
`Checkout.Session.consent_collection.promotions`,
`PaymentLink#create.consent_collection.promotions`, and
`PaymentLink.consent_collection.promotions` from `literal('auto')` to
`enum('auto'|'none')`
- Add support for new value `blik` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for new value `blik` on enums `Customer#list_payment_methods.type`
and `PaymentMethod#list.type`
- Add support for new value `blik` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new value `blik` on enums
`PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]`
- Add support for new value `blik` on enum `PaymentMethod#create.type`
- Add support for new value `blik` on enum `PaymentMethod.type`

### July 12, 2022

- Add support for `customer_details` on `Checkout.Session#list`
- Change `LineItem.amount_discount` and `LineItem.amount_tax` to be required
- Change type of `Transfer.source_type` from `nullable(string)` to `string`
- Change `Transfer.source_type` to be optional

### July 7, 2022

- Add support for `currency` on `Checkout.Session#create`,
`Invoice#upcomingLines`, `Invoice#upcoming`, `PaymentLink#create`,
`Subscription#create`, `SubscriptionSchedule#create.phases[]`,
`SubscriptionSchedule#update.phases[]`, `SubscriptionSchedule.phases[]`, and
`Subscription`
- Add support for `currency_options` on
`Checkout.Session#create.shipping_options[].shipping_rate_data.fixed_amount`,
`Coupon#create`, `Coupon#update`, `Coupon`,
`Order#create.shipping_cost.shipping_rate_data.fixed_amount`,
`Order#update.shipping_cost.shipping_rate_data.fixed_amount`, `Price#create`,
`Price#update`, `Price`, `Product#create.default_price_data`,
`PromotionCode#create.restrictions`, `PromotionCode.restrictions`,
`ShippingRate#create.fixed_amount`, and `ShippingRate.fixed_amount`
- Add support for `restrictions` on `PromotionCode#update`
- Add support for `fixed_amount` and `tax_behavior` on `ShippingRate#update`

### July 6, 2022

- Add support for `customer` on `Checkout.Session#list` and `Refund#create`
- Add support for `currency` and `origin` on `Refund#create`
- Add support for new values `financial_connections.account.created`,
`financial_connections.account.deactivated`,
`financial_connections.account.disconnected`,
`financial_connections.account.reactivated`, and
`financial_connections.account.refreshed_balance` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### June 29, 2022

- Add support for `deliver_card`, `fail_card`, `return_card`, and `ship_card`
test helper methods on resource `Issuing.Card`
- Change type of `PaymentLink#create.payment_method_types[]`,
`PaymentLink#update.payment_method_types[]`, and
`PaymentLink.payment_method_types[]` from `literal('card')` to `enum`
- Add support for `hosted_regulatory_receipt_url` on `Treasury.ReceivedCredit`
and `Treasury.ReceivedDebit`
- Remove support for value `treasury.received_credit.reversed` from enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### June 23, 2022

- Add support for `capture_method` on `PaymentIntent#confirm` and
`PaymentIntent#update`
- Change `Price.custom_unit_amount` to be required
- Add support for `reversal_details` on `Treasury.ReceivedCredit` and
`Treasury.ReceivedDebit`
- Add support for `debit_reversal` on `Treasury.ReceivedDebit.linked_flows`

### June 21, 2022

- Add support for `promptpay_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `promptpay` on `Charge.payment_method_details`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for new value `promptpay` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for `subtotal_excluding_tax` on `CreditNote` and `Invoice`
- Add support for `amount_excluding_tax` and `unit_amount_excluding_tax` on
`CreditNoteLineItem` and `InvoiceLineItem`
- Add support for new value `promptpay` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for `rendering_options` on `Invoice#create` and `Invoice#update`
- Add support for new value `promptpay` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for `total_excluding_tax` on `Invoice`
- Add support for `automatic_payment_methods` on `Order.payment.settings`
- Add support for new value `promptpay` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for `promptpay_display_qr_code` on `PaymentIntent.next_action`
- Add support for new value `promptpay` on enum `PaymentMethod#create.type`
- Add support for new value `promptpay` on enum `PaymentMethod.type`

### June 17, 2022

- Add support for `fund_cash_balance` test helper method on resource `Customer`
- Remove support for `fund_cash_balance` test helper method on resource
`CustomerBalanceTransaction`

### June 16, 2022

- Remove support for `list_funding_instructions` method on resource `Customer`

### June 7, 2022

- Add support for `affirm`, `afterpay_clearpay`, `au_becs_debit`, `bacs_debit`,
`bancontact`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `p24`,
`paynow`, `sepa_debit`, and `sofort` on
`Checkout.Session#create.payment_method_options`
- Add support for `card` on `Checkout.Session#create.payment_method_options` and
`Checkout.Session.payment_method_options`
- Add support for `setup_future_usage` on
`Checkout.Session#create.payment_method_options.acss_debit`,
`Checkout.Session#create.payment_method_options.alipay`,
`Checkout.Session#create.payment_method_options.boleto`,
`Checkout.Session#create.payment_method_options.konbini`,
`Checkout.Session#create.payment_method_options.oxxo`,
`Checkout.Session#create.payment_method_options.us_bank_account`,
`Checkout.Session#create.payment_method_options.wechat_pay`,
`Checkout.Session.payment_method_options.acss_debit`,
`Checkout.Session.payment_method_options.affirm`,
`Checkout.Session.payment_method_options.afterpay_clearpay`,
`Checkout.Session.payment_method_options.alipay`,
`Checkout.Session.payment_method_options.au_becs_debit`,
`Checkout.Session.payment_method_options.bacs_debit`,
`Checkout.Session.payment_method_options.bancontact`,
`Checkout.Session.payment_method_options.boleto`,
`Checkout.Session.payment_method_options.eps`,
`Checkout.Session.payment_method_options.fpx`,
`Checkout.Session.payment_method_options.giropay`,
`Checkout.Session.payment_method_options.grabpay`,
`Checkout.Session.payment_method_options.ideal`,
`Checkout.Session.payment_method_options.klarna`,
`Checkout.Session.payment_method_options.konbini`,
`Checkout.Session.payment_method_options.oxxo`,
`Checkout.Session.payment_method_options.p24`,
`Checkout.Session.payment_method_options.paynow`,
`Checkout.Session.payment_method_options.sepa_debit`,
`Checkout.Session.payment_method_options.sofort`, and
`Checkout.Session.payment_method_options.us_bank_account`
- Change `PaymentMethod.us_bank_account.networks` and
`SetupIntent.flow_directions` to be required
- Add support for `attach_to_self` on `SetupAttempt`, `SetupIntent#create`,
`SetupIntent#list`, and `SetupIntent#update`
- Add support for `flow_directions` on `SetupAttempt`, `SetupIntent#create`, and
`SetupIntent#update`

### June 6, 2022

- Add support for `affirm`, `bancontact`, `ideal`, `p24`, and `sofort` on
`Checkout.Session.payment_method_options`

### June 1, 2022

- Add support for `radar_options` on `Charge#create`, `Charge`,
`PaymentIntent#confirm.payment_method_data`, `PaymentIntent#confirm`,
`PaymentIntent#create.payment_method_data`, `PaymentIntent#create`,
`PaymentIntent#update.payment_method_data`, `PaymentMethod#create`,
`PaymentMethod`, `SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for `account_holder_name`, `account_number`, `account_type`,
`bank_code`, `bank_name`, `branch_code`, and `branch_name` on
`FundingInstructions.bank_transfer.financial_addresses[].zengin` and
`PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].zengin`
- Add support for new values `en-AU` and `en-NZ` on enums
`Order#create.payment.settings.payment_method_options.klarna.preferred_locale`,
`Order#update.payment.settings.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`
- Change type of
`Order.payment.settings.payment_method_options.customer_balance.bank_transfer.type`
and `PaymentIntent.payment_method_options.customer_balance.bank_transfer.type`
from `enum` to `literal('jp_bank_transfer')`
- Change
`PaymentIntent.next_action.display_bank_transfer_instructions.hosted_instructions_url`
to be required
- Add support for `network` on `SetupIntent.payment_method_options.card`
- Add support for new value `simulated_wisepos_e` on enums
`Terminal.Reader#list.device_type` and `Terminal.Reader.device_type`

### May 26, 2022

- Add support for `affirm_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `id_number_secondary` on `Account#create.individual`,
`Account#update.individual`, `Person#create`, `Person#update`,
`Token#create.account.individual`, and `Token#create.person`
- Add support for new value `affirm` on enum
`Checkout.Session#create.payment_method_types[]`
- Add support for `hosted_instructions_url` on
`PaymentIntent.next_action.display_bank_transfer_instructions`
- Add support for `id_number_secondary_provided` on `Person`
- Add support for `card_issuing` on `Treasury.FinancialAccount#create.features`,
`Treasury.FinancialAccount#update.features`, and
`Treasury.FinancialAccount#update_features`

### May 25, 2022

- Add support for `persons` method on resource `Account`
- Add support for `balance_transactions` method on resource `Customer`
- Add support for `link_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`

### May 23, 2022

- Add support for `treasury` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for new resource `Apps.Secret`
- Add support for `affirm` on `Charge.payment_method_details`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#create.payment_method_data`, and
`SetupIntent#update.payment_method_data`
- Add support for `link` on `Charge.payment_method_details`,
`Mandate.payment_method_details`,
`Order#create.payment.settings.payment_method_options`,
`Order#update.payment.settings.payment_method_options`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`, `SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_data`,
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_data`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_data`,
`SetupIntent#update.payment_method_options`, and
`SetupIntent.payment_method_options`
- Add support for new values `affirm` and `link` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for new value `link` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for new values `affirm` and `link` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`SetupIntent#confirm.payment_method_data.type`,
`SetupIntent#create.payment_method_data.type`, and
`SetupIntent#update.payment_method_data.type`
- Add support for new values `affirm` and `link` on enum
`PaymentMethod#create.type`
- Add support for new values `affirm` and `link` on enum `PaymentMethod.type`

### May 19, 2022

- Change
`BillingPortal.Configuration#create.features.customer_update.allowed_updates` to
be optional
- Add support for `financial_account` on `Issuing.Card`
- Add support for new values `treasury.credit_reversal.created`,
`treasury.credit_reversal.posted`, `treasury.debit_reversal.completed`,
`treasury.debit_reversal.created`,
`treasury.debit_reversal.initial_credit_granted`,
`treasury.financial_account.closed`, `treasury.financial_account.created`,
`treasury.financial_account.features_status_updated`,
`treasury.inbound_transfer.canceled`, `treasury.inbound_transfer.created`,
`treasury.inbound_transfer.failed`, `treasury.inbound_transfer.succeeded`,
`treasury.outbound_payment.canceled`, `treasury.outbound_payment.created`,
`treasury.outbound_payment.expected_arrival_date_updated`,
`treasury.outbound_payment.failed`, `treasury.outbound_payment.posted`,
`treasury.outbound_payment.returned`, `treasury.outbound_transfer.canceled`,
`treasury.outbound_transfer.created`,
`treasury.outbound_transfer.expected_arrival_date_updated`,
`treasury.outbound_transfer.failed`, `treasury.outbound_transfer.posted`,
`treasury.outbound_transfer.returned`, `treasury.received_credit.created`,
`treasury.received_credit.failed`, `treasury.received_credit.reversed`,
`treasury.received_credit.succeeded`, and `treasury.received_debit.created` on
enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`
- Remove support for resources `Treasury.BillingDetails` and
`Treasury.InitiatingPaymentMethodDetails`
- Add support for `save_default_payment_method` on
`Subscription#create.payment_settings`, `Subscription#update.payment_settings`,
and `Subscription.payment_settings`
- Add support for `czk` on `Terminal.Configuration#create.tipping`,
`Terminal.Configuration#update.tipping`, and `Terminal.Configuration.tipping`
- Change type of `Treasury.FinancialAccountFeatures.object` from
`literal('treasury.financial_account.features')` to
`literal('treasury.financial_account_features')`

### May 17, 2022

- Add support for new resource `Treasury.FinancialAccountFeatures`
- Add support for `retrieve_payment_method` method on resource `Customer`
- Change type of `BillingPortal.Session.return_url` from `string` to
`nullable(string)`
- Change type of `Treasury.FinancialAccount.features` from `$Features` to
`$Treasury.FinancialAccountFeatures`
- Add support for new value `issuing_authorization` on enum
`Treasury.TransactionEntry.flow_type`
- Add support for new values `issuing_authorization_hold` and
`issuing_authorization_release` on enum `Treasury.TransactionEntry.type`
- Remove support for values `received_hold_release` and `received_hold` from
enum `Treasury.TransactionEntry.type`

### May 13, 2022

- Add support for new resources `Treasury.BillingDetails`,
`Treasury.CreditReversal`, `Treasury.DebitReversal`,
`Treasury.FinancialAccount`, `Treasury.FlowDetails`, `Treasury.InboundTransfer`,
`Treasury.InitiatingPaymentMethodDetails`, `Treasury.OutboundPayment`,
`Treasury.OutboundTransfer`, `Treasury.ReceivedCredit`,
`Treasury.ReceivedDebit`, `Treasury.TransactionEntry`, and
`Treasury.Transaction`
- Add support for `list_owners` and `list` methods on resource
`FinancialConnections.Account`
- Add support for `afterpay_clearpay`, `au_becs_debit`, `bacs_debit`, `eps`,
`fpx`, `giropay`, `grabpay`, `klarna`, `paynow`, and `sepa_debit` on
`Checkout.Session.payment_method_options`
- Add support for `treasury` on `Issuing.Authorization`,
`Issuing.Dispute#create`, `Issuing.Dispute`, and `Issuing.Transaction`
- Add support for `financial_account` on `Issuing.Card#create`
- Add support for `client_secret` on `Order`
- Add support for `networks` on
`PaymentIntent#confirm.payment_method_options.us_bank_account`,
`PaymentIntent#create.payment_method_options.us_bank_account`,
`PaymentIntent#update.payment_method_options.us_bank_account`,
`PaymentMethod.us_bank_account`,
`SetupIntent#confirm.payment_method_options.us_bank_account`,
`SetupIntent#create.payment_method_options.us_bank_account`, and
`SetupIntent#update.payment_method_options.us_bank_account`
- Add support for `attach_to_self` and `flow_directions` on `SetupIntent`

### May 11, 2022

- Add support for `description` on `Checkout.Session#create.subscription_data`,
`Subscription#create`, `Subscription#update`, and `Subscription`
- Add support for `consent_collection`, `payment_intent_data`,
`shipping_options`, `submit_type`, and `tax_id_collection` on
`PaymentLink#create` and `PaymentLink`
- Add support for `customer_creation` on `PaymentLink#create`,
`PaymentLink#update`, and `PaymentLink`
- Add support for `metadata` on `SubscriptionSchedule#create.phases[]`,
`SubscriptionSchedule#update.phases[]`, and `SubscriptionSchedule.phases[]`
- Add support for new value `billing_portal.session.created` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### May 5, 2022

- Add support for new resource `FinancialConnections.AccountOwnership`
- Change type of `FinancialConnections.Account.ownership` from `$Ownership` to
`$FinancialConnections.AccountOwnership`
- Add support for `id` and `object` on `FinancialConnections.AccountOwner`
- Add support for `default_price_data` on `Product#create`
- Add support for `default_price` on `Product#update` and `Product`
- Add support for `instructions_email` on `Refund#create` and `Refund`

### May 4, 2022

- Add support for new resources `FinancialConnections.AccountOwner`,
`FinancialConnections.Account`, and `FinancialConnections.Session`
- Add support for `financial_connections` on
`Checkout.Session#create.payment_method_options.us_bank_account`,
`Checkout.Session.payment_method_options.us_bank_account`,
`Invoice#create.payment_settings.payment_method_options.us_bank_account`,
`Invoice#update.payment_settings.payment_method_options.us_bank_account`,
`Invoice.payment_settings.payment_method_options.us_bank_account`,
`PaymentIntent#confirm.payment_method_options.us_bank_account`,
`PaymentIntent#create.payment_method_options.us_bank_account`,
`PaymentIntent#update.payment_method_options.us_bank_account`,
`PaymentIntent.payment_method_options.us_bank_account`,
`SetupIntent#confirm.payment_method_options.us_bank_account`,
`SetupIntent#create.payment_method_options.us_bank_account`,
`SetupIntent#update.payment_method_options.us_bank_account`,
`SetupIntent.payment_method_options.us_bank_account`,
`Subscription#create.payment_settings.payment_method_options.us_bank_account`,
`Subscription#update.payment_settings.payment_method_options.us_bank_account`,
and `Subscription.payment_settings.payment_method_options.us_bank_account`
- Add support for `financial_connections_account` on
`PaymentIntent#confirm.payment_method_data.us_bank_account`,
`PaymentIntent#create.payment_method_data.us_bank_account`,
`PaymentIntent#update.payment_method_data.us_bank_account`,
`PaymentMethod#create.us_bank_account`, `PaymentMethod.us_bank_account`,
`SetupIntent#confirm.payment_method_data.us_bank_account`,
`SetupIntent#create.payment_method_data.us_bank_account`, and
`SetupIntent#update.payment_method_data.us_bank_account`
- Add support for `registered_address` on `Account#create.individual`,
`Account#update.individual`, `Person#create`, `Person#update`, `Person`,
`Token#create.account.individual`, and `Token#create.person`
- Change type of `PaymentIntent.amount_details.tip.amount` from
`nullable(integer)` to `integer`
- Change `PaymentIntent.amount_details.tip.amount` to be optional
- Add support for `payment_method_data` on `SetupIntent#confirm`,
`SetupIntent#create`, and `SetupIntent#update`

### May 2, 2022

- Add support for new resource `CashBalance`
- Change type of `BillingPortal.Configuration.application` from `$Application`
to `deletable($Application)`
- Add support for `alipay` on `Checkout.Session#create.payment_method_options`
and `Checkout.Session.payment_method_options`
- Change type of
`Checkout.Session#create.payment_method_options.konbini.expires_after_days` from
`emptyStringable(integer)` to `integer`
- Add support for new value `eu_oss_vat` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`, and `TaxId.type`
- Add support for new value `eu_oss_vat` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`, and `TaxId#create.type`
- Add support for `cash_balance` on `Customer`
- Add support for `application` on `Invoice`, `Quote`, `SubscriptionSchedule`,
and `Subscription`

### April 20, 2022

- Change type of `BillingPortal.Configuration.application` from `string` to
`expandable($Application)`
- Change `Issuing.Dispute#create.transaction` to be optional

### April 18, 2022

- Add support for `create_funding_instructions` method on resource `Customer`
- Remove support for `create` and `list` methods on resource
`FundingInstructions`
- Add support for `amount_details` on `PaymentIntent`

### April 15, 2022

- Add support for `verifone_p400` on `Terminal.Configuration#create`,
`Terminal.Configuration#update`, and `Terminal.Configuration`
- Remove support for `verifone_P400` on `Terminal.Configuration#create`,
`Terminal.Configuration#update`, and `Terminal.Configuration`

### April 13, 2022

- Add support for new resource `Terminal.Configuration`
- Add support for `configuration_overrides` on `Terminal.Location#create`,
`Terminal.Location#update`, and `Terminal.Location`
- Add support for new resource `FundingInstructions`
- Add support for `customer_balance` on `Charge.payment_method_details`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, and
`PaymentMethod`
- Add support for `cash_balance` on `Customer#create` and `Customer#update`
- Add support for new value `customer_balance` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for new value `customer_balance` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`, and
`PaymentIntent#update.payment_method_data.type`
- Add support for `display_bank_transfer_instructions` on
`PaymentIntent.next_action`
- Add support for new value `customer_balance` on enum
`PaymentMethod#create.type`
- Add support for new value `customer_balance` on enum `PaymentMethod.type`
- Add support for `increment_authorization` method on resource `PaymentIntent`
- Add support for `incremental_authorization_supported` on
`Charge.payment_method_details.card_present`
- Add support for `request_incremental_authorization_support` on
`PaymentIntent#confirm.payment_method_options.card_present`,
`PaymentIntent#create.payment_method_options.card_present`,
`PaymentIntent#update.payment_method_options.card_present`, and
`PaymentIntent.payment_method_options.card_present`

### April 7, 2022

- Add support for `apply_customer_balance` method on resource `PaymentIntent`
- Add support for new value `cash_balance.funds_available` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### April 1, 2022

- Add support for `capture_before` on
`Charge.payment_method_details.card_present`
- Remove support for `eu_bank_transfer` on
`Invoice#create.payment_settings.payment_method_options.customer_balance.bank_transfer`,
`Invoice#update.payment_settings.payment_method_options.customer_balance.bank_transfer`,
`Invoice.payment_settings.payment_method_options.customer_balance.bank_transfer`,
`Subscription#create.payment_settings.payment_method_options.customer_balance.bank_transfer`,
`Subscription#update.payment_settings.payment_method_options.customer_balance.bank_transfer`,
and
`Subscription.payment_settings.payment_method_options.customer_balance.bank_transfer`
- Add support for `request_extended_authorization` on
`PaymentIntent#confirm.payment_method_options.card_present`,
`PaymentIntent#create.payment_method_options.card_present`,
`PaymentIntent#update.payment_method_options.card_present`, and
`PaymentIntent.payment_method_options.card_present`

### March 31, 2022

- Add support for `bank_transfer_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `address` and `name` on `Checkout.Session.customer_details`
- Add support for `customer_balance` on
`Invoice#create.payment_settings.payment_method_options`,
`Invoice#update.payment_settings.payment_method_options`,
`Invoice.payment_settings.payment_method_options`,
`Subscription#create.payment_settings.payment_method_options`,
`Subscription#update.payment_settings.payment_method_options`, and
`Subscription.payment_settings.payment_method_options`
- Add support for new value `customer_balance` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for new values `payment_intent.partially_funded`,
`terminal.reader.action_failed`, and `terminal.reader.action_succeeded` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### March 29, 2022

- Add support for `cancel_action`, `process_payment_intent`,
`process_setup_intent`, and `set_reader_display` methods on resource
`Terminal.Reader`
- Change `Charge.failure_balance_transaction`,
`Invoice.payment_settings.payment_method_options.us_bank_account`,
`PaymentIntent.next_action.verify_with_microdeposits.microdeposit_type`,
`SetupIntent.next_action.verify_with_microdeposits.microdeposit_type`, and
`Subscription.payment_settings.payment_method_options.us_bank_account` to be
required
- Add support for `action` on `Terminal.Reader`

### March 25, 2022

- Add support for `search` method on resources `Charge`, `Customer`, `Invoice`,
`PaymentIntent`, `Price`, `Product`, and `Subscription`
- Add support for `us_bank_account_ach_payments` on
`Account#create.capabilities`, `Account#update.capabilities`, and
`Account.capabilities`
- Add support for `test_clock` on `Subscription#list`

### March 24, 2022

- Add support for `paynow_payments` on `Account#create.capabilities`,
`Account#update.capabilities`, and `Account.capabilities`
- Add support for `failure_balance_transaction` on `Charge`
- Add support for `paynow` on `Charge.payment_method_details`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, and
`PaymentMethod`
- Add support for `us_bank_account` on `Charge.payment_method_details`,
`Checkout.Session#create.payment_method_options`,
`Checkout.Session.payment_method_options`,
`Invoice#create.payment_settings.payment_method_options`,
`Invoice#update.payment_settings.payment_method_options`,
`Invoice.payment_settings.payment_method_options`,
`Mandate.payment_method_details`, `PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`,
`PaymentMethod#update`, `PaymentMethod`, `SetupAttempt.payment_method_details`,
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#create.payment_method_options`,
`SetupIntent#update.payment_method_options`,
`SetupIntent.payment_method_options`,
`Subscription#create.payment_settings.payment_method_options`,
`Subscription#update.payment_settings.payment_method_options`, and
`Subscription.payment_settings.payment_method_options`
- Add support for new values `paynow` and `us_bank_account` on enums
`Checkout.Session#create.payment_method_types[]` and `PaymentMethod#create.type`
- Add support for new values `paynow` and `us_bank_account` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for new values `paynow` and `us_bank_account` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for new values `paynow` and `us_bank_account` on enums
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`, and
`PaymentIntent#update.payment_method_data.type`
- Add support for `capture_method` on
`PaymentIntent#confirm.payment_method_options.afterpay_clearpay`,
`PaymentIntent#confirm.payment_method_options.card`,
`PaymentIntent#confirm.payment_method_options.klarna`,
`PaymentIntent#create.payment_method_options.afterpay_clearpay`,
`PaymentIntent#create.payment_method_options.card`,
`PaymentIntent#create.payment_method_options.klarna`,
`PaymentIntent#update.payment_method_options.afterpay_clearpay`,
`PaymentIntent#update.payment_method_options.card`,
`PaymentIntent#update.payment_method_options.klarna`,
`PaymentIntent.payment_method_options.afterpay_clearpay`,
`PaymentIntent.payment_method_options.card`,
`PaymentIntent.payment_method_options.klarna`, and
`PaymentIntentTypeSpecificPaymentMethodOptionsClient`
- Add support for `descriptor_code` on `PaymentIntent#verify_microdeposits` and
`SetupIntent#verify_microdeposits`
- Add support for `paynow_display_qr_code` on `PaymentIntent.next_action`
- Add support for `microdeposit_type` on
`PaymentIntent.next_action.verify_with_microdeposits` and
`SetupIntent.next_action.verify_with_microdeposits`
- Add support for `verification_method` on
`PaymentIntentTypeSpecificPaymentMethodOptionsClient` and
`SetupIntentTypeSpecificPaymentMethodOptionsClient`
- Add support for new values `paynow` and `us_bank_account` on enum
`PaymentMethod.type`

### March 23, 2022

- Add support for `cancel` method on resource `Refund`
- Add support for new values `bg_uic`, `hu_tin`, and `si_tin` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`, and `TaxId.type`
- Add support for new values `bg_uic`, `hu_tin`, and `si_tin` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`, and `TaxId#create.type`
- Change `Invoice#create.customer` to be optional
- Add support for `test_clock` on `Quote#list`
- Add support for new values `test_helpers.test_clock.advancing`,
`test_helpers.test_clock.created`, `test_helpers.test_clock.deleted`,
`test_helpers.test_clock.internal_failure`, and `test_helpers.test_clock.ready`
on enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### March 18, 2022

- Add support for `status` on `Card`

### March 11, 2022

- Add support for `mandate` on `Charge.payment_method_details.card`
- Add support for `mandate_options` on
`PaymentIntent#create.payment_method_options.card`,
`PaymentIntent#update.payment_method_options.card`,
`PaymentIntent#confirm.payment_method_options.card`,
`PaymentIntent.payment_method_options.card`,
`SetupIntent#create.payment_method_options.card`,
`SetupIntent#update.payment_method_options.card`,
`SetupIntent#confirm.payment_method_options.card`, and
`SetupIntent.payment_method_options.card`
- Add support for `card_await_notification` on `PaymentIntent.next_action`
- Add support for `customer_notification` on `PaymentIntent.processing.card`
- Change `PaymentLink#create.line_items` to be required

### March 9, 2022

- Add support for `test_clock` on `Customer#list`
- Change `Invoice.test_clock`, `InvoiceItem.test_clock`, `Quote.test_clock`,
`Subscription.test_clock`, and `SubscriptionSchedule.test_clock` to be required

### March 2, 2022

- Add support for new resources `CreditedItems` and `ProrationDetails`
- Add support for `proration_details` on `InvoiceLineItem`

### March 1, 2022

- Add support for `deletes_after` on `TestHelpers.TestClock`
- Add support for new resource `TestHelpers.TestClock`
- Add support for `test_clock` on `Customer#create`, `Customer`, `Invoice`,
`InvoiceItem`, `Quote#create`, `Quote`, `Subscription`, and
`SubscriptionSchedule`
- Add support for `pending_invoice_items_behavior` on `Invoice#create`
- Change type of `Product#update.url` from `string` to `emptyStringable(string)`
- Add support for `next_action` on `Refund`

### February 25, 2022

- Add support for new resource
`SetupIntentTypeSpecificPaymentMethodOptionsClient`
- Add support for `konbini_payments` on `Account#update.capabilities`,
`Account#create.capabilities`, and `Account.capabilities`
- Change
`BillingPortal.Configuration#create.business_profile.privacy_policy_url` and
`BillingPortal.Configuration#create.business_profile.terms_of_service_url` to be
optional
- Change type of
`BillingPortal.Configuration#update.business_profile.privacy_policy_url` and
`BillingPortal.Configuration#update.business_profile.terms_of_service_url` from
`string` to `emptyStringable(string)`
- Change type of
`BillingPortal.Configuration.business_profile.privacy_policy_url` and
`BillingPortal.Configuration.business_profile.terms_of_service_url` from
`string` to `nullable(string)`
- Add support for `konbini` on `Charge.payment_method_details`,
`Checkout.Session#create.payment_method_options`,
`Checkout.Session.payment_method_options`,
`Invoice#create.payment_settings.payment_method_options`,
`Invoice#update.payment_settings.payment_method_options`,
`Invoice.payment_settings.payment_method_options`,
`PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, `PaymentMethod`,
`Subscription#create.payment_settings.payment_method_options`,
`Subscription#update.payment_settings.payment_method_options`, and
`Subscription.payment_settings.payment_method_options`
- Add support for new value `konbini` on enums
`Checkout.Session#create.payment_method_types[]` and `PaymentMethod#create.type`
- Add support for new value `konbini` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for new value `konbini` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`
- Add support for new value `konbini` on enums
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`, and
`PaymentIntent#confirm.payment_method_data.type`
- Add support for `konbini_display_details` on `PaymentIntent.next_action`
- Add support for new value `konbini` on enum `PaymentMethod.type`

### February 23, 2022

- Add support for `setup_future_usage` on
`PaymentIntent#create.payment_method_options.acss_debit`,
`PaymentIntent#create.payment_method_options.afterpay_clearpay`,
`PaymentIntent#create.payment_method_options.alipay`,
`PaymentIntent#create.payment_method_options.au_becs_debit`,
`PaymentIntent#create.payment_method_options.bacs_debit`,
`PaymentIntent#create.payment_method_options.bancontact`,
`PaymentIntent#create.payment_method_options.boleto`,
`PaymentIntent#create.payment_method_options.eps`,
`PaymentIntent#create.payment_method_options.fpx`,
`PaymentIntent#create.payment_method_options.giropay`,
`PaymentIntent#create.payment_method_options.grabpay`,
`PaymentIntent#create.payment_method_options.ideal`,
`PaymentIntent#create.payment_method_options.klarna`,
`PaymentIntent#create.payment_method_options.oxxo`,
`PaymentIntent#create.payment_method_options.p24`,
`PaymentIntent#create.payment_method_options.sepa_debit`,
`PaymentIntent#create.payment_method_options.sofort`,
`PaymentIntent#create.payment_method_options.wechat_pay`,
`PaymentIntent#update.payment_method_options.acss_debit`,
`PaymentIntent#update.payment_method_options.afterpay_clearpay`,
`PaymentIntent#update.payment_method_options.alipay`,
`PaymentIntent#update.payment_method_options.au_becs_debit`,
`PaymentIntent#update.payment_method_options.bacs_debit`,
`PaymentIntent#update.payment_method_options.bancontact`,
`PaymentIntent#update.payment_method_options.boleto`,
`PaymentIntent#update.payment_method_options.eps`,
`PaymentIntent#update.payment_method_options.fpx`,
`PaymentIntent#update.payment_method_options.giropay`,
`PaymentIntent#update.payment_method_options.grabpay`,
`PaymentIntent#update.payment_method_options.ideal`,
`PaymentIntent#update.payment_method_options.klarna`,
`PaymentIntent#update.payment_method_options.oxxo`,
`PaymentIntent#update.payment_method_options.p24`,
`PaymentIntent#update.payment_method_options.sepa_debit`,
`PaymentIntent#update.payment_method_options.sofort`,
`PaymentIntent#update.payment_method_options.wechat_pay`,
`PaymentIntent#confirm.payment_method_options.acss_debit`,
`PaymentIntent#confirm.payment_method_options.afterpay_clearpay`,
`PaymentIntent#confirm.payment_method_options.alipay`,
`PaymentIntent#confirm.payment_method_options.au_becs_debit`,
`PaymentIntent#confirm.payment_method_options.bacs_debit`,
`PaymentIntent#confirm.payment_method_options.bancontact`,
`PaymentIntent#confirm.payment_method_options.boleto`,
`PaymentIntent#confirm.payment_method_options.eps`,
`PaymentIntent#confirm.payment_method_options.fpx`,
`PaymentIntent#confirm.payment_method_options.giropay`,
`PaymentIntent#confirm.payment_method_options.grabpay`,
`PaymentIntent#confirm.payment_method_options.ideal`,
`PaymentIntent#confirm.payment_method_options.klarna`,
`PaymentIntent#confirm.payment_method_options.oxxo`,
`PaymentIntent#confirm.payment_method_options.p24`,
`PaymentIntent#confirm.payment_method_options.sepa_debit`,
`PaymentIntent#confirm.payment_method_options.sofort`,
`PaymentIntent#confirm.payment_method_options.wechat_pay`,
`PaymentIntent.payment_method_options.acss_debit`,
`PaymentIntent.payment_method_options.afterpay_clearpay`,
`PaymentIntent.payment_method_options.alipay`,
`PaymentIntent.payment_method_options.au_becs_debit`,
`PaymentIntent.payment_method_options.bacs_debit`,
`PaymentIntent.payment_method_options.bancontact`,
`PaymentIntent.payment_method_options.boleto`,
`PaymentIntent.payment_method_options.eps`,
`PaymentIntent.payment_method_options.fpx`,
`PaymentIntent.payment_method_options.giropay`,
`PaymentIntent.payment_method_options.grabpay`,
`PaymentIntent.payment_method_options.ideal`,
`PaymentIntent.payment_method_options.klarna`,
`PaymentIntent.payment_method_options.oxxo`,
`PaymentIntent.payment_method_options.p24`,
`PaymentIntent.payment_method_options.sepa_debit`,
`PaymentIntent.payment_method_options.sofort`, and
`PaymentIntent.payment_method_options.wechat_pay`
- Add support for new values `bbpos_wisepad3` and `stripe_m2` on enums
`Terminal.Reader#list.device_type` and `Terminal.Reader.device_type`

### February 9, 2022

- Add support for `verify_microdeposits` method on resources `PaymentIntent` and
`SetupIntent`
- Add support for new value `grabpay` on enums
`Invoice#create.payment_settings.payment_method_types[]`,
`Invoice#update.payment_settings.payment_method_types[]`,
`Invoice.payment_settings.payment_method_types[]`,
`Subscription#create.payment_settings.payment_method_types[]`,
`Subscription#update.payment_settings.payment_method_types[]`, and
`Subscription.payment_settings.payment_method_types[]`

### February 8, 2022

- Add support for `pin` on `Issuing.Card#update`

### February 3, 2022

- Add support for new value `au_becs_debit` on enum
`Checkout.Session#create.payment_method_types[]`
- Change type of `Refund.reason` from `string` to
`enum('duplicate'|'expired_uncaptured_charge'|'fraudulent'|'requested_by_customer')`

### January 25, 2022

- Add support for new value `is_vat` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`, and `TaxId.type`
- Add support for new value `is_vat` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`, and `TaxId#create.type`
- Change `Checkout.Session.payment_link` to be required
- Add support for `phone_number_collection` on `PaymentLink#create` and
`PaymentLink`
- Add support for new values `payment_link.created` and `payment_link.updated`
on enums `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### January 19, 2022

- Add support for new resource `PaymentLink`
- Add support for `payment_link` on `Checkout.Session`
- Change type of `Charge.status` from `string` to
`enum('failed'|'pending'|'succeeded')`
- Add support for `bacs_debit` and `eps` on
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`, and
`PaymentIntent.payment_method_options`
- Add support for `image_url_png` and `image_url_svg` on
`PaymentIntent.next_action.wechat_pay_display_qr_code`

### January 12, 2022

- Add support for `paid_out_of_band` on `Invoice`
- Add support for `customer_creation` on `Checkout.Session#create` and
`Checkout.Session`
- Add support for `fpx` and `grabpay` on
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`, and
`PaymentIntent.payment_method_options`

### December 23, 2021

- Add support for `mandate_options` on
`Subscription#create.payment_settings.payment_method_options.card`,
`Subscription#update.payment_settings.payment_method_options.card`, and
`Subscription.payment_settings.payment_method_options.card`

### December 22, 2021

- Add support for `au_becs_debit` on
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`, and
`PaymentIntent.payment_method_options`
- Change type of `PaymentIntent.processing.type` from `string` to
`literal('card')`

### December 21, 2021

- Add support for new values `en-FR`, `es-US`, and `fr-FR` on enums
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`
- Add support for `boleto` on `SetupAttempt.payment_method_details`

### December 17, 2021

- Add support for `processing` on `PaymentIntent`

### December 15, 2021

- Add support for new resource
`PaymentIntentTypeSpecificPaymentMethodOptionsClient`
- Add support for `setup_future_usage` on
`PaymentIntent#create.payment_method_options.card`,
`PaymentIntent#update.payment_method_options.card`,
`PaymentIntent#confirm.payment_method_options.card`, and
`PaymentIntent.payment_method_options.card`

### December 9, 2021

- Add support for `metadata` on `BillingPortal.Configuration#create`,
`BillingPortal.Configuration#update`, and `BillingPortal.Configuration`
- Add support for new values `ge_vat` and `ua_vat` on enums
`Checkout.Session.customer_details.tax_ids[].type`,
`Invoice.customer_tax_ids[].type`, and `TaxId.type`
- Add support for new values `ge_vat` and `ua_vat` on enums
`Customer#create.tax_id_data[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`, and `TaxId#create.type`
- Change type of
`PaymentIntent#create.payment_method_data.billing_details.email`,
`PaymentIntent#update.payment_method_data.billing_details.email`,
`PaymentIntent#confirm.payment_method_data.billing_details.email`,
`PaymentMethod#create.billing_details.email`, and
`PaymentMethod#update.billing_details.email` from `string` to
`emptyStringable(string)`
- Add support for `giropay` on `PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`, and
`PaymentIntent.payment_method_options`
- Add support for new value `en-IE` on enums
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`

### November 19, 2021

- Add support for `wallets` on `Issuing.Card`
- Add support for `interac_present` on
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`, and
`PaymentIntent.payment_method_options`
- Add support for new value `jct` on enums `TaxRate#create.tax_type`,
`TaxRate#update.tax_type`, and `TaxRate.tax_type`

### November 17, 2021

- Add support for new resource `AutomaticPaymentMethodsPaymentIntent`
- Add support for `automatic_payment_methods` on `PaymentIntent#create` and
`PaymentIntent`

### November 15, 2021

- Add support for new resource `ShippingRate`
- Add support for `shipping_options` on `Checkout.Session#create` and
`Checkout.Session`
- Add support for `shipping_rate` on `Checkout.Session`

### November 12, 2021

- Add support for new value `agrobank` on enums
`Charge.payment_method_details.fpx.bank`,
`PaymentIntent#create.payment_method_data.fpx.bank`,
`PaymentIntent#update.payment_method_data.fpx.bank`,
`PaymentIntent#confirm.payment_method_data.fpx.bank`,
`PaymentMethod#create.fpx.bank`, and `PaymentMethod.fpx.bank`

### November 11, 2021

- Add support for `expire` method on resource `Checkout.Session`
- Add support for `status` on `Checkout.Session`

### November 3, 2021

- Remove support for `ownership_declaration_shown_and_signed` on
`Token#create.account`(this API was unused)
- Add support for `ownership_declaration_shown_and_signed` on
`Token#create.account.company`

### November 1, 2021

- Add support for `ownership_declaration` on `Account#update.company`,
`Account#create.company`, `Account.company`, and `Token#create.account.company`
- Add support for `proof_of_registration` on `Account#update.documents` and
`Account#create.documents`
- Add support for `ownership_declaration_shown_and_signed` on
`Token#create.account`
- Change type of `Account#update.individual.full_name_aliases`,
`Account#create.individual.full_name_aliases`,
`Person#create.full_name_aliases`, `Person#update.full_name_aliases`,
`Token#create.account.individual.full_name_aliases`, and
`Token#create.person.full_name_aliases` from `array(string)` to
`emptyStringable(array(string))`
- Add support for new values `en-BE`, `en-ES`, and `en-IT` on enums
`PaymentIntent#create.payment_method_options.klarna.preferred_locale`,
`PaymentIntent#update.payment_method_options.klarna.preferred_locale`, and
`PaymentIntent#confirm.payment_method_options.klarna.preferred_locale`

### October 19, 2021

- Change `Account.controller.type` to be required
- Add support for `buyer_id` on `Charge.payment_method_details.alipay`

### October 15, 2021

- Change type of `UsageRecord#create.timestamp` from `integer` to
`literal('now') | integer`
- Change `UsageRecord#create.timestamp` to be optional

### October 14, 2021

- Change `Charge.payment_method_details.klarna.payment_method_category`,
`Charge.payment_method_details.klarna.preferred_locale`,
`Checkout.Session.customer_details.phone`, and `PaymentMethod.klarna.dob` to be
required
- Add support for new value `klarna` on enum
`Checkout.Session#create.payment_method_types[]`

### October 9, 2021

- Add support for `payment_method_category` and `preferred_locale` on
`Charge.payment_method_details.klarna`
- Add support for new value `klarna` on enums
`Customer#list_payment_methods.type` and `PaymentMethod#list.type`
- Add support for `klarna` on `PaymentIntent#create.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent.payment_method_options`, `PaymentMethod#create`, and
`PaymentMethod`
- Add support for new value `klarna` on enums
`PaymentIntent#create.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`, and
`PaymentIntent#confirm.payment_method_data.type`
- Add support for new value `klarna` on enum `PaymentMethod#create.type`
- Add support for new value `klarna` on enum `PaymentMethod.type`

### October 8, 2021

- Add support for `list_payment_methods` method on resource `Customer`

### October 7, 2021

- Add support for `phone_number_collection` on `Checkout.Session#create` and
`Checkout.Session`
- Add support for `phone` on `Checkout.Session.customer_details`
- Change `PaymentMethod#list.customer` to be optional
- Add support for new value `customer_id` on enums
`Radar.ValueList#create.item_type` and `Radar.ValueList.item_type`
- Add support for new value `bbpos_wisepos_e` on enums
`Terminal.Reader#list.device_type` and `Terminal.Reader.device_type`

### September 29, 2021

- Add support for `klarna_payments` on `Account#update.capabilities`,
`Account#create.capabilities`, and `Account.capabilities`

### September 24, 2021

- Add support for `amount_authorized` and `overcapture_supported` on
`Charge.payment_method_details.card_present`

### September 16, 2021

- Add support for `full_name_aliases` on `Account#update.individual`,
`Account#create.individual`, `Person#create`, `Person#update`, `Person`,
`Token#create.account.individual`, and `Token#create.person`

### September 7, 2021

- Change `Account.future_requirements.alternatives`,
`Account.requirements.alternatives`,
`Capability.future_requirements.alternatives`,
`Capability.requirements.alternatives`, `Checkout.Session.after_expiration`,
`Checkout.Session.consent`, `Checkout.Session.consent_collection`,
`Checkout.Session.expires_at`, `Checkout.Session.recovered_from`,
`Person.future_requirements.alternatives`, and
`Person.requirements.alternatives` to be required
- Change type of `Capability.future_requirements.alternatives`,
`Capability.requirements.alternatives`,
`Person.future_requirements.alternatives`, and
`Person.requirements.alternatives` from `array(AccountRequirementsAlternative)`
to `nullable(array(AccountRequirementsAlternative))`
- Add support for new value `rst` on enums `TaxRate#create.tax_type`,
`TaxRate#update.tax_type`, and `TaxRate.tax_type`
- Add support for new value `checkout.session.expired` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### September 1, 2021

- Add support for `future_requirements` on `Account`, `Capability`, and `Person`
- Add support for `alternatives` on `Account.requirements`,
`Capability.requirements`, and `Person.requirements`
- Change type of
`Checkout.Session.after_expiration.recovery.allow_promotion_codes` and
`Checkout.Session.after_expiration.recovery.enabled` from `nullable(boolean)` to
`boolean`

### August 31, 2021

- Add support for `after_expiration`, `consent_collection`, and `expires_at` on
`Checkout.Session#create` and `Checkout.Session`
- Add support for `consent` and `recovered_from` on `Checkout.Session`

### August 26, 2021

- Change type of
`BillingPortal.Configuration#create.features.subscription_cancel.cancellation_reason.options[]`,
`BillingPortal.Configuration#update.features.subscription_cancel.cancellation_reason.options[]`,
and
`BillingPortal.Configuration.features.subscription_cancel.cancellation_reason.options[]`
from `string` to `enum`

### August 25, 2021

- Add support for `cancellation_reason` on
`BillingPortal.Configuration.features.subscription_cancel`

### August 24, 2021

- Add support for `cancellation_reason` on
`BillingPortal.Configuration#create.features.subscription_cancel` and
`BillingPortal.Configuration#update.features.subscription_cancel`

### August 11, 2021

- Add support for `locale` on `BillingPortal.Session#create` and
`BillingPortal.Session`
- Change type of `Invoice.collection_method` and
`Subscription.collection_method` from
`nullable(enum('charge_automatically'|'send_invoice'))` to
`enum('charge_automatically'|'send_invoice')`

### August 4, 2021

- Changed type of
`PaymentIntent#create.payment_method_options.sofort.preferred_language`,
`PaymentIntent#update.payment_method_options.sofort.preferred_language`, and
`PaymentIntent#confirm.payment_method_options.sofort.preferred_language` from
`enum` to `emptyStringable(enum)`

### July 28, 2021

- Add support for `account_type` on `BankAccount`, `ExternalAccount#update`, and
`Token#create.bank_account`

### July 27, 2021

- Add support for `category_code` on `Issuing.Authorization.merchant_data` and
`Issuing.Transaction.merchant_data`
- Add support for new value `redacted` on enum `Review.closed_reason`

### July 22, 2021

- Remove support for `payment_settings` on `Customer#create` and
`Customer#update`

### July 21, 2021

- Add support for new values `hr`, `ko`, and `vi` on enums
`Checkout.Session#create.locale` and `Checkout.Session.locale`
- Add support for `payment_settings` on `Customer#create`, `Customer#update`,
`Subscription#create`, `Subscription#update`, and `Subscription`
- Remove support for values `api_connection_error`, `authentication_error`, and
`rate_limit_error` from enums `StripeError.type`,
`StripeErrorResponse.error.type`, `Invoice.last_finalization_error.type`,
`PaymentIntent.last_payment_error.type`, `SetupAttempt.setup_error.type`, and
`SetupIntent.last_setup_error.type`
- Add support for `wallet` on `Issuing.Transaction`
- Add support for `ideal` on `PaymentIntent#create.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`, and
`PaymentIntent.payment_method_options`

### July 14, 2021

- Add support for new values `quote.accepted`, `quote.canceled`,
`quote.created`, and `quote.finalized` on enums
`WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]`

### July 12, 2021

- Add support for `list_computed_upfront_line_items` method on resource `Quote`

### July 8, 2021

- Add support for `finalize_quote` method on resource `Quote`
- Remove support for `finalize` method on resource `Quote`

### July 7, 2021

- Add support for new resource `Quote`
- Changed type of `Charge.payment_method_details.card.three_d_secure.result` and
`SetupAttempt.payment_method_details.card.three_d_secure.result` from `enum` to
`nullable(enum)`
- Changed type of `Charge.payment_method_details.card.three_d_secure.version`
and `SetupAttempt.payment_method_details.card.three_d_secure.version` from
`enum('1.0.2'|'2.1.0'|'2.2.0')` to `nullable(enum('1.0.2'|'2.1.0'|'2.2.0'))`
- Add support for `quote` on `Invoice`
- Add support for new value `quote_accept` on enum `Invoice.billing_reason`

### June 30, 2021

- `Invoice#update.payment_settings.payment_method_types[]`,
`Invoice#create.payment_settings.payment_method_types[]` and
`Invoice.payment_settings.payment_method_types[]` added new enum members:
`boleto`

### June 29, 2021

- Added support for `boleto_payments` on `Account#create.capabilities`,
`Account#update.capabilities` and `Account.capabilities`
- Added support for `boleto` and `oxxo` on
`Session#create.payment_method_options` and
`Checkout.Session.payment_method_options`
- `Session#create.payment_method_types[]` added new enum members: `boleto and
oxxo`

### June 25, 2021

- Added support for `boleto` on `PaymentMethod#create`,
`PaymentIntent.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#create.payment_method_data`, `Charge.payment_method_details` and
`PaymentMethod`
- Added support for `boleto_display_details` on `PaymentIntent.next_action`
- `TaxId#create.type`, `Invoice.customer_tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Customer#create.tax_id_data[].type`,
`Checkout.Session.customer_details.tax_ids[].type` and `TaxId.type` added new
enum members: `il_vat`
- `PaymentMethod#list.type`, `PaymentMethod#create.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type` and `PaymentMethod.type` added
new enum members: `boleto`

### June 18, 2021

- `TaxId#create.type`, `Invoice.customer_tax_ids[].type`,
`Invoice#upcomingLines.customer_details.tax_ids[].type`,
`Invoice#upcoming.customer_details.tax_ids[].type`,
`Customer#create.tax_id_data[].type`,
`Checkout.Session.customer_details.tax_ids[].type` and `TaxId.type` added new
enum members: `ca_pst_mb, ca_pst_bc, ca_gst_hst and ca_pst_sk`

### June 7, 2021

- Added support for `tax_id_collection` on `Session#create` and
`Checkout.Session`
- `Terminal.Reader.location` changed from `string` to
`expandable($Terminal.Location)`

### June 4, 2021

- Added support for `controller` on `Account`

### June 3, 2021

- Added support for new resource `TaxCode`
- Added support for `automatic_tax` on `SubscriptionSchedule.default_settings`,
`SubscriptionSchedule#update.phases[]`,
`SubscriptionSchedule#update.default_settings`,
`SubscriptionSchedule#create.phases[]`,
`SubscriptionSchedule#create.default_settings`, `Subscription`,
`Subscription#update`, `Subscription#create`, `Invoice`,
`Invoice#upcomingLines`, `Invoice#update`, `Invoice#upcoming`, `Invoice#create`,
`Checkout.Session`, `Session#create` and `SubscriptionSchedule.phases[]`
- Added support for `customer_update` on `Session#create`
- Added support for `tax_behavior` on
`SubscriptionSchedule#update.phases[].add_invoice_items[].price_data`,
`SubscriptionSchedule#create.phases[].items[].price_data`,
`SubscriptionSchedule#create.phases[].add_invoice_items[].price_data`,
`SubscriptionItem#update.price_data`, `SubscriptionItem#create.price_data`,
`Subscription#update.items[].price_data`,
`Subscription#update.add_invoice_items[].price_data`,
`Subscription#create.items[].price_data`,
`Subscription#create.add_invoice_items[].price_data`, `Price`, `Price#update`,
`Price#create`, `InvoiceItem#update.price_data`,
`InvoiceItem#create.price_data`,
`Invoice#upcomingLines.subscription_items[].price_data`,
`Invoice#upcomingLines.invoice_items[].price_data`,
`Invoice#upcoming.subscription_items[].price_data`,
`Invoice#upcoming.invoice_items[].price_data`,
`Session#create.line_items[].price_data` and
`SubscriptionSchedule#update.phases[].items[].price_data`
- Added support for `tax_code` on `Product#update`, `Product#create`,
`Price#create.product_data`, `Plan#create.product[0]`,
`Session#create.line_items[].price_data.product_data` and `Product`
- Added support for `tax` on `Customer#update`, `Customer#create` and `Customer`
- Added support for `customer_details` on `Invoice#upcoming` and
`Invoice#upcomingLines`
- Added support for `tax_type` on `TaxRate#update`, `TaxRate#create` and
`TaxRate`

### May 26, 2021

- Added support for `documents` on `Person#update`, `Person#create` and
`Token#create.person`
- `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]` added new enum members:
`identity.verification_session.requires_input,
identity.verification_session.redacted,
identity.verification_session.processing, identity.verification_session.created,
identity.verification_session.canceled and
identity.verification_session.verified`

### May 19, 2021

- Added support for `acss_debit` on `PaymentMethod#update`
- `Identity.VerificationReport.created` changed from `integer` to `DateTime`

### May 18, 2021

- `Identity.VerificationSession.client_secret` changed from `string` to
`nullable(string)`

### May 17, 2021

- Removed support for method: `PaymentIntent#verify_microdeposits`
- Removed support for method: `SetupIntent#verify_microdeposits`

### May 13, 2021

- New method: `PaymentIntent#verify_microdeposits`
- New method: `SetupIntent#verify_microdeposits`

### May 11, 2021

- `Account#update.business_profile.support_url` and
`Account#create.business_profile.support_url` changed from `string` to
`emptyStringable(string)`
- `File.purpose` added new enum members: `finance_report_run,
document_provider_identity_document and sigma_scheduled_query`

### May 6, 2021

- Added support for `reference` on
`Charge.payment_method_details.afterpay_clearpay`
- Added support for `afterpay_clearpay` on
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#create.payment_method_options` and
`PaymentIntent.payment_method_options`

### May 5, 2021

- Added support for `payment_intent` on `EarlyFraudWarning#list` and
`Radar.EarlyFraudWarning`

### May 4, 2021

- Added support for `currency` on
`Checkout.Session.payment_method_options.acss_debit`
- Added support for `card_present` on
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#create.payment_method_options` and
`PaymentIntent.payment_method_options`
- `SubscriptionItem#create.payment_behavior`,
`Subscription#update.payment_behavior`, `Subscription#create.payment_behavior`
and `SubscriptionItem#update.payment_behavior` added new enum members:
`default_incomplete`

### April 21, 2021

- `Account.company.structure`, `Account#create.company.structure`,
`Account#update.company.structure` and `Token#create.account.company.structure`
added new enum members: `single_member_llc`
- `Issuing.Card.shipping.carrier` added new enum members: `dhl and royal_mail`

### April 8, 2021

- Added support for `acss_debit_payments` on `Account#create.capabilities`,
`Account#update.capabilities` and `Account.capabilities`
- Added support for `payment_method_options` on `Session#create` and
`Checkout.Session`
- Added support for `acss_debit` on
`SetupIntent#confirm.payment_method_options`,
`SetupIntent#update.payment_method_options`,
`SetupIntent#create.payment_method_options`,
`SetupAttempt.payment_method_details`, `PaymentMethod`, `PaymentMethod#create`,
`PaymentIntent.payment_method_options`,
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#create.payment_method_options`,
`PaymentIntent#create.payment_method_data`, `Mandate.payment_method_details` and
`SetupIntent.payment_method_options`
- Added support for `verify_with_microdeposits` on `PaymentIntent.next_action`
and `SetupIntent.next_action`
- `PaymentMethod#list.type`, `PaymentMethod#create.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`Session#create.payment_method_types[]` and `PaymentMethod.type` added new enum
members: `acss_debit`

### April 2, 2021

- Added support for `subscription_pause` on `Configuration#update.features`,
`Configuration#create.features` and `BillingPortal.Configuration.features`

### March 31, 2021

- Added support for `transfer_data` on `Session#create.subscription_data`

### March 26, 2021

- Added support for `card_issuing` on `Account#create.settings`,
`Account#update.settings` and `Account.settings`

### March 25, 2021

- `Capability.requirements.errors[].code`, `Account.requirements.errors[].code`
and `Person.requirements.errors[].code` added new enum members:
`verification_missing_owners, verification_missing_executives and
verification_requires_additional_memorandum_of_associations`
- `Session#create.locale` and `Checkout.Session.locale` added new enum members:
`th`

### February 19, 2021

- Added support for `prices` on
`BillingPortal.Configuration.features.subscription_update.products[]`
- Added support for new resource `BillingPortal.Configuration`
- Added support for `configuration` and `on_behalf_of` on `Session#create` and
`BillingPortal.Session`
- `WebhookEndpoint#create.enabled_events[]` and
`WebhookEndpoint#update.enabled_events[]` added new enum members:
`billing_portal.configuration.created and billing_portal.configuration.updated`

### February 17, 2021

- Added support for `on_behalf_of` on `Invoice#update`, `Invoice#create` and
`Invoice`
- `PaymentMethod.ideal.bank`, `PaymentMethod#create.ideal.bank`,
`PaymentIntent#confirm.payment_method_data.ideal.bank`,
`PaymentIntent#update.payment_method_data.ideal.bank`,
`PaymentIntent#create.payment_method_data.ideal.bank`,
`Charge.payment_method_details.ideal.bank` and
`SetupAttempt.payment_method_details.ideal.bank` added new enum members:
`revolut`
- `PaymentMethod.ideal.bic`, `Charge.payment_method_details.ideal.bic` and
`SetupAttempt.payment_method_details.ideal.bic` added new enum members:
`REVOLT21`
- Added support for `afterpay_clearpay` on `PaymentMethod#create`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#create.payment_method_data`, `Charge.payment_method_details` and
`PaymentMethod`
- Added support for `adjustable_quantity` on `Session#create.line_items[]`
- Added support for `bacs_debit`, `au_becs_debit` and `sepa_debit` on
`SetupAttempt.payment_method_details`
- `PaymentMethod#list.type`, `PaymentMethod#create.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`Session#create.payment_method_types[]` and `PaymentMethod.type` added new enum
members: `afterpay_clearpay`

### February 9, 2021

- Added support for `afterpay_clearpay_payments` on
`Account#create.capabilities`, `Account#update.capabilities` and
`Account.capabilities`
- Added support for `payment_settings` on `Invoice#update`, `Invoice#create` and
`Invoice`

### February 5, 2021

- `LineItem.amount_subtotal` and `LineItem.amount_total` changed from
`nullable(integer)` to `integer`

### February 2, 2021

- Added support for `nationality` on `Person`, `Person#update`, `Person#create`
and `Token#create.person`
- `TaxId#create.type`, `Invoice.customer_tax_ids[].type`,
`Customer#create.tax_id_data[].type`,
`Checkout.Session.customer_details.tax_ids[].type` and `TaxId.type` added new
enum members: `gb_vat`

### January 22, 2021

- `Issuing.Transaction.type` dropped enum members: ‘dispute’
- `LineItem.price` changed from `$Price` to `nullable($Price)`

### January 14, 2021

- Added support for `dynamic_tax_rates` on `Session#create.line_items[]`
- Added support for `customer_details` on `Checkout.Session`
- Added support for `type` on `Transaction#list`
- Added support for `country` and `state` on `TaxRate#update`, `TaxRate#create`
and `TaxRate`

### January 7, 2021

- Added support for `company_registration_verification`,
`company_ministerial_decree`, `company_memorandum_of_association`,
`company_license` and `company_tax_id_verification` on
`Account#update.documents` and `Account#create.documents`

### December 15, 2020

- Added support for `card_present` on `SetupAttempt.payment_method_details`

### December 10, 2020

- Added support for `bank` on `PaymentMethod#create.eps`,
`PaymentIntent#confirm.payment_method_data.eps`,
`PaymentIntent#update.payment_method_data.eps`,
`PaymentIntent#create.payment_method_data.eps`,
`Charge.payment_method_details.p24`, `Charge.payment_method_details.eps` and
`PaymentMethod.eps`
- Added support for `tos_shown_and_accepted` on
`PaymentIntent#update.payment_method_options.p24`,
`PaymentIntent#create.payment_method_options.p24` and
`PaymentIntent#confirm.payment_method_options.p24`
- Added support for `bacs_debit` on `PaymentMethod#update`
- Added support for `application_fee_percent` on
`SubscriptionSchedule#update.default_settings`,
`SubscriptionSchedule#create.default_settings` and
`SubscriptionSchedule.default_settings`

### December 4, 2020

- Added support for `documents` on `Account#update` and `Account#create`
- `File#list.purpose` and `File.purpose` added new enum members:
`account_requirement`

### November 24, 2020

- Added support for `account_tax_ids` on `Invoice#update`, `Invoice#create` and
`Invoice`
- Added support for `sepa_debit` on
`PaymentIntent#confirm.payment_method_options`,
`PaymentIntent#update.payment_method_options`,
`PaymentIntent#create.payment_method_options` and
`PaymentIntent.payment_method_options`

### November 20, 2020

- Added support for `grabpay_payments` on `Account#create.capabilities`,
`Account#update.capabilities` and `Account.capabilities`

### November 19, 2020

- Added support for `mandate_options` on
`SetupIntent#confirm.payment_method_options.sepa_debit`,
`SetupIntent#update.payment_method_options.sepa_debit`,
`SetupIntent#create.payment_method_options.sepa_debit` and
`SetupIntent.payment_method_options.sepa_debit`
- `PaymentMethod.type` added new enum members: `card_present and
interac_present`

### November 18, 2020

- Added support for `grabpay` on `PaymentMethod#create`,
`PaymentIntent#confirm.payment_method_data`,
`PaymentIntent#update.payment_method_data`,
`PaymentIntent#create.payment_method_data`, `Charge.payment_method_details` and
`PaymentMethod`
- `PaymentMethod#list.type`, `PaymentMethod#create.type`,
`PaymentIntent#confirm.payment_method_data.type`,
`PaymentIntent#update.payment_method_data.type`,
`PaymentIntent#create.payment_method_data.type`,
`Session#create.payment_method_types[]` and `PaymentMethod.type` added new enum
members: `grabpay`

## Links

- [Changelog](https://docs.stripe.com/changelog)
- [upgrade guide](https://docs.stripe.com/upgrades)