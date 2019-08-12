
/***************   GAUGE CHARTS VISUALIZATION (D3JS)   ****************

  Create one or multiple gauge charts based on JSON data. 


DATASET STRUCTURE

  See reference.json file for templates.

  ⚠️ The 'gaugecharts' data is first added in the mib_interface module 
   'converters' then modified in the mib_interface module 'visualizations'
   then added in a html page to finally be used here with d3js.

*********************************************************************/

//Get JSON from HTML DOM
let elements = JSON.parse(gaugecharts);

//Create the gauge charts
$.each(elements, (i,element)=>{

	//Svg margin, height, width
	let mg = {left:40, right:40, top:80, bottom:70},
			h = 280,
			w = $('.width').width() - 10;//dynamic Bootstrap;	

	//*INMIND* responsive svg size for mobile devices 
  let m = 50, //margin
      r = 130, //radius
  		svg_size = (window.innerWidth>460) ? (r+m)*2 : (r+m)*1.7,
  		g_position = (window.innerWidth>460) ? (r+m) : (r+m-36);
		
	//Gauge dimensions
	let size = 250,
			//inner radius & outer radius
			oR = size - 150,
			iR = size - oR - 95;

	//Define an arc generator
	let arc = d3.svg.arc()
	  .innerRadius(iR)
	  .outerRadius(oR)
	  .startAngle(-90*Math.PI/180);


	//Insert an svg for each element of the dataset
	let svg = d3.select("#"+element.id).selectAll("#"+element.id)
		.data(d3.values(element.dataset))
		.enter()
	  .append("div")
	    .style("display", "inline-block")
	    .style("width", svg_size +"px")
	    .style("height", svg_size +"px")
			.append('svg')
				.attr('width', svg_size)
				.attr('height', svg_size)
				//.style('background', 'lightcyan')
				.append('g')
		    	.attr("transform", "translate("+ g_position +","+ g_position +")");

	//Element title
	svg.append('text')
	  .attr('transform', 'translate('+ (- size) +', -136)')
	  .style('font-size', '.9em')
	  .text(d=> d.title);

	//Element legend
	svg.append('text')
	  .attr('transform', 'translate('+ (size-mg.right*2) +','+ mg.bottom +')')
	  .attr('text-anchor', 'middle')
	  .style('font-size', '.8em')
	  .text(d=> d.name1 +' / '+ d.name2);

	//Add background arc to svg
	svg.append('path')
	  .datum({ endAngle: 90*Math.PI/180 })
	  .attr('d', arc);

let test = svg.data;
console.log(test);
	//Add foreground arc to svg
	svg.append('path')
	  .style('fill', d=> d.color)
	  .datum({ endAngle: -90*Math.PI/180 })
	  .attr('d', arc)
	  .transition()
	  	.duration(500)
	  	.call(arcTween, d=> Math.floor(d.metric1*180/d.metric2-90)*Math.PI/180);

	//Add minimum value label
	svg.append('text')
  .attr('transform', 'translate('+ -(iR+((oR-iR)/2)) +',15)') // Set between inner and outer Radius
  .attr('text-anchor', 'middle')
  .text('0');
	//Add total value label
	svg.append('text')
	  .attr('transform', 'translate('+ (iR+((oR-iR)/2)) +',15)') // Set between inner and outer Radius
	  .attr('text-anchor', 'middle')
	  .text(d=> d.metric2);
	//Add quota value label
	svg.append('text')
	  .attr('transform', 'translate(0,'+ -(-20+iR/4) +')') // Push up from center 1/4 of innerRadius
	  .attr('text-anchor', 'middle')
	  .style('font-size', '1.5em')
	  .style('font-weight','bold')
	  .text(d=> d.metric1);

	//Gauge color animation
	function arcTween(transition, newAngle) {
		console.log(newAngle);
	  transition.attrTween('d', d=> {
	    let interpolate = d3.interpolate(d.endAngle, newAngle);
	    return t=> { d.endAngle = interpolate(t); return arc(d); };
		});
	}

});




