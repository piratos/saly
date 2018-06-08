// TEST
function addItem(){
  var before_last = $("#sortable li:last")[0];
  var taskname = $('#in_taskname')[0]
  var li = document.createElement("li");
  var taskname_div = document.createElement('div');
  taskname_div.innerHTML = taskname.value;
  li.appendChild(taskname_div);
  // send api
  $.get('/addItem/'+taskname.value, function(data){
  	console.log(data);
  	if (data=='FAIL'){
  		return;
  	}
  	taskname_div.style.backgroundColor =  '#ea4e4e';
  	taskname_div.id = data;
  	var task_div1 = document.createElement('div')
  	var task_div2 = document.createElement('div')
  	task_div1.style.backgroundColor =  '#ea4e4e';
  	task_div2.style.backgroundColor =  '#ea4e4e';
  	task_div1.innerHTML = 'stuck';
  	task_div2.innerHTML = '0';
  	taskname_div.className = 'divsin';
  	task_div1.className = 'divsin';
  	task_div2.className = 'divsin';
  	li.appendChild(task_div1);
  	li.appendChild(task_div2);

  })
  before_last.after(li);
  $('#in_taskname').val('');
}

function delItem(id){
	$.get('/delItem/'+id, function(data){
		if (data=='OK'){
			$('#'+id).remove();
		}
	})
}

$(document).ready(function(){
var changed = function( event, ui ) {
};
var theone = $("#sortable").sortable({change: changed});
$("#sortable").disableSelection();
















});
