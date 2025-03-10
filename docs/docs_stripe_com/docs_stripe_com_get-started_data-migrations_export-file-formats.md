# Export file formats

## Review the exported data for different payment types.

Stripe won’t change our export format. New processors can filter, map, and
adjust the format of export files as needed. Our standard service level
agreement (SLA) is 10 days to complete an export after we receive all valid data
(excluding BACS).

We export ACH, SEPA, BACS, and PADs/ACSS as a CSV. We can also export card data
in both CSV and JSON formats.

## Card export fields

Card exports include the following fields.

- CSV exports don’t include unique metadata fields by default, but we can
include them if you provide an exact list of field names.
- Small JSON exports include the customer metadata by default.
FieldDescription`description`Text attached to the customer object`name`Name
associated with the customer`email`Customer’s email`id`Stripe’s unique
identifier of the customer (cus_XXXXX format)`card.address_city`City associated
with the card`card.address_country`Country associated with the
card`card.address_line1`First address line associated with the
card`card.address_line2`Second address line associated with the
card`card.address_state`State or province associated with the
card`card.address_zip`Postal code associated with the card`card.exp_month`The
month the card expires`card.exp_year`The year the card expires`card.id`The
Stripe card ID object (card_XXXXX format)`card.name`Customer’s name on the
card`card.number`The PAN (credit card number)`default_source`Stripe object
associated with the customer’s default payment method (could be card_ID, pm_ID,
src_ID, or ba_ID)`card.transaction_ids`Network transaction ID status for SCA
compliance
### Example card data export

DESCRIPTIONNAMEEMAILIDCARD.ADDRESS_CITYCARD.ADDRESS_COUNTRYCARD.ADDRESS_LINE1CARD.ADDRESS_LINE2CARD.ADDRESS_STATECARD.ADDRESS_ZIPCARD.EXP_MONTHCARD.EXP_YEARCARD.IDCARD.NAMECARD.NUMBERDEFAULT_SOURCECARD.TRANSACTION_IDSUser
descriptionStripey McStripetest@example.comcus_JeGmWqYRVUNu44AnytownUS101 1st
AveApt 1CA9021092021card_1J0yEyH65PkfON7E6pXEeoyZStripey
McStripe5555551BT8Gs4444card_1J0yEyH65PkfON7EQ0Owsy3Q012345678901234User
descriptionStripey McStripetest@example.comcus_JeGmWqYRVUNu44AnytownUS101 1st
AveApt 1CA9021092021card_1J0yEyH65PkfON7EQ0Owsy3QStripey
McStripe424242TPSa0L4242card_1J0yEyH65PkfON7EQ0Owsy3Q012345678901234User
descriptionStripey McStripetest@example.comcus_JeGmJLltEqM9jdAnytownUS101 1st
AveApt 1CA9021092021card_1J0yEyH65PkfON7EzGiGLo9cStripey
McStripe424242TPSa0L4242card_1J0yEyH65PkfON7EzGiGLo9c012345678901234User
descriptionStripey McStripetest@example.comcus_JeGmdHOz48B3XAAnytownUS101 1st
AveApt 1CA9021092021card_1J0yExH65PkfON7E7ZHA0keFStripey
McStripe424242TPSa0L4242card_1J0yExH65PkfON7E7ZHA0keF012345678901234
## ACH Export Fields

ACH exports include the following fields.

FieldDescription`customer_id`Stripe’s unique identifier of the customer
(cus_XXXXX format)`customer_created`Date that the customer object was created in
Stripe`email`Customer’s email`description`Description text attached to the
customer object`default_source`Stripe object associated with the customer’s
default payment method (could be card_ID, pm_ID, src_ID, or
ba_ID)`bank_account_id`The Stripe bank account object ID (ba_XXXXX
format)`routing_number`Bank routing number`account_number`Customer’s bank
account number`account_holder_name`Customer name associated with the bank
account`account_holder_type`Boolean value that marks whether the account is
owned by an individual or company`country`Country associated with the bank
account
### Example ACH data export

customer_idcustomer_creatednameemaildescriptiondefault_sourcebank_account_idrouting_numberaccount_numberaccount_holder_nameaccount_holder_typecountryusecus_JdW0ZauDFfHkfi2021-06-09T00:08:59.062ZStripey
McStripetest@example.comUser
descriptionba_1J0EydH65PkfON7EQIkjVJUbba_1J0EydH65PkfON7EQIkjVJUb110000000000123456789Stripey
McStripeindividualUScheckingcus_JdW0wbOcikkCIK2021-06-09T00:08:59.659ZStripey
McStripetest@example.comUser
descriptionba_1J0EydH65PkfON7EuWIUgHnwba_1J0EydH65PkfON7EuWIUgHnw110000000000123456789Stripey
McStripeindividualUScheckingcus_JdW05ASZDyr9mS2021-06-09T00:09:00.161ZStripey
McStripetest@example.comUser
descriptionba_1J0EyeH65PkfON7E98oBUhwDba_1J0EyeH65PkfON7E98oBUhwD110000000000123456789Stripey
McStripeindividualUScheckingcus_JdW02JwM87cx9r2021-06-09T00:09:00.711ZStripey
McStripetest@example.comUser
descriptionba_1J0EyeH65PkfON7EfaUw4Excba_1J0EyeH65PkfON7EfaUw4Exc110000000000123456789Stripey
McStripeindividualUScheckingcus_JdW02JwM87cx9r2021-06-09T00:09:00.711ZStripey
McStripetest@example.comUser
descriptionba_1J0EyeH65PkfON7EfaUw4Excba_1J0EyfH65PkfON7EyHeoTbF9110000000000444444440Stripey
McStripeindividualUSchecking
## SEPA export fields

SEPA exports include the following fields.

FieldDescription`customer_id`Stripe’s unique identifier of the customer
(cus_XXXXX format)`email`Customer’s email`description`Description text attached
to the customer object`source_id`Stripe source ID associated with the customer’s
payment method`payment_method_id`Stripe payment method ID associated with the
customer’s payment method`owner_name`Customer name associated with the direct
debit account`iban`IBAN associated with the mandate`mandate_reference`Unique
identifier of the direct debit mandate on Stripe`currency`Currency associated
with the payment method
### Example SEPA data export

CUSTOMER_IDEMAILDESCRIPTIONSOURCE_IDPAYMENT_METHOD_IDOWNER_NAMEIBANMANDATE_REFERENCECURRENCYcus_111111111test@example.comDescription1src_1111111Stripey
McStripeGB22TESTBB20201555555555mandate_xxxxeurcus_222222222test@example.comDescription2pm_2222222Rory
O’DDE22TESTBB20201555555555mandate_yyyyeurcus_333333333test2@example.comDescription3pm_3333333Frankie
CIE22TESTBB20201555555555mandate_zzzzeur
## Bacs export fields

Bacs exports include the following fields.

FieldDescription`merchant`The unique identifier of the Stripe account we’re
exporting from (acct_XXXXX format)customer_idThe Stripe unique identifier of the
customer (cus_XXXXX format)`bacs_id` Stripe payment method object associated
with the customer’s direct debit mandate (in the format
pm_XXXXX)`mandate_reference`Unique identifier of the direct debit mandate on
Stripe`token``sort_code`Customer’s bank account sort code (6 digits in length
and might include leading zeros)`account_number`Customer’s bank account number
(8 digits in length and might include leading zeros)`effective_date`Date the
mandate was activated on Stripe`recipient` nameCustomer’s name on the bank
account`recipient_address_street`Customer’s street address associated with the
customer’s bank account`recipient_address_city`Customer’s city address
associated with the customer’s bank account`recipient_address_state`Customer’s
state address associated with the customer’s bank
account`recipient_address_zip`Customer’s postal code associated with their bank
account`recipient_address_country`Country associated with the bank account
### Example BACS data export

MERCHANTCUSTOMER_IDBACS_IDMANDATE_REFERENCETOKENSORT_CODEACCOUNT_NUMBEREFFECTIVE_DATERECIPIENT__NAMERECIPIENT__ADDRESS__STREETRECIPIENT__ADDRESS__CITYRECIPIENT__ADDRESS__STATERECIPIENT__ADDRESS__ZIPRECIPIENT__ADDRESS__COUNTRYacct_111111cus_1111pm_111xxx*USERxxx*USER1111111111111120220609T00:00:00ZJOHN
DOE25
AvenueLONDONLONDONEXXXXXGBacct_111111cus_2222pm_222yyy*USERyyy*USER1111111111111120220609T00:00:00ZStripe
McStripe26
StreetLONDONLONDONEXXXXXGBacct_111111cus_3333pm_333zzz*USERzzz*USER1111111111111120220609T00:00:00ZRory
C27 WayLONDONLONDONEXXXXXGB