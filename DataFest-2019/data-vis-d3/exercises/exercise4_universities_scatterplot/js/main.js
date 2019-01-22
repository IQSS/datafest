// Placeholder variables
var allData = [];
var scatterplot;
var allConferences;
// Sets hold unique values; only one copy of each, which is what we want for our selectbox
var conferencesSet = new Set();

function loadData(){
  d3.csv("data/universities_ranked_2017_conferences.csv", function(err, csvData){
    if(!err){
      allData = csvData;

      //Turn quantitative data into ints; add conferences to set
      allData.forEach(function(d){
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

        //TO DO: add the conference names to conferencesSet
      });

      // Getting an array from the set
      allConferences = Array.from(conferencesSet).sort();

      allConferences.forEach(function(d){
        //TO DO: add an <option> for each item in allConferences
      })

      createVis();
    }
  });
}

function createVis(){
  //Instantiate visualization object
  scatterplot = new Scatterplot("scatterplot", allData);

  //TO DO: add the filtering functionality here
}

//Start application
loadData();
