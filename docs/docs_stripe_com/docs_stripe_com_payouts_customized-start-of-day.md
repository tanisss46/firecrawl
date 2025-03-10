# Customized start of day

## Set your start of day to make your automatic payouts reconciliation easier to track.

Stripe supports customized start of day for automatic
[payouts](https://docs.stripe.com/payouts) to group and send payments in your
local timezone with a “customized day” starting time. This makes payout
reconciliation easier to track as payouts contain payments processed in a day of
your timezone, versus payments processed in a UTC day.

For example, if a user in Singapore starts their customized day at midnight SGT
(Singapore Time), the payments they process from midnight SGT to the following
midnight SGT belong to the same day. If they start their day at 06:00 SGT,
payments collected between 06:00 SGT on a given day and 06:00 SGT the next day
are attributed to the given day.

Your default start of day is UTC midnight [except for some users in Asia-Pacific
(APAC)
markets](https://support.stripe.com/questions/default-start-of-day-for-asia-pacific-%28apac%29-payouts).
You can change your start of day to a time in the allowed range (usually between
midnight and morning) in your local timezone.

## Feature availability

Customized start of day is available in the following countries:

AustraliaHong KongIndiaIndonesiaJapanMalaysiaNew
ZealandPhilippinesSingaporeThailand
## Interested in this feature for the United States?

Access to Custom Start of Day is currently limited to US private beta users. To
get access, enter your email address below. We'll determine your eligibility,
and add you to the waiting list.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Change start of day

To change the start of day:

- In the Dashboard, navigate to **Settings** > **Business** > [Bank accounts and
currencies](https://dashboard.stripe.com/settings/payouts).
- In the **Start of day** section, change the default setting to your preferred
start of day.

![Start of day settings in the
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/payout-schedule-page-start-of-day-1.b11ce1ceac6e24873a3a5a2a68594ba3.png)

After you set the start of day, it doesn’t take effect immediately. The new
start of day only takes effect at the new time. For example, if your current
time is equivalent to 07:00 Asia/Singapore, and you set the start of day to
00:00 Asia/Singapore, this new start of day takes effect in 17 hours.

![Dashboard callout notifying when the new start of day takes
effect](https://b.stripecdn.com/docs-statics-srv/assets/payout-schedule-page-start-of-day-2.f64163c5eb39a0eb6c1f6757e50d73b7.png)

The settings at the time of the original transaction apply to the payout as
well. For example, if the settings at the time of the original transaction
indicate a 7-day payout timing, this rule applies to the payout regardless of
any later changes in time zones. Let’s say a merchant has a balance of 1000 USD.
500 USD is attributed to UTC Monday and 500 USD is attributed to UTC Tuesday. If
their start of the day changes to Singapore Time (SGT) on Wednesday, the 1000
USD balance is still assigned to UTC Monday and Tuesday, and the payout will be
processed on the next Monday and Tuesday under UTC, not SGT. Only the payments
created after the change to SGT will follow the new time zone in terms of payout
timing.

## Example

A restaurant merchant’s business hours are 10AM to 9PM PST, all the transactions
made before the start of business count towards the previous day because they’ve
chosen 10AM as their start of day. Assuming this merchant is on a daily
automatic payout plan and a 4 business day schedule, all transactions made
between 10AM PST Monday and 10AM PST Tuesday are grouped into Monday’s sales and
arrive in the merchant’s bank before the end of Friday in one payout.

## See also

- [Receiving payouts](https://docs.stripe.com/payouts)

## Links

- [payouts](https://docs.stripe.com/payouts)
- [except for some users in Asia-Pacific (APAC)
markets](https://support.stripe.com/questions/default-start-of-day-for-asia-pacific-%28apac%29-payouts)
- [privacy policy](https://stripe.com/privacy)
- [Bank accounts and currencies](https://dashboard.stripe.com/settings/payouts)