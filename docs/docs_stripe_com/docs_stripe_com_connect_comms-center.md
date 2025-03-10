# Comms Center

## Collect and send communications to connected accounts.

## Overview

Platforms that want to update the emails Stripe has on file for connected
accounts can update them using the [Comms Center collection
flow](https://dashboard.stripe.com/connect/comms_center/collect).

## Collecting emails

After hitting Get Started you see the main page for collection and validation.

![Comms Center Getting
Started](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-get-started.0342e9ed411102b9c81f3bfd3b075010.png)

### 1. Download a template with all of your connected accounts that are eligible for receiving communications.

![Comms Center Download
Step](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-download-emails.0f98ff258879870ce5a83603524c33ac.png)

You get a template CSV like this:

```
Account ID,Business Name,First Name,Last Name,Email Address (please add or
replace),User has claimed primary user email address
acct_123abc,Connected Account A,John,Doe,,✔
acct_456def,Connected Account B,,,,✗

```

### 2. Add the email addresses you want to add to the business within Stripe

For example, a filled out CSV might look like this:

```
Account ID,Business Name,First Name,Last Name,Email Address (please add or
replace),User has claimed primary user email address
acct_123abc,Connected Account A,John,Doe,email-a@email.com,✔
acct_456def,Connected Account B,,,email-b@email.com,✗

```

### 3. Upload the file with your changes

The filename doesn’t matter. Only the *Account ID* and *Email Address (please
add or replace)* fields matter here, the rest are only for validating your
changes.

![Comms Center Upload
Step](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-upload-emails.9ec27a2b1c9e46fd2d342f2b2c5ed923.png)

### 4. Wait for validation to complete and verify the account changes are correct.

![Comms Center Validation
Step](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-validation.09e86d5773685dea8a7ce28578abaaff.png)

### 5. Confirm your changes

After confirming, you see the completion state. Updates can take some time,
depending on how many emails you’ve uploaded. We send email updates to any
webhooks you’ve configured.

![Comms Center
Confirmed](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-confirmed.b5a1286831c481edc0055551ad4c5f6d.png)

## Important usage notes

- Comms Center can only currently handle CSVs with 500,000 rows. If you have
more than that, break up your CSV into multiple files.
- If you get validation errors, make sure your headers on your CSV match the
expected headers. The required columns are `Account ID` which has the `acct_`
tokens and `Email Address (please add or replace)` which has the desired email.

## Links

- [Comms Center collection
flow](https://dashboard.stripe.com/connect/comms_center/collect)