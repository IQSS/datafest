/*
 * Scatterplot - Object constructor function
 * @param _parentElement 	-- the HTML element in which to draw the plot
 * @param _data						-- the dataset
 */

Scatterplot = function(_parentElement, _data){
	this.parentElement = _parentElement;
	this.data = _data;

	this.initVis();
}

/*
 * Initialize visualization (static content; e.g. SVG area, axes)
 */

Scatterplot.prototype.initVis = function(){
  var vis = this;

  vis.margin = { top: 20, right: 50, bottom: 100, left: 150 };
  vis.width = 1000 - vis.margin.left - vis.margin.right;
  vis.height = 600 - vis.margin.top - vis.margin.bottom;

  vis.svg = d3.select("#" + vis.parentElement).append("svg")
	    .attr("width", vis.width + vis.margin.left + vis.margin.right)
	    .attr("height", vis.height + vis.margin.top + vis.margin.bottom)
        .append("g")
	       .attr("transform", "translate(" + vis.margin.left + "," + vis.margin.top + ")");

  // Scales and axes
  // Domains are fixed - don't update on data change
	// TO DO: Create a currency format for the axis, and use it as a .tickFormat()
	//				add ranges and domains to the scales
  var formatAsCurrency = d3.format("$");
	vis.x = d3.scaleLinear();
    //add domain and range to the scale; use d3.min and d3.max on d.total_cost_per_year

  vis.xAxis = d3.axisBottom()
    //add tickFormat and scale to the axis

  vis.xAxisGroup = vis.svg.append("g")
    .attr("class", "x-axis axis")
    .attr("transform", "translate(0," + vis.height + ")");

  vis.xAxisGroup.append("text")
    .attr("transform",
        "translate(" + (vis.width/2) + " ," +
                       (50) + ")")
    .style("text-anchor", "middle")
    .attr("class", "axisLabel")
    .text("Average Graduate Debt");

  vis.y = d3.scaleLinear()
		// Add range and domain to the scale; use the vis.height property for range
		// and d3.min/max and d.grad_salary for the domain

  vis.yAxis = d3.axisLeft()
    //add tickFormat and scale to the axis

  vis.yAxisGroup = vis.svg.append("g")
    .attr("class", "y-axis axis");

  vis.yAxisGroup.append("text")
    .attr("transform", "rotate(-90)")
        .attr("y", 0 - vis.margin.left + 50)
        .attr("x",0 - (vis.height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .attr("class", "axisLabel")
        .text("Average Graduate Salary");

  // Color scale
  vis.colorScale = d3.scaleThreshold()
    .domain([25, 50, 100, 150, 200])
		// TO DO: use an array of hex colors as the range
		// Check out http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3 for ideas
  vis.rankScale = d3.scaleThreshold()
    .domain([25, 50, 100, 150, 200])
    .range(['Top 25','25-50','50-100','100-150','150-200','200+'])

  // Legend
  var legendSvg = d3.select("#legend").append("svg")
    .attr("width", 200)
    .attr("height", 300);
  vis.legend = legendSvg.selectAll(".legendRange")
    .data([0, 25, 50, 100, 150, 200])
    .enter()
    .append("g")
    .attr("class", "legendRange")
    .attr("transform", function (d, i){
      return "translate(0," + i * 20 + ")"
    });
	//TO DO: add <rects> and <text> elements for each item in the legend
	//Make sure to use the colorScale for the rect colors, and the rankScale for the text values
	//The data has already been bound above

  //vis.legend
    //.append("rect")
    // ...

  // Tooltip
  // Needs to be on top of SVG - select the parent element
  vis.tooltip = d3.select("#" + vis.parentElement).append("div")
    .attr("class", "details")
    .style("opacity", 0);

  vis.wrangleData();
}

/*
 *  Data wrangling
 */

Scatterplot.prototype.wrangleData = function(){
  var vis = this;

  // Filter data
	// TO DO: if you have implemented the filter selectbox, filter the data here
	// instead of just making setting displayData
  vis.displayData = vis.data;

  vis.updateVis();
}

/*
 *  The drawing function
 */
Scatterplot.prototype.updateVis = function(){
  var vis = this;

  //Draw all of the points

  //Bind the data
  vis.schools = vis.svg.selectAll(".school")
    .data(vis.displayData);

  // TO DO
  // add a circle for each school; the radius should return avg_grad_debt (appropriately scaled down)
  // Merge the data (remember the enter, update, remove pattern)
  // cx should use the x scale and total_cost_per_year
  // cy should use the y scale and grad_salary
  // fill should use the colorscale and school rankScale
  // mouseover should change html of the tooltip to something useful, like a label displaying data about the school
  vis.schools.enter()
      //APPEND A CIRCLE
      .attr("class", "school")
      //MERGE THE DATA
      .attr("r", function(d){
        //
      })
      .attr("cx", function(d){
        //
      })
      .attr("cy", function(d){
        //
      })
      .style("fill", function(d){
        //
      })
      .on("mouseover", function(d){
        vis.tooltip.transition()
          .duration(200)
          .style("opacity", .9);
        vis.tooltip.html("LABEL")
          .style("left", (d3.event.pageX) + "px")
          .style("top", (d3.event.pageY - 28) + "px");
      })
      .on("mouseout", function(d){
        vis.tooltip.transition()
          .duration(200)
          .style("opacity", 0);
          d3.select(this)
            .style("fill", function(d){
              return vis.colorScale(d.rank);
            })
      });

    //Remove old data
    vis.schools.exit()
  		.remove();

    //Update axes
    vis.yAxisGroup.call(vis.yAxis);
    vis.xAxisGroup.call(vis.xAxis);

}
