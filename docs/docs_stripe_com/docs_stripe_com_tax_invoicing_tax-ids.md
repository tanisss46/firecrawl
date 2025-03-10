# Account and customer tax IDs with Invoicing

## Learn about storing, validating, and rendering tax ID numbers for Invoicing.

With Stripe, you can manage tax IDs ​​for both yourself and your customers. Both
the account and customer tax IDs display in the header of
[invoice](https://docs.stripe.com/api/invoices) and credit note PDFs.

## Account tax IDs

Displaying your tax IDs on invoice documents is a common regulatory requirement.

With Stripe, you can add up to 25 tax IDs to your account. You can see your tax
IDs in the header of invoice and credit note PDFs. You can:

- Select default tax IDs to appear on every invoice and credit note PDF.
- Define a list of tax IDs to appear on a specific invoice.

#### Caution

You can’t add, change, or remove account tax IDs after an invoice is finalized.

## Managing account tax IDs

You can add and delete tax IDs using the [invoice
settings](https://dashboard.stripe.com/settings/billing/invoice) page in the
Dashboard. After you add a tax ID in the Dashboard, you can set it as the
default tax ID for every invoice and credit note PDF. Tax IDs are immutable—you
can’t change the country and ID after you save the tax ID to your account.

Additionally, you can add and delete tax IDs with the
[create](https://docs.stripe.com/api/tax_ids/create) and
[delete](https://docs.stripe.com/api/tax_ids/delete) endpoints.

### Adding and removing IDs

DashboardAPI
Visit the [invoice
settings](https://dashboard.stripe.com/settings/billing/invoice) page. Click the
**Tax** tab and add a new tax ID or remove an existing tax ID:

![Manage tax IDs in the Stripe
Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/manage-add.f10a7efcaf2ce75e42bc986ff3954c0b.png)

Manage account tax IDs in the Dashboard

### Setting default tax IDs

On the [invoice settings](https://dashboard.stripe.com/settings/billing/invoice)
page, click the **Tax** tab and locate the tax ID you want to set as the
default. Click the overflow menu (), select **Set as default**, and click
**Save**.

![Set default tax ID in the Stripe
Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/manage-default.c36bf6e90db0825b107b5b6d375396cf.png)

Set default account tax ID in the Dashboard

​​After you set a tax ID as the default, you can see a label in the tax
information box:

![A default tax ID in the Stripe
Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/manage-default-set.a1c4d9a7605eabbe0491fb64cf031397.png)

A default account tax ID in the Dashboard

## Displaying tax IDs on invoices

Stripe automatically pulls your [default tax
IDs](https://docs.stripe.com/tax/invoicing/tax-ids#default-tax-ids) during
invoice finalization.

To override the default and display multiple tax IDs on invoices, you can set
tax IDs in the Dashboard or by using the API. To learn more about taxes and
invoices, see [Taxes](https://docs.stripe.com/invoicing/taxes).

DashboardAPI
You can set a list of tax IDs in the Dashboard using the Invoice Editor. ​​You
can’t modify account tax IDs after an Invoice has been finalized.

In the Invoice Editor, scroll down to the **Advanced Options** section. Click
the checkboxes to toggle which tax IDs ​​to display on that invoice. To remove
tax IDs from the invoice, uncheck the boxes.

![Tax ID invoice settings in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/invoice-editor.1e64187379099e87ac0eb00a4a1c0e15.png)

Advanced Options section in the Invoice Editor

## Customer tax IDs

Collecting and displaying a customer’s tax ID on an invoice is a common
requirement for B2B sales. With Stripe, you can add up to five tax IDs to a
customer. You can see a customer’s tax IDs in the header of invoice and credit
note PDFs. You can collect a tax ID with Stripe Checkout, or pass us a tax ID
directly.

#### Note

[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to enable Stripe Tax.

## Supported tax ID types

#### Note

Need another tax ID type? Request additional tax ID types by emailing us at
[stripe-tax@stripe.com](mailto:stripe-tax@stripe.com?subject=%5BTax%20ID%20request%5D).

Currently, Stripe supports the following tax ID types in the following regions:

CountryEnumDescriptionExampleAlbania`al_tin`Albania Tax Identification
NumberJ12345678NAndorra`ad_nrt`Andorran NRT numberA-123456-ZAngola`ao_tin`Angola
Tax Identification Number5123456789Argentina`ar_cuit`Argentinian tax ID
number12-3456789-01Armenia`am_tin`Armenia Tax Identification
Number02538904Australia`au_abn`Australian Business Number (AU
ABN)12345678912Australia`au_arn`Australian Taxation Office Reference
Number123456789123Austria`eu_vat`European VAT
numberATU12345678Bahamas`bs_tin`Bahamas Tax Identification
Number123.456.789Bahrain`bh_vat`Bahraini VAT
Number123456789012345Barbados`bb_tin`Barbados Tax Identification
Number1123456789012Belarus`by_tin`Belarus TIN
Number123456789Belgium`eu_vat`European VAT
numberBE0123456789Bolivia`bo_tin`Bolivian tax ID123456789Bosnia &
Herzegovina`ba_tin`Bosnia and Herzegovina Tax Identification
Number123456789012Brazil`br_cnpj`Brazilian CNPJ
number01.234.456/5432-10Brazil`br_cpf`Brazilian CPF
number123.456.789-87Bulgaria`bg_uic`Bulgaria Unified Identification
Code123456789Bulgaria`eu_vat`European VAT
numberBG0123456789Cambodia`kh_tin`Cambodia Tax Identification
Number1001-123456789Canada`ca_bn`Canadian BN123456789Canada`ca_gst_hst`Canadian
GST/HST number123456789RT0002Canada`ca_pst_bc`Canadian PST number (British
Columbia)PST-1234-5678Canada`ca_pst_mb`Canadian PST number
(Manitoba)123456-7Canada`ca_pst_sk`Canadian PST number
(Saskatchewan)1234567Canada`ca_qst`Canadian QST number
(Québec)1234567890TQ1234Chile`cl_tin`Chilean TIN12.345.678-KChina`cn_tin`Chinese
tax ID123456789012345678Colombia`co_nit`Colombian NIT number123.456.789-0Congo -
Kinshasa`cd_nif`Congo (DR) Tax Identification Number (Número de Identificação
Fiscal)A0123456MCosta Rica`cr_tin`Costa Rican tax
ID1-234-567890Croatia`eu_vat`European VAT
numberHR12345678912Croatia`hr_oib`Croatian Personal Identification
Number12345678901Cyprus`eu_vat`European VAT numberCY12345678ZCzech
Republic`eu_vat`European VAT numberCZ1234567890Denmark`eu_vat`European VAT
numberDK12345678Dominican Republic`do_rcn`Dominican RCN
number123-4567890-1Ecuador`ec_ruc`Ecuadorian RUC
number1234567890001Egypt`eg_tin`Egyptian Tax Identification Number123456789El
Salvador`sv_nit`El Salvadorian NIT
number1234-567890-123-4Estonia`eu_vat`European VAT
numberEE123456789EU`eu_oss_vat`European One Stop Shop VAT number for non-Union
schemeEU123456789Finland`eu_vat`European VAT
numberFI12345678France`eu_vat`European VAT
numberFRAB123456789Georgia`ge_vat`Georgian VAT123456789Germany`de_stn`German Tax
Number (Steuernummer)1234567890Germany`eu_vat`European VAT
numberDE123456789Greece`eu_vat`European VAT
numberEL123456789Guinea`gn_nif`Guinea Tax Identification Number (Número de
Identificação Fiscal)123456789Hong Kong`hk_br`Hong Kong BR
number12345678Hungary`eu_vat`European VAT numberHU12345678Hungary`hu_tin`Hungary
tax number (adószám)12345678-1-23Iceland`is_vat`Icelandic
VAT123456India`in_gst`Indian GST
number12ABCDE3456FGZHIndonesia`id_npwp`Indonesian NPWP
number012.345.678.9-012.345Ireland`eu_vat`European VAT
numberIE1234567ABIsrael`il_vat`Israel VAT000012345Italy`eu_vat`European VAT
numberIT12345678912Japan`jp_cn`Japanese Corporate Number (*Hōjin
Bangō*)1234567891234Japan`jp_rn`Japanese Registered Foreign Businesses'
Registration Number (*Tōroku Kokugai Jigyōsha no Tōroku
Bangō*)12345Japan`jp_trn`Japanese Tax Registration Number (*Tōroku
Bangō*)T1234567891234Kazakhstan`kz_bin`Kazakhstani Business Identification
Number123456789012Kenya`ke_pin`Kenya Revenue Authority Personal Identification
NumberP000111111ALatvia`eu_vat`European VAT
numberLV12345678912Liechtenstein`li_uid`Liechtensteinian UID
numberCHE123456789Liechtenstein`li_vat`Liechtensteinian VAT
number12345Lithuania`eu_vat`European VAT
numberLT123456789123Luxembourg`eu_vat`European VAT
numberLU12345678Malaysia`my_frp`Malaysian FRP
number12345678Malaysia`my_itn`Malaysian ITNC 1234567890Malaysia`my_sst`Malaysian
SST numberA12-3456-78912345Malta`eu_vat`European VAT
numberMT12345678Mauritania`mr_nif`Mauritania Tax Identification Number (Número
de Identificação Fiscal)12345678Mexico`mx_rfc`Mexican RFC
numberABC010203AB9Moldova`md_vat`Moldova VAT
Number1234567Montenegro`me_pib`Montenegro PIB
Number12345678Morocco`ma_vat`Morocco VAT Number12345678Nepal`np_pan`Nepal PAN
Number123456789Netherlands`eu_vat`European VAT numberNL123456789B12New
Zealand`nz_gst`New Zealand GST number123456789Nigeria`ng_tin`Nigerian Tax
Identification Number12345678-0001North Macedonia`mk_vat`North Macedonia VAT
NumberMK1234567890123Norway`no_vat`Norwegian VAT
number123456789MVANorway`no_voec`Norwegian VAT on e-commerce
number1234567Oman`om_vat`Omani VAT NumberOM1234567890Peru`pe_ruc`Peruvian RUC
number12345678901Philippines`ph_tin`Philippines Tax Identification
Number123456789012Poland`eu_vat`European VAT
numberPL1234567890Portugal`eu_vat`European VAT
numberPT123456789Romania`eu_vat`European VAT
numberRO1234567891Romania`ro_tin`Romanian tax ID
number1234567890123Russia`ru_inn`Russian INN1234567891Russia`ru_kpp`Russian
KPP123456789Saudi Arabia`sa_vat`Saudi Arabia
VAT123456789012345Senegal`sn_ninea`Senegal NINEA
Number12345672A2Serbia`rs_pib`Serbian PIB
number123456789Singapore`sg_gst`Singaporean
GSTM12345678XSingapore`sg_uen`Singaporean UEN123456789FSlovakia`eu_vat`European
VAT numberSK1234567891Slovenia`eu_vat`European VAT
numberSI12345678Slovenia`si_tin`Slovenia tax number (davčna
številka)12345678South Africa`za_vat`South African VAT number4123456789South
Korea`kr_brn`Korean BRN123-45-67890Spain`es_cif`Spanish NIF number (previously
Spanish CIF number)A12345678Spain`eu_vat`European VAT
numberESA1234567ZSuriname`sr_fin`Suriname FIN
Number1234567890Sweden`eu_vat`European VAT
numberSE123456789123Switzerland`ch_uid`Switzerland UID numberCHE-123.456.789
HRSwitzerland`ch_vat`Switzerland VAT numberCHE-123.456.789
MWSTTaiwan`tw_vat`Taiwanese VAT12345678Tajikistan`tj_tin`Tajikistan Tax
Identification Number123456789Tanzania`tz_vat`Tanzania VAT
Number12345678AThailand`th_vat`Thai VAT1234567891234Turkey`tr_tin`Turkish Tax
Identification Number0123456789Uganda`ug_tin`Uganda Tax Identification
Number1014751879Ukraine`ua_vat`Ukrainian VAT123456789United Arab
Emirates`ae_trn`United Arab Emirates TRN123456789012345United
Kingdom`eu_vat`Northern Ireland VAT numberXI123456789United
Kingdom`gb_vat`United Kingdom VAT numberGB123456789United States`us_ein`United
States EIN12-3456789Uruguay`uy_ruc`Uruguayan RUC
number123456789012Uzbekistan`uz_tin`Uzbekistan TIN
Number123456789Uzbekistan`uz_vat`Uzbekistan VAT
Number123456789012Venezuela`ve_rif`Venezuelan RIF
numberA-12345678-9Vietnam`vn_tin`Vietnamese tax ID
number1234567890Zambia`zm_tin`Zambia Tax Identification
Number1004751879Zimbabwe`zw_tin`Zimbabwe Tax Identification Number1234567890
## Validation

It’s your responsibility to make sure customer information is accurate
(including their tax ID). Stripe displays a customer tax ID on an invoice,
whether or not it is valid.

Stripe checks the format of the tax ID against the expected format, and
asynchronously validates the tax ID against the external tax authority system
for the tax ID types below.

### Australian Business Numbers (ABN)

Stripe automatically validates all Australian Business Numbers (ABNs) with the
[Australian Business Register (ABR)](https://abr.gov.au/).

### European Value-Added-Tax (EU VAT) Numbers

Stripe automatically validates all European Value-Added-Tax (EU VAT) numbers
with the [European Commission’s VAT Information Exchange System
(VIES)](http://ec.europa.eu/taxation_customs/vies/). This process only validates
whether or not the tax ID is valid—you still need to verify the customer’s name
and address to make sure it matches the registration information.

VIES validation usually takes only a few seconds,but may take longer, depending
on the availability of the external tax authority system. Stripe will
automatically handle VIES downtime and attempt retries for you.

### United Kingdom Value-Added-Tax (GB VAT) Numbers

Stripe automatically validates all UK Value-Added-Tax (GB VAT) numbers with the
[United Kingdom’s Revenue & Customs (HMRC)](https://www.gov.uk/). This process
only verifies that the tax ID is valid—you still need to verify the customer’s
name and address to make sure it matches the registration information.

HMRC validation usually takes only a few seconds, but may take longer, depending
on the availability. Stripe automatically handles HMRC downtime and attempts
retries for you.

### Validation webhooks and Dashboard display

Because this validation process happens asynchronously, the
customer.tax_id.updated webhook notifies you of validation updates.

!

The Dashboard displays the results of the validation while displaying the
customer details, including those returned from the government databases and the
registered name and address.

When automatic validation isn’t available, you need to manually verify these
IDs.

## Managing customer tax IDs

You can manage tax IDs in the Customers page in the Dashboard, in the customer
portal, or with the API.

DashboardAPI
To add a customer tax ID in the Dashboard, navigate to the Customers page, and
click **Update details** in the top of the **Details** panel. The Update
customer invoice details modal opens, with the tax ID section visible.

Clicking the **Add tax ID** link adds a row to the tax ID list, where you can
select the ID type and value. Removing the row removes a tax ID from a customer.

![A customer's tax IDs in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/ids_update_customer.4a68e5df884bdad0b0ce78264850b107.png)

## See also

- [Activating Stripe Tax](https://docs.stripe.com/tax/set-up)
- [Checkout and tax IDs](https://docs.stripe.com/tax/checkout/tax-ids)
- [Understanding zero tax amounts](https://docs.stripe.com/tax/zero-tax)
- [Connected account tax IDs on
invoices](https://docs.stripe.com/connect/invoices#account-tax-ids)

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [invoice settings](https://dashboard.stripe.com/settings/billing/invoice)
- [create](https://docs.stripe.com/api/tax_ids/create)
- [delete](https://docs.stripe.com/api/tax_ids/delete)
- [Taxes](https://docs.stripe.com/invoicing/taxes)
- [Log in](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [Australian Business Register (ABR)](https://abr.gov.au/)
- [European Commission’s VAT Information Exchange System
(VIES)](http://ec.europa.eu/taxation_customs/vies/)
- [United Kingdom’s Revenue & Customs (HMRC)](https://www.gov.uk/)
- [Activating Stripe Tax](https://docs.stripe.com/tax/set-up)
- [Checkout and tax IDs](https://docs.stripe.com/tax/checkout/tax-ids)
- [Understanding zero tax amounts](https://docs.stripe.com/tax/zero-tax)
- [Connected account tax IDs on
invoices](https://docs.stripe.com/connect/invoices#account-tax-ids)