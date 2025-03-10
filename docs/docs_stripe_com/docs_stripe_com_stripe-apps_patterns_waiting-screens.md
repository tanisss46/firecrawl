# Waiting screens for Stripe Apps

## Learn how to use the waiting screen.

Keep users informed throughout the entire onboarding process and set clear
expectations of wait times and next steps with waiting screens.

## Before you begin

[Create an app](https://docs.stripe.com/stripe-apps/create-app).

## Suggested use

- If users navigate back to Stripe during the onboarding flow, keep them
informed about what’s happening. For example:

![A screen with a step to complete, supporting context, an action to complete,
and affordance to start
over](https://b.stripecdn.com/docs-statics-srv/assets/waiting-screens-01.9722e1605d31c8f01f2045f1a5587f33.png)

- Only add a call-to-action if it leads users to the next step of the onboarding
process, or to provide additional context they need to complete in the next
step.
- Keep language clear and concise. Avoid providing more context than what users
might actually require. For example:

![A screen that prompts users to complete an application or start
over](https://b.stripecdn.com/docs-statics-srv/assets/waiting-screens-02.1e3d5a7715a3911377a7c1b98575faef.png)

- If you must take users outside of Stripe to connect to your account (**not**
recommended), use a waiting screen that clearly communicates this transition.
For example:

![A screen that prompts users to finish onboarding or start
over](https://b.stripecdn.com/docs-statics-srv/assets/waiting-screens-03.d4038dfb4db72022ac2b627d863d9df8.png)

## Example

The following sample shows a waiting screen built in a `ContextView` component:

```
import {
 Box,
 Button,
 ContextView,
 Icon,
 Inline,
 Link,
} from "@stripe/ui-extension-sdk/ui";
const WaitingScreen = () => {
 return (
 <ContextView
 title="Finish onboarding"
 footerContent={
 <Box>
 <Button type="primary" css={{ width: "fill" }}>
 Finish onboarding
 </Button>
 <Box
 css={{
 marginTop: "small",
 textAlign: "center",
 stack: "x",
 alignX: "center",
 gap: "small",
 }}
 >
 <Box>Want to go back?</Box>
 <Link>Start over.</Link>
 </Box>
 </Box>
 }
 >
 <Box css={{ marginBottom: "xlarge" }}>
 <Inline
 css={{
 backgroundColor: "container",
 keyline: "neutral",
 borderRadius: "small",
 paddingX: "small",
 paddingTop: "small",
 paddingBottom: "xsmall",
 }}
 >
 <Icon name="clock" css={{ fill: "secondary" }} />
 </Inline>
 </Box>
 <Box>Please finish onboarding to SuperTodo.</Box>
 </ContextView>
 );
};
```

## Links

- [Create an app](https://docs.stripe.com/stripe-apps/create-app)