$(document).ready(function() {
	$.getJSON('../data.json', function(json) {
		output_html = "";
		$.each(json, function(key,value) {
			output_html += "<tr>";
			$.each(value, function(key,value) {
				if(key=='url') {
					url = value;
				} else if(key=='title') {
					output_html += '<td><a href="' + url + '">';
					output_html += value;
					output_html += '</a></td>';

				} else {
					output_html += '<td>'+value[0]+'</td>';
				}
			});
			output_html += "</tr>";
		});
		$('tbody').append(output_html);
		$('#command-table').dataTable({
			"order": [[ 1, "desc" ]],
			"iDisplayLength" : 25
		});
	});

});
