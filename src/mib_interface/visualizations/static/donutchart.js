
/***************   DONUT CHARTS VISUALIZATION (D3JS)   ****************

  Create one or multiple donut charts based on JSON data. 


DATASET STRUCTURE

  See reference.json file for templates.

  ⚠️ The 'donutcharts' data is first added in the mib_interface module 
   'converters' then modified in the mib_interface module 'visualizations'
   then added in a html page to finally be used here with d3js.

*********************************************************************/

//Get JSON from HTML DOM
let elements = JSON.parse(donutcharts);

//Create the donut charts
$.each(elements, (i,element)=>{

  //Margin, radius, color
  let m = 50,
      r = 130,
      color = d3.scale.category20c();

  //*INMIND* responsive svg size for mobile devices 
  let svg_size = (window.innerWidth>460) ? (r+m)*2 : (r+m)*1.7;
  let g_position = (window.innerWidth>460) ? (r+m) : (r+m-36);

  //Define a pie layout
  let pie = d3.layout.pie()
    .value(d=> + d.metric1)
    .sort((a,b)=> b.metric1 - a.metric1);

  //Define an arc generator
  let arc = d3.svg.arc()
    .innerRadius(r/2.4) //Donut width
    .outerRadius(r);

  //Insert an svg for each element of the dataset
  let svg = d3.select("#"+element.id).selectAll("#"+element.id)
    .data(d3.values(element.dataset))
    .enter()
    .append("div")
      .style("display", "inline-block")
      .style("width", svg_size +"px")
      .style("height", svg_size +"px")
      .append("svg")
        .attr("width", svg_size)
        .attr("height", svg_size)
        .append("g")
          .attr("transform", "translate("+ g_position +","+ g_position +")");

  //Element title
  svg.append("text")
    .attr("dy", ".35em")
    .attr("text-anchor", "middle")
    .style("font-weight", "bold")
    .text(d=> d.title)

  //Pass the nested per-donut values to the pie layout
  let g = svg.selectAll("g")
    .data(d=> pie(d.aggregation1.map(d=> d))) //aggregation1 agg1-metric1 values
    .enter()
    .append("g");

  //Add a colored arc path, with a mouseover title showing the metric1.
  g.append("path")
    .attr("d", arc)
    //.attr('', (d) => console.log(d.data.agg1))
    .style("fill", d=> color(d.data.agg1))
    .append("title")
      .text(d=> d.data.agg1 +": "+ d.data.metric1);

  //Add a label to the larger arcs, translated to the arc centroid and rotated.
  g.filter(d=> d.endAngle - d.startAngle > .2)
    .append("text")
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .attr("transform", d=> "translate("+ arc.centroid(d) +")rotate("+ angle(d) +")")
      .text(d=> d.data.agg1);

  //Computes the label angle of an arc, converting from radians to degrees.
  function angle(d) {
    let a = (d.startAngle + d.endAngle) *90/Math.PI-90;
    return a > 90 ? a - 180 : a;
  }

});
