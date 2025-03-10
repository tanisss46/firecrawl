# Send events to Amazon EventBridge

## Consume Stripe events in your AWS infrastructure.

#### Enable Workbench

To send events to Amazon EventBridge, enable Workbench in your [Developer
settings](https://dashboard.stripe.com/settings/developers) in the Dashboard.

[Amazon
EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
is a serverless, event-driven service provided by AWS that helps connect your
applications together by ingesting, transforming, and delivering events.
Integrating with EventBridge using an event destination allows you to receive
event data from Stripe directly in your AWS account, instead of handling the
traffic and managing integration code logic yourself. When events are received,
EventBridge can route them to [20 supported
targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html)
to process or trigger business automations.

## Send events to Amazon EventBridge

Complete the steps below to receive events in EventBridge. This involves
creating a new event destination in Workbench and setting up EventBridge
configuration in the [AWS Management
Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/learn-whats-new.html).

#### Warning

You won’t receive any event data in your Amazon EventBridge until you complete
each step.

[Add a new event
destinationWorkbench](https://docs.stripe.com/event-destinations/eventbridge#add-eventbridge-destination)
#### Send events in your sandbox

Use your live account or [sandboxes](https://docs.stripe.com/sandboxes) to send
events to Amazon EventBridge.

Create an event destination using Workbench in the Dashboard or programmatically
with the [API](https://docs.stripe.com/api/v2/event-destinations).

DashboardAPI
To create an event destination in the Dashboard:

- Open the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench.
- Click **Create new destination**.
- Select where you want to receive events from. Stripe supports two types of
configurations: **Your account** and [Connected
accounts](https://docs.stripe.com/connect). Select **Account** to listen to
events from your own account. If you created a [Connect
application](https://docs.stripe.com/connect) and want to listen to events from
your connected accounts, select **Connected accounts**.
- Select the [event types](https://docs.stripe.com/api/events/types) that you
want this destination to receive. Then, click **Continue**.
- Select **Amazon EventBridge** as your destination type, then click
**Continue**.
- Enter the following information:- [AWS account
ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html):
The AWS account that hosts your EventBridge instance for receiving events.
- [AWS
region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/): The
AWS region that hosts your EventBridge instance for receiving events.
- *(Optional)* **Destination name**: A unique name of this event destination
resource in Stripe. If you don’t provide one, we generate a random name for you.
You can change it later.
- *(Optional)* **Description**: A description that distinguishes your event
destination instance. You can modify this later.
- Click **Create destination**.

![Register a new webhook using the Webhooks
tab](https://b.stripecdn.com/docs-statics-srv/assets/create-webhook.f728025897e9e4ca2ba623abe34995a0.png)

Register a new webhook in the **Webhooks** tab

[Associate the partner event sourceAWS
Console](https://docs.stripe.com/event-destinations/eventbridge#associate-partner-event-source)
After you set up an event destination, Stripe creates a [partner event
source](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EventSource.html)
in the AWS account and region you provided during configuration. To start
receiving events, you need to associate this event source with an [event
bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
within 7 days of the event destination’s creation. If you don’t associate it
within this time frame, Amazon automatically deletes the pending event source.
After an event source is deleted, your Stripe event destination is automatically
disabled and you must create a new destination to receive events.

- Under **EventBridge** in your [AWS
console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/learn-whats-new.html),
navigate to the [Partner event sources
page](https://console.aws.amazon.com/events/home#/partners) that’s listed in the
**Integration** section of the left-hand panel.

![Navigate to **Partner event
sources**](https://b.stripecdn.com/docs-statics-srv/assets/aws-select-partner-event-source.14ff917248eeb4f333195e6b3a431447.png)

- Use the **Region** dropdown list located at the top of the console to select
the region you chose when configuring your [event destination in
Workbench](https://docs.stripe.com/event-destinations/eventbridge#add-eventbridge-destination).

![Select your AWS
region](https://b.stripecdn.com/docs-statics-srv/assets/aws-region.6a68960287ba6356f8e856501295a039.png)

- Choose the newly created partner event source in the dropdown. To find the
Event Source ARN field in Workbench, select your event destination. Your partner
source matches the part of the ARN that reads
`event-source/aws.partner/stripe.com/{UNIQUE_ID}`. Then, click **Associate with
event bus**.

![Associate the partner event source with event
bus](https://b.stripecdn.com/docs-statics-srv/assets/aws-associate-partner-event-source.c89d540961356ff06e3fb095956ba80f.png)

- Select permissions you want to grant for this event bus as needed, then click
**Associate**.

![Select permissions and finalize
association](https://b.stripecdn.com/docs-statics-srv/assets/aws-associate-event-bus.28dcbc4781d814799076258c8f1b9a04.png)

[Create EventBridge rulesAWS
Console](https://docs.stripe.com/event-destinations/eventbridge#create-evenbridge-rule)
EventBridge groups and routes events based on
[rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)
you define. After you create an event destination and associate its partner
event source to an event bus, you must define rules to make sure that
EventBridge knows how to handle the events it receives on the event bus. You can
repeat these steps multiple times to define multiple rules.

- Navigate to the AWS management console, then click
[Rules](https://console.aws.amazon.com/events/home#/events).

![Navigate to
**Rules**](https://b.stripecdn.com/docs-statics-srv/assets/aws-select-rules.f385d0e668caafc9614584e2ae635138.png)

- Click **Create Rule**, then provide a rule name and description.

![Provide rule name and
description](https://b.stripecdn.com/docs-statics-srv/assets/aws-define-rule.ce885bcbea4d7492f082eba2f38fd840.png)

- Select your event bus from the dropdown. To find your event bus, navigate to
Workbench, select your destination in the **Webhooks** tab, then view the
**Event source ARN** field, which shares the same name as your event source ARN.
Then, click **Next**.
- Under **Event source**, select **AWS events or EventBridge partner events**
because Stripe events are partner events.

![Select event
source](https://b.stripecdn.com/docs-statics-srv/assets/aws-event-source.29ee4d4e795b0f7d89db7163ab7b9ac5.png)

- *(Optional)* Include a sample Stripe event.
- Under **Creation Method**, choose **Use pattern form** to use a predefined
pattern. Alternatively, you can create a custom event pattern.

![Use a predefined rule
patter](https://b.stripecdn.com/docs-statics-srv/assets/aws-create-rule-pattern.3246a6c5a409b1b0571f56acc6e7b91b.png)

- Under **Event Pattern**, select **EventBridge partners** as the **Event
Source**.
- Under **Event Pattern**, select **Stripe** as the **Partner**.
- Select the appropriate event type you want to create a rule for or select
**All events** to match this rule to all event types, then click **Next**.
- Select the
[target](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html)
you want this rule to send events to, then click **Next**.

#### Recommendation

We recommend you [create a CloudWatch Logs
target](https://repost.aws/knowledge-center/cloudwatch-log-group-eventbridge)
for each event bus to enable monitoring for your event destination. Consider
using other [common architecture
patterns](https://docs.stripe.com/event-destinations/eventbridge#common-architecture)
with EventBridge and Stripe events.

![Select rule
target](https://b.stripecdn.com/docs-statics-srv/assets/aws-select-target.d9da569a26cf0d6fcc81f753b16d0e60.png)

- Add optional tags, then click **Next**.
- Review your rule and make changes as needed, then click **Create Rule**.

Your Stripe events are now successfully delivered to EventBridge and its
corresponding targets defined in your rule.

## Trigger test events

To send test events, trigger an event type that your webhook is subscribed to by
manually creating an object in the Stripe Dashboard. Alternatively, you can use
the following command in either [Stripe
Shell](https://docs.stripe.com/stripe-shell/overview) or [Stripe
CLI](https://docs.stripe.com/stripe-cli).

This example triggers a `payment_intent.succeeded` event:

```
stripe trigger payment_intent.succeeded
Running fixture for: payment_intent
Trigger succeeded! Check dashboard for event details.
```

Learn how to trigger events with [Stripe for VS
Code](https://docs.stripe.com/stripe-vscode).

## Event delivery behaviors

This section helps you understand different behaviors to expect regarding how
Stripe sends events to Amazon EventBridge.

### Automatic retries

Stripe attempts to deliver events to your destination for up to three days with
an exponential back off in live mode. View when the next retry will occur, if
applicable, in your event destination’s **Event deliveries** tab. We retry event
deliveries created in a sandbox three times over the course of a few hours. If
your destination has been disabled or deleted when we attempt a retry, we
prevent future retries of that event. However, if you disable and then re-enable
the event destination before we’re able to retry, you still see future retry
attempts.

### Manual retries

There are two ways to manually retry events:

- In the Stripe Dashboard, click **Resend** when looking at a specific event.
This works for up to 15 days after the event creation.
- With the [Stripe CLI](https://docs.stripe.com/cli/events/resend), run the
`stripe events resend <event_id> --webhook-endpoint=<endpoint_id>` command. This
works for up to 30 days after the event creation.

### Event ordering

Stripe doesn’t guarantee the delivery of events in the order that they’re
generated. For example, creating a subscription might generate the following
events:

- `customer.subscription.created`
- `invoice.created`
- `invoice.paid`
- `charge.created` (if there’s a charge)

Make sure that your event destination isn’t dependent on receiving events in a
specific order. Be prepared to manage their delivery appropriately. You can also
use the API to retrieve any missing objects. For example, you can retrieve the
invoice, charge, and subscription objects with the information from
`invoice.paid` if you receive this event first.

### API versioning

The API version in your account settings when the event occurs dictates the API
version, and therefore the structure of an
[Event](https://docs.stripe.com/api/v1/events) sent to your destination. For
example, if your account is set to an older API version, such as 2015-02-16, and
you change the API version for a specific request with
[versioning](https://docs.stripe.com/api#versioning), the
[Event](https://docs.stripe.com/api/v1/events) object generated and sent to your
destination is still based on the 2015-02-16 API version. You can’t change
[Event](https://docs.stripe.com/api/v1/events) objects after creation. For
example, if you update a charge, the original charge event remains unchanged. As
a result, subsequent updates to your account’s API version don’t retroactively
alter existing [Event](https://docs.stripe.com/api/v1/events) objects.
Retrieving an older [Event](https://docs.stripe.com/api/v1/events) by calling
`/v1/events` using a newer API version also has no impact on the structure of
the received event. You can set test event destinations to either your default
API version or the latest API version. The
[Event](https://docs.stripe.com/api/v1/events) sent to the destination is
structured for the event destination’s specified version.

## Event destination status

Amazon EventBridge destinations have several statuses that describe their
readiness to receive events:

- **Active**: You have successfully associated the event destination with an
event bus. If you configure an EventBridge rule correctly, you receive the
events in your chosen event consumers.
- **Disabled**: Stripe isn’t sending events to Amazon EventBridge. Your
destination will be in this status either because you manually disabled it or
Stripe automatically disabled it due to an AWS misconfiguration.
- **Pending**: After the event destination successfully creates a partner event
source in AWS, you need to associate that event source with an event bus. The
destination remains in a pending state and won’t receive any events until you
make this association, at which point the status of the destination changes to
active.

## Event structure

EventBridge uses its own [event
structure](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html)
that wraps the Stripe `event` JSON object within a top-level `detail` field.

This example is a `customer.created` event payload from EventBridge:

```
{
 "version":"0",
 "id":"17e8dff5-d6cd-3770-ace9-aeac02b6ac3f",
 "detail-type":"customer.created",

"source":"aws.partner/stripe.com/ed_61PgtRTG5aTCIz98516PLsRGLISQK0Otk6FWKjBrcDia",
 "account":"506417113029",
 "time":"2024-03-07T18:27:56Z",
 "region":"us-west-2",
 "resources":[
```

See all 60 lines
## Support events types where Stripe waits for a response

Stripe sends most event types asynchronously; however, for certain event types,
Stripe waits for a response. The presence or absence of a response from the
event destination directly influences Stripe’s actions regarding these specific
event types.

Amazon EventBridge destinations offer limited support for event types that
require a response:

- You can’t subscribe to the `issuing_authorization.request` event type for
Amazon EventBridge destinations. Instead, set up a [webhook
endpoint](https://docs.stripe.com/webhooks) to subscribe to this event type. Use
`issuing_authorization.request` to authorize purchase requests in real-time.
This requires your destination to approve or decline requests by responding to
the event. EventBridge handles the response to Stripe before sending it to your
consumers. As a result, this destination type can’t use this event type to
authorize any payments.
- You can subscribe to `checkout_sessions.completed` when using Amazon
EventBridge. However, this doesn’t [handle redirect
behavior](https://docs.stripe.com/checkout/fulfillment#redirect-hosted-checkout)
when you embed [Checkout](https://docs.stripe.com/payments/checkout) directly in
your website or redirect customers to a Stripe-hosted payment page. Delivering a
`checkout_sessions.completed` event to Amazon EventBridge won’t affect redirect
behavior. To influence Checkout redirect behavior, process this event type with
a [webhook endpoint](https://docs.stripe.com/webhooks).

## Common architecture patterns with EventBridge and Stripe events

Consider the following architectural patterns when you use Amazon EventBridge
with Stripe:

- **Trigger serverless functions with Lambda to define business automations**:
Send Stripe events from EventBridge to Lambda to trigger serverless compute
functions, such as creating a shipping label after a payment succeeds.
- **Enable event monitoring with CloudWatch**: Send events from EventBridge to
CloudWatch Logs to store events as log data that you can interactively search
and analyze. Monitor usage patterns and errors with CloudWatch. Consider setting
up alerts for errors (for example, when an EventBridge rule is broken).
- **Trigger low and no code workflows with Step Functions**: Send events to a
StepFunction workflow that trigger your business scenarios, such as notifying
your customers that their trial is about to end.
- **Fan out events to internal systems with Simple Notification Service (SNS) or
Simple Queue Service (SQS)**: Send Stripe events to SNS or SQS to fan out Stripe
event data to your internal teams to make sure that they can own and process
them.

## See also

- [List of thin event
types](https://docs.stripe.com/api/v2/core/events/event-types)
- [List of snapshot event types](https://docs.stripe.com/api/events/)
- [Event destinations overview](https://docs.stripe.com/event-destinations)
- [Send events to webhook endpoints](https://docs.stripe.com/webhooks)

## Links

- [Developer settings](https://dashboard.stripe.com/settings/developers)
- [Amazon
EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [20 supported
targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html)
- [AWS Management
Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/learn-whats-new.html)
- [sandboxes](https://docs.stripe.com/sandboxes)
- [API](https://docs.stripe.com/api/v2/event-destinations)
- [Webhooks](https://dashboard.stripe.com/webhooks)
- [Connected accounts](https://docs.stripe.com/connect)
- [event types](https://docs.stripe.com/api/events/types)
- [AWS account
ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html)
- [AWS
region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [partner event
source](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EventSource.html)
- [event
bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
- [Partner event sources
page](https://console.aws.amazon.com/events/home#/partners)
- [event destination in
Workbench](https://docs.stripe.com/event-destinations/eventbridge#add-eventbridge-destination)
-
[rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)
- [Rules](https://console.aws.amazon.com/events/home#/events)
- [create a CloudWatch Logs
target](https://repost.aws/knowledge-center/cloudwatch-log-group-eventbridge)
- [common architecture
patterns](https://docs.stripe.com/event-destinations/eventbridge#common-architecture)
- [Stripe Shell](https://docs.stripe.com/stripe-shell/overview)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Stripe for VS Code](https://docs.stripe.com/stripe-vscode)
- [Stripe CLI](https://docs.stripe.com/cli/events/resend)
- [Event](https://docs.stripe.com/api/v1/events)
- [versioning](https://docs.stripe.com/api#versioning)
- [event
structure](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html)
- [webhook endpoint](https://docs.stripe.com/webhooks)
- [handle redirect
behavior](https://docs.stripe.com/checkout/fulfillment#redirect-hosted-checkout)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Lambda](https://aws.amazon.com/lambda/)
- [CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Step Functions](https://aws.amazon.com/step-functions/)
- [Simple Notification Service (SNS)](https://aws.amazon.com/sns/)
- [Simple Queue Service (SQS)](https://aws.amazon.com/sqs/)
- [List of thin event
types](https://docs.stripe.com/api/v2/core/events/event-types)
- [List of snapshot event types](https://docs.stripe.com/api/events/)
- [Event destinations overview](https://docs.stripe.com/event-destinations)