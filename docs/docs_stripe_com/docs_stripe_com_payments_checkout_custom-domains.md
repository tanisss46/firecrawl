# Use your custom domain

## Learn how to bring your own custom domain to Stripe Checkout, Payment Links, and customer portal.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
If you’re using the [Stripe-hosted
page](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
for Checkout, you can add your own custom domain to Stripe. Adding custom
domains is a paid feature. For information about cost, see Checkout’s
[Pricing](https://stripe.com/pricing).

[Add your custom domain to the Stripe
Dashboard](https://docs.stripe.com/payments/checkout/custom-domains#add-your-custom-domain)
Decide what subdomain to use with your Checkout Sessions, Payment Links, and
customer portal.

#### Note

If your domain is `example.com`, we recommend using `payments.example.com` as
your custom subdomain. You can replace `payments` with anything you like, as
long it’s a valid subdomain. You can’t use a path like `example.com/checkout`
and must specify a subdomain of your existing domain.

After you decide on a subdomain, visit the [Custom domains settings
page](https://dashboard.stripe.com/settings/custom-domains) to start the domain
connection process.

On the settings page click **Add your domain**.

In the pop up, enter your desired subdomain. Click **Add** when you’re done.
You’ll see the popup update with instructions for setting up your DNS records.

Your custom domain is activated automatically when your DNS records are
verified. To disable this behavior, uncheck the **Switch to this domain once
added** checkbox.

#### When will my domain be added?

When your domain is in the `Adding...` state, we wait to verify your DNS records
that you set up in the next step. After Stripe verifies the DNS records, we
create TLS certificates for your subdomain, set up the correct CDN routing, and
then your domain is `ready` to enable and use.

[Identify your DNS
Provider](https://docs.stripe.com/payments/checkout/custom-domains#your-dns-provider)
To start, figure out what service is managing your DNS records, so you know
exactly where to login and create the new records.

If you **already know** your DNS provider, you can move on to the next section.

Often, it’s the same place you registered your domain, but sometimes the DNS
provider is different from your domain registrar.

If you’re not certain who your DNS provider is, try looking up your domain’s
nameservers, replacing **stripe.com** with your own domain in this command:

```
nslookup -querytype=NS stripe.com
```

You’ll see a list of nameservers for your domain in the output. Here’s some
example output for **stripe.com**:

```
# Looks like AWS is providing our DNS here:
stripe.com	nameserver = ns-423.awsdns-52.com.
stripe.com	nameserver = ns-705.awsdns-24.net.
stripe.com	nameserver = ns-1087.awsdns-07.org.
stripe.com	nameserver = ns-1882.awsdns-43.co.uk.

```

If you’re more comfortable using a browser-based tool, go to [MXLookup’s DNS
Lookup tool](https://mxtoolbox.com/DnsLookup.aspx) and enter your domain. It
might be able to tell you who your DNS provider is (but not always).

[Create required DNS
records](https://docs.stripe.com/payments/checkout/custom-domains#create-dns-records)
In this section, you’ll create the DNS records you need to connect your domain.
As you go through each step, check each checkbox to keep track of where you are
in the process.

Select the tab that matches your DNS provider from the tabs below—this gives you
specific, guided instructions for creating the required DNS records. If your DNS
provider isn’t an option, follow the Standard instructions:

Standard instructionsGoDaddyCloudflare
These are standard instructions for creating your DNS records. If you have
issues with any of the steps, please contact your DNS provider for more
assistance.

#### Note

To track your progress, go through each step and check it off when you’ve
completed it.

- Sign into your DNS provider
Most DNS providers have a control panel you can sign into to manage your DNS.
Find your provider’s control panel page and sign in.
- Find the page to manage the DNS for your domain
Now that you’re logged in, find where you can manage the DNS records for your
domain in your provider’s control panel.

If you’re having issues finding the right page, you can:

- See if your DNS provider has a help article for adding new DNS records that
can point you in the right direction.
- Contact your DNS provider for additional support.
- Create your CNAME record
From your DNS control panel, add a new record that maps your desired subdomain
to Checkout. Most DNS providers ask you for the record type, name, value, and
TTL or expiration when creating a new record.

#### Note

This record is what connects your subdomain to Stripe Checkout.

Enter these values and save the new DNS record:

FieldInstructionsDescriptionTypeSelect `CNAME` from the dropdownWhat kind of DNS
record this is.Name
If your custom subdomain is **checkout.powdur.me**, enter `checkout`

For CNAME records, this field is the first part of your subdomain (the part
leading up to the first period).
**Value**

Enter `hosted-checkout.stripecdn.com`

This is what the new subdomain record points to–in this case, Stripe.

Some providers may expect a trailing period (`.`) after the CNAME value. Make
sure to verify that your CNAME value matches the format your provider expects.

TTL/ExpiryEnter `300`An expiration of 5 minutes (300 seconds) is OK. Your DNS
provider might not allow you to change the TTL value. If this field is missing
or you can’t change it, it’s safe to ignore this part of the configuration.
- Create your TXT record
From your DNS control panel, add a new TXT record.

#### Note

This TXT record lets us verify that you’re the owner of this domain. This is
required to issue TLS certificates for your domain, so you can continue to
accept payments securely.

Enter these values and save the new DNS record:

FieldInstructionsDescriptionTypeSelect `TXT` from the dropdownWhat kind of DNS
record this is.Name
If your custom domain is **checkout.powdur.me**, enter
`_acme-challenge.checkout`

For TXT records, this field is the subdomain portion of your domain.Value
Visit the [Dashboard
settings](https://dashboard.stripe.com/settings/custom-domains) and click **View
instructions** to copy the correct TXT value record.

This is a long, unique string used for domain verification.TTL/ExpiryEnter
`300`An expiration of 5 minutes (300 seconds) is OK. Your DNS provider might not
allow you to change the TTL value. If this field is missing or you can’t change
it, it’s safe to ignore this part of the configuration.
- Verify your CNAME record is setup
After you save your DNS record, verify that it has the correct values.

Verify in your terminalVerify with your web browser- Wait up to 10 minutes for
your DNS provider to update its nameservers.
- Replace **checkout.powdur.me** with your custom domain in the following
command and run it from your terminal:

```
nslookup -querytype=CNAME checkout.powdur.me
```

You should see output like:

```
<your subdomain> 	canonical name = hosted-checkout.stripecdn.com.

```

When you see that output, move onto the next step.
- Verify your TXT record
After you save your DNS record, verify that it has the correct values.

Verify in your terminalVerify with your web browser- Wait up to 10 minutes for
your DNS provider to update its nameservers.
- Replace **checkout.powdur.me** with your custom domain in the following
command and run it from your terminal:

```
nslookup -querytype=TXT _acme-challenge.checkout.powdur.me
```

You should see output like this:

```
_acme-challenge.<your domain> text = "<your unique TXT record value>"

```

If you don’t see your unique TXT record value in the output, wait a bit longer
and try running the command again.

When you finish this step, your DNS records are configured.

Now that you’ve created your DNS records and verified them, Stripe verifies the
connection and provisions your domain on our end. We’ll send you an email and a
Dashboard notification when the domain is ready for you to enable it. You can
also visit the [Dashboard
settings](https://dashboard.stripe.com/settings/custom-domains) at any time to
see the current status of your custom domain connection.

[OptionalTest your custom
domain](https://docs.stripe.com/payments/checkout/custom-domains#test-your-domain)[OptionalRemoving
your custom
domain](https://docs.stripe.com/payments/checkout/custom-domains#removing-your-domain)[OptionalUsing
custom domains with
Connect](https://docs.stripe.com/payments/checkout/custom-domains#connect)[OptionalTroubleshooting
your
integration](https://docs.stripe.com/payments/checkout/custom-domains#troubleshooting-integration)[OptionalTroubleshooting
CAA DNS
records](https://docs.stripe.com/payments/checkout/custom-domains#troubleshooting-caa-records)[OptionalTroubleshooting
a blocked
domain](https://docs.stripe.com/payments/checkout/custom-domains#troubleshooting-a-blocked-domain)

## Links

- [Stripe-hosted
page](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [Pricing](https://stripe.com/pricing)
- [Custom domains settings
page](https://dashboard.stripe.com/settings/custom-domains)
- [MXLookup’s DNS Lookup tool](https://mxtoolbox.com/DnsLookup.aspx)