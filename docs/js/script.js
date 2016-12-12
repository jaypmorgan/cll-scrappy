$(document).ready(function() {
	$.getJSON('../data.json', function(json) {
		output_html = "";
		$.each(json, function(key,value) {
			output_html += "<tr>";
			$.each(value, function(key,value) {
				output_html += "<td>";
				output_html += value;
				output_html += "</td>";
			});
			output_html += "</tr>";
		});
		$('tbody').append(output_html);
		$('#command-table').dataTable({
			"order": [[ 1, "desc" ]]
		});
	});

});
