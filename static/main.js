// TEST
function addItem(){
  var before_last = $("#sortable li:last")[0];
  var taskname = $('#in_taskname')[0]
  var li = document.createElement("li");
  var taskname_div = document.createElement('div');
  taskname_div.innerHTML = taskname.value;
  li.appendChild(taskname_div);
  before_last.before(li);
  $('#in_taskname').val('');
}

$(document).ready(function(){
var changed = function( event, ui ) {
};
var theone = $("#sortable").sortable({change: changed});
$("#sortable").disableSelection();
















});
