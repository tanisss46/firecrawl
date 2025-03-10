# Sparkline component for Stripe Apps

## A type of line chart to display data succinctly as a simple line.

SDK version8.x9.x
To add the `Sparkline` component to your app:

```
import {Sparkline} from '@stripe/ui-extension-sdk/ui';
```

The following shows a preview of the `Sparkline` UI component:

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
 <Sparkline data={sales} x="date" y="sold" />
 </Box>
)
```

### Sparkline props

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
[Channel](https://docs.stripe.com/stripe-apps/components/sparkline#channel).

`y`

Required
`string | number | Channel`

The property or accessor for the point on the y axis.

Related types:
[Channel](https://docs.stripe.com/stripe-apps/components/sparkline#channel).

`color`

Optional
`(string | number | Channel) | undefined`

Groups data by color based on a property or accessor.

Related types:
[Channel](https://docs.stripe.com/stripe-apps/components/sparkline#channel).

`tooltip`

Optional
`boolean | undefined`

Determines whether to render a tooltip when hovering over the chart.

`z`

Optional
`(string | number | Channel) | undefined`

Groups data based on a property or accessor.

Related types:
[Channel](https://docs.stripe.com/stripe-apps/components/sparkline#channel).

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
[Currency](https://docs.stripe.com/stripe-apps/components/sparkline#currency),
[UnitIdentifier](https://docs.stripe.com/stripe-apps/components/sparkline#unitidentifier).

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
 <Sparkline data={sales} x="date" y="sold" color="product" />
 </Box>
)
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)