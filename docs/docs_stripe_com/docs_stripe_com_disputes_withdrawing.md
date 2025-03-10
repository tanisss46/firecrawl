# Dispute withdrawals

## Learn what to do when a cardholder withdraws their dispute.

The most effective dispute strategy is to [reduce the number of
disputes](https://docs.stripe.com/disputes/prevention) you receive in the first
place. For the best results, work directly with your customer to resolve the
issue if you do receive a dispute.

Every card network has some provision in its dispute system for the cardholder
to retract a dispute after filing it. Settling the dispute amicably with your
customer and convincing them to withdraw it is the best way to win it.

## Withdrawn disputes

A withdrawn dispute is one that your customer has asked their card issuer to
cancel. It isn’t *necessarily* a won dispute, because the dispute might still
resolve as a loss if you haven’t submitted evidence.

A withdrawn dispute is otherwise no different from any other dispute:

- It doesn’t resolve as a win or loss more quickly than other disputes.
- It doesn’t show up differently from any other dispute in the Dashboard or API.
- It still counts against your [dispute
rate](https://docs.stripe.com/disputes/measuring) with the card network.

Cardholders can only fully withdraw financial disputes—that is, a chargeback,
where your account balance has been debited. They can’t withdraw an [early fraud
warning](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
or an [inquiry](https://docs.stripe.com/disputes/how-disputes-work#inquiries),
which don’t have any financial impact. The cardholder might decline to escalate
these, but can’t undo them.

## Pursue a dispute withdrawal

Although a dispute withdrawal is a good way to turn a dispute into a win and
resolve a negative experience for your customer, it also requires some effort.
You need to weigh the amount of effort against how much it helps your dispute
win rate.

For disputes with a [high likelihood of
winning](https://docs.stripe.com/disputes/best-practices#likelihood-of-winning-disputes),
you can generally submit evidence to fight it, without reaching out to your
customer. For low value disputes, you can go ahead and [accept the
dispute](https://docs.stripe.com/disputes/responding#decide) if you don’t want
to invest time and resources to fight it.

## Talk to your customer

Contact your customer to try to work through the problem with them. If you can
reach a resolution, ask them to contact their card issuer and withdraw the
dispute. The process for this varies by issuer.

If your customer agrees to withdraw the dispute, you can ask them to provide
confirmation of the withdrawal, such as a confirmation email from their bank or
a screenshot of their mobile banking statement that shows they were re-billed
for the charge. This evidence isn’t required for your response to the issuer,
but provide it if you can.

#### Warning

If resolving the issue with your customer involves agreeing to issue a refund,
be aware that it might take weeks or even months before you can do so. Your
customer withdrawing the dispute doesn’t necessarily accelerate their issuer’s
dispute timeline. You [can’t issue a
refund](https://docs.stripe.com/disputes/how-disputes-work#receive-dispute) on a
disputed charge until your customer’s card issuer decides in your favor.

## Submit evidence

Regardless of what happens between you and your customer, you still need to
[submit evidence](https://docs.stripe.com/disputes/responding#respond) if you
want to win the dispute.

Always provide evidence for every dispute you hope to have resolved in your
favor, even if your customer told you they’re withdrawing the dispute. Many card
issuers treat failure to submit evidence as an acceptance of liability on your
part. This means you can still lose the dispute if you don’t submit evidence,
even if the customer withdrew the dispute with their issuer.

You can submit evidence for a dispute just one time, so you want to wait long
enough for your conversation with the customer to play out, but not so long that
you miss the deadline. The card network rules don’t allow you to submit evidence
after the deadline.

If you can’t convince the customer to withdraw the dispute before the evidence
deadline, that’s okay. You still need to file [appropriate
evidence](https://docs.stripe.com/disputes/categories) to challenge the dispute
reason.

## Dispute resolution

Generally, a withdrawn dispute doesn’t resolve any faster than other types of
disputes. After your customer withdraws it and you submit evidence, expect the
dispute to follow the [normal dispute
timeline](https://docs.stripe.com/disputes/how-disputes-work#timing).

## Late dispute withdrawal

Every card network allows cardholders to withdraw a dispute after the response
deadline, even long after a dispute is lost. However, some card issuers within
the network might not support late withdrawal in every case. As with any
dispute, the cardholder must contact their issuer to request a late withdrawal
and determine if it’s allowed.

Late withdrawals often occur outside the networks’ dispute systems. Unlike the
regular dispute lifecycle, they aren’t governed by network rules or regulations.
As a result, when a customer withdraws an old, lost dispute, it’s difficult to
set a realistic expectation for when you’ll see it reflected in your Stripe
account. The cardholder’s issuer might take weeks or months to process this type
of adjustment.

## Links

- [reduce the number of disputes](https://docs.stripe.com/disputes/prevention)
- [dispute rate](https://docs.stripe.com/disputes/measuring)
- [early fraud
warning](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
- [inquiry](https://docs.stripe.com/disputes/how-disputes-work#inquiries)
- [high likelihood of
winning](https://docs.stripe.com/disputes/best-practices#likelihood-of-winning-disputes)
- [accept the dispute](https://docs.stripe.com/disputes/responding#decide)
- [can’t issue a
refund](https://docs.stripe.com/disputes/how-disputes-work#receive-dispute)
- [submit evidence](https://docs.stripe.com/disputes/responding#respond)
- [appropriate evidence](https://docs.stripe.com/disputes/categories)
- [normal dispute
timeline](https://docs.stripe.com/disputes/how-disputes-work#timing)