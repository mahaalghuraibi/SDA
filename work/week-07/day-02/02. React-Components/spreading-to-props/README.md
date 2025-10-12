<h1>
  <span class="headline">React Components</span>
  <span class="subhead">Spreading to Props</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to use JavaScript's spread syntax to pass props

## JavaScript spread syntax

Earlier, we refactored `FounderListItem` to accept the `founder` object on `props`. This meant we could only access the properties of `founder` on `founder.something`. In some cases, this isn't ideal. When this is the case, JavaScript has a tool to simplify passing multiple `props` as a bundle - the spread operator  `...`.

The spread operator `...` in JavaScript is a convenient way to pass ***all the properties*** of an object as `props` to a React component.

```jsx
// src/App.jsx

const App = () => {
  return (
    <>
      <Navbar />
      <main>
        <h1>Welcome to Hyperbo.ly</h1>
        <h2>The future is firmly in front of us!</h2>
        <p>If you can't explain it to a fifth-grader, our product does it.</p>
      </main>
      <h2>Our Founders</h2>
      <ul>
        {founders.map((founder) => (
          <FounderListItem key={founder.id} {...founder} />
        ))}
      </ul>
    </>
  );
};
```

In the `App` component, when you use the spread operator for `{...founder}`, what you're doing is essentially taking each key-value pair from the `founder` object and passing them as separate props to the `FounderListItem` component.

When used with a component like `FounderListItem`, it allows us to maintain a clean and concise syntax while still being able to access each property within the component individually.

```jsx
// src/components/FounderListItem/FounderListItem.jsx

const FounderListItem = (props) => {
  return (
    <li>
      <h3>Hello, I'm {props.name} the {props.title}!</h3>
      <p>{props.credential}</p>
    </li>
  );
};
```

We could even destructure these items from props directly:

```jsx
// src/components/FounderListItem/FounderListItem.jsx

const FounderListItem = ({ name, title, credential }) => {
  return (
    <li>
      <h3>Hello, I'm {name} the {title}!</h3>
      <p>{credential}</p>
    </li>
  );
};
```

In the `FounderListItem` component, you can define concise parameters like `{name, title, credential}`. These directly correspond to the keys in the founder object. By using object destructuring, you can extract each of these properties from the `props` object.
