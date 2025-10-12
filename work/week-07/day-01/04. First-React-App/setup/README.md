<h1>
  <span class="headline">Building Your First React App</span>
  <span class="subhead">Setup</span>
</h1>

## Setup

1. `npm create vite@latest project-name`
2. `Select a framework:` => `React`
3. `Select a variant` => `Javascript`
4. `Use rolldown-vite (Experimental)?:` => `No`
5. `Install with npm and start now?:` => `Yes`
6. Navigate to `localhost:5173` (check app is running)
7. `ctrl+c` => terminate running application
8. `cd project-name`
9. `npm i -D @types/react @types/react-dom` (helps with intellisense / autocomplete!)
10. `npm run dev` when ready to spin up your app!

## Configurations

### jsconfig.json
[VSCode JSConfig.json File Explanation](https://code.visualstudio.com/docs/languages/javascript#_javascript-projects-jsconfigjson)

This file serves to ensure it is clear to the project that the current folder and all sub-folders are part of the current javascript project. 

The point of creating and including this file is to ensure that your current javascript file can use intellisense. While this isn't that big of a loss if we do not have it, it does make a difference in ensuring we are accessing the files we wish to access. It just makes more sense and is easier to include it and have access to it. 

Add a `jsconfig.json` file in the main project folder

**jsconfig.json Settings Explained**

- **module: "ESNext"** → Uses modern ECMAScript module syntax. Best for Vite and ESM-based projects.  
- **target: "ES6"** → Compiles code targeting ES6-compatible browsers.  
- **jsx: "react-jsx"** → Enables IntelliSense for React JSX syntax and props.  
- **moduleResolution: "bundler"** → Makes module resolution behave like Vite/webpack instead of Node.  
- **baseUrl: "."** → Defines the project root for resolving imports (useful for aliases).  
- **paths: {}** → Lets you define custom path aliases for cleaner imports (empty for now).  
- **exclude: `["node_modules", "dist"]`** → Tells VSCode to ignore dependencies and build outputs.  


> Together, these settings enable **IntelliSense, autocomplete, and error checking** in VSCode for a smooth React + Vite development experience.


`jsconfig.json`:
```js
{
  "compilerOptions": {
    "module": "ESNext",               
    "target": "ES6",                   
    "jsx": "react-jsx",                
    "moduleResolution": "bundler",     
    "baseUrl": ".",
    "paths": {}
  },
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```

### Update: eslint.config.js

These changes make ESLint React-aware, enforce Hooks best practices, and reduce unnecessary warnings, providing a smoother development experience for students.

- **React & JSX support** → Adds `eslint-plugin-react` and its recommended rules to properly lint React components and JSX syntax.  
- **React Hooks rules** → Enforces best practices with `'react-hooks/rules-of-hooks'` (required) and `'react-hooks/exhaustive-deps'` (dependency warnings).  
- **`no-unused-vars` update** → Ignores variables starting with capital letters or underscores, useful for constants or components.  
- **Overrides and relaxations** → Turns off rules like `'react/prop-types'`, `'react/no-unescaped-entities'`, and `'react/jsx-no-target-blank'` to reduce friction for students.  
- **Settings** → Automatically detects the installed React version for proper linting.

```js
import js from "@eslint/js";
import reactPlugin from "eslint-plugin-react";

export default [
  {
    files: ["**/*.{js,jsx}"],
    languageOptions: { ecmaVersion: "latest", sourceType: "module" },
    plugins: { react: reactPlugin },
    rules: {
      'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
      ...js.configs.recommended.rules,
      ...reactPlugin.configs.recommended.rules,
      ...reactPlugin.configs["jsx-runtime"].rules,
      'react-hooks/rules-of-hooks': 'error',
      'react-hooks/exhaustive-deps': 'warn',
      'react/jsx-no-target-blank': 'off',
      'react/prop-types': 'off',
      'react/no-unescaped-entities': 'off'
    },
    settings: { react: { version: "detect" } }
  }
];
```

### Update App.jsx

Open the `App.jsx` file in the `src` directory and replace the contents of it with the following:

```jsx
// src/App.jsx

const App = () => {

  return (
    <h1>Hello, world!</h1>
  );
};

export default App;
```

### Test the development server

- `npm run dev`

You should see that `Vite` is available on port number 5173:

```plaintext
localhost:5173
``` 

###  Run Build for Production

- **Purpose:** Compiles your React + Vite project into optimized, production-ready files.  
- **What it does:**  
  - Bundles all JavaScript, CSS, and assets into the `dist` folder.  
  - Minifies and optimizes code for faster loading.  
  - Handles module resolution, path aliases, and JSX compilation.  
- **Result:** A set of static files that can be deployed to any web server or hosting service.

**Why you run `npm run build` during project setup:**

- **Verify the setup works:** Ensures Vite, React, JSX, and all configurations (like path aliases and ESLint rules) are correctly processed without errors.  
- **Catch issues early:** If there are syntax errors, misconfigured imports, or plugin problems, the build will fail, letting you fix them before development.  
- **Prepare for deployment:** Even in a dev setup, running a build confirms that your project can produce production-ready files when needed.

> Essentially, it’s a quick test that the entire project configuration is correct and functional.

```bash
npm run build
```