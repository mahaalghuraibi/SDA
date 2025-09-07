<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Setup</span>
</h1>

With your terminal open in the current lecture on Javascript Control Flow, we will create a new directory called `javascript-control-flow`, then enter this directory:

```bash
mkdir javascript-control-flow
cd javascript-control-flow
```

Then, create an `app.js` and an `index.html` file. These files will hold your work for this lecture:

```bash
touch index.html app.js
```

Open the `index.html` file and add HTML boilerplate by typing `!` and then hitting the `Tab` key. Then make use of the `app.js` file by adding this line inside the `<head>` tag:

```html
<script defer src="./app.js"></script>
```

With this setup complete, we'll have two methods at our disposal for executing the code we write in `app.js`:

- Open the `index.html` file in your browser and access the console output in your browser's dev tools.

- Use node to execute the `app.js` file directly by using this command in your terminal:

  ```bash
  node app.js
  ```

While either method is acceptable, you should use the same method as your instructor for simplicity.
