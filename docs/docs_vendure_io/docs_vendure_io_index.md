[Skip to main content](https://docs.vendure.io/#__docusaurus_skipToContent_fallback)

# Developer Documentation

Build better multichannel commerce experiences faster. Vendure is the headless commerce platform that is built to adapt to your needs. Not the other way round.

[Get Started](https://docs.vendure.io/guides/getting-started/installation/) [Learn Vendure](https://docs.vendure.io/guides/developer-guide/overview/) [API Reference](https://docs.vendure.io/reference/)

Playground - https://readonlydemo.vendure.io/shop-api

{"version":"1.7.42","settings":{"request.credentials":"include"},"canSaveConfig":false}

New Tab

Close Tab

Opens a New Tab

PrettifyHistory

Copy CURL

```
xxxxxxxxxx
```

22

1

```
query GetProductList {
```

2

```
  products(
```

3

```
    options: {
```

4

```
      take: 10
```

5

```
      filter: { name: { contains: "shoe" } }
```

6

```
      sort: { name: ASC }
```

7

```
    }
```

8

```
  ) {
```

9

```
    totalItems
```

10

```
    items {
```

11

```
      id
```

12

```
      name
```

13

```
      slug
```

14

```
      featuredAsset {
```

15

```
        preview
```

16

```
        mimeType
```

17

```
        width
```

18

```
        height
```

19

```
      }
```

20

```
    }
```

21

```
  }
```

22

```
}
```

Query VariablesHTTP Headers

```
xxxxxxxxxx
```

1

```
​
```

```
xxxxxxxxxx
```

```
​
```

Hit the Play Button to get a response here

TracingQuery Plan

This GraphQL server either doesn't support Apollo Federation, or the query plan extensions is disabled. See the [docs](https://www.apollographql.com/docs/apollo-server/federation/introduction) for setting up query plan viewing with Apollo Federation.

Docs

Schema

Settings