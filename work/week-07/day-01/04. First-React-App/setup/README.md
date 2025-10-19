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
