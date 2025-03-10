# Supported attributes

## Review a complete list of attributes supported in Radar rules.

Use the following attributes within Radar to write rules. Learn how to write
effective [rules](https://docs.stripe.com/radar/rules/reference).

## Risk scores and levels

Attribute Type Example Value risk_levelCase Insensitive StringnormalThe risk
level of a given payment, as determined by Stripe. The supported values are:
normal, elevated, highest, not_assessed.risk_scoreNumeric50The risk score of a
given payment, as determined by Stripe. The values range between 0 (least risky)
and 100 (riskiest). By default, a risk score of 65 or above corresponds to a
risk level of elevated, while a risk score of 75 or above corresponds to a risk
level of highest. You can adjust the thresholds at [Risk
Settings](https://docs.stripe.com/radar/risk-settings).
## 3D Secure

Attribute Type Example Value is_3d_secureBooleantrueIdentifies if the payment
uses a 3D Secure source.is_3d_secure_authenticatedBooleantrueIdentifies if the
payment was authenticated after a successfully completed 3D Secure verification
(either risk-based or challenge-based).has_liability_shiftBooleantrueTrue if the
[liability shift
rule](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
might apply for this payment.
## Address

Attribute Type Example Value billing_addressCase Insensitive String1234 Main St
#2A Brooklyn NY 10022 USThe full provided cardholder billing
address.billing_address_line1Case Insensitive String1234 Main StThe first line
of the provided cardholder billing address (typically a street name and
number).billing_address_line2Case Insensitive String#2AThe second line of the
provided cardholder billing address (typically an apartment or unit
number).billing_address_postal_codeCase Insensitive String10022The postal code
(ZIP) of the provided cardholder billing address.billing_address_cityCase
Insensitive StringBrooklynThe city of the provided cardholder billing
address.billing_address_stateCase Insensitive StringNYThe state of the provided
cardholder billing address.billing_address_countryCase Insensitive CountryUSThe
two-letter code corresponding to the country of the provided cardholder billing
address.shipping_addressCase Insensitive String1234 Main St #2A Brooklyn NY
10022 USThe full provided shipping address.shipping_address_line1Case
Insensitive String1234 Main StThe first line of the provided shipping address
(typically a street name and number).shipping_address_line2Case Insensitive
String#2AThe second line of the provided shipping address (typically an
apartment or unit number).shipping_address_postal_codeCase Insensitive
String10022The postal code (ZIP) of the provided shipping
address.shipping_address_cityCase Insensitive StringBrooklynThe city of the
provided shipping address.shipping_address_stateCase Insensitive StringNYThe
state of the provided shipping address.shipping_address_countryCase Insensitive
CountryUSThe two-letter code corresponding to the country of the provided
shipping address.
## Amount

Attribute Type Example Value amount_in_xyzNumeric50The amount of the payment,
converted to the currency specified by xyz (for example, amount_in_usd). Specify
one of the following supported currencies and Stripe automatically calculates a
[converted
amount](https://docs.stripe.com/radar/rules/supported-attributes#converted-amounts)
to use: aed, ars, aud, brl, cad, chf, clp, cop, czk, dkk, eur, gbp, hkd, huf,
idr, ils, inr, jpy, khr, krw, mxn, myr, nok, nzd, php, pln, ron, rub, sek, sgd,
thb, try, twd, or usd. For decimal currencies (for example, usd), rules use the
base currency unit rather than sub units (for example, dollars, not
cents).average_usd_amount_attempted_on_card_all_timeNumeric50The average amount
(in USD) of attempted transactions for the card on your account within the past
five years. This value includes payments from 2020
onwards.average_usd_amount_attempted_on_customer_all_timeNumeric50The average
amount (in USD) of attempted transactions for the
[Customer](https://docs.stripe.com/api/customers) object on your account within
the past five years. This value includes payments from 2020
onwards.average_usd_amount_successful_on_card_all_timeNumeric50The average
amount (in USD) of transactions that resulted in an authorization for the card
on your account within the past five years. This value includes payments from
2020 onwards.average_usd_amount_successful_on_customer_all_timeNumeric50The
average amount (in USD) of transactions that resulted in an authorization for
the [Customer](https://docs.stripe.com/api/customers) object on your account.
This value includes payments from 2020
onwards.total_usd_amount_charged_on_card_all_timeNumeric50The total amount (in
USD) of transactions from this card that were attempted on your account. This
value includes payments from 2020
onwards.total_usd_amount_charged_on_customer_all_timeNumeric50The total amount
(in USD) of transactions from the
[Customer](https://docs.stripe.com/api/customers) object that were attempted on
your account. This value includes payments from 2020
onwards.total_usd_amount_failed_on_card_all_timeNumeric50The total amount (in
USD) of transactions from this card that failed (blocked or declined) on your
account. This value includes payments from 2020
onwards.total_usd_amount_failed_on_customer_all_timeNumeric50The total amount
(in USD) of transactions from the
[Customer](https://docs.stripe.com/api/customers) object that failed (blocked or
declined) on your account. This value includes payments from 2020
onwards.total_usd_amount_successful_on_card_all_timeNumeric50The total amount
(in USD) of transactions that resulted in an authorization for the card on your
account. This value includes payments from 2020
onwards.total_usd_amount_successful_on_customer_all_timeNumeric50The total
amount (in USD) of transactions that resulted in an authorization for the
[Customer](https://docs.stripe.com/api/customers) object on your account. This
value includes payments from 2020 onwards.
## Card Info

Attribute Type Example Value card_binCase Insensitive String483312The Bank
Identification Number (BIN) of the card used to make the payment. The BIN is the
first six digits of the card number.card_brandCase Insensitive StringvisaThe
brand of the card used to make the payment. The supported values are: amex
(American Express), visa (Visa), mc (Mastercard), dscvr (Discover), diners
(Diners Club), interac (Interac), jcb (JCB), and cup (UnionPay).card_countryCase
Insensitive CountryUSThe two-letter code corresponding to the country where the
card was issued.card_fingerprintCase Sensitive Stringexample_fingerprintThe
fingerprint of the card used to make the payment. The card fingerprint is a
unique identifier of a particular card number.card_fundingCase Insensitive
StringcreditWhether the card is a prepaid, debit, or credit card. The supported
values are: credit, debit, prepaid, unknown.card_3d_secure_supportCase
Insensitive StringrequiredThe level of [3D
Secure](https://docs.stripe.com/payments/3d-secure) support for the card used to
make the payment. The supported values are: required, recommended, optional, and
not_supported.charge_descriptionCase Insensitive Stringpayment for order #12The
description supplied with the payment.statement_descriptor NewCase Insensitive
Stringexample descriptorThe [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
provided on a payment.
## Card Usage

Attribute Type Example Value is_new_card_on_customerBooleantrueIdentifies if the
card associated with the [Customer](https://docs.stripe.com/api/customers)
object hasn’t been seen on a payment by that customer on your
account.card_count_for_billing_address_all_timeBounded numeric (≤25)10The number
of cards associated with this billing address from transactions on this account
within the past five years. This value includes payments from 2020
onwards.card_count_for_billing_address_weeklyBounded numeric (≤25)10The number
of cards associated with this billing address from transactions on this account
in the past week.card_count_for_billing_address_dailyBounded numeric (≤25)10The
number of cards associated with this billing address from transactions on this
account in the past day.card_count_for_billing_address_hourlyBounded numeric
(≤25)10The number of cards associated with this billing address from
transactions on this account in the past
hour.card_count_for_customer_all_timeBounded numeric (≤25)10The number of cards
associated with the [Customer](https://docs.stripe.com/api/customers) object
from transactions on this account within the past five years. This value
includes payments from 2020 onwards.card_count_for_customer_weeklyBounded
numeric (≤25)10The number of cards associated with the
[Customer](https://docs.stripe.com/api/customers) object from transactions on
this account in the past week.card_count_for_customer_dailyBounded numeric
(≤25)10The number of cards associated with the
[Customer](https://docs.stripe.com/api/customers) object from transactions on
this account in the past day.card_count_for_customer_hourlyBounded numeric
(≤25)10The number of cards associated with the
[Customer](https://docs.stripe.com/api/customers) object from transactions on
this account in the past hour.card_count_for_email_all_timeBounded numeric
(≤25)10The number of cards associated with this email from transactions on this
account within the past five years. This value includes payments from 2020
onwards.card_count_for_email_weeklyBounded numeric (≤25)10The number of cards
associated with this email from transactions on this account in the past
week.card_count_for_email_dailyBounded numeric (≤25)10The number of cards
associated with this email from transactions on this account in the past
day.card_count_for_email_hourlyBounded numeric (≤25)10The number of cards
associated with this email from transactions on this account in the past
hour.card_count_for_ip_address_all_timeBounded numeric (≤25)10The number of
cards associated with this IP address from transactions on your account within
the past five years. This value includes payments from 2020
onwards.card_count_for_ip_address_weeklyBounded numeric (≤25)10The number of
cards associated with this IP address from transactions on your account in the
past week.card_count_for_ip_address_dailyBounded numeric (≤25)10The number of
cards associated with this IP address from transactions on your account in the
past day.card_count_for_ip_address_hourlyBounded numeric (≤25)10The number of
cards associated with this IP address from transactions on your account in the
past hour.card_count_for_shipping_address_all_timeBounded numeric (≤25)10The
number of cards associated with this shipping address from transactions on your
account within the past five years. This value includes payments from 2020
onwards.card_count_for_shipping_address_weeklyBounded numeric (≤25)10The number
of cards associated with this shipping address from transactions on your account
in the past week.card_count_for_shipping_address_dailyBounded numeric (≤25)10The
number of cards associated with this shipping address from transactions on your
account in the past day.card_count_for_shipping_address_hourlyBounded numeric
(≤25)10The number of cards associated with this shipping address from
transactions on your account in the past hour.
## Charges that were authorized

Attribute Type Example Value
authorized_charges_per_billing_address_all_timeNumeric10The number of charges
that resulted in a successful authorization on this billing address on your
account within the past five years. This value includes payments from 2020
onwards.authorized_charges_per_billing_address_weeklyNumeric10The number of
charges that resulted in a successful authorization on this billing address in
the past week on your
account.authorized_charges_per_billing_address_dailyNumeric10The number of
charges that resulted in a successful authorization on this billing address in
the past day on your
account.authorized_charges_per_billing_address_hourlyNumeric10The number of
charges that resulted in a successful authorization on this billing address in
the past hour on your
account.authorized_charges_per_card_number_all_timeNumeric10The number of
charges that resulted in a successful authorization on this card on your account
within the past five years. This value includes payments from 2020
onwards.authorized_charges_per_card_number_weeklyNumeric10The number of charges
that resulted in a successful authorization on this card in the past week on
your account.authorized_charges_per_card_number_dailyNumeric10The number of
charges that resulted in a successful authorization on this card in the past day
on your account.authorized_charges_per_card_number_hourlyNumeric10The number of
charges that resulted in a successful authorization on this card in the past
hour on your account.authorized_charges_per_customer_all_timeNumeric10The number
of charges that resulted in a successful authorization from the
[Customer](https://docs.stripe.com/api/customers) object on your account within
the past five years. This value includes payments from 2020
onwards.authorized_charges_per_customer_weeklyNumeric10The number of charges
that resulted in a successful authorization from the
[Customer](https://docs.stripe.com/api/customers) object in the past week on
your account.authorized_charges_per_customer_dailyNumeric10The number of charges
that resulted in a successful authorization from the
[Customer](https://docs.stripe.com/api/customers) object in the past day on your
account.authorized_charges_per_customer_hourlyNumeric10The number of charges
that resulted in a successful authorization from the
[Customer](https://docs.stripe.com/api/customers) object in the past hour on
your account.authorized_charges_per_email_all_timeNumeric10The number of charges
that resulted in a successful authorization from this email on your account
within the past five years. This value includes payments from 2020
onwards.authorized_charges_per_email_weeklyNumeric10The number of charges that
resulted in a successful authorization from this email in the past week on your
account.authorized_charges_per_email_dailyNumeric10The number of charges that
resulted in a successful authorization from this email in the past day on your
account.authorized_charges_per_email_hourlyNumeric10The number of charges that
resulted in a successful authorization from this email in the past hour on your
account.authorized_charges_per_shipping_address_all_time NewNumeric10The number
of charges that resulted in a successful authorization on this shipping address
on your account within the past five years. This value includes payments from
2020 onwards.authorized_charges_per_shipping_address_weekly NewNumeric10The
number of charges that resulted in a successful authorization on this shipping
address in the past week on your
account.authorized_charges_per_shipping_address_dailyNumeric10The number of
charges that resulted in a successful authorization on this shipping address in
the past day on your
account.authorized_charges_per_shipping_address_hourlyNumeric10The number of
charges that resulted in a successful authorization on this shipping address in
the past hour on your
account.authorized_charges_per_ip_address_all_timeNumeric10The number of charges
that resulted in a successful authorization from this IP address on your account
within the past five years. This value includes payments from 2020
onwards.authorized_charges_per_ip_address_weeklyNumeric10The number of charges
that resulted in a successful authorization from this IP address in the past
week on your account.authorized_charges_per_ip_address_dailyNumeric10The number
of charges that resulted in a successful authorization from this IP address in
the past day on your
account.authorized_charges_per_ip_address_hourlyNumeric10The number of charges
that resulted in a successful authorization from this IP address in the past
hour on your account.
## Charges that were blocked

Attribute Type Example Value
blocked_charges_per_billing_address_all_timeNumeric10The number of charges
blocked on this billing address on your account within the past five years. This
value includes payments from 2020
onwards.blocked_charges_per_billing_address_weeklyNumeric10The number of charges
blocked on this billing address in the past week on your
account.blocked_charges_per_billing_address_dailyNumeric10The number of charges
blocked on this billing address in the past day on your
account.blocked_charges_per_billing_address_hourlyNumeric10The number of charges
blocked on this billing address in the past hour on your
account.blocked_charges_per_card_number_all_timeNumeric10The number of charges
blocked on this card on your account within the past five years. This value
includes payments from 2020
onwards.blocked_charges_per_card_number_weeklyNumeric10The number of charges
blocked on this card in the past week on your
account.blocked_charges_per_card_number_dailyNumeric10The number of charges
blocked on this card in the past day on your
account.blocked_charges_per_card_number_hourlyNumeric10The number of charges
blocked on this card in the past hour on your
account.blocked_charges_per_customer_all_timeNumeric10The number of charges
blocked from the [Customer](https://docs.stripe.com/api/customers) object on
your account within the past five years. This value includes payments from 2020
onwards.blocked_charges_per_customer_weeklyNumeric10The number of charges
blocked from the [Customer](https://docs.stripe.com/api/customers) object in the
past week on your account.blocked_charges_per_customer_dailyNumeric10The number
of charges blocked from the [Customer](https://docs.stripe.com/api/customers)
object in the past day on your
account.blocked_charges_per_customer_hourlyNumeric10The number of charges
blocked from the [Customer](https://docs.stripe.com/api/customers) object in the
past hour on your account.blocked_charges_per_email_all_timeNumeric10The number
of charges blocked from this email on your account within the past five years.
This value includes payments from 2020
onwards.blocked_charges_per_email_weeklyNumeric10The number of charges blocked
from this email in the past week on your
account.blocked_charges_per_email_dailyNumeric10The number of charges blocked
from this email in the past day on your
account.blocked_charges_per_email_hourlyNumeric10The number of charges blocked
from this email in the past hour on your
account.blocked_charges_per_shipping_address_all_timeNumeric10The number of
charges blocked on this shipping address on your account within the past five
years. This value includes payments from 2020
onwards.blocked_charges_per_shipping_address_weeklyNumeric10The number of
charges blocked on this shipping address in the past week on your
account.blocked_charges_per_shipping_address_dailyNumeric10The number of charges
blocked on this shipping address in the past day on your
account.blocked_charges_per_shipping_address_hourlyNumeric10The number of
charges blocked on this shipping address in the past hour on your
account.blocked_charges_per_ip_address_all_timeNumeric10The number of charges
blocked on this IP address on your account within the past five years. This
value includes payments from 2020
onwards.blocked_charges_per_ip_address_weeklyNumeric10The number of charges
blocked on this IP address in the past week on your
account.blocked_charges_per_ip_address_dailyNumeric10The number of charges
blocked on this IP address in the past day on your
account.blocked_charges_per_ip_address_hourlyNumeric10The number of charges
blocked on this IP address in the past hour on your account.
## Charges that were declined

Attribute Type Example Value
declined_charges_per_billing_address_all_timeNumeric10The number of charges
declined on this billing address on your account within the past five years.
This value includes payments from 2020
onwards.declined_charges_per_billing_address_weeklyNumeric10The number of
charges declined on this billing address in the past week on your
account.declined_charges_per_billing_address_dailyNumeric10The number of charges
declined on this billing address in the past day on your
account.declined_charges_per_billing_address_hourlyNumeric10The number of
charges declined on this billing address in the past hour on your
account.declined_charges_per_card_number_all_timeNumeric10The number of charges
declined on this card on your account within the past five years. This value
includes payments from 2020
onwards.declined_charges_per_card_number_weeklyNumeric10The number of charges
declined on this card in the past week on your
account.declined_charges_per_card_number_dailyNumeric10The number of charges
declined on this card in the past day on your
account.declined_charges_per_card_number_hourlyNumeric10The number of charges
declined on this card in the past hour on your
account.declined_charges_per_customer_all_timeNumeric10The number of charges
declined from the [Customer](https://docs.stripe.com/api/customers) object on
your account within the past five years. This value includes payments from 2020
onwards.declined_charges_per_customer_weeklyNumeric10The number of charges
declined from the [Customer](https://docs.stripe.com/api/customers) object in
the past week on your account.declined_charges_per_customer_dailyNumeric10The
number of charges declined from the
[Customer](https://docs.stripe.com/api/customers) object in the past day on your
account.declined_charges_per_customer_hourlyNumeric10The number of charges
declined from the [Customer](https://docs.stripe.com/api/customers) object in
the past hour on your
account.declined_charges_per_shipping_address_all_timeNumeric10The number of
charges declined on this shipping address on your account within the past five
years. This value includes payments from 2020
onwards.declined_charges_per_shipping_address_weeklyNumeric10The number of
charges declined on this shipping address in the past week on your
account.declined_charges_per_shipping_address_dailyNumeric10The number of
charges declined on this shipping address in the past day on your
account.declined_charges_per_shipping_address_hourlyNumeric10The number of
charges declined on this shipping address in the past hour on your
account.declined_charges_per_ip_address_all_timeNumeric10The number of charges
declined on this IP address on your account within the past five years. This
value includes payments from 2020
onwards.declined_charges_per_ip_address_weeklyNumeric10The number of charges
declined on this IP address in the past week on your
account.declined_charges_per_ip_address_dailyNumeric10The number of charges
declined on this IP address in the past day on your
account.declined_charges_per_ip_address_hourlyNumeric10The number of charges
declined on this IP address in the past hour on your
account.declined_charges_per_email_all_timeNumeric10The number of charges
declined from this email on your account within the past five years. This value
includes payments from 2020
onwards.declined_charges_per_email_weeklyNumeric10The number of charges declined
from this email in the past week on your
account.declined_charges_per_email_dailyNumeric10The number of charges declined
from this email in the past day on your
account.declined_charges_per_email_hourlyNumeric10The number of charges declined
from this email in the past hour on your account.
## Total charges

Attribute Type Example Value
total_charges_per_billing_address_all_timeNumeric10The total number of charges
on this billing address on your account within the past five years. This value
includes payments from 2020
onwards.total_charges_per_billing_address_weeklyNumeric10The total number of
charges on this billing address in the past week on your
account.total_charges_per_billing_address_dailyNumeric10The total number of
charges on this billing address in the past day on your
account.total_charges_per_billing_address_hourlyNumeric10The total number of
charges on this billing address in the past hour on your
account.total_charges_per_card_number_all_timeNumeric10The total number of
charges on this card on your account within the past five years. This value
includes payments from 2020
onwards.total_charges_per_card_number_weeklyNumeric10The total number of charges
on this card in the past week on your
account.total_charges_per_card_number_dailyNumeric10The total number of charges
on this card in the past day on your
account.total_charges_per_card_number_hourlyNumeric10The total number of charges
on this card in the past hour on your
account.total_charges_per_customer_all_timeNumeric10The total number of charges
from the [Customer](https://docs.stripe.com/api/customers) object on your
account within the past five years. This value includes payments from 2020
onwards.total_charges_per_customer_weeklyNumeric10The total number of charges
from the [Customer](https://docs.stripe.com/api/customers) object in the past
week on your account.total_charges_per_customer_dailyNumeric10The total number
of charges from the [Customer](https://docs.stripe.com/api/customers) object in
the past day on your account.total_charges_per_customer_hourlyNumeric10The total
number of charges from the [Customer](https://docs.stripe.com/api/customers)
object in the past hour on your
account.total_charges_per_email_all_timeNumeric10The total number of charges
from this email on your account within the past five years. This value includes
payments from 2020 onwards.total_charges_per_email_weeklyNumeric10The total
number of charges from this email in the past week on your
account.total_charges_per_email_dailyNumeric10The total number of charges from
this email in the past day on your
account.total_charges_per_email_hourlyNumeric10The total number of charges from
this email in the past hour on your
account.total_charges_per_ip_address_all_timeNumeric10The total number of
charges from this IP address on your account within the past five years. This
value includes payments from 2020
onwards.total_charges_per_ip_address_weeklyNumeric10The total number of charges
from this IP address in the past week on your
account.total_charges_per_ip_address_dailyNumeric10The total number of charges
from this IP address in the past day on your
account.total_charges_per_ip_address_hourlyNumeric10The total number of charges
from this IP address in the past hour on your
account.total_charges_per_shipping_address_all_timeNumeric10The total number of
charges from this shipping address on your account within the past five years.
This value includes payments from 2020
onwards.total_charges_per_shipping_address_weeklyNumeric10The total number of
charges from this shipping address in the past week on your
account.total_charges_per_shipping_address_dailyNumeric10The total number of
charges from this shipping address in the past day on your
account.total_charges_per_shipping_address_hourlyNumeric10The total number of
charges from this shipping address in the past hour on your account.
## Client information

Attribute Type Example Value browserCase Insensitive StringChrome 103.0.0The
customer’s browser name and version.ispCase Insensitive StringCactus Practice
ISPThe customer’s Internet Service Provider (ISP) name.operating_systemCase
Insensitive StringMac OS X 10.15.7The customer’s operating system name and
version.user_agentCase Insensitive Stringmozilla/5.0 (macintosh; intel mac os x
10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/103.0.0.0
safari/537.36The customer’s user agent.
## Customers

Attribute Type Example Value customerCase Sensitive Stringcus_AeFLnRaI51AbRiThe
[Customer](https://docs.stripe.com/api/customers) object ID supplied with the
payment.total_customers_for_card_yearlyBounded numeric (≤25)10The total number
of [Customer](https://docs.stripe.com/api/customers) objects associated with
this card on your account. This attribute only includes live mode Customer
objects that interacted with your account in the past year. This data updates at
most every 72 hours.total_customers_for_card_weeklyBounded numeric (≤25)10The
total number of [Customer](https://docs.stripe.com/api/customers) objects
associated with this card on your account. This attribute only includes live
mode Customer objects that interacted with your account in the past week. This
data updates at most every 72 hours.total_customers_for_email_yearlyBounded
numeric (≤25)10The total number of
[Customer](https://docs.stripe.com/api/customers) objects associated with this
email on your account. This attribute only includes live mode Customer objects
that interacted with your account in the past year. This data updates at most
every 72 hours.total_customers_for_email_weeklyBounded numeric (≤25)10The total
number of [Customer](https://docs.stripe.com/api/customers) objects associated
with this email on your account. This attribute only includes live mode Customer
objects that interacted with your account in the past week. This data updates at
most every 72
hours.total_customers_with_prior_fraud_activity_for_card_yearlyBounded numeric
(≤25)10The total number of [Customer](https://docs.stripe.com/api/customers)
objects associated with this card that have fraud activity on your account.
Fraud activity includes fraud disputes, early fraud warnings, and high risk
Radar blocks. This attribute only includes live mode Customer objects that
interacted with your account in the past year. This data updates at most every
72 hours.total_customers_with_prior_fraud_activity_for_card_weeklyBounded
numeric (≤25)10The total number of
[Customer](https://docs.stripe.com/api/customers) objects associated with this
card that have fraud activity on your account. Fraud activity includes fraud
disputes, early fraud warnings, and high risk Radar blocks. This attribute only
includes live mode Customer objects that interacted with your account in the
past week. This data updates at most every 72
hours.total_customers_with_prior_fraud_activity_for_email_yearlyBounded numeric
(≤25)10The total number of [Customer](https://docs.stripe.com/api/customers)
objects associated with this email that have fraud activity on your account.
Fraud activity includes fraud disputes, early fraud warnings, and high risk
Radar blocks. This attribute only includes live mode Customer objects that
interacted with your account in the past year. This data updates at most every
72 hours.total_customers_with_prior_fraud_activity_for_email_weeklyBounded
numeric (≤25)10The total number of
[Customer](https://docs.stripe.com/api/customers) objects associated with this
email that have fraud activity on your account. Fraud activity includes fraud
disputes, early fraud warnings, and high risk Radar blocks. This attribute only
includes live mode Customer objects that interacted with your account in the
past week. This data updates at most every 72 hours.
## Distance

Attribute Type Example Value distance_between_billing_and_shipping_address
NewNumeric50The distance (in km) between the provided billing address and the
provided shipping address.distance_between_ip_and_billing_address
NewNumeric50The distance (in km) between the IP address from which the payment
originates and the provided billing
address.distance_between_ip_and_shipping_address NewNumeric50The distance (in
km) between the IP address from which the payment originates and the provided
shipping address.
## Disputes

Attribute Type Example Value dispute_count_on_card_number_all_timeBounded
numeric (<=25)10The count of fraudulent disputes associated with charges from
this card number on your account within the past five years. This value includes
payments from 2019 onwards.dispute_count_on_card_number_yearlyBounded numeric
(<=25)10The count of fraudulent disputes associated with charges from this card
number on your account in the past year.dispute_count_on_ip_all_timeBounded
numeric (≤25)10The count of fraudulent disputes associated with charges from
this IP address on your account within the past five years. This value includes
payments from 2020 onwards.dispute_count_on_ip_weeklyBounded numeric (≤25)10The
count of fraudulent disputes associated with charges from this IP address on
your account in the past week.dispute_count_on_ip_dailyBounded numeric
(≤25)10The count of fraudulent disputes associated with charges from this IP
address on your account in the past day.dispute_count_on_ip_hourlyBounded
numeric (≤25)10The count of fraudulent disputes associated with charges from
this IP address on your account in the past hour.
## Early Fraud Warnings

Attribute Type Example Value efw_count_on_card_all_timeBounded numeric
(≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this card on your account within the past five
years. This value includes EFWs from 2020
onwards.efw_count_on_card_weeklyBounded numeric (≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this card on your account in the past
week.efw_count_on_card_dailyBounded numeric (≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this card on your account in the past
day.efw_count_on_card_hourlyBounded numeric (≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this card on your account in the past
hour.efw_count_on_ip_all_timeBounded numeric (≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this IP address on your account within the past
five years. This value includes EFWs from 2020
onwards.efw_count_on_ip_weeklyBounded numeric (≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this IP address on your account in the past
week.efw_count_on_ip_dailyBounded numeric (≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this IP address on your account in the past
day.efw_count_on_ip_hourlyBounded numeric (≤25)10The number of
[EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
associated with charges from this IP address on your account in the past hour.
## Email

Attribute Type Example Value emailCase Insensitive Stringuser@example.comThe
email address supplied with the payment.email_domainCase Insensitive
Stringexample.comThe domain of the email address supplied with the
payment.is_disposable_emailBooleantrueIdentifies if the email address supplied
with the payment uses a known throwaway email address provider. Stripe maintains
a list of domains corresponding to throwaway email addresses.
The **email_domain** and **is_disposable_email** attributes use the email
address found in any of the following fields:

- The `receipt_email` of the payment
- The `description` of the payment
- The `name` of the card (if an email address has been provided as the
cardholder name)
- The `email` of the customer that the payment was created on
- The `description` of the customer

## Email usage

Attribute Type Example Value email_count_for_billing_address_all_timeBounded
numeric (≤25)10The number of emails associated with this billing address from
transactions on your account within the past five years. This value includes
payments from 2020 onwards.email_count_for_billing_address_weeklyBounded numeric
(≤25)10The number of emails associated with this billing address from
transactions on your account in the past
week.email_count_for_billing_address_dailyBounded numeric (≤25)10The number of
emails associated with this billing address from transactions on your account in
the past day.email_count_for_billing_address_hourlyBounded numeric (≤25)10The
number of emails associated with this billing address from transactions on your
account in the past hour.email_count_for_card_all_timeBounded numeric (≤25)10The
number of emails associated with this card from transactions on your account
within the past five years. This value includes payments from 2020
onwards.email_count_for_card_weeklyBounded numeric (≤25)10The number of emails
associated with this card from transactions on your account in the past
week.email_count_for_card_dailyBounded numeric (≤25)10The number of emails
associated with this card from transactions on your account in the past
day.email_count_for_card_hourlyBounded numeric (≤25)10The number of emails
associated with this card from transactions on your account in the past
hour.email_count_for_ip_all_timeBounded numeric (≤25)10The number of emails
associated with this IP address from transactions on your account within the
past five years. This value includes payments from 2020
onwards.email_count_for_ip_weeklyBounded numeric (≤25)10The number of emails
associated with this IP address from transactions on your account in the past
week.email_count_for_ip_dailyBounded numeric (≤25)10The number of emails
associated with this IP address from transactions on your account in the past
day.email_count_for_ip_hourlyBounded numeric (≤25)10The number of emails
associated with this IP address from transactions on your account in the past
hour.email_count_for_shipping_address_all_timeBounded numeric (≤25)10The number
of emails associated with this shipping address from transactions on your
account within the past five years. This value includes payments from 2020
onwards.email_count_for_shipping_address_weeklyBounded numeric (≤25)10The number
of emails associated with this shipping address from transactions on your
account in the past week.email_count_for_shipping_address_dailyBounded numeric
(≤25)10The number of emails associated with this shipping address from
transactions on your account in the past
day.email_count_for_shipping_address_hourlyBounded numeric (≤25)10The number of
emails associated with this shipping address from transactions on your account
in the past hour.
## IP address

Attribute Type Example Value ip_addressCase Insensitive String192.168.1.1The IP
address from which the payment originates. If payment is made with
digital_wallet, the IP address might be missing due to obfuscation of the
payment’s originating IP address.ip_address_connection_type NewCase Insensitive
StringcellularThe connection type of the IP address from which the payment
originates. We identify the following types of connections: cable/dsl, cellular,
corporate, dialup.ip_countryCase Insensitive CountryUSThe two-letter code
corresponding to the country-level geolocation of the IP address that the
payment originates from.ip_state NewCase Insensitive StateCAThe ISO code
corresponding to the state-level geolocation of the IP address that the payment
originates from. If the country doesn’t have a state, this attribute populates
with the country’s closest version of a
state.is_anonymous_ipBooleantrueIdentifies if the IP address from which the
payment originates is a known proxy or Tor exit node. This information updates
daily.is_my_login_ipBooleantrueIdentifies if the IP address from which the
payment originates has been used to log into your Stripe account. You can use
this attribute as a proxy for “is my IP address.”
## Issuer Checks

Attribute Type Example Value address_line1_checkCase Sensitive StringpassA check
by the card issuer to match the first line of the provided billing address
(typically a street name and number) against the information they have on file
for the cardholder. The supported values are: pass, fail, unavailable,
unchecked, not_provided. ([This is a post-authorization
attribute.](https://docs.stripe.com/radar/rules/supported-attributes#post-authorization-attributes))address_zip_checkCase
Sensitive StringpassA check by the card issuer to match the provided postal code
against the information they have on file for the cardholder. The supported
values are: pass, fail, unavailable, unchecked, not_provided. ([This is a
post-authorization
attribute.](https://docs.stripe.com/radar/rules/supported-attributes#post-authorization-attributes))cvc_checkCase
Sensitive StringpassA check by the card issuer to match the provided CVC (also
referred to as CVV) against the information they have on file for the
cardholder. The supported values are: pass, fail, unavailable, unchecked,
not_provided. ([This is a post-authorization
attribute.](https://docs.stripe.com/radar/rules/supported-attributes#post-authorization-attributes))
## Name

Attribute Type Example Value cardholder_nameCase Insensitive StringJane DoeThe
provided name with a purchaser’s card information. This attribute isn’t case
sensitive, but it’s punctuation sensitive. You should only use this attribute to
block names or name patterns of individuals who you have reason to believe have
previously committed fraud on your service. We recommend that your customer
service teams are prepared to respond to any customer complaints and to add
legitimate end-customers to an “allowlist” where
appropriate.name_count_for_card_all_timeBounded numeric (≤25)10The number of
names associated with this card from transactions on your account within the
past five years. This value includes payments from 2020
onwards.name_count_for_card_weeklyBounded numeric (≤25)10The number of names
associated with this card from transactions on your account in the past
week.name_count_for_card_dailyBounded numeric (≤25)10The number of names
associated with this card from transactions on your account in the past
day.name_count_for_card_hourlyBounded numeric (≤25)10The number of names
associated with this card from transactions on your account in the past hour.
## Other payment details

Attribute Type Example Value currency NewCase Insensitive StringusdThe 3-digit
currency code representing the currency in which the customer paid for the
transaction.destinationCase Sensitive Stringacct_19KCB9AlaaEw6AgRFor Connect
users creating [destination
charges](https://docs.stripe.com/connect/destination-charges), the destination
account on whose behalf the charge is made.digital_walletCase Insensitive
Stringapple_payThe type of digital wallet used to store payment information. The
supported values are: android_pay, amex_express_checkout, apple_pay, masterpass,
samsung_pay, visa_checkout, meta_pay, amazon_pay, revolut_pay, demo_pay,
unknown, none. Note: Except for android_pay (valid with or without cryptogram),
these are only valid when we receive a cryptogram that can only be generated by
a registered device, as opposed to an unencrypted Primary Account
Number.is_checkoutBooleantrueIdentifies if the payment is processed through
[Checkout](https://docs.stripe.com/payments/checkout). (This attribute only
applies to payments processed through the current version of
[Checkout](https://docs.stripe.com/payments/checkout) and doesn’t capture
payments through legacy Checkout.)is_off_sessionBooleantrueIndicates when a
Stripe Billing payment isn’t triggered by direct user action, or when the
off_session flag is set at PaymentIntent
confirmation.is_recurringBooleantrueIdentifies if the payment is recurring, for
example, from subscriptions.has_cryptogramBooleantrueTrue when we receive a
cryptogram that can only be generated by a registered device, as opposed to an
unencrypted Primary Account Number.transaction_typeStringchargeThe type of the
transaction. The supported values are: charge, payment_intent, setup_intent. The
payment_intent value is only supported for Request Credentials rules. In that
case, any Allow, Block, or Review rules run against the charge attempts created
when confirming the payment.
## Refunds

Attribute Type Example Value refund_count_on_card_all_timeBounded numeric
(≤25)10The number of refunds associated with this billing address from
transactions on your account within the past five years. This value includes
payments from 2020 onwards.refund_count_on_card_weeklyBounded numeric (≤25)10The
number of refunds associated with this card from transactions on your account in
the past week.refund_count_on_card_dailyBounded numeric (≤25)10The number of
refunds associated with this card from transactions on your account in the past
day.refund_count_on_card_hourlyBounded numeric (≤25)10The number of refunds
associated with this card from transactions on your account in the past hour.
## Time

Attribute Type Example Value hours_since_customer_was_createdNumeric50The number
of hours since the [Customer](https://docs.stripe.com/api/customers) object
making the payment was created on your
account.hours_since_email_first_seenNumeric50The number of hours (up to five
years) since the email address supplied with the payment first appeared on your
account. This value includes payments from 2020
onwards.hours_since_email_first_seen_on_stripeNumeric50The number of hours (up
to five years) since the email address supplied with the payment first appeared
on Stripe overall. This value includes payments from 2020
onwards.hours_since_card_first_seenNumeric50The number of hours (up to five
years) since the card for the payment first appeared on your account. This value
includes payments from 2020
onwards.hours_since_first_successful_auth_on_cardNumeric50The number of hours
since the first successful auth for the card associated with the payment
happened on your account. This value includes payments from 2020
onwards.minutes_since_customer_was_createdNumeric50The number of minutes since
the [Customer](https://docs.stripe.com/api/customers) object making the payment
was created on your account.minutes_since_email_first_seenNumeric50The number of
minutes (up to five years) since the email address supplied with the payment
first appeared on your account. This value includes payments from 2020
onwards.minutes_since_email_first_seen_on_stripeNumeric50The number of minutes
(up to five years) since the email address supplied with the payment first
appeared on Stripe overall. This value includes payments from 2020
onwards.minutes_since_card_first_seenNumeric50The number of minutes (up to five
years) since the card for the payment first appeared on your account. This value
includes payments from 2020
onwards.minutes_since_first_successful_auth_on_cardNumeric50The number of
minutes since the first successful auth for the card associated with the payment
happened on your account. This value includes payments from 2020
onwards.seconds_since_customer_was_createdNumeric50The number of seconds since
the [Customer](https://docs.stripe.com/api/customers) object making the payment
was created on your account.seconds_since_email_first_seenNumeric50The number of
seconds (up to five years) since the email address supplied with the payment
first appeared on your account. This value includes payments from 2020
onwards.seconds_since_email_first_seen_on_stripeNumeric50The number of seconds
(up to five years) since the email address supplied with the payment first
appeared on Stripe overall. This value includes payments from 2020
onwards.seconds_since_card_first_seenNumeric50The number of seconds (up to five
years) since the card for the payment first appeared on your account. This value
includes payments from 2020
onwards.seconds_since_first_successful_auth_on_cardNumeric50The number of
seconds since the first successful authorization for the card associated with
the payment on your account. This value includes payments from 2020 onwards.
## See also

- [Rules](https://docs.stripe.com/radar/rules)
- [Rules Reference](https://docs.stripe.com/radar/rules/reference)

## Links

- [rules](https://docs.stripe.com/radar/rules/reference)
- [Risk Settings](https://docs.stripe.com/radar/risk-settings)
- [liability shift
rule](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
- [Customer](https://docs.stripe.com/api/customers)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [EFWs](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Rules](https://docs.stripe.com/radar/rules)