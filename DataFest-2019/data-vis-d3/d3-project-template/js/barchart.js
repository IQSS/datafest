

/*
 * BarChart - Object constructor function
 * @param _parentElement 	-- the HTML element in which to draw the bar charts
 * @param _data						-- the dataset 'household characteristics'
 * @param _config					-- variable from the dataset (e.g. 'electricity') and title for each bar chart
 */

BarChart = function(_parentElement, _data, _config){
	this.parentElement = _parentElement;
	this.data = _data;
	this.config = _config;
	this.displayData = _data;

	this.initVis();
}



/*
 * Initialize visualization (static content; e.g. SVG area, axes)
 */

BarChart.prototype.initVis = function(){
	var vis = this;


	// * TO-DO *


	// (Filter, aggregate, modify data)
	vis.wrangleData();
}



/*
 * Data wrangling
 */

BarChart.prototype.wrangleData = function(){
	var vis = this;

	// (1) Group data by key variable (e.g. 'electricity') and count leaves
	// (2) Sort columsn descending


	// * TO-DO *


	// Update the visualization
	vis.updateVis();
}



/*
 * The drawing function - should use the D3 update sequence (enter, update, exit)
 */

BarChart.prototype.updateVis = function(){
	var vis = this;

	// (1) Update domains
	// (2) Draw rectangles
	// (3) Draw labels
	

	// * TO-DO *


	// Update the y-axis
	vis.svg.select(".y-axis").call(vis.yAxis);
}



/*
 * Filter data when the user changes the selection
 * Example for brushRegion: 07/16/2016 to 07/28/2016
 */

BarChart.prototype.selectionChanged = function(brushRegion){
	var vis = this;

	// Filter data accordingly without changing the original data

	
	// * TO-DO *


	// Update the visualization
	vis.wrangleData();
}
