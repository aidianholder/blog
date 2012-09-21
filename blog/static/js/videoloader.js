$(document).ready(function(){
			$(".show").colorbox({width:function(){
				viewport = $(window).width();
				if (viewport > 600) {width = "540"}
				else {width = "340"}
				return width;
				}
				});
			
			$("#midway").colorbox({title:"Midway Mayhem", innerWidth:"520", innerHeight:"640", iframe:true});
			
			$("#bombs").colorbox({title:"Bombs and Breakers", innerWidth:"520", innerHeight:"570", iframe:true});
			
			$("#faceoff").colorbox({title:"Final Face Off", innerWidth:"520", innerHeight:"670", iframe:true});
			
			$("#gasleak").colorbox({title:"Late Breaking", innerWidth:"520", innerHeight:"540", iframe:true});
			
			
			$("#sizzle").colorbox({title:"Summer Sizzle", innerWidth:"520", innerHeight:"550", iframe:true});
			
			$("#storm_chasing").colorbox({title:"Storm Chasing", innerWidth:"520", innerHeight:"640", iframe:true});
			
			$("#whales").colorbox({title:"Saving the Whales", innerWidth:"520", innerHeight:"570", iframe:true});
			
			$("#grass_fires").colorbox({title:"Grass Fires", innerWidth:"520", innerHeight:"560", iframe:true});
			
});