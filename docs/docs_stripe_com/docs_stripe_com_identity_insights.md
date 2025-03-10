# Insights

## Learn how to identify risks and understand signals from verification checks.

Stripe Identity’s machine learning system considers a variety of signals when
verifying a user’s identity. It examines a number of factors to produce insights
that can give further clarity into Stripe’s decision. These insights are more
nuanced than the top-level verification decisions, and you can use them to
assist with manual reviews or customer support processes.

See the following definitions:

- **Insights**: The name Stripe uses to refer to the collection of all insights.
- **Insight**: The specific attribute scored (for example, blur, authenticity).
It’s of either type `Level` or `Label`.- **Level**: These insights provide a
computed level, which is a score that translates to low, elevated, or high.
Insights of this type evaluate the potential risk to verification.
- **Label**: These insights provide a binary value of being either present or
absent. Some of these insights evaluate a potential risk to verification, but
others might be neutral, with no inherent risk associated with them.

## Document insights

These are the insights produced on [document
checks](https://docs.stripe.com/identity/verification-checks?type=document):

NameTypeDescriptionActivity on Stripe network`Label`Indicates whether the
identity presented fails to match a Stripe-known identity. It’s not uncommon for
an identity to be unknown, though it does represent higher risk than a known
user.Barcode or machine-readable zone`Level`Indicates if the machine-readable
zone or barcode is present and decoded, but was manipulated.Document
authenticity`Level`Indicates whether the document presented might have been
digitally manipulated or is otherwise inauthentic.Fraud`Level`This comprehensive
score evaluates various signals related to document verification, including
signals from Stripe Network data.Image blurriness`Level`Indicates the severity
of the blurriness of the document image presented during the verification
process.Physical document detection`Level`Indicates whether the document
presented is a screenshot of a document.Risky behavior on the Stripe
network`Label`Indicates whether the identity presented matches a Stripe-known
identity with a history of high risk activity.
## Selfie insights

These are the insights produced on [selfie
checks](https://docs.stripe.com/identity/verification-checks?type=selfie):

NameTypeDescriptionDuplicate selfie`Label`Indicates whether the selfie presented
matches a selfie from a previous identity verification.Duplicate selfie with a
data mismatch`Label`Indicates that the selfie presented matches a selfie from a
previous identity verification, but the extracted document data from each
doesn’t match.Selfie and document match`Level`Indicates whether the selfie isn’t
a high confidence match with the face on the document.Selfie
liveness`Level`Indicates that the selfie presented might not have been a live
person in front of the camera, such as a photograph or screen presentation
attack.
## Dashboard usage

The Dashboard page for a submitted VerificationSession contains a panel showing
the insights generated for this session.

## Links

- [document
checks](https://docs.stripe.com/identity/verification-checks?type=document)
- [selfie
checks](https://docs.stripe.com/identity/verification-checks?type=selfie)