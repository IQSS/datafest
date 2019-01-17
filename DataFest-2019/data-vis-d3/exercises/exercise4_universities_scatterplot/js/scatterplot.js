/*
 * Scatterplot - Object constructor function
 * @param _parentElement 	-- the HTML element in which to draw the plot
 * @param _data						-- the dataset
 */

Scatterplot = function(_parentElement, _data){
	this.parentElement = _parentElement;
	this.data = _data;
	this.displayData = _data;

	this.initVis();

}

/*
 * Initialize visualization (static content; e.g. SVG area, axes)
 */

Scatterplot.prototype.initVis = function(){
  var vis = this;

  vis.margin = { top: 20, right: 50, bottom: 20, left: 150 };
  vis.width = 1000 - vis.margin.left - vis.margin.right;
  vis.height = 600 - vis.margin.top - vis.margin.bottom;

  vis.svg = d3.select("#" + vis.parentElement).append("svg")
	    .attr("width", vis.width + vis.margin.left + vis.margin.right)
	    .attr("height", vis.height + vis.margin.top + vis.margin.bottom)
        .append("g")
	       .attr("transform", "translate(" + vis.margin.left + "," + vis.margin.top + ")");

  // Scales and axes
  // Domains are fixed - don't update
  vis.x = d3.scaleLinear()
    .range([0, vis.width])
    .domain([
      d3.min(vis.data, function(d){ return d.total_cost_per_year }) - 5000, //Padding
      d3.max(vis.data, function(d){ return d.total_cost_per_year })
    ]);

  vis.xAxis = d3.axisBottom()
    .scale(vis.x);

  vis.xAxisGroup = vis.svg.append("g")
    .attr("class", "x-axis axis")
    .attr("transform", "translate(0," + vis.height + ")");

  vis.y = d3.scaleLinear()
    .range([vis.height, 0])
    .domain([
      d3.min(vis.data, function(d){ return d.grad_salary }) - 5000, //Padding
      d3.max(vis.data, function(d){ return d.grad_salary })
    ]);

  vis.yAxis = d3.axisLeft()
    .scale(vis.y);

  vis.yAxisGroup = vis.svg.append("g")
    .attr("class", "y-axis axis");

  // Tooltip
  // Needs to be on top of SVG - select the parent element
  vis.tooltip = d3.select("#" + vis.parentElement).append("div")
    .attr("class", "details")
    .style("opacity", 0);

  // Color scale
  vis.colorScale = d3.scaleThreshold()
    .domain([25, 50, 100, 150, 200])
    .range(['#006837','#31a354','#78c679','#addd8e','#d9f0a3','#ffffcc'])
  vis.rankScale = d3.scaleThreshold()
    .domain([25, 50, 100, 150, 200])
    .range(['Top 25','25-50','50-100','100-150','150-200','200+'])

  // Legend
  // vis.legend = vis.svg.append("g")
  //   .attr("class","legend")
  //   .attr("transform","translate(50,30)")
  //   .style("font-size","12px")
  //   .call(d3.legend)
  var legendSvg = d3.select("#legend").append("g")
    .attr("width", 200)
    .attr("height", 300);
  vis.legend = legendSvg.selectAll(".legendRange")
    .data(vis.rankScale.domain());
  vis.legend.enter()
    .append("rect")
    .attr("class", "legendRange")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", '10px')
    .attr("height", '10px')
    .style("fill", function(d,i){
      return vis.colorScale(d)
    });
  vis.legend.enter()
    .append("text")
    .attr("x", 20)
    .attr("y", 10)
    .text(function(d,i){
      return vis.rankScale(d);
    });

  vis.wrangleData();
}

/*
 *  Data wrangling
 */

Scatterplot.prototype.wrangleData = function(){
  var vis = this;

  //Filter data
  var selected = $('#filter-conferences').val();
  vis.displayData = vis.data;
  vis.displayData = vis.displayData.filter(function(d){
    return selected.includes(d.conference);
  })

  vis.updateVis();
}

/*
 *  The drawing function
 */
Scatterplot.prototype.updateVis = function(){
  var vis = this;
  console.log("updateVis");

  //Draw points
  vis.schools = vis.svg.selectAll(".school")
    .data(vis.displayData);
  vis.schools.enter()
      .append("circle")
      .attr("class", "school")
      .merge(vis.schools)
      .attr("r", function(d){
        return d.avg_grad_debt / 5000;
      })
      .attr("cx", function(d){
        return vis.x(d.total_cost_per_year)
      })
      .attr("cy", function(d){
        return vis.y(d.grad_salary)
      })
      .style("fill", function(d){
        //return "grey";
        return vis.colorScale(d.rank);
      })
      // .attr("data-legend",function(d) {
      //   return vis.rankScale(d.rank);
      // })
      .on("mouseover", function(d){
        console.log(d3.event);
        vis.tooltip.transition()
          .duration(200)
          .style("opacity", .9);
        vis.tooltip.html(d.name)
          .style("left", (d3.event.pageX) + "px")
          .style("top", (d3.event.pageY - 28) + "px");
        console.log(vis.tooltip);
      })
      .on("mouseout", function(d){
        vis.tooltip.transition()
          .duration(200)
          .style("opacity", 0);
      });

    //Remove old data
    vis.schools.exit()
  		.remove();

    //Update axes
    vis.yAxisGroup.call(vis.yAxis);
    vis.xAxisGroup.call(vis.xAxis);

}
