# Customer Tax IDs

## Learn how to store, validate, and render customer tax ID numbers with Stripe Billing.

Displaying a customer’s tax ID on
[invoice](https://docs.stripe.com/api/invoices) documents is a common
requirement that you can satisfy by adding tax IDs to customers. A customer’s
tax IDs display in the header of invoice and credit note PDFs.

## Supported Tax ID types

Currently, Stripe supports the following Tax ID types in the following regions:

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

You’re responsible for the accuracy of customer information including their tax
ID number. The invoice includes the customer tax ID whether or not it’s valid.

Stripe provides automatic validation to help determine ​​if the formatting is
correct when you add the ID to our system. You can see the results of the
validation in the Dashboard along with other customer information, including
details returned from the government databases, and the registered name and
address. However, we don’t continue to validate them over time. ​​If automatic
validation isn’t available, you must manually verify these IDs.

### Australian Business Numbers (ABN)

Stripe automatically validates all Australian Business Numbers (ABNs) with the
[Australian Business Register (ABR)](https://abr.gov.au/).

### European Value-Added-Tax (EU VAT) Numbers

Stripe also automatically validates all European Value-Added-Tax (EU VAT)
numbers with the [European Commission’s VAT Information Exchange System
(VIES)](http://ec.europa.eu/taxation_customs/vies/). This process only validates
whether or not the tax ID is valid—you still need to verify the customer’s name
and address to make sure it matches the registration information.

VIES validation usually takes only a few seconds, but depending on the
availability of various government databases, might take longer. Stripe
automatically handles VIES downtime and attempts retries.

### United Kingdom Value-Added-Tax (GB VAT) Numbers

Stripe automatically validates all UK Value-Added-Tax (GB VAT) numbers with the
[United Kingdom’s Revenue & Customs (HMRC)](https://www.gov.uk/). This process
only validates whether or not the tax ID is valid—you still need to verify the
customer’s name and address to make sure it matches the registration
information.

HMRC validation usually takes only a few seconds, but depending on the
availability, might take longer. Stripe automatically handles HMRC downtime and
attempts retries.

### Testing customer tax ID verification

Use these magic tax IDs to trigger certain verification conditions in test mode.
The tax ID type must be either the EU VAT Number or Australian Business Number
(ABN).

NumberType`000000000`Successful verification`111111111`Unsuccessful
verification`222222222`Verification remains pending indefinitely
### Validation webhooks and Dashboard display

Because this validation process happens asynchronously, the
[customer.tax_id.updated](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.updated)
webhook notifies you of validation updates.

Hover over a customer’s EU VAT number to display their VIES information.

The Dashboard displays the results of the validation within the customer
details, including information returned from the government databases, and the
registered name and address.

When automatic validation isn’t available, you must manually verify these IDs.

## Managing

You can manage tax IDs in the Dashboard, with the [customer
portal](https://docs.stripe.com/customer-management), or the [Tax ID
API](https://docs.stripe.com/api/customer_tax_ids).

DashboardAPI
To add a tax ID:

- Navigate to the [Customers](https://dashboard.stripe.com/customers) page, and
select the applicable customer.
- Click the pencil icon next to **Details** on the right.
- Scroll down to **Tax Status** and **Tax ID** fields.
- Click **Add another ID** to add a row to the tax ID list, where you can select
the ID type and value.

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [Australian Business Register (ABR)](https://abr.gov.au/)
- [European Commission’s VAT Information Exchange System
(VIES)](http://ec.europa.eu/taxation_customs/vies/)
- [United Kingdom’s Revenue & Customs (HMRC)](https://www.gov.uk/)
-
[customer.tax_id.updated](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.updated)
- [customer portal](https://docs.stripe.com/customer-management)
- [Tax ID API](https://docs.stripe.com/api/customer_tax_ids)
- [Customers](https://dashboard.stripe.com/customers)