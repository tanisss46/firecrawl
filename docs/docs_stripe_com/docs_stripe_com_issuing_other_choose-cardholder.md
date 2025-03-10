# Choose a cardholder type

## Learn how to select the best cardholder type for your use case.

When creating a [Cardholder
object](https://docs.stripe.com/api/#issuing_cardholder_object), you can specify
a type: either `individual` or `company`—you can’t change the type after you
create the cardholder. Setting a type is optional and defaults to individual if
none is specified.

You might have to collect additional information, depending on the cardholder
type you choose. For individual cardholders, you must provide first name and
last name, and proof of acceptance of [Authorized User
Terms](https://docs.stripe.com/issuing/cards/virtual/issue-cards#accept-authorized-user-terms).
This data isn’t required for company cardholders.

## Find your use case

Choosing a cardholder type depends on your use case. View your use case and
other program details from the [Card
programs](https://dashboard.stripe.com/settings/issuing/card-programs) page in
the Dashboard.

### Individual cardholders

Create *individual cardholders* if you’re issuing the card to an employee or
contractor of your business or to an owner, employee, or contractor of one of
your connected accounts.

This is the default and most common type.

Some example use cases for individual cardholders include:

- Building a new expense management product for small businesses where the
platform issues cards to employees or contractors of those small businesses
- Giving cards to your own employees to make purchases for your company
- Building a fleet card product that issues cards to drivers
- Running a platform that enables businesses to give cards to their employees
for disbursing employee benefits or perks

### Company cardholders

Create *company cardholders* if you’re issuing the card directly to an entity.

This type is less common, and may not be available depending on the use-case you
provided at onboarding. If you’re restricted, Stripe returns the `Cardholder
type must be individual` error.

Here are some example use cases for company cardholders:

- A platform that creates virtual cards to use programmatically for online
purchases with company funds and for its benefit. For example, purchasing
inventory for resale or paying for cloud services. The cards are *not* given to
individual employees for individual expenses (for example, expensing a business
lunch).
- A platform that creates cards assigned to a vehicle (like a rental car or
semi-truck). The cards stay with the vehicle at all times. Alternating drivers
use the card to refuel the vehicle. The card does not belong to any one
individual.

#### Caution

In some cases, you may not be able to create company cardholders, depending on
Stripe’s review of your use case at onboarding. If this restriction applies to
you, Stripe notifies you. You receive an error message if you try to create a
company cardholder and your account has this restriction.

## Changing cardholder type

After a cardholder has been created, you can’t change its type.

If you have linked a card to the cardholder, you can’t change who the cardholder
is.

If you haven’t linked any cards to the cardholder, you can create a new
cardholder with the correct type. In most cases, you don’t need to delete the
existing cardholder. But make sure that you assign the appropriate type to new
cardholders to avoid any potential disruption in service.

## Links

- [Cardholder object](https://docs.stripe.com/api/#issuing_cardholder_object)
- [Authorized User
Terms](https://docs.stripe.com/issuing/cards/virtual/issue-cards#accept-authorized-user-terms)
- [Card programs](https://dashboard.stripe.com/settings/issuing/card-programs)