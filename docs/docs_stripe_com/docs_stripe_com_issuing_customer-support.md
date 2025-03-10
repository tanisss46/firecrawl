# Customer support for Issuing and Treasury

## Resolve common Issuing and Treasury questions and issues.

To prepare you for assisting your customers, employees, or contractors, this
guide provides example issues and resolutions for both
[Issuing](https://docs.stripe.com/issuing/customer-support#issuing-issues-resolutions)
and
[Treasury](https://docs.stripe.com/issuing/customer-support#treasury-issues-resolutions).
You’re responsible for responding to these questions, and your level of
interaction with individual customers and cardholders might vary based on your
specific use case.

Stripe recommends equipping your team with the necessary information and tools.
This could involve augmenting your existing customer or technical support tools
using Stripe’s APIs or training your support team to manage questions using the
[Dashboard](https://docs.stripe.com/issuing/connect#using-dashboard-issuing).

- **Embedded Finance users:** If your business, using Stripe Connect, issues
cards to customers or enables customers to issue cards to their employees or
contractors, it’s your responsibility to oversee all interactions with these
customers (connected accounts).

- It’s crucial to provide customers with a way to reach out for support, whether
through a self-serve support page or a dedicated support team.
- Typically, restrict questions to your customers’ admin users, such as finance
or accounting teams.
- **B2B Payments users:** Businesses that issue cards for their own use,
employees, or contractors using a Direct Issuing integration must make sure that
a dedicated team manages the cardholder experience.

- You must let this team use the Stripe Dashboard or API to respond to employee
questions and concerns.

If your team is unable to resolve a question or issue using the existing
resources, [contact our support team](https://support.stripe.com/contact/login).
We’ll investigate the issue and provide you with an outcome that you can relay
back to your customer or employee.

## Issuing issues and resolutions

Refer to the following table when answering common Issuing issues:

TopicIssue typeResolutionOrdering and replacing cards Lost or stolen cards[Make
an API
call](https://docs.stripe.com/issuing/cards/replacements#replacements-for-lost-or-stolen-cards)
to immediately cancel and replace any physical or virtual cards reported as
compromised.If any authorizations were approved on a compromised card, you might
[dispute the transactions](https://docs.stripe.com/issuing/purchases/disputes)
as fraud.Expired or damaged physical cards[Make an API
call](https://docs.stripe.com/issuing/cards/replacements) to replace physical
cards that are expired or damaged.Delayed physical cardsDelays in card
manufacturing can occur if there is a pending [cardholder watchlist
screening](https://support.stripe.com/questions/issuing-watchlist-reviews).
Ensure that the cardholder is active and has fulfilled all necessary
requirements. If you have chosen the Standard shipping method, which does not
provide tracking, and the cardholder has not received the card within 10
business days, we recommend canceling and ordering a replacement (Stripe will
credit the creation and shipment cost back to you).Alternatively, if you have
selected Express or Priority shipping methods, which include tracking, you can
retrieve the tracking number from the Dashboard or [via the
API](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-tracking_number).Cardholder
experience Authorization declined[Make an API
call](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
to retrieve the authorization and review the request_history.reason.Cancel
pending authorizationInform the cardholder that it is not possible to cancel
pending authorizations. Only the acquiring merchant can void an
authorization.Advise customers that the authorization will automatically expire
7 days after creation (31 days if hotels, airlines, and car rental companies)
and the held funds will be released at that time.Missing refund[Make an API
call](https://docs.stripe.com/api/issuing/transactions/list#list_issuing_transactions-type)
to retrieve a list of transactions associated with the card where the type is
`refund`.Stripe attempts to link refunds to original transactions. If this does
not happen, you can review the amount and merchant data across all results to
identify a match.Disputing a transactionEnsure that the cardholder has exhausted
other means of resolving the issue, and obtain documentation of these attempts
to use as evidence when filing the dispute.Make an API call to
[create](https://docs.stripe.com/issuing/purchases/disputes?dashboard-or-api=api)
and
[submit](https://docs.stripe.com/issuing/purchases/disputes?dashboard-or-api=api#submission)
a dispute on behalf of the cardholder.Dispute loss reasonIf you are interested
in the ability to retrieve a dispute loss reason via API, apply for the beta by
[submitting your interest](https://docs.stripe.com/issuing/purchases/disputes)
while logged into your platform account. If you do not have access to the beta,
[contact support](https://support.stripe.com/) for more information that you can
relay to the cardholder regarding why a dispute was lost.Excessive PIN retriesIf
a card’s PIN is entered incorrectly three consecutive times, the PIN becomes
blocked and the card becomes inactive. In most countries, cardholders can
[unblock a card’s PIN at an
ATM](https://docs.stripe.com/issuing/cards/pin-management#changing-a-cards-pin-at-an-atm).Users
who are gated into the encrypted PIN management feature might also [change the
PIN](https://docs.stripe.com/issuing/cards/pin-management#changing-a-pin-with-the-cards-api)
for an issued card using the Card Update API. However, depending on the region
the card is used in, the new PIN might not be immediately usable.Once the pin is
unblocked, you will need to [make an API
call](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-status)
to update the card status to active. If you would like to request access to
encrypted PIN management, [contact
support](https://support.stripe.com/).Cardholder inactive[Make an API
call](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-requirements)
to retrieve the cardholder requirements array so that you can review the
disabled_reason and confirm whether any information is past_due.Cannot add card
to digital walletEnsure you have already [configured digital
wallets](https://docs.stripe.com/issuing/cards/digital-wallets). If configured,
request screenshots from the cardholder of the error message being surfaced.
[Contact support](https://support.stripe.com/) for in-depth troubleshooting
assistance once you have obtained documentation from the cardholder.Fraud
management Turning on 3DSConfirm your customer understands that 3DS can only be
turned on at the connected account level, meaning they will not be able to
toggle the feature on or off for individual cardholders.After the feature is
enabled, acquiring merchants might immediately start challenging
card-not-present authorization requests for any users that have linked a phone
number or email address to the card or cardholder.Once you’re ready, [contact
support](https://support.stripe.com/) to request 3DS be enabled and provide the
Stripe ID of the connected account.Update spending controlsMake an API call to
update the spending controls on the [cardholder
object](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)
or the [card
object](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)
itself.Enabling fraud challenges betaIf you are providing cardholders with
notice of suspected fraud and the ability to override this warning, [apply for
enrollment in the
beta](https://docs.stripe.com/issuing/controls/fraud-challenges) by submitting
your interest while logged into your platform account.Issuing balance Top-ups
from external bank account[Make an API
call](https://docs.stripe.com/issuing/connect/funding) to add funds to a
connected account’s Issuing balance. Set appropriate expectations with
cardholders for settlement timing based on your region. If top-ups are
reportedly delayed, you can [make an API
call](https://docs.stripe.com/api/topups/retrieve) to retrieve a list of top-ups
associated with the connected account.Balance transfer (to fund from Stripe
balance)You must sign up for the [Balance Transfer API private
beta](https://docs.stripe.com/issuing/connect/funding#request-early-access) to
transfer funds from a connected account’s Stripe balance into their Issuing
balance.Payouts[Make an API
call](https://docs.stripe.com/issuing/connect/funding#pay-out-an-issuing-balance)
to pay out funds from a connected account’s issuing balance to their external
bank account.Complaints Operational complaintsStripe expects you to acknowledge
all operational complaints within 5 business days and resolve them within 15
business days from complaint submission date.In addition, you must [report an
aggregated list of
complaints](https://docs.stripe.com/treasury/handling-complaints) to Stripe on a
monthly basis.Executive complaintsPromptly notify Stripe within 1 business day
of complaint submission date. Executive complaints include any threats of
litigation and complaints received from regulators and complaints that allege
Unfair or Deceptive Acts and Practices (UDAP), discrimination, consumer harm or
legal concerns.Upon receipt of an Executive Complaint, refrain from further
interaction with the customer until Stripe reviews the complaint. Stripe works
closely with you to resolve all Executive Complaints. In addition, you must
[report an aggregated list of
complaints](https://docs.stripe.com/treasury/handling-complaints) to Stripe on a
monthly basis.
## Treasury issues and resolutions

Refer to the following table when answering common Treasury inquiries:

Inbound topicIssue typeResolution pathFinancial account Missing capabilities on
connected
account[Retrieve](https://docs.stripe.com/treasury/account-management/financial-account-features#retrieving-features)
a list of Treasury features on a connected account and the corresponding status
using the endpoint for [Treasury financial account
features](https://docs.stripe.com/api/treasury/financial_account_features).You
also have the ability to
[request](https://docs.stripe.com/treasury/account-management/financial-account-features#requesting-features)
or
[remove](https://docs.stripe.com/treasury/account-management/financial-account-features#removing-features)
Treasury capabilities on behalf of connected accounts.Restricted capabilitiesIn
some instances, your customer might fall into a [restricted business
type](https://docs.stripe.com/treasury/requirements#restricted-business-types)
and require enhanced review before they can finalize Treasury onboarding. If you
believe one of your users fits these criteria, [contact
support](https://support.stripe.com/) for assistance.Account and routing
numbersUse the [financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts#retrieve-a-financialaccount-and-account-number)
endpoint to retrieve the account and routing numbers for a customer’s connected
account.Money movement Payments balance to Treasury balance transfersUse
[financial account and routing numbers to set the financial account as the
external bank
account](https://docs.stripe.com/treasury/moving-money/payouts#financial-accounts-as-external-accounts)
on a Stripe connected account. You can then [set up automatic
payouts](https://docs.stripe.com/treasury/moving-money/payouts#automatic-payouts)
to transfer a customer’s revenue to their financial account if desired.Canceling
a transferNot all Treasury payments and transfers can be canceled. To confirm
whether cancelation is an option, you can use the [outbound
transfer](https://docs.stripe.com/api/treasury/outbound_transfers/object#outbound_transfer_object-cancelable)
and [outbound payment
endpoints](https://docs.stripe.com/api/treasury/outbound_payments/object#outbound_payment_object-cancelable)
to retrieve the “cancelable” attribute.Unexpected funds and transfer
reversalsDepending on the network and source flow, you might be able to [create
a credit
reversal](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/credit-reversals).Incorrect
debits and reversalsYou have approximately 1 business day to [return ACH debits
using the
API](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/debit-reversals#return-deadlines)
after receipt. After this time, ACH debit funds might still be returnable but
funds return isn’t guaranteed. [Contact support](https://support.stripe.com/) to
request a return of funds if the reversal deadline has passed.Processing times
for transfers and paymentsFind a detailed overview of processing timelines and
cutoff times based on the type of transfer or payment
[here](https://docs.stripe.com/treasury/money-movement/timelines).

## Links

- [Dashboard](https://docs.stripe.com/issuing/connect#using-dashboard-issuing)
- [contact our support team](https://support.stripe.com/contact/login)
- [Make an API
call](https://docs.stripe.com/issuing/cards/replacements#replacements-for-lost-or-stolen-cards)
- [dispute the transactions](https://docs.stripe.com/issuing/purchases/disputes)
- [Make an API call](https://docs.stripe.com/issuing/cards/replacements)
- [cardholder watchlist
screening](https://support.stripe.com/questions/issuing-watchlist-reviews)
- [via the
API](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-tracking_number)
- [Make an API
call](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
- [Make an API
call](https://docs.stripe.com/api/issuing/transactions/list#list_issuing_transactions-type)
-
[create](https://docs.stripe.com/issuing/purchases/disputes?dashboard-or-api=api)
-
[submit](https://docs.stripe.com/issuing/purchases/disputes?dashboard-or-api=api#submission)
- [contact support](https://support.stripe.com/)
- [unblock a card’s PIN at an
ATM](https://docs.stripe.com/issuing/cards/pin-management#changing-a-cards-pin-at-an-atm)
- [change the
PIN](https://docs.stripe.com/issuing/cards/pin-management#changing-a-pin-with-the-cards-api)
- [make an API
call](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-status)
- [Make an API
call](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-requirements)
- [configured digital
wallets](https://docs.stripe.com/issuing/cards/digital-wallets)
- [cardholder
object](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)
- [apply for enrollment in the
beta](https://docs.stripe.com/issuing/controls/fraud-challenges)
- [Make an API call](https://docs.stripe.com/issuing/connect/funding)
- [make an API call](https://docs.stripe.com/api/topups/retrieve)
- [Balance Transfer API private
beta](https://docs.stripe.com/issuing/connect/funding#request-early-access)
- [Make an API
call](https://docs.stripe.com/issuing/connect/funding#pay-out-an-issuing-balance)
- [report an aggregated list of
complaints](https://docs.stripe.com/treasury/handling-complaints)
-
[Retrieve](https://docs.stripe.com/treasury/account-management/financial-account-features#retrieving-features)
- [Treasury financial account
features](https://docs.stripe.com/api/treasury/financial_account_features)
-
[request](https://docs.stripe.com/treasury/account-management/financial-account-features#requesting-features)
-
[remove](https://docs.stripe.com/treasury/account-management/financial-account-features#removing-features)
- [restricted business
type](https://docs.stripe.com/treasury/requirements#restricted-business-types)
- [financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts#retrieve-a-financialaccount-and-account-number)
- [financial account and routing numbers to set the financial account as the
external bank
account](https://docs.stripe.com/treasury/moving-money/payouts#financial-accounts-as-external-accounts)
- [set up automatic
payouts](https://docs.stripe.com/treasury/moving-money/payouts#automatic-payouts)
- [outbound
transfer](https://docs.stripe.com/api/treasury/outbound_transfers/object#outbound_transfer_object-cancelable)
- [outbound payment
endpoints](https://docs.stripe.com/api/treasury/outbound_payments/object#outbound_payment_object-cancelable)
- [create a credit
reversal](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/credit-reversals)
- [return ACH debits using the
API](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/debit-reversals#return-deadlines)
- [here](https://docs.stripe.com/treasury/money-movement/timelines)