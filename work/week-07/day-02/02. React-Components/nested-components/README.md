<h1>
  <span class="headline">React Components</span>
  <span class="subhead">Nested Components</span>
</h1>

**Learning objective:** By the end of this lesson, learners will be able to break down a React component into smaller parts and understand the concept of passing `props` from a parent component to a grandchild component.

## Breaking the `App` into smaller components

Our web page's most modular, reusable parts have now been turned into components. Could we do more?

Let's explore how to refine our React components even further. We'll break our `Navbar` component into smaller components - specifically, individual `NavbarLink` components. This exercise will help us understand how to pass data through multiple levels of components in React.

## Refactor the `Navbar` list

While the items in the navbar are unlikely to change and are typically okay to hard-code, let's use the opportunity to practice this pattern of refactoring lists into separate components. The goal is to refactor the list of links in the `Navbar` to use the same mapping pattern as our list of founders.

Add the following array to `App.jsx` and practice passing it down as props into `Navbar`. Each object will represent a link with an `href` and `text`:

```jsx
// src/App.jsx

const navLinks = [
  { href: "/", text: "Home" },
  { href: "/about-us", text: "About Us" },
  { href: "/money-pit", text: "Investment Opportunities" },
  { href: "/the-fine-print", text: "Terms of Service" },
];

const App = () => {
  return (
    <>
      <Navbar links={navLinks} />
      {/* rest of the App components */}
    </>
  );
};
```

## 🎓 You Do

Create a new component, `NavbarLink`, which will be responsible for rendering a single navigation link. This component will receive the props `href` and `text` from the `Navbar` component.

## Render the `NavbarLink` components

Now, let's modify the `Navbar` component to accept the links `prop` and use it to render the individual `NavbarLink` components:

```jsx
// src/Navbar.jsx

import NavbarLink from '../NavbarLink/NavbarLink.jsx';

const Navbar = ({ links }) => {
  return (
    <nav id="top-navbar">
      {links.map((link, index) => (
        <NavbarLink key={index} href={link.href} text={link.text} />
      ))}
    </nav>
  );
};
```

Great Work! We've successfully passed our link data from the `App` component to the `Navbar` component and then to each `NavbarLink` component. This demonstrates a two-level `prop` passing pattern in React, where data flows from a parent component to a child and then to a grandchild component.

## How many is too many?

Was it necessary to refactor the static navbar list items into their components? Probably not! Just because you can make something into its own component doesn't mean you need to or should.

If repeated elements are based on dynamic, user-generated data, they should be separate components that accept `props`. If those elements are just static links, as in the `Navbar` example, they likely don't need separate components.

However, professional developer teams create component libraries that do precisely this: like in our app every link in the nav bar is now component with its own props, styling, and functionality. This could be useful if we wanted to show an icon next to these links or if we wanted to color one of them based on which one we are currently viewing.

This keeps things consistent no matter how large the app becomes. Suppose every developer uses the team's custom `<NavbarLink>` component instead of generic `<a>` elements. In that case, the team can benefit from modularized React components.

When joining a React dev team, you should expect to inherit a custom component library that the team uses throughout the application.
