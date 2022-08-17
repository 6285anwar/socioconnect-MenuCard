window.onload = function(){
var modal = document.getElementById("pop_up");

// // Get the button that opens the modal
// var btn =document.getElementsByClassName('.delete_popup')[0];
// console.log(btn)

// // Get the <span> element that closes the modal
// var span = document.getElementById("close");

// // When the user clicks the button, open the modal 
// btn.onclick = function() {
//   modal.style.display = "block";
// }

// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }

// // When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  
}



};


function delete_popup(){

  var modal = document.getElementById("pop_up");
  
  modal.style.display = "block";

}
function close_popup(){

  var modal = document.getElementById("pop_up");
  
  modal.style.display = "none";

}