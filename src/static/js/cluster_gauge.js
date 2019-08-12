//get data from php
var data = JSON.parse(cluster); 
color = '';
switch(data.status) {
  case 'green': color='#008000';break;
  case 'red': color='#FF0000';break;
  case 'yellow': color='#FFD700';break;
  default: color='#008000';
}
quota = data.active_primary_shards;
total = data.active_shards;

//svg dimensions
var margin = {left:40, right:40, top:80, bottom:70}
var height = 280;
var width = $('.width').width() - 10;//dynamic Bootstrap;	
//gauge dimensions
var size = 250;
var arcInset = 150;
var arcWidth = 95;
var transitionMs = 750;
var numPi = Math.floor(quota*180/total-90)*Math.PI/180;
//inner radius & outer radius
var oR = size - arcInset;
var iR = size - oR - arcWidth;

 
//definition of svg 
var svg = d3.select('#gauge')
	.append('svg')
		.attr('width', width)
		.attr('height', height)
		.style('background', 'lightcyan')
		.append('g')
    .attr('transform', 'translate('+ width/2 +','+ (height+margin.top)/2 +')');

//definction of arc
var arc = d3.svg.arc()
  .innerRadius(iR)
  .outerRadius(oR)
  .startAngle(-90* Math.PI/180);

//append background arc to svg
var background = svg.append('path')
  .datum({ endAngle: 90* Math.PI/180 })
  .attr('d', arc);

//append foreground arc to svg
var foreground = svg.append('path')
  .style('fill', color)
  .datum({ endAngle: -90* Math.PI/180 })
  .attr('d', arc)
  .transition()
  .duration(transitionMs)
  .call(arcTween, numPi);

//display Min, Max & current values
var max = svg.append('text')
  .attr('transform', 'translate('+ (iR+((oR-iR)/2)) +',15)') // Set between inner and outer Radius
  .attr('text-anchor', 'middle')
  .text(total);
var min = svg.append('text')
  .attr('transform', 'translate('+ -(iR+((oR-iR)/2)) +',15)') // Set between inner and outer Radius
  .attr('text-anchor', 'middle')
  .text(0);
var current = svg.append('text')
  .attr('transform', 'translate(0,'+ -(-20+iR/4) +')') // Push up from center 1/4 of innerRadius
  .attr('text-anchor', 'middle')
  .style('font-size', '1.2em')
  .style('font-weight','bold')
  .text(quota);

//display label & legend
var label = svg.append('text')
  .attr('transform', 'translate('+ (- size) +', -136)')
  .style('font-size', '.9em')
  .text('Cluster name: ' + data.cluster_name);
var legend = svg.append('text')
  .attr('transform', 'translate('+ (size-margin.right*2) +','+ margin.bottom +')')
  .attr('text-anchor', 'middle')
  .style('font-size', '.8em')
  .text('Primary shards / Total shards');


//animation gauge color
function arcTween(transition, newAngle) {
  transition.attrTween('d', function(d) {
    var interpolate = d3.interpolate(d.endAngle, newAngle);
    return function(t) {
      d.endAngle = interpolate(t);
      return arc(d);
    };
  });
}




