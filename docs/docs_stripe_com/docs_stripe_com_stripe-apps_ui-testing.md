# UI testing

## Test your Stripe app UI with a set of utilities and helpers.

The Extension SDK includes a set of tools to write unit tests for your app’s
user interface. We recommend running tests with [Jest](https://jestjs.io/) and
we include [Jest custom
matchers](https://docs.stripe.com/stripe-apps/ui-testing#matchers) to help with
writing assertions.

## Conceptual overview

When testing your Stripe app’s UI, you’re testing a remote engine that renders
your app, not the Document Object Model (DOM) tree directly.

For security purposes, the React code in your Stripe app repository is
serialized, sent through an extension loader using an iframe, and translated
into a DOM tree within the Stripe Dashboard. The testing tools provided by the
Extension SDK work with the remote rendering engine.

## Example

This example tests a
[Button](https://docs.stripe.com/stripe-apps/components/button) UI component
that changes text when clicked. In the test, we render the button, confirm that
the initial button text is correct, click the button, and confirm that the text
of the button has changed.

```
// App.tsx
import {useState} from 'react';
import {ContextView, Button} from '@stripe/ui-extension-sdk/ui';

const App = () => {
 const [isPressed, setIsPressed] = useState(false);
 return (
 <ContextView title="Hello world">
 <Button onPress={() => setIsPressed(true)}>
 {isPressed ? 'You pressed me!' : 'Press me'}
 </Button>
 </ContextView>
 );
};

export default App;

// App.test.tsx
import {render} from '@stripe/ui-extension-sdk/testing';
import {Button} from '@stripe/ui-extension-sdk/ui';
import App from './App';

describe('App', () => {
 it('changes button text when pressed', async () => {
 const {wrapper, update} = render(<App />);

 // Expect that the initial text is correct
 expect(wrapper.find(Button)).toContainText('Press me');

 // Press the button
 wrapper.find(Button)!.trigger('onPress');

 // This is needed if the "onPress" handler involves something asyncronous
 // like a promise or a React useEffect hook
 await update();

 // Expect that the text changed
 expect(wrapper.find(Button)).toContainText('You pressed me!');
 });
});
```

## Rendering a component

### `render(element: React.ReactElement)`

The `render` method accepts a React element and returns an object with the
following properties:

- `wrapper`: The root element of the component passed to `render`.
- `update`: A function that returns a promise that resolves after the JavaScript
event stack has been cleared. This is useful when mocking APIs, dealing with
promises, employing React hooks such as `useEffect`, or ensuring asynchronous
rendering completes before running subsequent test cases.

```
import {render} from '@stripe/ui-extension-sdk/testing';
import App from './App';

it('contains a Button', async () => {
 const {wrapper, update} = render(<App />);

 await update();

 // Continue testing...
});
```

## Element properties and methods

When working with the wrapper or any element within it, use the following
properties and methods to assess state and interact with your app:

### children: Element<unknown>[]

Returns an array of the direct children of the element.

### descendants: Element<unknown>[]

Returns an array of all elements below the element in the tree.

### debug(options?: {all?: boolean, depth?: number, verbosity?: number}): string

Returns a text representation of the element. You can modify `debug()` output
using the `options` parameter.

- `all` overrides the default props filtering behavior and instead includes all
props in the output. `debug()` omits `className`, `aria-*`, and `data-*` props
by default.
- `depth` defines the number of children printed. All children are printed by
default.
- `verbosity` defines the level of expansion for non-scalar props. The default
value of `1` expands objects one level deep.

### act<T>(action: () => T): T

Performs an action in the context of a React [act()
block](https://reactjs.org/docs/test-utils.html#act). Normally, you can use
`update()` (which uses `act()` internally) to handle asynchronous events.
However, in some cases you might need to call `act()` directly, such as when
your code uses timers (`setTimeout`, `setInterval`, `clearTimeout`,
`clearInterval`), and you want to test using [timer
mocks](https://jestjs.io/docs/timer-mocks). When using timer mocks, you need to
reset or cleanup mocks between tests (in jest this means calling
`runOnlyPendingTimers()` and `useRealTimers()`), otherwise library code that
uses timers won’t work properly.

### find(type: Type, props?: Partial<PropsForComponent<Type>>): Element<PropsForComponent<Type>> | null

Finds a descendant element that matches `type`, where `type` is a component. If
it doesn’t find a matching element, it returns null. If it finds a match, the
returned element has the correct prop typing, which provides excellent type
safety while navigating the React tree.

If the second `props` argument is passed, it finds the first element of `type`
with matching `props`.

```
// App.tsx
import {Button, ContextView} from '@stripe/ui-extension-sdk/ui';

const App = () => (
 <ContextView title="Hello world">
 <Button href="http://bad.example.com">Do not press me</Button>
 <Button href="http://example.com">Press me</Button>
 </ContextView>
);

export default App;

// App.test.tsx
import {render} from '@stripe/ui-extension-sdk/testing';
import {Button} from '@stripe/ui-extension-sdk/ui';
import App from './App';

it('contains a Button with text', () => {
 const {wrapper} = render(<App />);

 const button = wrapper.find(Button, {href: 'http://example.com'});

 expect(button).toContainText('Press me');
});
```

Be aware that when using any of the `findX` methods, saved results are
immediately stale and future updates to the component aren’t reflected. For
example:

```
// Bad - this will not work
const button = wrapper.find(Button);
expect(button).toContainText('Press me');
button!.trigger('onPress');
expect(button).toContainText('You pressed me!'); // button still contains 'Press
me'

// Good - this will work
expect(wrapper.find(Button)).toContainText('Press me');
wrapper.find(Button)!.trigger('onPress');
expect(wrapper.find(Button)).toContainText('You pressed me!');
```

### findAll(type: Type, props?: Partial<PropsForComponent<Type>>): Element<PropsForComponent<Type>>[]

Like `find`, but returns all matches as an array.

### findWhere<Type = unknown>(predicate: (element: Element<unknown>) => boolean): Element<PropsForComponent<Type>> | null

Finds the first descendant component matching the passed function. The function
is called with each element from `descendants` until it finds a match. If it
doesn’t find a match, it returns `null`.

`findWhere` accepts an optional TypeScript argument that you can use to specify
the type of the returned element. If you omit the generic argument, the returned
element has unknown props, so calling `.props` and `.trigger` on it causes type
errors, as those functions don’t know what props are valid on your element:

```
// App.tsx
import {Button, ContextView} from '@stripe/ui-extension-sdk/ui';

const App = () => (
 <ContextView title="Hello world">
 <Button href="http://example.com">Press me</Button>
 </ContextView>
);

export default App;

// App.test.tsx
import {render} from '@stripe/ui-extension-sdk/testing';
import {Button} from '@stripe/ui-extension-sdk/ui';
import App from './App';

it('contains a Button with a href', () => {
 const {wrapper} = render(<App />);

 const button = wrapper.findWhere<typeof Button>(
 (node) => node.is(Button) && node.prop('href').startsWith('http://example'),
 );

 expect(button).toContainText('Press me');
});
```

### findAllWhere<Type = unknown>(predicate: (element: Element<unknown>) => boolean): Element<PropsForComponent<Type>>[]

Like `findWhere`, but returns all matches as an array.

### is(type: Type): boolean

Returns a boolean indicating whether the component type matches the passed type.
This function also serves as a type guard, so subsequent calls to values like
`props` are typed as the prop type of the passed component.

```
import {Button} from '@stripe/ui-extension-sdk/ui';

// If we omit element.is here, we would not know whether 'href' was a valid prop
and Typescript
// would throw an error.
if (element.is(Button) && element.prop('href') === 'http://example.com') {
 // ...
}
```

### prop<K extends keyof Props>(key: K): Props[K]

Returns the current value of the passed prop name.

### props: Props

All props of the element.

### text: string

The text content of the element (that is, the string you would get by calling
`textContent`).

### trigger<K extends FunctionKeys<Props>>(prop: K, …args: Arguments<Props<K>>): ReturnType<Props<K>>

Simulates a function prop being called on your component. This is usually the
key to effective testing. After you mount your component, you simulate a change
in a subcomponent and assert that the resulting tree is in the expected state.

Optionally, each additional argument passed to `trigger` is passed to the
function. This is useful for testing components in isolation.

```
// App.tsx
import {useState} from 'react';
import {ContextView, Button} from '@stripe/ui-extension-sdk/ui';

const App = () => {
 const [buttonText, setButtonText] = useState<string>('Press me');
 return (
 <ContextView title="Hello world">
 <Button onPress={() => setButtonText('You pressed me!')}>
 {buttonText}
 </Button>
 </ContextView>
 );
};

export default App;

// App.test.tsx
import {render} from '@stripe/ui-extension-sdk/testing';
import {Button} from '@stripe/ui-extension-sdk/ui';
import App from './App';

describe('App', () => {
 it('changes button text when pressed', () => {
 const {wrapper} = render(<App />);

 expect(wrapper.find(Button)).toContainText('Press me');

 // Press the button
 wrapper.find(Button)!.trigger('onPress', 'You pressed me!');

 // Expect that the text changed
 expect(wrapper.find(Button)).toContainText('You pressed me!');
 });
});
```

### triggerKeypath<T>(keypath: string, …args: any[]): T

Like `trigger()`, but allows you to provide a keypath referencing nested
objects. Be aware that limitations in TypeScript prevent the same kind of
type-safety that `trigger` guarantees.

```
const App = ({action}: {action: {onAction(): void; label: string}}) => (
 <Button type="button" onPress={action.onAction}>
 {action.label}
 </Button>
);

const spy = jest.fn();
const app = mount(
 <App action={{label: 'Hi', onAction: spy}} />,
);
app.triggerKeypath('action.onAction');
expect(spy).toHaveBeenCalled();
```

## Matchers

The Extension SDK provides [Jest custom
matchers](https://jestjs.io/docs/using-matchers). These are imported
automatically when you import `@stripe/ui-extension-sdk/testing`.

### toContainComponent(type: RemoteComponentType, props?: object)

Asserts that at least one component matching `type` is in the descendants of the
passed node. If the second `props` argument is passed, it further filters the
matches by components whose props are equal to the passed object. Jest’s
asymmetric matchers, like `expect.objectContaining`, are fully supported.

```
// App.tsx
import {Button, ContextView} from '@stripe/ui-extension-sdk/ui';

const App = () => (
 <ContextView title="Hello world">
 <Button onPress={() => console.log('You pressed me!')}>Press me</Button>
 </ContextView>
);

export default App;

// App.test.tsx
import {render} from '@stripe/ui-extension-sdk/testing';
import {Button} from '@stripe/ui-extension-sdk/ui';
import App from './App';

it('contains a Button', () => {
 const {wrapper} = render(<App />);

 expect(wrapper).toContainComponent(Button, {
 onPress: expect.any(Function),
 });
});
```

### toContainComponentTimes(type: RemoteComponentType, times: number, props?: object)

Identical to `.toContainComponent`, but asserts that there are exactly `times`
matches within the passed node.

### toHaveProps(props: object)

Checks whether the node has the specified props.

```
// App.tsx
import {Button, ContextView} from '@stripe/ui-extension-sdk/ui';

const App = () => (
 <ContextView title="Hello world">
 <Button onPress={() => console.log('You pressed me!')}>Press me</Button>
 </ContextView>
);

export default App;

// App.test.tsx
import {render} from '@stripe/ui-extension-sdk/testing';
import {Button} from '@stripe/ui-extension-sdk/ui';
import App from './App';

it('contains a Button with an onPress function', () => {
 const {wrapper} = render(<App />);

 expect(wrapper.find(Button)).toHaveProps({
 onPress: expect.any(Function),
 });
});
```

### toContainText(text: string)

Checks that the rendered output of the component contains the passed string as
text content (that is, the text is included in what you would get by calling
`textContent` on all DOM nodes rendered by the component).

```
// App.tsx
import {Button, ContextView} from '@stripe/ui-extension-sdk/ui';

const App = () => (
 <ContextView title="Hello world">
 <Button>Press me</Button>
 </ContextView>
);

export default App;

// App.test.tsx
import {render} from '@stripe/ui-extension-sdk/testing';
import {Button} from '@stripe/ui-extension-sdk/ui';
import App from './App';

it('contains a Button with an onPress function', () => {
 const {wrapper} = render(<App />);

 expect(wrapper.find(Button)).toContainText('Press me');
});
```

## Mock context props

App views are passed [context
props](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#props)
in the Stripe Dashboard. You can generate a mock context props object for
testing purposes using the `getMockContextProps` function.

```
import {getMockContextProps} from '@stripe/ui-extension-sdk/testing';

const context = getMockContextProps();
const {wrapper} = render(<App {...context} />);
```

By default, the mock context props are standard test values like `id:
'usr_1234'` and `email: 'user@example.com'`. You can override these values by
passing in a partial object. The object you pass in is deep-merged with the
default object, so you only need to pass in the values you want to override.

```
import {getMockContextProps} from '@stripe/ui-extension-sdk/testing';

const context = getMockContextProps({
 environment: {
 objectContext: {
 id: 'inv_1234',
 object: 'invoice',
 },
 },
});
const {wrapper} = render(<App {...context} />);
```

## See also

- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [UI extension SDK
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)
- [UI components](https://docs.stripe.com/stripe-apps/components)

## Links

- [Jest](https://jestjs.io)
- [Button](https://docs.stripe.com/stripe-apps/components/button)
- [act() block](https://reactjs.org/docs/test-utils.html#act)
- [timer mocks](https://jestjs.io/docs/timer-mocks)
- [http://bad.example.com](http://bad.example.com)
- [http://example.com](http://example.com)
- [http://example](http://example)
- [Jest custom matchers](https://jestjs.io/docs/using-matchers)
- [context
props](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#props)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [UI extension SDK
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)
- [UI components](https://docs.stripe.com/stripe-apps/components)