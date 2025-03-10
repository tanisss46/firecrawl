# Using roles in UI extensions

## Learn how to include user roles in UI Extensions to tailor functionality to different roles.

Stripe Apps UI extensions can read the active user’s role in the Dashboard. Apps
can expose different functionality to different user roles.

The UI Extension SDK provides valuable information about the end user of your
app. The `roles` field of the `userContext` object gives a list of the active
user’s roles. You can tailor the app’s content based on the user’s role, using
the roles in the user context.

## How to determine the user’s Dashboard role

Extensions have a `userContext` prop that’s populated with information about the
active Dashboard user. This object has a `roles` field, which is an array of
`RoleDefinition` objects for each role that the active user is attributed to.

A role definition has these fields:

Field nameTypeExampletype‘builtIn’ | ‘custom’builtInSpecifies the role type.
Custom roles are only available to [private
apps](https://docs.stripe.com/stripe-apps/distribution-options#share-with-team-members).namestringDeveloperThe
name of the user role.
The name field provides the name of the user role, and you can use it to modify
the functionality of your UI Extension.

## Custom user roles (private apps only)

Each role definition has a type field, which specifies the role type. The type
field can either be ‘builtIn’ or ‘custom’. Because custom roles are specific to
a given account, these roles are only available for private apps.

## Tailoring content based on the Dashboard role

A common use of this information is to conditionally display content based on
the user role. Below is an example app that shows content tailored to particular
user roles.

```
import { Badge, Box, Inline, ContextView } from "@stripe/ui-extension-sdk/ui";
import type { ExtensionContextValue } from "@stripe/ui-extension-sdk/context";

const App = ({ userContext }: ExtensionContextValue) => {
const isAdmin = userContext?.roles?.some(role => role.name === 'Administrator');
const isDeveloper = !isAdmin && userContext?.roles?.some(role => role.name ===
'Developer');
 const isaAnotherRole = !isDeveloper && !isAdmin;

 return (
 <ContextView
 title="Role based access"
 >
 <Box>
<Box css={{ paddingBottom: 'large'}}>Active user roles:
{userContext?.roles?.map(role => <Badge
key={role.name}>{role.name}</Badge>)}</Box>

{ isAdmin && (<Box>Only <Inline css={{ fontWeight: 'semibold' }}>admin</Inline>
users can see this message.</Box>) }
{ isDeveloper && (<Box>Only <Inline css={{ fontWeight: 'semibold'
}}>developers</Inline> users can see this message.</Box>) }
{ isaAnotherRole && (<Box>Only users who are not admins or developers can see
this message.</Box>) }
 </Box>
 </ContextView>
 );
};

export default App;

```

![A screenshot of the result of the example code above for an Administrator
user](https://b.stripecdn.com/docs-statics-srv/assets/roles-example.7fb1048ac4656aee8a39a33d9179ad26.png)

The result of the example app when viewing the app as an Administrator user

## See also

- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)
- [Extension SDK API
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)
- [User roles](https://docs.stripe.com/get-started/account/teams/roles)

## Links

- [private
apps](https://docs.stripe.com/stripe-apps/distribution-options#share-with-team-members)
- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)
- [Extension SDK API
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)
- [User roles](https://docs.stripe.com/get-started/account/teams/roles)