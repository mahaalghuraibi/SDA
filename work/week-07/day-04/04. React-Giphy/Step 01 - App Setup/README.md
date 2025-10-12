<img width="100%" src="https://i.imgur.com/7zglvQY.gif" />

# React Giphy Searcher
We are going to build a searchable interface for the [Giphy API](https://developers.giphy.com/) using React. 

# STEP 1 - Application Setup

Project setup - nothing new here!

1. Open your Terminal application and navigate to your `~/code/SDA-Ghazal/applications` directory. 

```bash
npm create vite@latest
```

1. **Choose a project name:**
   - Let's name it: `react_giphy`.

2. **Select a framework:**
   - Use the arrow keys to choose the `React` option and hit `Enter`.

3. **Select a variant:** 
   - Again, use the arrow keys to choose `JavaScript` and hit `Enter`.

4. **Configuring ESLint**

Before we begin, we need to adjust the ESLint configuration. Add the indicated rules to the `rules` object in your `eslint.config.js` file:

```javascript
    rules: {
      ...js.configs.recommended.rules,
      ...react.configs.recommended.rules,
      ...react.configs['jsx-runtime'].rules,
      ...reactHooks.configs.recommended.rules,
      'react/jsx-no-target-blank': 'off',
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
      'react/prop-types': 'off', // add this line
      'react/no-unescaped-entities': 'off', // add this line
    },
```

- `cd react_giphy`
- Install Node Modules to access Vite
- in zsh / bash / gitbash... `npm i`

1. **Clear `App.jsx`**

Open the `App.jsx` file in the `src` directory and replace its contents with the following:

```jsx
// src/App.jsx

export default function App() {

  return (
    <h1>Welcome to React Giphy</h1>
  );
}
```

6. **Running the development server**

To start the development server and view our app in the browser, we'll use the following command:

```bash
npm run dev
```

You should see that `Vite` is available on port number 5173:

```plaintext
localhost:5173
```

7. Add JSCONFIG file:

[VSCode JSConfig.json File Explanation](https://code.visualstudio.com/docs/languages/javascript#_javascript-projects-jsconfigjson)

This file serves to ensure it is clear to the project that the current folder and all sub-folders are part of the current javascript project. 

The point of creating and including this file is to ensure that your current javascript file can use intellisense. While this isn't that big of a loss if we do not have it, it does make a difference in ensuring we are accessing the files we wish to access. It just makes more sense and is easier to include it and have access to it. 

In the root of our project directory, let's include a `jsconfig.json` file. 


`jsconfig.json`:
```js
{
    "compilerOptions": {
        "module": "CommonJS",
        "target": "ES6"
    },
    "exclude": [
        "node_modules"
    ]
}
```

That's it! Adding that file and information should ensure that intellisense is good to go for your Vite / React

## Add JSCONFIG file:

[VSCode JSConfig.json File Explanation](https://code.visualstudio.com/docs/languages/javascript#_javascript-projects-jsconfigjson)

This file serves to ensure it is clear to the project that the current folder and all sub-folders are part of the current javascript project. 

The point of creating and including this file is to ensure that your current javascript file can use intellisense. While this isn't that big of a loss if we do not have it, it does make a difference in ensuring we are accessing the files we wish to access. It just makes more sense and is easier to include it and have access to it. 

In the root of our project directory, let's include a `jsconfig.json` file. 


`jsconfig.json`:
```js
{
    "compilerOptions": {
        "module": "CommonJS",
        "target": "ES6"
    },
    "exclude": [
        "node_modules"
    ]
}
```

8. That's it! Adding that file and information should ensure that intellisense is good to go for your Vite / React project.

