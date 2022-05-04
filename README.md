# front-end-testing
 
## Setup
```npm init -y ```

```npm install tailwind postcss-cli autoprefixer```

```npx tailwind init```

create ```postcss.config.js```
```javascript
module.exports = {
    plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
    ]
}
```

create css/tailwind.css
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

modify ```package.json``` script from test to build
```javascript
  "scripts": {
    "build": "postcss css/tailwind.css -o public/build/tailwind.css"
  },
```

