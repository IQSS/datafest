//Margins and other global variables
var margin = {top: 50, right: 300, bottom: 50, left: 75};
var barChartWidth = 1500 - margin.left - margin.right,
		barChartHeight = 1500 - margin.top - margin.bottom
		barHeight = 8;


d3.csv("data/universities_ranked_2017.csv", function(data){

	console.log("data loaded");
	console.log(data);

	//format our data
	data.forEach(function(d){
		d.percentage_nonneedbased_aid = +d.percentage_nonneedbased_aid;
		d.four_year_grad_rate = +d.four_year_grad_rate;
		d.admit_rate = +d.admit_rate;
		d.avg_grad_debt = +d.avg_grad_debt;
		d.avg_needbased_aid = +d.avg_needbased_aid;
		d.instate_tuition = +d.instate_tuition;
		d.rank = +d.rank;
		d.value_rank = +d.value_rank;
		d.grad_salary = +d.grad_salary;
		d.total_cost_per_year = +d.total_cost_per_year;
		d.tuition_and_fees = +d.tuition_and_fees;
		d.undergrad_enrollment = +d.undergrad_enrollment;
		d.avg_nonneedbased_aid = +d.avg_nonneedbased_aid;
	});

	//sort our data
	function sortData(unsortedData,sortOn){
		var sorted = unsortedData.sort(function(a, b){
			return b[sortOn]-a[sortOn];
		});
		return sorted;
	}
	var sortedData = sortData(data, "grad_salary");

	console.log(sortedData);

	var barChart = d3.select("#bar-chart")
		.append("svg")
		.attr("width", barChartWidth + margin.left + margin.right)
		.attr("height", barChartHeight + margin.top + margin.bottom)
		.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	var xscale = d3.scaleLinear()
		.domain([0, d3.max(sortedData, function(d) {
			return d.grad_salary;
		})])
		.range([0, barChartWidth]);

	var yscale = d3.scaleLinear()
		.domain([0, sortedData.length])
		.range([0, barChartHeight]);

	var xAxis = d3.axisBottom()
							.scale(xscale)
							.ticks(10)
							//.tickFormat(d3.timeFormat("%B %Y"))
							.tickSizeOuter(0);

	var xBarAxis = d3.axisTop()
							.scale(xscale)
							.tickSizeOuter(0);

	var xBarGroup = barChart.append("g")
		.attr("class", "axis x-axis")
		//.attr("transform", "translate(0," + barChartWidth + ")")
		.attr("transform", "translate(0,-10)")
		.call(xBarAxis);

	var schools = barChart.selectAll("rect")
		.data(sortedData)
		.enter()
			.append("rect")
			.attr("class", "schoolBar")
			.attr("height", barHeight)
			.attr("width", function(d){
				return xscale(d.grad_salary);
			})
			.attr("y", function(d, i){
				return yscale(i);
			})
			.attr("x", function(d){
				return 0;
			});

	var barLabels = barChart.selectAll(".barLabels")
		.data(sortedData)
		.enter()
		.append("text")
			.attr("class", "barLabels")
			.text(function(d){
				return(`${d.name} | (${d.rank}) | $${d.grad_salary}`)
			})
			.attr("x", function(d){ return xscale(d.grad_salary) + 3})
			.attr("y", function(d,i){ return yscale(i)+8});

});
