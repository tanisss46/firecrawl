# Reviews

## Use reviews to supplement automated systems with human expertise.

While Stripe’s automated systems work to prevent fraud on your account, you can
use reviews to provide an extra layer of fraud protection by giving payments a
manual inspection.

For example, you might want to review transactions that:

- Have an [elevated
risk](https://docs.stripe.com/radar/risk-evaluation#elevated-risk) of fraud
according to Stripe’s fraud protection system
- Were made from outside your country
- Are greater than a certain amount
- Use an email address from an unusual domain

The review queue of Stripe Radar for Fraud Teams allows you to examine unusual
payments, without having to look at each payment individually. You can create a
targeted list of payments to review with criteria that you specify, and review
them in the Dashboard.

## Smart Refunds Preview

[Radar for Fraud Teams](https://docs.stripe.com/radar) users can use Smart
Refunds to proactively refund high risk payments. Smart Refunds leverages
Radar’s machine learning system to evaluate payments for their likelihood of
resulting in a dispute in the hours after a transaction completes. If the
dispute risk meets the threshold for high likelihood, Stripe flags a refund
recommendation in your **Reviews** list.

## Interested in getting early access to Smart Refunds?

Access to Smart Refunds is currently in private preview. If you're interested in
trying it out, enter your email address below.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Review payments

The Dashboard [review queue](https://dashboard.stripe.com/radar/reviews) is a
prioritized list of completed or to-be-captured payments that might need further
investigation. You can review payments by:

- [List view](https://docs.stripe.com/radar/reviews#list-view): Scan a list of
reviews without seeing details about each payment.
- [Detailed view](https://docs.stripe.com/radar/reviews#detailed-view): Review
customizable payment context for a particular review item.

#### Note

Payments placed into review are typically already successfully processed, unless
you [capture authorized payments
later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method). You
can approve a payment, refund it, or refund it and mark it as fraudulent.

### List view

The list view contains information to help you quickly get a sense for each
payment’s possible risk of fraud.

!

The manual review queue in the Stripe Dashboard

The list view highlights:

- The risk level Stripe assigns after evaluating the payment
- The [customer](https://docs.stripe.com/api/customers) name
- Payment method information
- Customer information
- The amount, date, and time of the payment
- The client

### Detailed view

Select the payment within the review queue to view its details page, which might
contain [metadata](https://docs.stripe.com/radar/reviews#best-practices) that
can help with your decision. You can navigate between payments to review using
the **Previous** and **Next** buttons.

The Stripe Radar machine learning system evaluates hundreds of signals when
scoring a charge. The [risk
insights](https://docs.stripe.com/radar/reviews/risk-insights) section on the
payment page identifies some of the most relevant signals, along with some key
data points that can help assess fraud on a payment. The [related
payments](https://docs.stripe.com/radar/reviews/risk-insights#related-payments)
section shows other payments made to your business that use the same email
address, IP address, or card number as the payment you’re currently reviewing.

## Actions

After you review a completed payment, you can remove it from the review queue by
taking one of the following actions:

- **Approve**: Closes the review with no changes made to the payment. You can
still refund and, optionally, report fraud on an approved payment.
- If you [capture payments
later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method), there
is also a **Capture** button. You can capture a payment before or after
approval.
- **Refund**: Refunds the payment without reporting it to Stripe as fraudulent.
A completed refund is permanent, you can’t undo it—you must process a new
payment. If you capture payments later, this button changes to **Cancel**. You
can read more about [this review process
here](https://docs.stripe.com/radar/reviews/auth-and-capture).
- **Refund and report fraud**: Refunds the payment and also reports it to Stripe
as fraudulent, for instance to [save dispute
fees](https://docs.stripe.com/disputes/prevention/best-practices#consider-proactively-refunding-suspicious-payments).
This adds the associated card fingerprint and customer email to your [block
lists](https://docs.stripe.com/radar/lists#default-lists) and further increases
the effectiveness of our fraud prevention.

#### Note

If a customer [disputes](https://docs.stripe.com/disputes) a payment that’s
currently in your review queue, the review is automatically closed.

### Customize the review queue

With Stripe Radar for Fraud Teams, you can create
[rules](https://docs.stripe.com/radar/rules#review-rules) that automatically
place payments in review based on your unique business needs. This gives you the
opportunity to identify payments that might require more investigation before
you can make an informed decision.

## Review assignments

Anyone managing the review queue can assign themselves to reviews to avoid
duplicating effort.

As a reviewer, you can see which reviews other people are working on and assign
or remove yourself from reviews. You can also filter the review queue to see
reviews you own or reviews that are currently unassigned.

#### Note

You can only change review assignments for yourself, not for other team members.

!

In the list view, use quick actions or the overflow menu to assign yourself to a
review.

To assign yourself to a review in the [list
view](https://docs.stripe.com/radar/reviews#list-view), hover over a review and
click the person icon or the **Assign to me** button in the overflow menu. In
the [detail view](https://docs.stripe.com/radar/reviews#detailed-view), click
**Assign to me**.

You can take action on a review assigned to another team member or assign it to
yourself. The review timeline shows a complete history of assignment changes and
other actions.

!

The timeline in the detail view displays a history of assignment changes.

## Listen for review events

You can listen for webhook events related to review activity to trigger relevant
response handling. Stripe sends the following review events:

- `review.opened`: Indicates that a transaction was added to the review queue,
generating a [review](https://docs.stripe.com/api/radar/reviews) object.
- `review.closed`: Indicates that a review object closed and provides the
`reason`.

## Best practices

Use the following best practices to get the most out of reviews and perform them
efficiently.

- **Focus time on payments where human judgment can add valuable insight to the
decision**

Automated systems can make decisions on the majority of payments but human
decision making can significantly improve accuracy when identifying fraud in
some cases. Because not every case benefits from human involvement, make sure
you choose transactions where the benefit is clear.
- **Use risk insights and related payments to make an informed decision**

Use the data in the [risk
insights](https://docs.stripe.com/radar/reviews/risk-insights) section to see
how Stripe Radar came up with a score for a charge. Combining the reasons for a
score, knowledge about your business, and human judgement can help you make an
informed choice about when to trust or ignore the score assigned by Radar.
- **Leverage the insights from reviewers to develop hypotheses for fraud
prevention strategies**

As reviewers sort through your transactions, they develop intuitions for fraud
prevention that you can translate into better rules. Collect insights from
reviewers to [test custom rules on your
account](https://docs.stripe.com/radar/testing#rules).
- **Customize the process by presenting data unique to your business at review
time**

Pass along any additional customer or order information as metadata so that all
relevant information is in the Dashboard at the time of review. Some examples of
useful metadata include:

- More information about the order and its shipping information
- [Google Maps](https://maps.google.com/) and Street View links to the
customer’s shipping address so the reviewer can see if the address might be a
drop-shipping or freight-forwarding service
- **Don’t slow down your customer**

A review implies some amount of time between order placement and delivery. If
your business has an inherent delay of this type (for example, you’re shipping
physical goods), taking the time to review a transaction doesn’t affect the
customer’s delivery expectation. If you don’t have a built-in delay between
orders and fulfillment with your business, adding a review process might slow
down orders and create a bottleneck for good customers. Consider the impact on
customers before you implement a review process.

## See also

- [Rules](https://docs.stripe.com/radar/rules)

## Links

- [elevated risk](https://docs.stripe.com/radar/risk-evaluation#elevated-risk)
- [Radar for Fraud Teams](https://docs.stripe.com/radar)
- [privacy policy](https://stripe.com/privacy)
- [review queue](https://dashboard.stripe.com/radar/reviews)
- [capture authorized payments
later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [customer](https://docs.stripe.com/api/customers)
- [risk insights](https://docs.stripe.com/radar/reviews/risk-insights)
- [related
payments](https://docs.stripe.com/radar/reviews/risk-insights#related-payments)
- [this review process
here](https://docs.stripe.com/radar/reviews/auth-and-capture)
- [save dispute
fees](https://docs.stripe.com/disputes/prevention/best-practices#consider-proactively-refunding-suspicious-payments)
- [block lists](https://docs.stripe.com/radar/lists#default-lists)
- [disputes](https://docs.stripe.com/disputes)
- [rules](https://docs.stripe.com/radar/rules#review-rules)
- [list view](https://docs.stripe.com/radar/reviews#list-view)
- [detail view](https://docs.stripe.com/radar/reviews#detailed-view)
- [review](https://docs.stripe.com/api/radar/reviews)
- [test custom rules on your
account](https://docs.stripe.com/radar/testing#rules)
- [Google Maps](https://maps.google.com)
- [Rules](https://docs.stripe.com/radar/rules)