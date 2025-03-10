# Test pricing schemes

## Simulate application fees on payments to test the effects of your pricing scheme.

You can test your pricing scheme configurations before enabling it for your live
accounts using either of the methods described in this guide.

## Test mode

In test mode, you can use all of the functionality of pricing tools without
making actual charges to connected accounts. Within test mode you can construct
payments matching any of the supported conditions on test businesses, allowing
you to make sure your integration works correctly. This feature helps you
identify any errors or margin loss in your pricing configuration before you go
live.

### Test in a sandbox

You can use [Sandboxes](https://docs.stripe.com/sandboxes) to test pricing
changes in an isolated environment. To access sandboxes, click **Sandboxes** in
the Dashboard account picker.

Each new sandbox copies the live mode pricing tools configuration to a new test
instance. A new sandbox assigns all groups to the default scheme, allowing you
to configure different defaults and test different grouping strategies.

## Platform pricing testing tool

Before rolling out a pricing change using pricing tools, you can simulate the
impact of a pricing change on historical charges (a before and after simulation)
where you paid the fees.

- From the [Platform
Pricing](https://dashboard.stripe.com/settings/connect/platform_pricing) page of
your Dashboard, click the overflow menu () of the pricing scheme, then select
**Test**.
- Enter the ID of a historic charge, then click **Add**. You can add up to 50
charges to simulate.
- Select the charges to compare (or select all), then click **Test
transactions**.

The simulation returns the following information for each transaction:

PropertyDescriptionTransaction amountThe amount on the historical
charge.Original application feeThe application fee you collected for this
charge.Recalculated application feeThe application fee collected for the same
charge according to the pricing scheme changes that you’re testing.Original
matched ruleThe conditions of the rule used to calculate the original
application fee if a pricing scheme computed it.Recalculated matched ruleThe
conditions of the rule used to calculate the alternate application fee based on
the changes that you’re testing.
You can only test charges where your platform paid the Stripe fees. Testing
against a historic charge where you didn’t pay the Stripe fees fails.

If you’re satisfied with the test, return to the pricing scheme page and either
submit your pricing changes or continue to experiment.

## Links

- [Sandboxes](https://docs.stripe.com/sandboxes)
- [Platform
Pricing](https://dashboard.stripe.com/settings/connect/platform_pricing)