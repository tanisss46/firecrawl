# Uses Visa's Compelling Evidence 3.0 to respond to qualifying disputes

## What’s new

Adding a new
[enhanced_evidence](https://docs.stripe.com/api/disputes/update#update_dispute-evidence-enhanced_evidence)
object to the [Dispute](https://docs.stripe.com/api/disputes) resource allows
you to [submit
evidence](https://docs.stripe.com/api/disputes/update#update_dispute-submit)
using [Visa’s Compelling Evidence
3.0](https://docs.stripe.com/disputes/api/visa-ce3).

You can use the new
[evidence_details.enhanced_eligibility](https://docs.stripe.com/api/disputes/object#dispute_object-evidence_details-enhanced_eligibilitys)
property to track
[qualification](https://docs.stripe.com/disputes/api/visa-ce3#visa-qualifying-disputes).

## Impact

Submitting evidence using [Visa’s Compelling Evidence
3.0](https://docs.stripe.com/disputes/api/visa-ce3) typically results in an
improved win rate for [qualifying
disputes](https://docs.stripe.com/disputes/api/visa-ce3#visa-qualifying-disputes).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsenhanced_evidenceAdded[Dispute#update.evidence](https://docs.stripe.com/api/disputes/update#update_dispute-evidence)[Dispute.evidence](https://docs.stripe.com/api/disputes/object#dispute_object-evidence)enhanced_eligibility_typesAdded[Dispute](https://docs.stripe.com/api/disputes)enhanced_eligibilityAdded[Dispute.evidence_details](https://docs.stripe.com/api/disputes/object#dispute_object-evidence_details)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Links

-
[enhanced_evidence](https://docs.stripe.com/api/disputes/update#update_dispute-evidence-enhanced_evidence)
- [Dispute](https://docs.stripe.com/api/disputes)
- [submit
evidence](https://docs.stripe.com/api/disputes/update#update_dispute-submit)
- [Visa’s Compelling Evidence
3.0](https://docs.stripe.com/disputes/api/visa-ce3)
-
[evidence_details.enhanced_eligibility](https://docs.stripe.com/api/disputes/object#dispute_object-evidence_details-enhanced_eligibilitys)
-
[qualification](https://docs.stripe.com/disputes/api/visa-ce3#visa-qualifying-disputes)
-
[Dispute#update.evidence](https://docs.stripe.com/api/disputes/update#update_dispute-evidence)
-
[Dispute.evidence](https://docs.stripe.com/api/disputes/object#dispute_object-evidence)
-
[Dispute.evidence_details](https://docs.stripe.com/api/disputes/object#dispute_object-evidence_details)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)