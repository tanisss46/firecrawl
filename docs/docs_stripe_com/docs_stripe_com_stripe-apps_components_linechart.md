# LineChart component for Stripe Apps

## A line chart visualizes data as a series of data points connected into a line.

SDK version8.x9.x
To add the `LineChart` component to your app:

```
import {LineChart} from '@stripe/ui-extension-sdk/ui';
```

The following shows a preview of the `LineChart` UI component:

Loading example...
```
const sales = [
 {
 date: 'Jan',
 sold: 1,
 },
 {
 date: 'Feb',
 sold: 4,
 },
 {
 date: 'Mar',
 sold: 2,
 },
 {
 date: 'Apr',
 sold: 3,
 },
];

return (
 <Box css={{width: 'fill'}}>
 <LineChart data={sales} x="date" y="sold" />
 </Box>
)
```

### LineChart props

PropertyType
`data`

Required
`{ [x: string]: any; }[]`

The data used to generate the chart.

`x`

Required
`string | number | Channel`

The property or accessor for the point on the x axis.

Related types:
[Channel](https://docs.stripe.com/stripe-apps/components/linechart#channel).

`y`

Required
`string | number | Channel`

The property or accessor for the point on the y axis.

Related types:
[Channel](https://docs.stripe.com/stripe-apps/components/linechart#channel).

`axis`

Optional
`("x" | "y" | "both" | "none") | undefined`

Determines whether to render labels and ticks for each axis.

`color`

Optional
`(string | number | Channel) | undefined`

Groups data by color based on a property or accessor.

Related types:
[Channel](https://docs.stripe.com/stripe-apps/components/linechart#channel).

`grid`

Optional
`("x" | "y" | "both" | "none") | undefined`

Determines whether to render grid lines for each axis.

`legend`

Optional
`boolean | undefined`

Determines whether to render the legend (when more than one item is present).

`tooltip`

Optional
`boolean | undefined`

Determines whether to render a tooltip when hovering over the chart.

`z`

Optional
`(string | number | Channel) | undefined`

Groups data based on a property or accessor.

Related types:
[Channel](https://docs.stripe.com/stripe-apps/components/linechart#channel).

### Channel

PropertyType
`domain`

Optional
`any[] | undefined`

`format`

Optional
`((Currency | UnitIdentifier) | ("capitalize" | { [x: string]: string; })) |
undefined`

Related types:
[Currency](https://docs.stripe.com/stripe-apps/components/linechart#currency),
[UnitIdentifier](https://docs.stripe.com/stripe-apps/components/linechart#unitidentifier).

`label`

Optional
`string | undefined`

`value`

Optional
`(string | number) | undefined`

### Currency

PropertyType
`currency`

Required
`'AED' | 'AFN' | 'ALL' | 'AMD' | 'ANG' | 'AOA' | 'ARS' | 'AUD' | 'AWG' | 'AZN' |
'BAM' | 'BBD' | 'BDT' | 'BGN' | 'BHD' | 'BIF' | 'BMD' | 'BND' | 'BOB' | 'BRL' |
'BSD' | 'BTN' | 'BWP' | 'BYN' | 'BZD' | 'CAD' | 'CDF' | 'CHF' | 'CLP' | 'CNY' |
'COP' | 'CRC' | 'CUC' | 'CUP' | 'CVE' | 'CZK' | 'DJF' | 'DKK' | 'DOP' | 'DZD' |
'EGP' | 'ERN' | 'ETB' | 'EUR' | 'FJD' | 'FKP' | 'GBP' | 'GEL' | 'GHS' | 'GIP' |
'GMD' | 'GNF' | 'GTQ' | 'GYD' | 'HKD' | 'HNL' | 'HRK' | 'HTG' | 'HUF' | 'IDR' |
'ILS' | 'INR' | 'IQD' | 'IRR' | 'ISK' | 'JMD' | 'JOD' | 'JPY' | 'KES' | 'KGS' |
'KHR' | 'KMF' | 'KPW' | 'KRW' | 'KWD' | 'KYD' | 'KZT' | 'LAK' | 'LBP' | 'LKR' |
'LRD' | 'LSL' | 'LYD' | 'MAD' | 'MDL' | 'MGA' | 'MKD' | 'MMK' | 'MNT' | 'MOP' |
'MRU' | 'MUR' | 'MVR' | 'MWK' | 'MXN' | 'MYR' | 'MZN' | 'NAD' | 'NGN' | 'NIO' |
'NOK' | 'NPR' | 'NZD' | 'OMR' | 'PAB' | 'PEN' | 'PGK' | 'PHP' | 'PKR' | 'PLN' |
'PYG' | 'QAR' | 'RON' | 'RSD' | 'RUB' | 'RWF' | 'SAR' | 'SBD' | 'SCR' | 'SDG' |
'SEK' | 'SGD' | 'SHP' | 'SLL' | 'SOS' | 'SRD' | 'SSP' | 'STN' | 'SYP' | 'SZL' |
'THB' | 'TJS' | 'TMT' | 'TND' | 'TOP' | 'TRY' | 'TTD' | 'TWD' | 'TZS' | 'UAH' |
'UGX' | 'USD' | 'UYU' | 'UZS' | 'VES' | 'VND' | 'VUV' | 'WST' | 'XAF' | 'XCD' |
'XOF' | 'XPF' | 'YER' | 'ZAR' | 'ZMW'`

### UnitIdentifier

PropertyType
`unit`

Required
`'acre' | 'bit' | 'byte' | 'celsius' | 'centimeter' | 'day' | 'degree' |
'fahrenheit' | 'fluid-ounce' | 'foot' | 'gallon' | 'gigabit' | 'gigabyte' |
'gram' | 'hectare' | 'hour' | 'inch' | 'kilobit' | 'kilobyte' | 'kilogram' |
'kilometer' | 'liter' | 'megabit' | 'megabyte' | 'meter' | 'mile' |
'mile-scandinavian' | 'milliliter' | 'millimeter' | 'millisecond' | 'minute' |
'month' | 'ounce' | 'percent' | 'petabyte' | 'pound' | 'second' | 'stone' |
'terabit' | 'terabyte' | 'week' | 'yard' | 'year' | `${'acre' | 'bit' | 'byte' |
'celsius' | 'centimeter' | 'day' | 'degree' | 'fahrenheit' | 'fluid-ounce' |
'foot' | 'gallon' | 'gigabit' | 'gigabyte' | 'gram' | 'hectare' | 'hour' |
'inch' | 'kilobit' | 'kilobyte' | 'kilogram' | 'kilometer' | 'liter' | 'megabit'
| 'megabyte' | 'meter' | 'mile' | 'mile-scandinavian' | 'milliliter' |
'millimeter' | 'millisecond' | 'minute' | 'month' | 'ounce' | 'percent' |
'petabyte' | 'pound' | 'second' | 'stone' | 'terabit' | 'terabyte' | 'week' |
'yard' | 'year'}-per-${'acre' | 'bit' | 'byte' | 'celsius' | 'centimeter' |
'day' | 'degree' | 'fahrenheit' | 'fluid-ounce' | 'foot' | 'gallon' | 'gigabit'
| 'gigabyte' | 'gram' | 'hectare' | 'hour' | 'inch' | 'kilobit' | 'kilobyte' |
'kilogram' | 'kilometer' | 'liter' | 'megabit' | 'megabyte' | 'meter' | 'mile' |
'mile-scandinavian' | 'milliliter' | 'millimeter' | 'millisecond' | 'minute' |
'month' | 'ounce' | 'percent' | 'petabyte' | 'pound' | 'second' | 'stone' |
'terabit' | 'terabyte' | 'week' | 'yard' | 'year'}``

## Using color

The `color` channel groups data:

Loading example...
```
const sales = [
 {
 date: 'Jan',
 sold: 1,
 product: 'tables',
 },
 {
 date: 'Jan',
 sold: 2,
 product: 'chairs',
 },
 {
 date: 'Feb',
 sold: 4,
 product: 'tables',
 },
 {
 date: 'Feb',
 sold: 6,
 product: 'chairs',
 },
 {
 date: 'Mar',
 sold: 2,
 product: 'tables',
 },
 {
 date: 'Mar',
 sold: 4,
 product: 'chairs',
 },
 {
 date: 'Apr',
 sold: 7,
 product: 'tables',
 },
 {
 date: 'Apr',
 sold: 9,
 product: 'chairs',
 },
];

return (
 <Box css={{width: 'fill'}}>
 <LineChart data={sales} x="date" y="sold" color="product" />
 </Box>
)
```

## Axis and value formatting

Instead of passing a string for an axis value, you can add richer formatting by
passing an object including the `value`, `label` and/or `format` properties.

PropertyType
`value`

`string | number`

The property name in the data set. Required.

`label`

`string`

The display text for the axis.

`format`

`object`

Format a number with one of the [supported currency
codes](https://raw.githubusercontent.com/unicode-org/cldr/main/common/validity/currency.xml)
for example `{currency: 'USD'}`, or a [supported
unit](https://tc39.es/proposal-unified-intl-numberformat/section6/locales-currencies-tz_proposed_out.html#sec-issanctionedsimpleunitidentifier)
such as `{unit: 'minute'}`. You can also create a compound unit with `-per-` in
between, such as `{unit: 'megabyte-per-hour'}`.

Loading example...
```
<Box css={{width: 'fill'}}>
 <LineChart
 data={[
 {
 date: 'January',
 sold: 10,
 },
 {
 date: 'February',
 sold: 41,
 },
 {
 date: 'March',
 sold: 22,
 },
 {
 date: 'April',
 sold: 38,
 },
 ]}
 x="date"
 y={{value: 'sold', label: 'Price', format: {currency: 'USD'}}}
 />
</Box>
```

## Domain

To set the minimum and maximum values of an axis, use the `domain` prop. For
example, if you always want the `y` axis to go from 0 to 10 (rather than
automatically adjusting to the data provided), add the `domain` property to your
configuration:

Loading example...
```
const sales = [
 {
 date: 'Jan',
 sold: 1,
 },
 {
 date: 'Feb',
 sold: 4,
 },
 {
 date: 'Mar',
 sold: 2,
 },
 {
 date: 'Apr',
 sold: 3,
 },
];

return (
 <Box css={{width: 'fill'}}>
 <LineChart
 data={sales}
 x="date"
 y={{value: 'sold', label: 'Sold', domain: [0, 10]}}
 />
 </Box>
)
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [supported currency
codes](https://raw.githubusercontent.com/unicode-org/cldr/main/common/validity/currency.xml)
- [supported
unit](https://tc39.es/proposal-unified-intl-numberformat/section6/locales-currencies-tz_proposed_out.html#sec-issanctionedsimpleunitidentifier)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)