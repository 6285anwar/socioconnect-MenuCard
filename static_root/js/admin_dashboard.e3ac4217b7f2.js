$(document).ready(function () {
  $("#dtBasicExample").DataTable({ order: [[0, "desc"]] });
});

// function prop_popup(click=0){

//     var modal = document.getElementById("popup");
//     click += 1;
//     console.log(click)
//     modal.style.display = "block";

//   }

window.onload = function () {
  var button = document.getElementById("prop_id");
  var button2 = document.getElementById("prop_id2");
  var button3 = document.getElementById("prop_id3");

  count = 0;
  button.onclick = function () {
    count += 1;
    if (count % 2 != 0) {
      var modal = document.getElementById("popup");
      modal.style.display = "block";
    } else {
      var modal = document.getElementById("popup");
      modal.style.display = "none";
    }
  };
  count1 = 0;
  button2.onclick = function () {
    count1 += 1;
    if (count1 % 2 != 0) {
      var modal = document.getElementById("popup2");
      modal.style.display = "block";
    } else {
      var modal = document.getElementById("popup2");
      modal.style.display = "none";
    }
  };
  count2 = 0;
  button3.onclick = function () {
    count2 += 1;
    if (count2 % 2 != 0) {
      var modal = document.getElementById("popup3");
      modal.style.display = "block";
    } else {
      var modal = document.getElementById("popup3");
      modal.style.display = "none";
    }
  };
};
