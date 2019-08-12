//list of all users from elasticsearch cdae index with their worked hours
//from cdae.html
users_list = JSON.parse(users_list);

var users = [];

$.each(users_list, function(i,d){
	var user = {};
  user.name = d.user;
	user.hours = d.hours;
	user.color='#029302';
	users.push(user);
});
//console.log(users.length);

//get maximum percentage
var max_data = null;
$.each(users, function(i,d){
    if(!max_data || d.hours > max_data){
        max_data = d.hours;
    }
});
//console.log(max_data);
var charWidth = $('.width12').width() - 24;//dynamic Bootstrap
var margin = {left:70, right:40, top:60, bottom:160}
var height = 500 - margin.top - margin.bottom;
var width = charWidth - margin.left - margin.right;	
var animateDuration = 700;
var animateDelay = 40;

//width and height dynamic scales for the svg canvas
var xScale = d3.scale.ordinal()
	.domain(d3.range(0, users.length))
	.rangeBands([0, width]);

var yScale = d3.scale.linear()
	.domain([0, max_data])
	.range([0, height]);

//dynamic colors
/*faire 3 ranges de colors: green, orange & red*/
var colors = d3.scale.linear()
	.domain([0, max_data])
	.range(['gold','darkgreen']);

//tooltip for each bar
var tooltip = d3.select('body')
	.append('div')
		.style('position','absolute')
		.style('background','lightsteelblue')
		.style('padding','5px 15px')
		.style('border','1px solid white')
		.style('border-radius','5px')
		.style('opacity','0')
		.style('font-size', '.8em');


//definition of the barchart
var myChart = d3.select('#barchart')
	.append('svg')
		.attr('width', width + margin.left + margin.right)
		.attr('height', height + margin.top + margin.bottom)
		.style('background', '#abcbcc')
		.append('g')
		.attr('transform', 'translate('+ margin.left +','+ margin.top +')')
		.selectAll('rect')
			.data(users)
			.enter().append('rect')
				//.attr('test_d', d => console.log(d.color))
				.style('fill', (d,i) => colors(d.hours))
				.attr('fill', d => d.color)
				.attr('width', xScale.rangeBand())
				.attr('x', (d,i) => xScale(i))
				.attr('height', 0)				
				.attr('y', height)
				.on('mouseover', function(d){
					tooltip.transition()
						.style('opacity', 1);
					tooltip.html(d.name + ': ' + d.hours + ' h')
						.style('left', (d3.event.pageX) + 'px')
						.style('top', (d3.event.pageY) + 'px');
					d3.select(this)
						.style('opacity', 0.5)
				})
				.on('mouseout', function(d){
					tooltip.transition()
						.style('opacity', 0);
					d3.select(this)
						.style('opacity', 1)
				});

//animation at loading page
myChart.transition()
	//.attr('test_d', (d,i) => console.log(typeof i))
	.attr('height', d => yScale(d.hours))
	.attr('y', d => height - yScale(d.hours))
	.duration(animateDuration)
	.delay((d,i) => i * animateDelay)
	.ease('elastic');


//horizontal dynamic scale for axe and guide of the svg canvas
var xScale = d3.scale.ordinal()
	.domain(users.map(d => d.name))
	.rangeBands([0, width]);
//horizontal dynamic axis
var xAxis = d3.svg.axis()
	.scale(xScale)
	.orient('bottom')
	.tickValues(users.map(d => d.name));

	//console.log(hAxis.tickValues());
//horizontal dynamic guide
var xGuide = d3.select('svg')
	.append('g')
		xAxis(xGuide)
		xGuide.attr('transform', 'translate('+ margin.left +','+ (height + margin.top) +')')
		xGuide.selectAll('path')
			.style('fill','none')
			.attr('stroke','black')
		xGuide.selectAll('line')
			.attr('stroke','black')
		xGuide.selectAll('text')  
      .style('text-anchor', 'end')
      .style('font-size', '.7em')
      .style('cursor','default')
      .attr('dx', '-.8em')
      .attr('dy', '.15em')
      .attr('transform', 'rotate(-65)')
      .data(users)
			.on('mouseover', function(d){
			  tooltip.transition()
				  .style('opacity', 1);
			  tooltip.html(d.name + ': ' + d.hours + ' h')
					.style('left', (d3.event.pageX) + 'px')
					.style('top', (d3.event.pageY) + 'px');
				d3.select(this)
					.style('opacity', 0.5)
			})
			.on('mouseout', function(d){
				tooltip.transition()
					.style('opacity', 0);
				d3.select(this)
					.style('opacity', 1)
			});
      
//vertical dynamic scale for axe and guide of the svg canvas
var yScale = d3.scale.linear()
	.domain([0, max_data])
	.range([height, 0]);
//vertical dynamic axis
var yAxis = d3.svg.axis()
	.scale(yScale)
	.orient('left')
	.ticks(10)
	.tickPadding(5);
//vertical dynamic guide
var yGuide = d3.select('svg')
	.append('g')
		yAxis(yGuide)
		yGuide.attr('transform', 'translate('+ margin.left +', '+ margin.top +')')
		yGuide.selectAll('path')
			.style('fill','none')
			.attr('stroke','black')
		yGuide.selectAll('line')
			.attr('stroke','black')
		yGuide.selectAll('text')  
     .style('font-size', '.7em');
//vertical axis legend
yGuide.append('g')
  .append('text')
    .attr("y", -12)
    .style('font-size', '.9em')
    .text('Nb heures travaillées');
