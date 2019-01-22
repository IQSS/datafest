// Here's a real data set drawn from our solar system. Let's combine this data with our previous visualization to make a simple model of our solar system.
/**Data set **/
//Source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
//Planet diameters in km, because science
var planetDiameters = [4879,	12104,	12756, 6792,	142984,	120536,	51118,	49528];

//Planet distances from the sun, 10^6 km
var planetDistances = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1];

//Planet colors, web safe colors http://curious.astro.cornell.edu/about-us/58-our-solar-system/planets-and-dwarf-planets/planet-watching/249-what-color-is-each-planet-intermediate
var planetColors = ["Gray", "PaleGoldenrod", "Blue", "DarkRed", "DarkOrange", "Gold", "PowderBlue", "SteelBlue"];

//Planet names
var planetNames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

//Lets manage this data a bit better
var planets =[];
for (var i = 0; i < planetDiameters.length; i++){
  planet = {};
  planet.name = planetNames[i];
  planet.radius = planetDiameters[i] / 2;
  planet.distance = planetDistances[i];
  planet.color = planetColors[i];
  planets.push(planet);
}
console.log(planets);

/**D3 **/
// create the svg, same as before.
   var svgContainer = d3.select("body").append("svg")
      .attr('height',600)
      .attr('width',2000);

   var circles = svgContainer.selectAll("circle")
      .data(planets)
      .enter()
      .append("circle")
        .attr("cx", function(d) {return d.distance / 3 })
        .attr("cy", 200)
        .attr("r", function (d) { return d.radius / 1000; })
        .style("fill", function (d) { return d.color; });

//Labels

var gText = svgContainer.selectAll("gText")
			.data(planets)
			.enter()
        .append("g")
			  .attr("y", 10)
			  .attr("transform", function(d, i){
          return "translate(" + (d.distance / 1000) + ",200)";
        });

gText.append("text")
			.text(function(d, i) {
        return d.name;
      })
			.attr("text-anchor","start")
			.attr("transform", function(d, i){
        return("translate(" + (d.distance / 3) + ",-" + (10 + d.radius/1000) +")rotate(-45,0,0)");
      });
