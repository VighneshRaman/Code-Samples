$(document).ready(function() {
	$("#results").click(function() {
		//Hide Answer Key:
		$("#closing").hide();
		//Check if all questions are answered
		if (!$("input[@name=q1]:checked").val() ||
			!$("input[@name=q2]:checked").val() ||            
			!$("input[@name=q3]:checked").val() ) {alert("You're not done yet!");}        
		else {
			//Variables to be displayed When question is answere incorrectly:            
			var cat1name = "1";
			var cat2name = "2";
			var cat3name = "3";
			//Define the Correct Answers for Each Question
			//Check if questions are answered incorrectly.
			var cat1 = ($("input[@name=q1]:checked").val() != "a");
			var cat2 = ($("input[@name=q2]:checked").val() != "b");
			var cat3 = ($("input[@name=q3]:checked").val() != "c");
			var cat4 = (!cat1 && !cat2 && !cat3);
			//Show Catergory list & Display Score:
			var categories = [];
			var total = 5;
			if (cat1) { categories.push(cat1name) };
			if (cat2) { categories.push(cat2name) };
			if (cat3) { categories.push(cat3name) };

			if (categories.length < 1) {var catStr = 'You answered all questions correctly!';}
			else {var catStr = 'You answered the following questions incorrectly: ' + categories.join(', ') + '\n';}

			var score = total - categories.length;
			var scorestr = 'Total Score: ' + score + '/' + total;

			$("#categorylist").text(catStr);
			$("#categorylist").show("slow");
			$("#tally").text(scorestr);
			$("#tally").show("slow");

		}
    });
	//Show Answer Key:
	$("#key").click(function() {
		$("#category1").show("slow");
		$("#category2").show("slow");
		$("#category3").show("slow");
		{ $("#closing").show("slow"); };
	});
});