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
  var formatAsCurrency = d3.format("$");
  vis.x = d3.scaleLinear()
    .range([0, vis.width])
    .domain([
      d3.min(vis.data, function(d){ return d.total_cost_per_year }) - 5000, //Padding
      d3.max(vis.data, function(d){ return d.total_cost_per_year })
    ]);

  vis.xAxis = d3.axisBottom()
    .tickFormat(formatAsCurrency)
    .scale(vis.x);

  vis.xAxisGroup = vis.svg.append("g")
    .attr("class", "x-axis axis")
    .attr("transform", "translate(0," + vis.height + ")");

  vis.xAxisGroup.append("text")
    .attr("transform",
        "translate(" + (vis.width/2) + " ," +
                       (50) + ")")
    .style("text-anchor", "middle")
    .attr("class", "axisLabel")
    .text("Total Cost Per Year");

  vis.y = d3.scaleLinear()
    .range([vis.height, 0])
    .domain([
      d3.min(vis.data, function(d){ return d.grad_salary }) - 5000, //Padding
      d3.max(vis.data, function(d){ return d.grad_salary })
    ]);

  vis.yAxis = d3.axisLeft()
    .tickFormat(formatAsCurrency)
    .scale(vis.y);

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
    .range(['#006837','#31a354','#78c679','#addd8e','#d9f0a3','#ffffcc'])
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
  vis.legend
    .append("rect")
    .attr("class", "legendRange")
    .attr("x", 10)
    .attr("y", 10)
    .attr("width", 10)
    .attr("height", 10)
    .style("stroke", "black")
    .style("fill", function(d,i){
      return vis.colorScale(d)
    });
  vis.legend
    .append("text")
    .attr("x", 25)
    .attr("y", 20)
    .text(function(d,i){
      return vis.rankScale(d);
    });

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
        return vis.colorScale(d.rank);
      })
      .on("mouseover", function(d){
        vis.tooltip.transition()
          .duration(200)
          .style("opacity", .9);
        vis.tooltip.html(`
          <div id="detail-title">${d.name}</div>
          <div>USN&WR Rank: ${d.rank}</div>
          <div>Value Rank: ${d.value_rank}</div>
          <div>Av. Grad Salary: $${d.grad_salary}</div>
          <div>Av. Grad Debt: $${d.avg_grad_debt}</div>
          `)
          .style("left", (d3.event.pageX) + "px")
          .style("top", (d3.event.pageY - 28) + "px");
        d3.select(this)
          .style("fill", "red");
        console.log(d);
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
