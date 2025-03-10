# Supported card brands

## Learn about the card brands supported by Stripe Terminal.

When you integrate Stripe Terminal, you can begin accepting a diversity of card
brands. Your reader will automatically configure itself to accept the brands
relevant for its region.

## In-person brand capabilities

The following table describes some of the different features and restrictions of
each card brand **in-person**, including limitations on countries where Stripe
users can accept the brand (Stripe Account Country), support for different
reader types, and card presentment modes. Terminal is available in the following
countries.

AustraliaAustriaBelgiumCanadaCzech
RepublicDenmarkFinlandFranceGermanyIrelandItalyLuxembourgMalaysiaNetherlandsNew
ZealandNorwayPortugalSingaporeSpainSwedenSwitzerlandUnited KingdomUnited States
### Available in Preview

Poland
When processing an in-person transaction, Terminal requires that you use local
currency. Terminal supports NFC-based mobile wallets (Apple Pay, Google Pay, and
Samsung Pay).

Card brandTerminal location and Stripe account countryReader typesCard
presentment modeVisaAll countries where Terminal is supportedAllAllMastercardAll
countries where Terminal is supportedAllAllAmerican ExpressAll countries where
Terminal is supported, except MalaysiaAllAllDiscover & DinersUnited States,
Canada, and EMEAUS: Verifone P400, Stripe M2, Chipper 2X BT, and Tap to Pay on
iPhoneUS, CA, EMEA: WisePOS E and Stripe Reader S700CA, EMEA: WisePad 3AllChina
Union Pay 1United States, CanadaStripe M2, WisePad 3, WisePOS E3, Stripe Reader
S700AlleftposAustraliaWisePad 3, WisePOS E, Stripe Reader S700, and Tap to Pay
on iPhoneAllgirocardGermanyWisePad
3All[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments)CanadaWisePad
3, WisePOS E, Verifone P400, Stripe Reader S700, and Tap to Pay on iPhoneAllJCB
2United States, Canada, Australia, and New ZealandStripe M2, WisePad 3, WisePOS
E3, Stripe Reader S700AllMaestroAll non-US countries where Terminal is
supported. As of July 2023, new Maestro cards aren’t issued. Expired cards will
be replaced with Debit Mastercard.WisePad 3, WisePOS E, Verifone P400, Stripe
Reader S700, Tap to Pay on iPhone, and Tap to Pay on AndroidAll
1China Union Pay is supported over the Discover network in the United States and
Canada.

2JCB is supported over the Discover network in the United States and the
American Express network in Canada, Australia and New Zealand.

3The WisePOS E only supports China Union Pay and JCB for EMV chip transactions
where the card is inserted into the reader. Contactless is not supported.

## Links

-
[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments)