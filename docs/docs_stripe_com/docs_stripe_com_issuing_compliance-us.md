# Issuing product marketing, design, and compliance guidelines

## Learn how to keep your Issuing program and marketing campaigns compliant.

#### Legal Disclaimer

Don’t consider any of the information in this guide as legal advice. If you use
Stripe Treasury and Stripe Issuing, consult your own legal counsel for advice
about product branding and using Stripe products to offer financial services.

This information applies to both Treasury and Issuing integrations. To offer and
promote Treasury and Issuing products to your customers and connected accounts,
your marketing and user interfaces must adhere to the guidelines that we outline
here. These guidelines help you navigate the financial regulations that apply to
Stripe products. We’ve organized them into the following sections:

- [Account
management](https://docs.stripe.com/issuing/compliance-us#account-management)
- [Required agreements and disclosures for
Issuing](https://docs.stripe.com/issuing/compliance-us#issuing-terms)
- [Required agreements and disclosures for
Treasury](https://docs.stripe.com/issuing/compliance-us#treasury-terms)
- [Required agreements and disclosures for fees, credits, and rewards
programs](https://docs.stripe.com/issuing/compliance-us#fees-credits-rewards-terms)
- [Customer communications and
documents](https://docs.stripe.com/issuing/compliance-us#customer-communications-and-documents)
- [Going live and
marketing](https://docs.stripe.com/issuing/compliance-us#going-live)
- [Recordkeeping](https://docs.stripe.com/issuing/compliance-us#recordkeeping)

The following table outlines the steps you must complete before onboarding your
first connected accounts. If you need help, contact the Stripe Compliance team
at [platform-compliance@stripe.com](mailto:platform-compliance@stripe.com).

If you make changes to any items in the table at a later date, you must submit a
request to the Stripe Compliance team using the [Change Request
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835).

TopicChecklistProduct applicabilityApplication flowYour application flow:-
Includes bank disclosures
- Includes required agreements
- Required KYC fields
- Approved by Stripe Compliance
Treasury and IssuingFees and creditsYou’ve [submitted your planned fees and
credits to
Stripe](https://docs.stripe.com/treasury/compliance#fees-credits-rewards-terms)Treasury
and IssuingMarketing and user interfacesYour marketing materials, including your
website landing pages, dashboards, and support pages:- Are approved by Stripe
Compliance (or align with messaging guidelines)
- Include bank disclosures
Treasury and IssuingCustomer service channelsYour customers can access your
customer service channels and they can:- Submit complaints
- Submit disputes
Treasury and IssuingAccount statements (optional)If you choose to send account
statements, they must:- Be approved by Stripe Compliance
- Include Bank disclosures and relevant contact information
TreasuryReceiptsYou have a mechanism to send your customers Stripe-generated
money transmission receiptsTreasury and IssuingRegulated customer noticesYou
send regulated customer notices to applicants and accountholders, and they’re
either:- Sent by Stripe on your behalf
- Sent by your platform with templates approved by Stripe Compliance
Issuing Spend Card and Charge CardRecordkeepingYou have a mechanism to retain
copies of:- Customer consent to open accounts
- Marketing materials and user interfaces
- Customer communications, such as support emails
- Account statements, if applicable
Treasury and Issuing
## Account management

Before you launch Treasury or Issuing, you must implement the proper internal
compliance controls. You also need to build the processes described in this
section into your various workflows, customer service, and product channels.

### Complaints program guidance

Complaints are any expression of dissatisfaction with a product, service,
policy, or employee related to Treasury or Issuing, except those expressions
made by employees of your company. Properly handling complaints is mandatory
when offering financial services products. See the [Handling
complaints](https://docs.stripe.com/treasury/handling-complaints) guide for
detailed complaint management requirements.

### Disputes and charge errors

As part of providing customer support, you might be notified of suspected
disputed charges, charge errors, or both. The two most common types of disputes
or errors are:

- You or your customer believe a charge is unauthorized
- You or your customer see an error on an account statement

If these errors occur, submit the dispute through the Stripe Dashboard. Select
the relevant transactions and choose **Dispute**. Be prepared to provide Stripe
with specific information to investigate the dispute, such as:

- Details about the authorized user
- Details about the disputed charge amount
- The transaction date
- An explanation of why the disputed charge is an error or unauthorized

You must report any disputed charge or error immediately upon notification of
it. Failure to do so might impact your financial liability. To avoid a sustained
reduction to your available balance, you can pay the disputed charge while we
determine the validity of the dispute. If Stripe deems the dispute valid, we
credit the disputed charge amount back to the appropriate account.

### Application flow

Your platform must provide for three main compliance requirement workflows:

- Collection of required KYC information
- Presentation of the required bank disclosure
- Ensuring that your applicant reads and accepts the required legal agreements

### Customer-facing dashboards

If your platform plans to allow connected accounts to store balances with
multiple Treasury bank partners, display balances separately within any
dashboard user interface or servicing communications that disclose balances.
Provide a specific disclosure for each individual balance, indicating which bank
holds the balance. This ensures that the connected account is aware of their
potential insurance limits at each bank.

## Required agreements and disclosures for Issuing

If you’re a platform and you’re not using [Stripe-hosted
onboarding](https://docs.stripe.com/connect/hosted-onboarding), you must:

- Present the following program-specific agreements and disclosures for your
connected accounts to accept when they open their account.
- Provide connected accounts with ongoing access to these agreements.
- Present each agreement separately. You can’t combine them into one agreement
for your cardholders to accept.

*Connected Account Agreements and Disclosures.*

You must provide the following agreements to your connected accounts before they
can start using the Issuing Spend Card Program:

- [Stripe Connected Account Agreement](https://stripe.com/legal/connect-account)
- [Stripe Issuing Accountholder
Terms](https://stripe.com/legal/issuing-accountholder)
- **Issuing Bank Terms**- *Celtic Bank Users only:* [Issuing Bank Terms - Spend
Card (Celtic Bank)](https://stripe.com/legal/celtic-spend-card)
- *Cross River Bank Users only:* [Issuing Bank Terms - Spend Card (Cross River
Bank)](https://stripe.com/legal/issuing/crb-spend-card)
- **Apple Pay Terms** (if enabled for your program)- [Apple Pay Accountholder
Terms](https://stripe.com/issuing/celtic/apple-payment-platform-program-manager-customer-terms-and-conditions/legal#exhibit-c-pass-through-provisions)

In addition to the above agreements, you must provide the following disclosures
to your connected accounts before they can start using the Issuing Spend Card
Program:

- **Electronic Signature Consent**: You must include text near the “Issuing Bank
Terms” link that states: “By clicking “submit application,” you agree to the
Issuing Bank Terms, Stripe Connected Account Agreement, and Stripe Issuing
Accountholder Terms, and you consent to electronic signatures as set forth in
the Issuing Bank Terms.”
- **Commercial Financing Disclosure**: For Connected Accounts with a business
address in CA, NY, or UT, you must present one of the following disclosures:-
For platforms that don’t charge fees:- *Celtic Bank Users only:* [Commercial
Financing Disclosure (Celtic Bank) (no
fee)](https://stripe.com/legal/issuing-offer-document)
- *Cross River Bank Users only:* [Commercial Financing Disclosure (Cross River
Bank) (no fee)](https://stripe.com/legal/crb-issuing-offer-document)
- For platforms that charge a $0.10 fee when creating cards for users:- *Celtic
Bank Users only:* [Commercial Financing Disclosure (Celtic Bank) (fee
included)](https://stripe.com/legal/issuing-offer-document-fees)
- *Cross River Bank Users only:* [Commercial Financing Disclosure (Cross River
Bank) (fee included)](https://stripe.com/legal/crb-issuing-offer-document-fees)
- For platforms that charge fees other than a $0.10 fee when creating cards for
users:- If you charge fees beyond Stripe’s fee of 0.10 USD, you might be
required to create your own commercial financing disclosure to present to your
connected accounts for creating virtual cards. You must report custom fees
through Stripe’s [Change Request
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835), and
you must submit custom commercial financing disclosures to
[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com). Both
the custom fee and custom disclosure are subject to Stripe’s review and
approval. To assess the applicability of commercial financing disclosures to
your program, contact
[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com).

*Authorized User Agreements and Disclosures.*

If you or your connected accounts create an `individual` type
[Cardholder](https://docs.stripe.com/api/issuing/cardholders/object), also known
as an “authorized user,” you must present to cardholders—typically during the
card activation process—the following agreements:

- [Stripe E-Sign Disclosure](https://stripe.com/issuing/e-sign-disclosure/legal)
- Authorized User Terms- *Celtic Bank Users only:* [Authorized User Terms
(Celtic Bank)](https://stripe.com/legal/issuing/celtic-authorized-user-terms)
- *Cross River Bank Users only:* [Authorized User Terms (Cross River
Bank)](https://stripe.com/legal/issuing/crb-authorized-user-terms)

### Charge card users

*Connected Account Agreements and Disclosures.*

You must provide the following agreements to your connected accounts before they
can start using the Issuing Charge Card Program:

- [Stripe Connected Account Agreement](https://stripe.com/legal/connect-account)
- [Stripe Issuing Accountholder
Terms](https://stripe.com/legal/issuing-accountholder) or Custom Platform
Accountholder Terms
- **Issuing Bank Terms**- *Celtic Bank Users only:* [Issuing Bank Terms - Charge
Card (Celtic Bank)](https://stripe.com/legal/celtic-charge-card)
- *Cross River Bank Users only:* [Issuing Bank Terms - Charge Card (Cross River
Bank)](https://stripe.com/legal/issuing/crb-charge-card)
- **Apple Pay Terms** (if enabled for your program)- [Apple Pay Accountholder
Terms](https://stripe.com/issuing/celtic/apple-payment-platform-program-manager-customer-terms-and-conditions/legal#exhibit-c-pass-through-provisions)
- **Card Program Terms**: These are your bespoke program terms that supplement
the Issuing Bank Terms. At a minimum, consider including the following items in
your terms. Consult your legal counsel about which items to define within your
own Card Program Terms.- Repayment methods, including automatic withdrawal
consents
- Billing cycles, including due dates
- Fees
- Rewards
- Credit limits
- Account closure requirements

In addition to the above agreements, you must provide the following disclosures
to your connected accounts before they can start using the Issuing Spend Card
Program:

- **Electronic Signature Consent**: You must include text near the **Issuing
Bank Terms** link stating that signing the Issuing Bank Terms signifies consent
to electronic signatures and communications. For example, your message might
read: “By clicking the submit application button, you agree to the Issuing Bank
Terms, Stripe Connected Account Agreement, and Stripe Issuing Accountholder
Terms; and you consent to electronic signatures as set forth in the Issuing Bank
Terms.”
- **Commercial Financing Disclosure**: For connected accounts with a business
address in CA, NY, or UT, you must present your own custom commercial financing
disclosure. You must report custom fees through Stripe’s [Change Request
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835), and
you must submit custom commercial financing disclosures to
[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com). Both
the custom fee and custom disclosure are subject to Stripe’s review and
approval. Contact
[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com) to
assess the commercial financing disclosure requirements of your program.

**Authorized User Agreements and Disclosures.**

If you or your connected accounts create an `individual` type
[Cardholder](https://docs.stripe.com/api/issuing/cardholders/object), also known
as an “authorized user,” you must present to cardholders—typically during the
card activation process—the following agreements:

- [Stripe E-Sign Disclosure](https://stripe.com/issuing/e-sign-disclosure/legal)
- Authorized User Terms- *Celtic Bank Users only:* [Authorized User Terms
(Celtic Bank)](https://stripe.com/legal/issuing/celtic-authorized-user-terms)
- *Cross River Bank Users only:* [Authorized User Terms (Cross River
Bank)](https://stripe.com/legal/issuing/crb-authorized-user-terms)

### Commercial prepaid debit users

You must provide the following agreements to your connected accounts before they
can start using your Issuing Commercial Prepaid Debit Card Program:

- [Stripe Connected Account Agreement](https://stripe.com/legal/connect-account)
- [Stripe Issuing Accountholder
Terms](https://stripe.com/legal/issuing-accountholder)
- [Issuing Bank Terms (Sutton
Bank)](https://stripe.com/legal/issuing/commercial-prepaid-sutton-terms)

**Authorized User Agreements and Disclosures.**

If you or your connected accounts create an `individual` type
[Cardholder](https://docs.stripe.com/api/issuing/cardholders/object), also known
as an “authorized user,” you must present to cardholders—typically during the
card activation process—the following agreements:

- [Stripe E-Sign Disclosure](https://stripe.com/issuing/e-sign-disclosure/legal)
- [Sutton Bank Authorized User
Terms](https://stripe.com/legal/issuing/sutton-authorized-user-terms)

## Required agreements and disclosures for Treasury

You must provide the following terms of service to your connected accounts and
record their agreement before they can start using your Treasury Program:

- [Stripe Services Agreement](https://stripe.com/legal/ssa)
- [Stripe Treasury Terms - Connected
Accounts](https://stripe.com/legal/ssa#services-terms)

## Required agreements and disclosures for fees, credits, and rewards programs

In addition to the previous agreements, your terms of service and fee schedule
must clearly outline the fees and terms that you implement as part of your
Treasury or Issuing program.

You must report to Stripe the details of any fees, credits, and rewards programs
that you plan to offer. That helps make sure your user interfaces and marketing
materials are compliant with financial regulations regarding fees or offer
credits, especially in the form of rewards programs. Use the [Change Request
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835).

## Customer communications and documents

To comply with applicable laws and regulations, you must send certain
communications to both your applicants and accountholders upon certain trigger
events.

To learn about customer communication requirements when using Issuing and
Treasury together, see [Issuing regulated customer
notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices).

### Statements

Providing statements, while optional, is a best practice that allows your
Treasury or Issuing customers to periodically check their transaction history.
If you send statements, make sure they contain the following information:

- [Company] name and address.
- Your company’s customer support contact number and website
- Customer account number
- Customer name and address
- Required disclosures
- Transaction history (including opening and closing balances for the statement
period)
- Fees and credits.
- Information about how you resolve errors and complaints

### Receipts

One of the most important ongoing obligations you have in overseeing your
Treasury or Issuing program is providing your customers with money transmissions
receipts. Every regulated transaction your customers initiate generates a
compliant money transmission receipt URL that you must share with your customer.
You can provide these URL receipts in a few different ways, such as emailing
them or making them available in your customer’s Dashboard. See the [Regulatory
receipts
guide](https://docs.stripe.com/treasury/moving-money/regulatory-receipts) for
more information on how to access hosted receipts. If you plan to charge your
connected account owners any fees, whether they’re transactional or monthly
recurring, include a description of the fee on the receipt so that they can
reconcile it to corresponding transactions or monthly statements.

## Going live and marketing

The following information pertains to marketing and releasing your Treasury or
Issuing programs to the public.

### General requirements for marketing your account offerings

Any message or communication you provide to the public for financial products or
services they don’t currently use must be truthful and fair, and in the interest
of your potential customers.

### UDAP and correct messaging

Federal regulation prohibits unfair and deceptive acts or practices (UDAP). To
avoid UDAP violations, you must think of the end user first when developing and
deploying any marketing materials.

Make sure that marketing materials use clear messaging that fully explains
product features, costs, benefits, and limitations. Don’t leave out key terms or
fees, and don’t advertise product uses or features that aren’t true.

DoDon’tOnly use statements about products that are true, accurate, and aligned
with how users engage with the products.Don’t leave out key information from
marketing content. If the information is likely to affect whether someone uses
the product, then it’s “key."If you make claims that require additional data to
support them, or if an end user needs to know more details to know how a certain
claim is true, you must:- Provide documented evidence
- Disclose that information
Make exaggerated claims that are hard to prove. Don’t make absolute statements
that are disproved by a single exception. For example, “number 1," “every,"
“only," “all," “never," “always."Clearly explain all qualifying limitations and
requirements needed by end users to get the product or features that you’ve
advertised.Don’t advertise features or programs that only a few applicants
actually qualify for.All disclosures must meet a “clear and conspicuous”
standard:- Font size must be large enough to read.
- Font color must visibly contrast with the background.
- Dynamic or video ads must have the disclosure on screen long enough to be
read.
Don’t make disclosures hard to read.Disclosures used to explain or modify a
claim must be tied to the claim they’re explaining.- Use a hyperlink directly
linking to the disclosure (or include the disclosure next to the claim in the
copy itself)
- Use reference text or symbols (an asterisk, for example) directly after the
claim and before the disclosure language.
Don’t bury disclosures in other non-key disclosures or footnotes.Disclose all
account fees, costs, benefits, and terms as part of onboarding before your end
users take out a product.Don’t advertise products as “free” if you’re charging
fees.Make sure all images used are properly licensed and that you can document
this fact.Don’t use images, formatting, or copy that implies products are
endorsed by, or affiliated with, government entities or celebrities.
### Messaging guidelines

Use the following suggested messaging guidelines to convey key aspects of
Issuing, Treasury, or both programs. Stripe or our banking partners have
validated (proven as true) this content, so you can confidently use this
messaging in user-facing materials.

-
[Issuing](https://docs.stripe.com/issuing/compliance-us#issuing-messaging-guidelines)
-
[Treasury](https://docs.stripe.com/issuing/compliance-us#treasury-messaging-guidelines)

The following tables include validated content you can provide in your marketing
campaigns. You can make non-substantive changes (for example, changing the
design or infusing your brand’s voice) to the suggested messaging as long as the
key information remains the same. Any substantive deviations from these
guidelines require you to submit marketing materials and get approval from
Stripe and our bank partners. Approvals might take up to 10 business days to
process.

You’re responsible for training employees on these requirements if they engage
in marketing or sales activities for your Treasury or Issuing program.

#### Issuing messaging guidelines

The following table provides guidelines for you to follow when developing
messaging around your Issuing program.

Topic categoryDoDon’t
Logo and name usage

Your card program name and your brand name must have equal status, as with plain
text: Widget balance® + Stripe. When referencing registered brand products, you
must adhere to their separate brand guidelines. You only need to use the ®, ™,
SM, mark once per asset.

Don’t maintain unequal status between the card program name and your brand name:

**Widget balance®** + Stripe

Comparison value propositionsUse language promoting the benefits of the card:-
Better than cash
- Safer than carrying cash
- Manage your money hassle free
- Spend only what you load
- Spend only what you have on your card
Don’t make disparaging remarks about other financial products or institutions:
this includes debit, credit, bank accounts, banks, or other financial products
used or issued by financial institutions. Don’t allude to prepaid card programs
as superior to other card products with terms like:- Better than credit
- Better than a bank account
- No interest
- No security deposit
- No debt
Currency and using the fundsUse phrases like:- Access your contractor earnings
- All [card program] cards are USD denominated
- [Card program] cards can be used anywhere that accepts Visa cards
Don’t use phrases like:- Access your wages
- Get funds in any format you want
- Can spend money across the world
What you can use the card for and limitationsUse phrases like:- Use [card
program] for business needs
- Get [card program] for your commercial needs
- [Card program] can only be used for commercial purposes, and can’t be used for
personal, family, or household purposes
- Spend only what you load
- Spend only what you have on your card
Don’t use phrases like:- Use [card program] for anything you want
- Spend funds to buy the things you love
- Personal cards
- Use these cards like a payday loan, title loan, or pawn shop loan
Where to spend fundsUse phrases like:- [Card program] can only be used for
commercial purposes, and can’t be used for personal, family, or household
purposes
- Spend funds easily on your business
Don’t use phrases like:- Can be used just like a personal account
- Get consumer cards
- Spend funds to buy the things you love

#### Issuing messaging specifics per product

The following table provides guidelines for you to follow when developing
messaging for specific cards in your Issuing program.

CardDoDon’tSpend card onlyUse phrases like:- …is a commercial credit program
- A business credit card
Don’t use phrases like:- Debit card
- Prepaid card
- Better than a debit card
Payout account only (Treasury account connected)Money management accountDon’t
use phrases like:- Bank account
- Deposit account
- Checking account
- Savings account
- Similar terms to the previous ones that connote a traditional bank account
product

#### Treasury messaging guidelines

Don’t use words like “bank account,” “deposit account," “checking account,”
“savings account,” or similar terms that imply a traditional bank account
product because Stripe isn’t a bank. Pre-approved terms include the following:

- Business account
- Cash management account
- Financial account
- Money transfer account

See [Marketing Treasury-based
services](https://docs.stripe.com/treasury/marketing-treasury) for a full list
of terms you can and can’t use to describe your accounts and to learn how to
talk about FDIC pass-through insurance eligibility. Inaccurately referring to
Treasury accounts as “bank accounts” could result in regulatory action,
including fines.

CategoryDoDon’t
Logo and name usage

When referencing registered/® brand products, you must adhere to their separate
brand guidelines. You only need to reference the ®, ™, SM mark once per asset.

Don’t apply unequal status between the card program name and your brand name:

**Widget balance®** + Stripe

Description of account value propositionsUse the following terms:- Business
account
- Cash management account
- Financial account
- Money transfer account
Don’t use the following terms:- “Bank account”
- “Deposit account”
- “Checking account”
- “Savings account”
- Similar terms to the previous ones that imply a traditional bank account
product, because Stripe isn’t a bank
FDIC insuranceUse the following terms that incorporate the term “eligible”:-
“Eligible for FDIC insurance”
- “FDIC insurance-eligible accounts”
- “Eligible for FDIC pass-through insurance”
- “Eligible for FDIC insurance up to the standard maximum deposit insurance per
depositor in the same capacity"
- “Eligible for FDIC insurance up to $250K”
Don’t use the following terms:- “FDIC insured”
- “FDIC insured accounts”
- “FDIC pass-through insurance guaranteed”

### CAN-SPAM

The CAN-SPAM Act regulates marketing activity conducted by email. An email is
deemed a commercial message, subject to the CAN-SPAM act, if the primary purpose
of the email is to convey a commercial advertisement, or to promote a product or
service. A transactional email is an email sent to a customer that has a primary
purpose relating to a particular transaction or relationship between you and the
customer, such as a payment reminder. The CAN-SPAM Act imposes more rigorous
requirements on commercial email messages, as compared with transactional
messages. Transactional messages aren’t subject to most of the requirements of
the CAN-SPAM Act. If a message contains both transactional content and
commercial content, the CAN-SPAM Act commercial email requirements might apply,
if the primary purpose of the message can be considered commercial.

To facilitate compliance with the CAN-SPAM Act, any employee or staff using or
having access to your email systems and resources for marketing must adhere to
the following guidelines:

- Misleading header information. Any email message, whether commercial or
transactional, must not contain:- False or misleading header information.
- A “from” line that doesn’t accurately identify any person (individual or
business) who initiated the message.
- Inaccurate or misleading identification of a protected computer used to
initiate the message for purposes of disguising its origin.
- Deceptive subject headings. Any commercial email message must not contain
deceptive subject headings. For example, a deceptive subject heading is one that
likely misleads the recipient about a material fact regarding the message’s
contents or subject matter.
- Opt-out mechanism. You must provide your customers with the ability to opt-out
of receiving future commercial messages, and you must honor customer requests to
opt-out within 10 days. You can’t require a user to pay a fee or provide
information other than an email address to opt-out.
- Advertisement identification. Any commercial email message must contain clear
and conspicuous identification that the message is an advertisement or
solicitation.
- Physical address disclosure. Any commercial email message must disclose a
valid physical address of the sender.

Failure to comply with CAN-SPAM could result in large fines for each violation.

### Testimonials

If you’re using testimonials or endorsements in advertising Stripe products to
your users, consider the following:

- The person giving a testimonial must be a real person and a true, bona fide
user of the service or product they’re talking about.
- You must obtain and keep their permission in writing to use their quote. You
must update that permission every 24 months.
- Product benefits, costs, or features in any quotes must be verifiable and true
to what most users can expect to get.
- If you paid someone for their quote, or gave them anything of value, you must
put a disclaimer near the quote stating this fact. This includes paid actors, if
their scripting makes it sound like they’re giving a testimonial.

### Prohibited advertising

You can’t advertise Issuing or Treasury in print, radio, TV, on the internet, or
in any other format in a manner that promotes any unlawful activity or that
causes reputation concerns for Stripe or our bank partners.

### Prohibition on international marketing

Treasury isn’t available to users or merchants located outside the US, so limit
all marketing for Treasury to US domestic audiences.

For Issuing, although you can ship cards to international addresses for
US-domiciled cardholders, you must not market the Issuing program
internationally or to persons outside of the United States. That includes
advertising or promoting Issuing through marketing channels such as social
media, email, and paid search results. As with all other aspects of the Issuing
program, your marketing activities must comply with card network rules.

### Required marketing disclosures

Your users must understand the role that Stripe’s bank partners play in offering
and operating certain financial products—and in many cases, that they’re
entering into a contractual relationship with these banks. Your users must also
understand the material costs and fees associated with their use of each
financial product. We require you to build the following disclosures into your
marketing materials:

#### Disclosures when marketing Issuing

If you offer Issuing products, you must include the following information in an
easily discoverable and accessible area on all marketing materials, account
opening flows, and product interfaces:

- The name for your card program (for example, Rocket Rides Corporate Card).
- The relevant statement from the following table identifying the issuing bank.
It can be in the footers section of your materials; however, the font must be a
legible size and a contrasting color to the background.
Statement for Celtic Bank usersStatement for Sutton Bank usersStatement for
Cross River Bank users[Card Program Name] Visa® Commercial cards are powered by
Stripe and issued by Celtic Bank.[Card Program Name] Visa® Prepaid Cards are
issued by Sutton Bank®, Member FDIC, pursuant to a license from Visa USA
Inc.[Card Program Name] Charge Cards are issued by Cross River Bank, Member
FDIC.
#### Disclosures when marketing Treasury

If you offer Treasury products, you must include the following information in an
easily discoverable and accessible area on all marketing materials, account
opening flows, and product interfaces:

- A statement that you’re neither a bank nor a money transmitter.
- Statement of partnership with Stripe.
- “Stripe Payments Company” must be hyperlinked and point to
`https://stripe.com`.
Statement for Evolve bank usersStatement for Goldman Sachs bank usersStatement
for Fifth Third bank users[Company Name] partners with [Stripe Payments
Company](https://stripe.com/) for money transmission services and account
services with funds held at Evolve Bank & Trust, Member FDIC.[Company Name]
partners with [Stripe Payments Company](https://stripe.com/) for money
transmission services and account services with funds held at Goldman Sachs Bank
USA, Member FDIC.[Company Name] partners with [Stripe Payments
Company](https://stripe.com/) for money transmission services and account
services with funds held at Fifth Third Bank N.A., Member FDIC.- If you’re
integrating with multiple Treasury bank partners, you must reference them all
within your disclosure.

#### Disclosures when marketing both Treasury and Issuing

If you offer both Treasury and Issuing products, you must include the following
information in an easily discoverable and accessible area on all marketing
materials, account opening flows, and product interfaces:

- A name for your card program (for example, Rocket Rides Corporate Card).
- A combined statement identifying both the issuing and treasury banks and
saying that you’re neither a bank nor a money transmitter.
Example combined statement[Company Name] partners with [Stripe Payments
Company](https://stripe.com/) for money transmission services and account
services with funds held at [Treasury bank], Member FDIC. [Card Program Name]
Visa® Prepaid Cards are issued by [Issuing bank], Member FDIC.
### Materials submission

Submit copies of your marketing materials and user interface mockups through our
[Change Request
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835) for
review before you launch. If you make any changes to marketing materials,
application flows, or user communications, Stripe’s compliance team must perform
a review before going live. Our team of compliance specialists reviews them with
our bank partners and responds within 10 business days.

When submitting your materials:

- Provide full screenshots of product pages that include headings and footers.
- The preferable format for materials is PDF, however any format where all text
is legible is acceptable.
- Describe the types of marketing material you’re submitting (for example, web
banners, emails, search engine marketing, and whether it’s only text or images
and text).
- You can send up to 5 attachments per submission.

Send any additional questions to our team at
[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com).

We might request that you change your marketing materials to comply with
regulatory requirements. If we request a change, it’s your responsibility to
update the materials and provide evidence of the change to Stripe. Failure to
update materials at our request might result in Stripe disabling your Treasury
or Issuing capabilities.

## Recordkeeping

You must demonstrate your adherence to the requirements listed in this guide.
Keep thorough records of all marketing materials, customer data, account
information, and other disclosures you make to customers for at least 5 years.
The following is a list of all records to keep, with examples of record types.

Record typeExample form of recordsProduct user experienceScreenshots of all
deployed versions of the product user experience and their deployment dates.
Include application flow, customer dashboard, support pages, and so
on.MarketingInventory of all marketing copy deployed, email distribution lists
used, and email solicitation opt-out lists, including timestamps of user
opt-outs.Customer communications and complaintsEmail interactions and
documentation developed in the course of resolving complaints.ReceiptsReceipts
provided by Stripe and evidence that they’re uploaded to the customer’s
Dashboard.Customer statementsHistorical statements generated and made available
to customers for download.
## See also

- [Customer
communications](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices)

## Links

- [Change Request
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835)
- [submitted your planned fees and credits to
Stripe](https://docs.stripe.com/treasury/compliance#fees-credits-rewards-terms)
- [Handling complaints](https://docs.stripe.com/treasury/handling-complaints)
- [Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding)
- [Stripe Connected Account Agreement](https://stripe.com/legal/connect-account)
- [Stripe Issuing Accountholder
Terms](https://stripe.com/legal/issuing-accountholder)
- [Issuing Bank Terms - Spend Card (Celtic
Bank)](https://stripe.com/legal/celtic-spend-card)
- [Issuing Bank Terms - Spend Card (Cross River
Bank)](https://stripe.com/legal/issuing/crb-spend-card)
- [Apple Pay Accountholder
Terms](https://stripe.com/issuing/celtic/apple-payment-platform-program-manager-customer-terms-and-conditions/legal#exhibit-c-pass-through-provisions)
- [Commercial Financing Disclosure (Celtic Bank) (no
fee)](https://stripe.com/legal/issuing-offer-document)
- [Commercial Financing Disclosure (Cross River Bank) (no
fee)](https://stripe.com/legal/crb-issuing-offer-document)
- [Commercial Financing Disclosure (Celtic Bank) (fee
included)](https://stripe.com/legal/issuing-offer-document-fees)
- [Commercial Financing Disclosure (Cross River Bank) (fee
included)](https://stripe.com/legal/crb-issuing-offer-document-fees)
- [Cardholder](https://docs.stripe.com/api/issuing/cardholders/object)
- [Stripe E-Sign Disclosure](https://stripe.com/issuing/e-sign-disclosure/legal)
- [Authorized User Terms (Celtic
Bank)](https://stripe.com/legal/issuing/celtic-authorized-user-terms)
- [Authorized User Terms (Cross River
Bank)](https://stripe.com/legal/issuing/crb-authorized-user-terms)
- [Issuing Bank Terms - Charge Card (Celtic
Bank)](https://stripe.com/legal/celtic-charge-card)
- [Issuing Bank Terms - Charge Card (Cross River
Bank)](https://stripe.com/legal/issuing/crb-charge-card)
- [Issuing Bank Terms (Sutton
Bank)](https://stripe.com/legal/issuing/commercial-prepaid-sutton-terms)
- [Sutton Bank Authorized User
Terms](https://stripe.com/legal/issuing/sutton-authorized-user-terms)
- [Stripe Services Agreement](https://stripe.com/legal/ssa)
- [Stripe Treasury Terms - Connected
Accounts](https://stripe.com/legal/ssa#services-terms)
- [Issuing regulated customer
notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices)
- [Regulatory receipts
guide](https://docs.stripe.com/treasury/moving-money/regulatory-receipts)
- [Marketing Treasury-based
services](https://docs.stripe.com/treasury/marketing-treasury)
- [Stripe Payments Company](https://stripe.com/)