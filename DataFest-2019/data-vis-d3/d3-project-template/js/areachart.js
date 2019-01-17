
/*
 * AreaChart - Object constructor function
 * @param _parentElement 	-- the HTML element in which to draw the area chart
 * @param _data						-- the dataset 'household characteristics'
 */

AreaChart = function(_parentElement, _data){
	this.parentElement = _parentElement;
	this.data = _data;
	this.displayData = [];

	this.initVis();
}


/*
 * Initialize visualization (static content; e.g. SVG area, axes, brush component)
 */

AreaChart.prototype.initVis = function(){
	var vis = this;

	// * TO-DO *


	// (Filter, aggregate, modify data)
	vis.wrangleData();
}


/*
 * Data wrangling
 */

AreaChart.prototype.wrangleData = function(){
	var vis = this;

	// (1) Group data by date and count survey results for each day
	// (2) Sort data by day

	
	// * TO-DO *


	// Update the visualization
	vis.updateVis();
}


/*
 * The drawing function
 */

AreaChart.prototype.updateVis = function(){
	var vis = this;

	// * TO-DO *
	
}

