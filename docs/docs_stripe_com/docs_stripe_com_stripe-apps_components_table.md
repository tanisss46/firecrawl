# Table component for Stripe Apps

## Display a table using the Table component.

SDK version8.x9.x
To add the `Table` component to your app:

```
import {Table, TableBody, TableCell, TableFooter, TableHead, TableHeaderCell,
TableRow} from '@stripe/ui-extension-sdk/ui';
```

The following shows a preview of a `Table` component with a header, several rows
of data, and a footer:

Loading example...
```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <Table>
 <TableHead>
 <TableRow>
 <TableHeaderCell>Charge type</TableHeaderCell>
 <TableHeaderCell>Amount</TableHeaderCell>
 </TableRow>
 </TableHead>
 <TableBody>
 <TableRow>
 <TableCell>Setup fee</TableCell>
 <TableCell>$95.00</TableCell>
 </TableRow>
 <TableRow>
 <TableCell>Maintenance fee</TableCell>
 <TableCell>$50.45</TableCell>
 </TableRow>
 <TableRow>
 <TableCell>Extra storage space (per GB)</TableCell>
 <TableCell>$5.95</TableCell>
 </TableRow>
 <TableRow>
 <TableCell>Premium features</TableCell>
 <TableCell>$109.00</TableCell>
 </TableRow>
 </TableBody>
 <TableFooter>
 <TableRow>
 <TableCell>
 <Inline css={{font: 'heading'}}>Total</Inline>
 </TableCell>
 <TableCell>
 <Inline css={{font: 'heading'}}>$260.40</Inline>
 </TableCell>
 </TableRow>
 </TableFooter>
 </Table>
</Box>
```

### Table props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

## Sub-components

## TableBody

The `TableBody` component contains the rows and cells in a table.

### TableBody props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

## TableCell

The `TableCell` component contains one unit of information in a table
corresponding to a row and column.

### TableCell props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`align`

Optional
`("center" | "left" | "right") | undefined`

`colSpan`

Optional
`number | undefined`

`maxWidth`

Optional
`("auto" | "maximized" | "minimized" | number) | undefined`

`minWidth`

Optional
`("auto" | "maximized" | "minimized" | number) | undefined`

`rowSpan`

Optional
`number | undefined`

`vAlign`

Optional
`("baseline" | "bottom" | "middle" | "top") | undefined`

`width`

Optional
`("auto" | "maximized" | "minimized" | number) | undefined`

`wrap`

Optional
`boolean | undefined`

## TableFooter

The `TableFooter` component summarizes or aggregates the columns of information
contained in a table.

### TableFooter props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

## TableHead

The `TableHead` component describes the columns of information contained in a
table.

### TableHead props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

## TableHeaderCell

The `TableHeaderCell` component describes one column of information in a table.

### TableHeaderCell props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`align`

Optional
`("center" | "left" | "right") | undefined`

`colSpan`

Optional
`number | undefined`

`maxWidth`

Optional
`("auto" | "maximized" | "minimized" | number) | undefined`

`minWidth`

Optional
`("auto" | "maximized" | "minimized" | number) | undefined`

`rowSpan`

Optional
`number | undefined`

`vAlign`

Optional
`("baseline" | "bottom" | "middle" | "top") | undefined`

`width`

Optional
`("auto" | "maximized" | "minimized" | number) | undefined`

`wrap`

Optional
`boolean | undefined`

## TableRow

The `TableRow` component is an entry in a table composed of cells containing
information for each column.

### TableRow props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)