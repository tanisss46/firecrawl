# Custom email domain

## Set up your own custom domain to interact with your customers.

By default, when Stripe sends invoices, receipts, and failed payment
notifications to your customers, it sends them from the `stripe.com` domain. You
can change this to a custom domain.

## Set up a custom email domain

To start sending emails from your own domain, complete the following steps:

- [Add your
domain](https://docs.stripe.com/get-started/account/email-domain#adding_domain)
in the Dashboard.
- [Verify your
domain](https://docs.stripe.com/get-started/account/email-domain#verifying_domain)
to allow sending.
- [Set your sending
domain](https://docs.stripe.com/get-started/account/email-domain#setting_sending_domain)
as your domain.

To modify the look and feel of your emails, go to your
[Branding](https://dashboard.stripe.com/account/branding) settings.

[Add your
domain](https://docs.stripe.com/get-started/account/email-domain#adding_domain)
Navigate to your [Customer email](https://dashboard.stripe.com/settings/emails)
settings and add the domain that you want to send customer emails from.

[Verify your
domain](https://docs.stripe.com/get-started/account/email-domain#verifying_domain)
To verify your domain, you must configure the Domain Name System (DNS) records
provided in the Dashboard. These DNS records are necessary to verify your domain
ownership and reliable email delivery.

The procedure for adding DNS records to the DNS server for your domain depends
on who provides your DNS service. Consult the documentation for your DNS service
for specific instructions.

### Instructions for popular providers

It can take up to 72 hours for DNS record changes to be confirmed. Stripe lets
you know whether your domain has been verified.

### Troubleshoot DNS issues

If your domain hasn’t been verified after 72 hours, try the following:

- Correct any typos. You can check your domain records in the Dashboard’s
[Customer emails](https://dashboard.stripe.com/settings/emails) settings by
clicking **Verify domain** to filter issues.
- Make sure you don’t have any records that share the same name as the provided
CNAME records. CNAME records must be the [only record
present](https://tools.ietf.org/html/rfc2181#section-10.1) for a record name.
- Make sure the added record names don’t include your domain twice. Some
providers automatically append DNS record names with the domain name. For
example, to create a record with the name **bounce.example.com**, enter only
`bounce` in the **Name** field.
- Check that the DNS records are published. You can verify this by using a [DNS
lookup tool](https://dnschecker.org/all-dns-records-of-domain.php), which
displays the published records for your domain.

If you’ve tried all of our troubleshooting recommendations and are still having
trouble verifying your domain, contact your DNS provider.

### DNS records

Each category of record that needs to be configured has a purpose.

Record CategoryTypePurposeStripe proof-of-ownershipTXTBefore you can send email
from a domain, we must confirm ownership of the domain you plan to use.Mail From
DomainCNAMEThis specifies the source of the message to the receiving email
server and the [Sender Policy Framework
(SPF)](https://tools.ietf.org/html/rfc7208) policy to allow sending.[DomainKeys
Identified Mail (DKIM)](http://dkim.org/)CNAMEThese allow a mail server to
verify that a third party didn’t modify a message in transit.
#### Caution

After we verify the domain, don’t delete the provided DNS records from your
domain. Stripe frequently checks these records. If a record becomes invalid or
goes missing, we notify you. Also, make sure to correct DNS records within 48
hours. If you don’t, we send customer emails from *stripe.com* until you resolve
the problem.

### Sender authentication (DMARC)

To use a custom email domain, you need to set up a DMARC policy for your domain.
[Domain-based Message Authentication, Reporting & Conformance
(DMARC)](https://dmarc.org/) shields your domain from impersonation attacks,
such as phishing. Notably, major email providers like Google and Yahoo now
necessitate DMARC for those sending bulk emails.

You publish DMARC policy as a DNS TXT record. The record’s name is always
`_dmarc`, and the value comprises tag-value pairs that symbolize your policy.
Additionally, you can learn about all the [supported tags and their
uses](https://dmarc.org/overview/), but let’s cover some of the most significant
tags:

TagDescriptionSample valuev requiredThe protocol version. This must always be
DMARC1.v=DMARC1p requiredThe policy for domain. The possible values are: none,
quarantine, reject.p=nonerua optionalAddress(es) to receive aggregate
reportsrua=mailto:report@example.com
If you’re new to DMARC, we suggest beginning with a `p=none` policy for initial
monitoring, then switch to either `quarantine` or `reject` in due course. After
you’ve settled on the appropriate policy, you must incorporate the following DNS
record into your domain:

TypeNameValueTXT`_dmarc`Your DMARC policy. For example: `v=DMARC1; p=none;
rua=mailto:report@example.com`
#### Caution

We don’t currently support strict SPF alignment. Make sure your DMARC policy
doesn’t have `aspf=s`.

If you’re already using this domain to send email, use caution when adding DMARC
to make sure that it doesn’t interfere with your existing configuration. Consult
an email or IT professional before adding or modifying this record.

[Set your sending
domain](https://docs.stripe.com/get-started/account/email-domain#setting_sending_domain)
If Stripe has verified your domain, you’ll see a **Verified** badge under the
**Verification** column in your [Customer
email](https://dashboard.stripe.com/settings/emails) settings. Customer emails
are now sent from your domain. You can send a test email by clicking the
overflow menu ().

Whenever a customer replies to your emails, their responses are sent to the
support email address you specified in your [public business
information](https://dashboard.stripe.com/settings/public).

## Change email domains

We must verify each domain that you want to set as your sending domain. To
switch to a new domain, return to [Add your
domain](https://docs.stripe.com/get-started/account/email-domain#setup). You can
always switch back to sending your customer emails using `stripe.com`.

When you’re no longer using a domain to send customer emails, you can remove it
from your [Customer email](https://dashboard.stripe.com/settings/emails)
settings. In the **Your custom email domains** section, click the overflow menu
() next to the domain name and select **Remove domain**. After removing the
domain from your Dashboard, remove the unused DNS records from your DNS service.

### Instructions for popular providers

## Use the same email domain on multiple Stripe accounts

You can use the same email domain on multiple Stripe accounts by following the
steps described above. To verify the domain, create one TXT record for each
account, or if your provider doesn’t support this, create a single TXT record
with one account per line.

## Links

- [Branding](https://dashboard.stripe.com/account/branding)
- [Customer email](https://dashboard.stripe.com/settings/emails)
- [only record present](https://tools.ietf.org/html/rfc2181#section-10.1)
- [DNS lookup tool](https://dnschecker.org/all-dns-records-of-domain.php)
- [Sender Policy Framework (SPF)](https://tools.ietf.org/html/rfc7208)
- [DomainKeys Identified Mail (DKIM)](http://dkim.org/)
- [Domain-based Message Authentication, Reporting & Conformance
(DMARC)](https://dmarc.org/)
- [supported tags and their uses](https://dmarc.org/overview/)
- [public business information](https://dashboard.stripe.com/settings/public)