<img width="100%" src="https://i.imgur.com/7zglvQY.gif" />

# React Giphy Searcher
We are going to build a searchable interface for the [Giphy API](https://developers.giphy.com/) using React. 

# STEP 1 - Application Setup

Project setup - nothing new here!

1. Navigate to your `~/code/SDA-SIRAJ/applications` directory. 
2. `npm create vite@latest project-name`
3. `Select a framework:` => `React`
4. `Select a variant` => `Javascript`
5. `Use rolldown-vite (Experimental)?:` => `No`
6. `Install with npm and start now?:` => `Yes`
7. Navigate to `localhost:5173` (check app is running)
8. `ctrl+c` => terminate running application
9. `cd project-name`
10. `npm i -D @types/react @types/react-dom` (helps with intellisense / autocomplete!)
11. `npm run dev` when ready to spin up your app!

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

6. **Run the development server**

To start the development server and view our app in the browser, we'll use the following command:

```bash
npm run dev
```

You should see that `Vite` is available on port number 5173:

```plaintext
localhost:5173
```

`ctrl+c` to disconnect the server

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
