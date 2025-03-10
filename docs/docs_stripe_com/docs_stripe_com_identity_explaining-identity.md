# Explain Identity to your customers

## Answer customer questions about ID verification and Stripe Identity.

If you use Stripe Identity for ID verification, copy and customize these
questions and answers to create Frequently Asked Questions (FAQs) around ID
verification. To obtain Stripe logos, badges, and buttons for your site, visit
the **Media assets** section on
[stripe.com](https://stripe.com/newsroom/information).

## Pre-approved content

In your Stripe Identity FAQ, address the following questions by using the
provided pre-approved copy:

### How does identity verification work?

### What are the best practices for a successful verification?

### Who has access to my verification data?

## Open-ended questions

For the following questions, provide your preferred answer:

QuestionAdditional informationWhy am I asked to verify my identity?Provide your
preferred answer. Some users might be hesitant to share their ID information, so
it’s important to help them understand why you’re asking for this informationWhy
was I rejected?You might want to offer alternative methods for verification if a
user disputes their results.Can I get verified using a different method?Privacy
laws might require you to provide an alternative verification process that
doesn’t use biometric technology if the user doesn’t consent to use of their
biometric information. Consult your legal counsel for regional requirements.
**How can I access or delete my verification data?**

Provide your data privacy process.

The Identity API has a [redaction
endpoint](https://docs.stripe.com/api/identity/verification_sessions/redact)
that allows you to delete the verification data that Stripe Identity stores on
behalf of your business. For example, you can use this tool to meet your
deletion requirements when an end-user from Europe or California asks you to
delete their data, or when you collect an ID from a country such as Germany that
requires you to delete an ID card upon completion of the verification even if
there’s no deletion request from the end user. If you’ve created additional
copies of a user’s data, you might also need to delete these as well.

Stripe doesn’t delete data on your behalf when we store the data as your
processor, even if your end-user asks us to, because we recognize you must
conduct your own legal analysis on whether deletion is appropriate.

If your end-user reaches out to us requesting deletion, we’ll respond to the
request with respect to any data that we hold as data controller, and also
recommend the end-user reach out to you to request deletion.

## Links

- [stripe.com](https://stripe.com/newsroom/information)
- [redaction
endpoint](https://docs.stripe.com/api/identity/verification_sessions/redact)