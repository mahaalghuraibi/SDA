<h1>
  <span class="headline">Intro to CSS</span>
  <span class="subhead">Setup</span>
</h1>

Open your Terminal application and navigate to your `SDA-SIRAJ/work/week-01/day-02/04. Intro-to-CSS` directory:

Make a new directory called `intro-to-css`, then enter this directory:

```bash
mkdir intro-to-css
cd intro-to-css
```

Then, create an `index.html` file, and a `./css/style.css`.</br>
These files will hold your work for this lecture:

```bash
touch index.html ./css/style.css
```

Open the `index.html` file and add HTML boilerplate by typing `!` and then hitting the `Tab` key. Then make use of the `style.css` file by adding this line inside the `<head>` tag:

```html
<link rel="stylesheet" href="./css/style.css">
```

Replace the existing `<body>` tag with the following:

```html
<body>
  <h1>Intro to CSS</h1>
  <p id="about">More About CSS</p>
  <div>This is a DIV</div>
  <div class="important">This is another DIV</div>
  <div class="important super-cool">
    <p>This is a paragraph inside of the third DIV</p>
  </div>
  <a href="https://github.com">Visit GitHub</a>

  <div id="comments">
    <h2>Comments</h2>
    <ul>
      <li>Comment One</li>
      <li class="super-cool">Comment Two</li>
    </ul>
    <button>This button does nothing</button>
  </div>

  <footer>Here's a footer</footer>
</body>
```

Open the `index.html` file in your browser.
