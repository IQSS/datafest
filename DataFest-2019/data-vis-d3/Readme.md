# Interactive Data Visualization with D3

<a href="https://d3js.org/">D3.js</a> is a JavaScript library for manipulating documents based on data. D3 helps you bring data to life using HTML, SVG, and CSS. D3’s emphasis on web standards gives you the full capabilities of modern browsers without tying yourself to a proprietary framework, combining powerful visualization components and a data-driven approach to DOM manipulation.

In this workshop, we're going present several exercises and go through some core D3 functionality in a whirlwind crash course to this popular library.

## Preparation

+ Clone the repo
+ Get a text editor for writing code
+ Have a local webserver for serving code (Python, ideally)

To prepare for this workshop, please clone this repository with the example exercises and materials.

You'll also need a text editor which ideally includes code formatting and highlighting. I recommend <a href="https://atom.io/">Atom</a> or Sublime, though many others are excellent as well.

You will also need a local webserver. The easiest way to set this up is with <a href="https://www.python.org/downloads/">Python</a>. Macs typically have Python installed already; you'll probably need to download and install it on a Windows machine. Check if it's installed on your terminal / command prompt with

`python -V`

Then:

  ```
  # If Python version returned above is 3.X
  python3 -m http.server 2222
  # If Python version returned above is 2.X
  python -m SimpleHTTPServer 2222
  ```

This will run it on port 2222; you can use a different port if desired. Run this out of /data-vis-d3/exercises, and you'll be able to easily switch between the exercise materials without closing and restarting the server.

If you can't run a local webserver, you can sign up for a CodePen account and copy the code to a CodePen project instead.
