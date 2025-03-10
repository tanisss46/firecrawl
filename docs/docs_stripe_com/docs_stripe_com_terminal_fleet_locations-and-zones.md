# Manage locations

## Group and manage your readers by physical location.

You can streamline the management of multiple readers across different physical
sites by using locations and zones.

Locations and zones help by associating each reader with specific operational
sites and guarantee that the correct regional configurations are downloaded.

- **Locations**: Allows you to group readers, monitor their connectivity status,
and modify your settings based on physical location. This functionality is
beneficial for marketplaces with multiple connected accounts.
- **Zones**: Offers an optional method to further categorize locations and
readers. Zones enable you to represent broader groups of readers or locations,
such as larger geographic regions (for example, countries) or organizational
sub-brands. Multiple locations can belong to a single zone, and you can create a
hierarchical structure by grouping multiple zones under a single zone.

#### Note

Zones provide an additional way to group locations. You must still assign
readers to a location, and you can assign a location to only one zone.

North America Zone

California Zone

Washington Zone

Bay Area Zone

SFO Location

Terminal 1 Reader

Terminal 2 Reader

Seattle Location

San Francisco Location

Checkout 1 Reader

Checkout 2 Reader

Example organization strategy
## Locations

You can create a location for each physical place where your readers operate.
You can [register](https://docs.stripe.com/terminal/fleet/register-readers)
multiple readers to each location, and nest these locations within zones. Before
you can use a reader, you must register it to a location.

The required [address
properties](https://docs.stripe.com/api/terminal/locations/create#create_terminal_location-address)
for a location vary by country:

CountriesRequired Address PropertiesAustraliaCanadaItalySpainUnited
States`line1`, `city`, `state`, `postal_code`, and `country`AustriaBelgiumCzech
RepublicDenmarkFinlandFranceGermanyLuxembourgMalaysiaNetherlandsNew
ZealandNorwayPoland+PortugalSwedenSwitzerlandUnited Kingdom`line1`, `city`,
`postal_code`, and `country`IrelandSingapore`line1`, `postal_code`, and
`country`+Terminal is currently in beta in this country.**Compatibility for this
mobile SDK also applies when used with React Native.
#### Common mistake

You can use the Dashboard or API to update a `Location` object. After you create
a location, you can’t change its country. Instead, create a new location in the
new country, and then re-register any readers associated with the old location.

## Zones

Zones are the top-level groups that can consist of either more zones or
locations. You can add more zones nested under an existing one, creating
additional hierarchy levels, such as “West coast.” However, organizing your
locations into zones is optional.

## Create locations and zones

DashboardAPI
First, you must [register your reader to a
location](https://docs.stripe.com/terminal/fleet/register-readers?dashboard-or-api=dashboard)
to accept payments. You can manage your locations and zones in the [Manage
locations](https://dashboard.stripe.com/terminal/locations) page. To open this
page from the Terminal reader page, click the **Manage locations** button on the
Readers tab.

### Create a location

To create a location:

- Click the overflow menu () on the **All locations** row, then click **Create
location**.
- Enter a name and a valid address. Providing an address ensures that the
correct configuration and settings are applied based on the region where the
readers are operating.
- Click **Done**.

You can also create a specific
[configuration](https://docs.stripe.com/terminal/fleet/configurations-overview)
for that location.

### Create a zone

To create a zone:

- Click the overflow menu () on the **All locations** row, then click **Create
zone**.
- Enter a name.
- Click **Done**.

### Create a nested zone

To create a nested zone:

- Click the overflow menu () on the zone for which you want to create a nested
zone, then click **Create zone**.
- Enter a name.
- Click **Done**.

### Add or move a location to a zone

To add or move a location to a zone:

- Click the overflow menu () on the location, then click **Move location**.
- Choose the zone or nested zone where you want to move the location.
- Click **Done**.

### Delete a location

To delete a location, you must remove the readers associate with it:

- Remove all readers from the location in which you want to delete.
- Click the overflow menu () on the location, then click **Delete location**.
- Click **Yes, delete location**.

### Delete a zone

To delete a zone, you must remove the readers associate with it:

- Remove all readers from the location you want to delete, and remove all
locations under the zones.- (Optional) Move the locations with readers to a
different zone.
- Click the overflow menu () on the zone, then click **Delete zone**.
- Click **Yes, delete zone**.

## Links

- [register](https://docs.stripe.com/terminal/fleet/register-readers)
- [address
properties](https://docs.stripe.com/api/terminal/locations/create#create_terminal_location-address)
- [register your reader to a
location](https://docs.stripe.com/terminal/fleet/register-readers?dashboard-or-api=dashboard)
- [Manage locations](https://dashboard.stripe.com/terminal/locations)
-
[configuration](https://docs.stripe.com/terminal/fleet/configurations-overview)