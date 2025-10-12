<h1>
  <span class="headline">Intro to React</span>
  <span class="subhead">JSX</span>
</h1>

**Learning objective:** By the end of this lesson, students will be introduced to the use of JSX in React.

## Markup with JSX

JSX is an HTML-like syntax extension of JavaScript. It allows you to write markup and logic together in a single file. Using it you can rapidly construct user interfaces without having to write more complicated JavaScript. This JSX is *transpiled* into more complex pure JavaScript which will ultimately result in HTML being rendered to the page. Because JSX resembles HTML, we can more easily visualize the UI it will create.

> 📚 *Transpiled* is when code is converted from one language of similar abstraction to another. In the case of JSX, it is converted to JavaScript.

## Syntax

This is what JSX looks like in the context of a component:

![Component anatomy](./assets/component-anatomy.png)

1. The function definition. Determines the name of the component.
2. The markup returned from the component. This is JSX, notice how similar it is to HTML!
3. The syntax used to render the component.
