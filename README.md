# Front-end Testing


## Preview (https://sampom100.github.io/front-end-testing/)
<img width="780" alt="Screen Shot 2022-05-11 at 8 13 47 PM" src="https://user-images.githubusercontent.com/28206070/167967372-3e7aab19-025c-42ad-be79-3100a35c348c.png">




## Setup

```npm init -y```

```npm install tailwindcss postcss-cli autoprefixer```

```npx tailwind init```
```javascript
module.exports = {
  theme: {
    extend: {}
  },
  variants: {},
  plugins: []
}
```

```touch postcss.config.js```
```javascript
module.exports = {
    plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
    ]
}
```

mkdir css
cd css
touch ```tailwind.css```
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Add this build script in ```package.json```
```javascript
  "scripts": {
    "build": "postcss css/tailwind.css -o public/build/tailwind.css"
  },
```
In ```package.json``` using an older version of tailwind
```javascript
  "dependencies": {
    "autoprefixer": "^9.6.1",
    "postcss-cli": "^6.1.2",
    "tailwindcss": "^1.0.4"
  }
```

```npm run build```

make an ```index.html``` in /public

```html
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="/build/tailwind.css">
</head>
<body>
  <h1 class="text-4xl text-blue-500 text-center">Hello world!</h1>
</body>
</html>
```


```npm install -g live-server```

```live-server public```
