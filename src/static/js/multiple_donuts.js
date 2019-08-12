
/**************   INMIND TECHNOLOGIES   ****************/
/*
MULTIPLE DONUTS : Create multiple donuts based on CSV ingestion. 
The number of donuts is based on the number of unique entries 
of the first value of each line of the csv.

TYPE OF INGESTION: CSV

DATA TYPES
The CSV data type must conform to this configuration:
	* title -> string: name of each donut
	* aggregation1 -> string: name of each donut parcel for 1st aggregation
	* metric1 -> number: value of each donut parcel for 1st metric
  * aggregation2 -> string: name of each donut parcel for 2nd aggregation
  * metric2 -> number: value of each donut parcel for 2nd metric

DATA STRUCTURE
The CSV can have 3 types of data structure only:
  * 3 datas -> title,aggregation1,metric1
  * 5 datas -> title,aggregation1,metric1,aggregation2,metric2

⚠️The CSV must have these header names, or you have to change it
  in the code below.
⚠️You must create a <div> with id="multiple_donuts" for nesting the visualization
*/

/* CUSTOM VALUES */
//CSV path
let csv = "../../static/files/splunk_indexes.csv";

/*****************************************************/

// Define the margin, radius, and color scale. Colors are assigned lazily, so
// if you want deterministic behavior, define a domain for the color scale.
let m = 50,
    r = 130,
    z = d3.scale.category20c();

//*INMIND* responsive svg size for mobile devices 
let svg_size = (window.innerWidth>460) ? (r+m)*2 : (r+m)*1.7;
let g_position = (window.innerWidth>460) ? (r+m) : (r+m-36);

// Define a pie layout: the pie angle encodes the count of lines. Since our
// data is stored in CSV, the counts are strings which we coerce to numbers.
let pie = d3.layout.pie()
  .value(function(d) { return +d.metric1; })
  .sort(function(a, b) { return b.metric1 - a.metric1; });

// Define an arc generator. Note the radius is specified here, not the layout.
let arc = d3.svg.arc()
  .innerRadius(r/2.4) //width of the donut
  .outerRadius(r);

// Load the csv data asynchronously.
d3.csv(csv, function(error, rows) {
  if (error) throw error;

  // Nest each line data by its first value (which will be the number of donuts created). 
  let donuts = d3.nest()
    .key(function(d) { return d.title; }).sortKeys(d3.ascending)
    .entries(rows);

  // Insert an svg element (with margin) for each donut in our dataset. A
  // child g element translates the title to the pie center.
  let svg = d3.select("#multiple_donuts").selectAll("#multiple_donuts")
    .data(donuts)
    .enter().append("div")
      .style("display", "inline-block")
      .style("width", svg_size + "px")
      .style("height", svg_size + "px")
    .append("svg")
      .attr("width", svg_size)
      .attr("height", svg_size)
    .append("g")
      .attr("transform", "translate(" + g_position + "," + g_position + ")");

  // Add a label for the donut. The `key` comes from the nest operator.
  svg.append("text")
    .attr("dy", ".35em")
    .attr("text-anchor", "middle")
    .style("font-weight", "bold")
    .text(function(d) { return d.key; });

  // Pass the nested per-donut values to the pie layout. The layout computes
  // the angles for each arc. Another g element will hold the arc and its label.
  let g = svg.selectAll("g")
    .data(function(d) { return pie(d.values); })
    .enter().append("g");

  // Add a colored arc path, with a mouseover title showing the metric1.
  g.append("path")
    .attr("d", arc)
    .style("fill", function(d) { return z(d.data.aggregation1); })
    .append("title")
    .text(function(d) { return d.data.aggregation1 + ": " + d.data.metric1; });

  // Add a label to the larger arcs, translated to the arc centroid and rotated.
  g.filter(function(d) { return d.endAngle - d.startAngle > .2; }).append("text")
    .attr("dy", ".35em")
    .attr("text-anchor", "middle")
    .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")rotate(" + angle(d) + ")"; })
    .text(function(d) { return d.data.aggregation1; });

  // Computes the label angle of an arc, converting from radians to degrees.
  function angle(d) {
    let a = (d.startAngle + d.endAngle) * 90 / Math.PI - 90;
    return a > 90 ? a - 180 : a;
  }
});

