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

// TODO reset the select form if result is not OK
function changeStatus(val, id){
  console.log(val+' '+id);
  $.get('/status/'+id+'/'+val+'/', function(data){
  	console.log(data);
    if (data['result'] == 'OK'){
    	// change the color of the row
    	$('#'+id).children().css('background-color', data['color'])
    }
  })
}

// Main routine
$(document).ready(function(){
$("#ex1").slider({});
var changed = function( event, ui ) {
};
var theone = $("#sortable").sortable({change: changed});
$("#sortable").disableSelection();















});
