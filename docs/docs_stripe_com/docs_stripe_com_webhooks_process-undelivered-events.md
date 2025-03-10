# Process undelivered webhook events

## Learn how to manually process undelivered webhook events.

If your webhook endpoint temporarily can’t process events, Stripe [automatically
resends](https://docs.stripe.com/webhooks#automatic-retries) the undelivered
events to your endpoint for up to three days, increasing the time for your
webhook endpoint to eventually receive and process all events.

This guide explains how to speed up that process by manually processing the
undelivered events.

## List webhook events

Call the [List Events](https://docs.stripe.com/api/events/list) API with the
following parameters:

- `ending_before`: Specify an event ID that was sent just before the webhook
endpoint became unavailable.
- `types`: Specify the list of event types to retrieve.
- `delivery_success`: Set to `false` to retrieve events that were unsuccessfully
delivered to at least one of your webhook endpoints.

Stripe only returns events created in the last 30 days.

```
curl -G https://api.stripe.com/v1/events \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d ending_before=evt_001 \
 -d "types[]"="payment_intent.succeeded" \
 -d "types[]"="payment_intent.payment_failed" \
 -d delivery_success=false
```

By default, the response returns up to 10 events. To retrieve all events, use
[auto-pagination](https://docs.stripe.com/api/pagination/auto) after retrieving
the results.

```
events = Stripe::Event.list({
 ending_before: 'evt_001',
 types: ['payment_intent.succeeded', 'payment_intent.payment_failed'],
 delivery_success: false,
})

events.auto_paging_each do |event|
 # This function is defined in the next section
 process_event(event)
end
```

Using `ending_before` with auto-pagination returns events in chronological
order. This lets you process events in their created order.

## Process the events

Process only unsuccessfully processed events according to your own logic to
avoid processing a single event multiple times by, for example:

- Inadvertently running the script twice in a row
- Simultaneously running the script while Stripe automatically resends some of
the unprocessed events

```
def process_event(event)
 if is_processing_or_processed(event)
 puts "skipping event #{event.id}"
 else
 puts "processing event #{event.id}"
 mark_as_processing(event)

 # Process the event
 # ...

 mark_as_processed(event)
 end
end
```

Define the following functions that prevent processing duplication:

- `is_processing_or_processed` to check the event’s status in your database.
- `mark_as_processing` to update your database to mark the event as processing.
- `mark_as_processed` to update your database to mark the event as processed.

## Respond to automatic retries

Stripe still considers your manually preocessed events as undelivered, so
continues to automaticly retry them.

When your webhook endpoint receives an already processed event, ignore the event
and return a successful response to stop future retries.

```
require 'json'

# Using Sinatra
post '/webhook' do
 payload = request.body.read
 event = nil

 begin
 event = Stripe::Event.construct_from(
 JSON.parse(payload, symbolize_names: true)
 )
 rescue JSON::ParserError => e
 # Invalid payload
 status 400
 return
 end

 if is_processing_or_processed(event)
 puts "skipping event #{event.id}"
 else
 puts "processing event #{event.id}"
 mark_as_processing(event)

 # Process the event
 # ...

 mark_as_processed(event)
 end

 status 200
end
```

## Links

- [automatically resends](https://docs.stripe.com/webhooks#automatic-retries)
- [List Events](https://docs.stripe.com/api/events/list)
- [auto-pagination](https://docs.stripe.com/api/pagination/auto)