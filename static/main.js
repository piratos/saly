// main.js
function addItem(){
  var taskname = $('#in_taskname')[0]
  // send api
  $.get('/addItem/'+taskname.value, function(data){
  	console.log(data);
  	if (data=='FAIL'){
  		return;
  	}
  	// create an element from template and append it to the ul
  	var template = $('#li_template').clone();
  	template.attr('id', data);
  	template.children()[0].innerHTML = taskname.value;
  	template.find('*').attr('taskid', data);
  	$('#sortable').append(template);
  	template.removeAttr('hidden');
  	$('#in_taskname').val('');

  })
}

function delItem(id){
	$.get('/delItem/'+id, function(data){
		if (data=='OK'){
			$('#'+id).remove();
		}
	})
}


// Main routine
$(document).ready(function(){
var changed = function( event, ui ) {
};
var theone = $("#sortable").sortable({change: changed});
$("#sortable").disableSelection();















});
