[Skip to main content](https://docs.vendure.io/guides/core-concepts/collections/#__docusaurus_skipToContent_fallback)

On this page

[`Collections`](https://docs.vendure.io/reference/typescript-api/entities/collection/) are used to categorize and organize your catalog. A collection
contains multiple product variants, and a product variant can belong to multiple collections. Collections can be nested to
create a hierarchy of categories, which is typically used to create a menu structure in the storefront.

![Collections](https://docs.vendure.io/assets/images/collections-20faee4362e958c1b33c40781deba17e.webp)

Collections are not _only_ used as the basis of storefront navigation. They are a general-purpose organization tool which can be used
for many purposes, such as:

- Creating a collection of "new arrivals" which is used on the homepage.
- Creating a collection of "best sellers" which is used to display a list of popular products.
- Creating a collection of "sale items" which is used to apply a discount to all products in the collection, via a promotion.

## Collection filters [​](https://docs.vendure.io/guides/core-concepts/collections/\#collection-filters "Direct link to Collection filters")

The specific product variants that belong to a collection are determined by the collection's [`CollectionFilters`](https://docs.vendure.io/reference/typescript-api/configuration/collection-filter/).
A collection filter is a piece of logic which is used to determine whether a product variant should be included in the collection. By default, Vendure
includes a number of collection filters:

- **Filter by facet values**: Include all product variants which have a specific set of facet values.
- **Filter by product variant name**: Include all product variants whose name matches a specific string.
- **Manually select product variants**: Allows manual selection of individual product variants.
- **Manually select products**: Allows manual selection of entire products, and then includes all variants of those products.

![Collection filters](https://docs.vendure.io/assets/images/collection-filters-20aaa0950798367037f8150142b0d5b3.webp)

It is also possible to create your own custom collection filters, which can be used to implement more complex logic. See the section on [creating a collection filter](https://docs.vendure.io/guides/core-concepts/collections/#creating-a-collection-filter) for more details.

### Filter inheritance [​](https://docs.vendure.io/guides/core-concepts/collections/\#filter-inheritance "Direct link to Filter inheritance")

When a collection is nested within another collection, the child collection can inherit the parent's collection filters. This means that the child collection
will _combine_ its own filters with the parent's filters.

![Filter inheritance](https://docs.vendure.io/assets/images/filter-inheritance-5eb61291b7dc96f43ebe2efcac6f8971.webp)

In the example above, we have a parent collection "Menswear", with a child collection "Mens' Casual". The parent collection has a filter which includes all
product variants with the "clothing" and "mens" facet values. The child collection is set to inherit the parent's filters, and has an additional filter which
includes all product variants with the "casual" facet value.

Thus, the child collection will include all product variants which have the "clothing", "mens" and "casual" facet values.

note

When filter inheritance is enabled, a child collection will contain a **subset** of the product variants of its parent collection.

In order to create a child collection which contains product variants _not_ contained by the parent collection, you must disable filter inheritance
in the child collection.

### Creating a collection filter [​](https://docs.vendure.io/guides/core-concepts/collections/\#creating-a-collection-filter "Direct link to Creating a collection filter")

You can create your own custom collection filters with the [`CollectionFilter`](https://docs.vendure.io/reference/typescript-api/configuration/collection-filter/) class. This class
is a [configurable operation](https://docs.vendure.io/guides/developer-guide/strategies-configurable-operations/#configurable-operations) where the specific
filtering logic is implemented in the `apply()` method passed to its constructor.

The `apply()` method receives an instance of the [TypeORM SelectQueryBuilder](https://typeorm.io/select-query-builder) which should have filtering logic
added to it using the `.andWhere()` method.

Here's an example of a collection filter which filters by SKU:

src/config/sku-collection-filter.ts

```codeBlockLines_e6Vv
import { CollectionFilter, LanguageCode } from '@vendure/core';

export const skuCollectionFilter = new CollectionFilter({
    args: {
        // The `args` object defines the user-configurable arguments
        // which will get passed to the filter's `apply()` function.
        sku: {
            type: 'string',
            label: [{ languageCode: LanguageCode.en, value: 'SKU' }],
            description: [\
                {\
                    languageCode: LanguageCode.en,\
                    value: 'Matches any product variants with an SKU containing this value',\
                },\
            ],
        },
    },
    code: 'variant-sku-filter',
    description: [{ languageCode: LanguageCode.en, value: 'Filter by matching SKU' }],

    // This is the function that defines the logic of the filter.
    apply: (qb, args) => {
        // Sometimes syntax differs between database types, so we use
        // the `type` property of the connection options to determine
        // which syntax to use.
        const LIKE = qb.connection.options.type === 'postgres' ? 'ILIKE' : 'LIKE';

        return qb.andWhere(`productVariant.sku ${LIKE} :sku`, {
            sku: `%${args.sku}%`
        });
    },
});

```

In the `apply()` method, the product variant entity is aliased as `'productVariant'`.

This custom filter is then added to the defaults in your config:

src/vendure-config.ts

```codeBlockLines_e6Vv
import { defaultCollectionFilters, VendureConfig } from '@vendure/core';
import { skuCollectionFilter } from './config/sku-collection-filter';

export const config: VendureConfig = {
    // ...
    catalogOptions: {
        collectionFilters: [\
            ...defaultCollectionFilters,\
            skuCollectionFilter\
        ],
    },
};

```

info

To see some more advanced collection filter examples, you can look at the source code of the
[default collection filters](https://github.com/vendure-ecommerce/vendure/blob/master/packages/core/src/config/catalog/default-collection-filters.ts).

- [Collection filters](https://docs.vendure.io/guides/core-concepts/collections/#collection-filters)
  - [Filter inheritance](https://docs.vendure.io/guides/core-concepts/collections/#filter-inheritance)
  - [Creating a collection filter](https://docs.vendure.io/guides/core-concepts/collections/#creating-a-collection-filter)