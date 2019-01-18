

    // The first thing we have to do is append an svg element to the <body>
    // We also have to size it, using d3's `attr` (attribute) function
    var svg = d3.select("body").append("svg")
      .attr("height",50)
      .attr("width",200);

    // Now let's add a text element to the svg element through the svg variable.
    // We have to size this too.
    svg.append("text")
      .text("Hello, SVG world!")
      .attr("x",0)
      .attr("y",15);

    // Now let's draw a crude picture of the world, because it's svg and we can
    svg.append("circle")      //shape name
        .attr("cx",150)       //x-axis coordinate in px, in relation to svg element in DOM
        .attr("cy",15)        //y-axis coordinate
        .attr("fill","blue")  //color
        .attr("r",20);        //radius length (px)
