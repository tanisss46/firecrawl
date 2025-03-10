# Collect customer tax IDs with Checkout

## Learn how to collect VAT and other customer tax IDs with Checkout.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
Displaying a customer’s tax ID and legal business name on
[invoices](https://docs.stripe.com/api/invoices) is a common requirement that
you can satisfy by enabling tax ID collection in Checkout. This guide assumes
that you’ve already integrated Checkout. If you haven’t, see the [Accept a
payment guide](https://docs.stripe.com/payments/accept-a-payment).

[Enable Tax ID
collection](https://docs.stripe.com/tax/checkout/tax-ids#create-session)
With tax ID collection enabled, Checkout shows and hides the tax ID collection
form depending on your customer’s location. If your customer is in a location
supported by tax ID collection, Checkout shows a checkbox allowing the customer
to indicate that they’re purchasing as a business. When a customer checks the
box, Checkout displays fields for them to enter the tax ID and legal entity name
for the business. If available, Checkout uses the customer’s shipping address to
determine their location, otherwise Checkout uses the customer’s billing
address. Customers can only enter one tax ID.

### New Customers

To enable tax ID collection for new customers, set
[tax_id_collection[enabled]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-tax_id_collection-enabled)
to `true` when creating a Checkout session.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][currency]"=eur \
 -d "line_items[0][quantity]"=2 \
 -d "tax_id_collection[enabled]"=true \
 -d mode=payment \
 -d ui_mode=embedded \
 --data-urlencode return_url="https://example.com/return"
```

This example creates a Session in `payment` mode with tax ID collection enabled.
For subscriptions, make the same changes with the
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
set to `subscription`.

You can additionally configure Checkout to create a new
[Customer](https://docs.stripe.com/api/customers/object) for you using
[customer_creation](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_creation).
If you do, Checkout saves any tax ID information collected during a Session to
that new [Customer](https://docs.stripe.com/api/customers). If not, the tax ID
information will still be available at
[customer_details.tax_ids](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids).

### Existing Customers

If you pass an existing Customer when creating a Session, Checkout updates the
Customer with any tax ID information collected during the Session. Checkout
saves the collected business name onto the Customer’s
[name](https://docs.stripe.com/api/customers/object#customer_object-name)
property, and adds the collected tax ID to the Customer’s
[customer.tax_ids](https://docs.stripe.com/api/customers/object#customer_object-tax_ids)
array. Since the collection of a business name could result in the Customer’s
existing
[name](https://docs.stripe.com/api/customers/object#customer_object-name) being
overridden, you must set
[customer_update.name](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-name)
to `auto` when creating the Session.

#### Caution

Checkout only collects tax IDs on Customers that don’t already have an existing
tax ID. If a Customer has one or more tax IDs saved, Checkout doesn’t display
the tax ID collection form even if tax ID collection is enabled.

When collecting tax IDs for existing customers you can either base their
location on existing addresses on the customer or the addresses entered during
checkout. By default, Checkout looks for existing addresses on the customer to
assess their location:

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][currency]"=eur \
 -d "line_items[0][quantity]"=2 \
 -d "tax_id_collection[enabled]"=true \
 -d "customer_update[name]"=auto \
 -d mode=payment \
 -d ui_mode=embedded \
 --data-urlencode return_url="https://example.com/return"
```

If you don’t have the addresses of your existing customers saved, you can base
their location on the billing or shipping address entered during Checkout. To
specify that you want to use the billing address entered during Checkout to
assess the customer’s location, you must set
[customer_update.address](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-address)
to `auto`. When setting
[customer_update.address](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-address)
to `auto`, Checkout replaces any previously saved addresses on the customer with
the address entered during the session.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][currency]"=eur \
 -d "line_items[0][quantity]"=2 \
 -d "tax_id_collection[enabled]"=true \
 -d "customer_update[name]"=auto \
 -d "customer_update[address]"=auto \
 -d mode=payment \
 -d ui_mode=embedded \
 --data-urlencode return_url="https://example.com/return"
```

If you’re collecting shipping addresses for existing customers, you must base
their location on the shipping address entered during checkout. To do so, set
[customer_update.shipping](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-shipping)
to `auto`. When setting
[customer_update.shipping](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-shipping)
to `auto`, Checkout replaces any previously saved shipping addresses on the
customer with the shipping address entered during the session.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_HQmikpKnGHkNwW \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][currency]"=eur \
 -d "line_items[0][quantity]"=2 \
 -d "tax_id_collection[enabled]"=true \
 -d "customer_update[name]"=auto \
 -d "customer_update[shipping]"=auto \
 -d "shipping_address_collection[allowed_countries][0]"=DE \
 -d mode=payment \
 -d ui_mode=embedded \
 --data-urlencode return_url="https://example.com/return"
```

This example creates a Session in `payment` mode with tax ID collection enabled.
For subscriptions, make the same changes with the
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
set to `subscription`.

[OptionalRequire tax ID
collection](https://docs.stripe.com/tax/checkout/tax-ids#requiring-collection)[Retrieve
Customer Tax ID details after a
Session](https://docs.stripe.com/tax/checkout/tax-ids#retrieving-details)
Checkout includes provided tax IDs on the resulting
[Session](https://docs.stripe.com/api/checkout/sessions/object) object. After
each completed Session, Checkout emits a
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event that you can listen for in a [webhook](https://docs.stripe.com/webhooks)
endpoint. If you want to retrieve the collected tax ID from the Session object,
it’s available under the Session’s
[customer_details.tax_ids](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids)
array:

```
{
 "object": {
 "id": "cs_test_a1dJwt0TCJTBsDkbK7RcoyJ91vJxe2Y",
 "object": "checkout.session",
 ...
 "customer": "cus_id_of_new_customer",
 "customer_details": {
 ...
 "tax_ids": [
 {
 "type": "eu_vat",
 "value": "FRAB123456789"
 }
 ]
 },
 ...
 "tax_id_collection": {
 "enabled": true
 },
 ...
 }
}
```

Checkout also saves collected tax IDs and business names to the
[Customer](https://docs.stripe.com/api/customers/object) object if one is
associated with the Session. A tax ID collected during checkout is accessible
under the Customer’s
[customer.tax_ids](https://docs.stripe.com/api/customers/object#customer_object-tax_ids)
array. You can also retrieve all tax IDs saved to a Customer with the [Tax
IDs](https://docs.stripe.com/api/tax_ids/list) resource by specifying the
[owner.type](https://docs.stripe.com/api/tax_ids/list#list_tax_ids-owner-type)
parameter to `customer` and
[owner.customer](https://docs.stripe.com/api/tax_ids/list#list_tax_ids-owner-customer)
to the Customer’s ID. Every new tax ID includes an associated legal business
name, which Checkout saves to the Customer’s
[name](https://docs.stripe.com/api/customers/object#customer_object-name)
property. In doing so, the collected legal business name is always visible on
any subscription invoices for that Customer.

[Test your integration](https://docs.stripe.com/tax/checkout/tax-ids#testing)
In test mode, you can enter any alphanumeric string that is in the correct
format of a supported tax ID type (for example, `DE123456789` for `eu_vat`). For
a full list of example tax IDs you can reference our [Customer Tax ID
guide](https://docs.stripe.com/billing/customer/tax-ids#supported-tax-id). You
can also use our [test tax
IDs](https://docs.stripe.com/connect/testing#test-business-tax-ids) to test
various verification state flows.

## Validation

Checkout performs checks during the Session to make sure that provided tax IDs
are formatted correctly. We don’t verify that provided tax IDs are valid during
the Session. You’re responsible for ensuring the validity of customer
information collected during Checkout. To help, Stripe automatically performs
asynchronous validation against government databases for [Australian Business
(ABN)](https://docs.stripe.com/billing/customer/tax-ids#abn) numbers, [European
Value-Added-Tax (EU
VAT)](https://docs.stripe.com/billing/customer/tax-ids#eu-vat) numbers, and
[United Kingdom Value-Added-Tax (GB
VAT)](https://docs.stripe.com/billing/customer/tax-ids#gb-vat) numbers. You can
read more on the validation we perform, and how to consume the status of those
checks in our [Customer Tax ID
guide](https://docs.stripe.com/billing/customer/tax-ids#validation).

## Supported Tax ID types

Checkout collects the following tax ID types in the given regions:

CountryEnumDescriptionExampleAlbania`al_tin`Albania Tax Identification
NumberJ12345678NAngola`ao_tin`Angola Tax Identification
Number5123456789Armenia`am_tin`Armenia Tax Identification
Number02538904Australia`au_abn`Australian Business Number (AU
ABN)12345678912Austria`eu_vat`European VAT
numberATU12345678Bahamas`bs_tin`Bahamas Tax Identification
Number123.456.789Bahrain`bh_vat`Bahraini VAT
Number123456789012345Barbados`bb_tin`Barbados Tax Identification
Number1123456789012Belarus`by_tin`Belarus TIN
Number123456789Belgium`eu_vat`European VAT numberBE0123456789Bosnia &
Herzegovina`ba_tin`Bosnia and Herzegovina Tax Identification
Number123456789012Bulgaria`eu_vat`European VAT
numberBG0123456789Cambodia`kh_tin`Cambodia Tax Identification
Number1001-123456789Canada`ca_bn`Canadian BN123456789Canada`ca_gst_hst`Canadian
GST/HST number123456789RT0002Canada`ca_pst_bc`Canadian PST number (British
Columbia)PST-1234-5678Canada`ca_pst_mb`Canadian PST number
(Manitoba)123456-7Canada`ca_pst_sk`Canadian PST number
(Saskatchewan)1234567Canada`ca_qst`Canadian QST number
(Québec)1234567890TQ1234Chile`cl_tin`Chilean TIN12.345.678-KCongo -
Kinshasa`cd_nif`Congo (DR) Tax Identification Number (Número de Identificação
Fiscal)A0123456MCosta Rica`cr_tin`Costa Rican tax
ID1-234-567890Croatia`eu_vat`European VAT
numberHR12345678912Cyprus`eu_vat`European VAT numberCY12345678ZCzech
Republic`eu_vat`European VAT numberCZ1234567890Denmark`eu_vat`European VAT
numberDK12345678Ecuador`ec_ruc`Ecuadorian RUC
number1234567890001Egypt`eg_tin`Egyptian Tax Identification
Number123456789Estonia`eu_vat`European VAT
numberEE123456789Finland`eu_vat`European VAT
numberFI12345678France`eu_vat`European VAT
numberFRAB123456789Georgia`ge_vat`Georgian VAT123456789Germany`eu_vat`European
VAT numberDE123456789Greece`eu_vat`European VAT
numberEL123456789Guinea`gn_nif`Guinea Tax Identification Number (Número de
Identificação Fiscal)123456789Hungary`eu_vat`European VAT
numberHU12345678Iceland`is_vat`Icelandic VAT123456India`in_gst`Indian GST
number12ABCDE3456FGZHIreland`eu_vat`European VAT
numberIE1234567ABItaly`eu_vat`European VAT
numberIT12345678912Kazakhstan`kz_bin`Kazakhstani Business Identification
Number123456789012Kenya`ke_pin`Kenya Revenue Authority Personal Identification
NumberP000111111ALatvia`eu_vat`European VAT
numberLV12345678912Liechtenstein`li_vat`Liechtensteinian VAT
number12345Lithuania`eu_vat`European VAT
numberLT123456789123Luxembourg`eu_vat`European VAT
numberLU12345678Malta`eu_vat`European VAT
numberMT12345678Mauritania`mr_nif`Mauritania Tax Identification Number (Número
de Identificação Fiscal)12345678Mexico`mx_rfc`Mexican RFC
numberABC010203AB9Moldova`md_vat`Moldova VAT
Number1234567Montenegro`me_pib`Montenegro PIB
Number12345678Morocco`ma_vat`Morocco VAT Number12345678Nepal`np_pan`Nepal PAN
Number123456789Netherlands`eu_vat`European VAT numberNL123456789B12New
Zealand`nz_gst`New Zealand GST number123456789Nigeria`ng_tin`Nigerian Tax
Identification Number12345678-0001North Macedonia`mk_vat`North Macedonia VAT
NumberMK1234567890123Norway`no_vat`Norwegian VAT
number123456789MVAOman`om_vat`Omani VAT NumberOM1234567890Peru`pe_ruc`Peruvian
RUC number12345678901Poland`eu_vat`European VAT
numberPL1234567890Portugal`eu_vat`European VAT
numberPT123456789Romania`eu_vat`European VAT
numberRO1234567891Russia`ru_inn`Russian INN1234567891Russia`ru_kpp`Russian
KPP123456789Saudi Arabia`sa_vat`Saudi Arabia
VAT123456789012345Senegal`sn_ninea`Senegal NINEA
Number12345672A2Serbia`rs_pib`Serbian PIB
number123456789Singapore`sg_gst`Singaporean
GSTM12345678XSlovakia`eu_vat`European VAT
numberSK1234567891Slovenia`eu_vat`European VAT numberSI12345678South
Africa`za_vat`South African VAT number4123456789South Korea`kr_brn`Korean
BRN123-45-67890Spain`es_cif`Spanish NIF number (previously Spanish CIF
number)A12345678Spain`eu_vat`European VAT
numberESA1234567ZSuriname`sr_fin`Suriname FIN
Number1234567890Sweden`eu_vat`European VAT
numberSE123456789123Switzerland`ch_vat`Switzerland VAT numberCHE-123.456.789
MWSTTaiwan`tw_vat`Taiwanese VAT12345678Tajikistan`tj_tin`Tajikistan Tax
Identification Number123456789Tanzania`tz_vat`Tanzania VAT
Number12345678AThailand`th_vat`Thai VAT1234567891234Turkey`tr_tin`Turkish Tax
Identification Number0123456789Uganda`ug_tin`Uganda Tax Identification
Number1014751879Ukraine`ua_vat`Ukrainian VAT123456789United Arab
Emirates`ae_trn`United Arab Emirates TRN123456789012345United
Kingdom`eu_vat`Northern Ireland VAT numberXI123456789United
Kingdom`gb_vat`United Kingdom VAT numberGB123456789Uruguay`uy_ruc`Uruguayan RUC
number123456789012Uzbekistan`uz_tin`Uzbekistan TIN
Number123456789Uzbekistan`uz_vat`Uzbekistan VAT
Number123456789012Zambia`zm_tin`Zambia Tax Identification
Number1004751879Zimbabwe`zw_tin`Zimbabwe Tax Identification Number1234567890

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [Accept a payment guide](https://docs.stripe.com/payments/accept-a-payment)
-
[tax_id_collection[enabled]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-tax_id_collection-enabled)
- [https://example.com/return](https://example.com/return)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
- [Customer](https://docs.stripe.com/api/customers/object)
-
[customer_creation](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_creation)
- [Customer](https://docs.stripe.com/api/customers)
-
[customer_details.tax_ids](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids)
- [name](https://docs.stripe.com/api/customers/object#customer_object-name)
-
[customer.tax_ids](https://docs.stripe.com/api/customers/object#customer_object-tax_ids)
-
[customer_update.name](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-name)
-
[customer_update.address](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-address)
-
[customer_update.shipping](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-shipping)
- [Session](https://docs.stripe.com/api/checkout/sessions/object)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [webhook](https://docs.stripe.com/webhooks)
- [Tax IDs](https://docs.stripe.com/api/tax_ids/list)
- [owner.type](https://docs.stripe.com/api/tax_ids/list#list_tax_ids-owner-type)
-
[owner.customer](https://docs.stripe.com/api/tax_ids/list#list_tax_ids-owner-customer)
- [Customer Tax ID
guide](https://docs.stripe.com/billing/customer/tax-ids#supported-tax-id)
- [test tax IDs](https://docs.stripe.com/connect/testing#test-business-tax-ids)
- [Australian Business
(ABN)](https://docs.stripe.com/billing/customer/tax-ids#abn)
- [European Value-Added-Tax (EU
VAT)](https://docs.stripe.com/billing/customer/tax-ids#eu-vat)
- [United Kingdom Value-Added-Tax (GB
VAT)](https://docs.stripe.com/billing/customer/tax-ids#gb-vat)
- [Customer Tax ID
guide](https://docs.stripe.com/billing/customer/tax-ids#validation)