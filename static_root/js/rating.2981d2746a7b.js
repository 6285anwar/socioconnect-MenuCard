window.onload = function() {

    var ones = document.querySelectorAll("[id='one']")

    var one = document.getElementById('one');
    var two = document.getElementById('two');
    var three = document.getElementById('three');
    var four = document.getElementById('four');
    var five = document.getElementById('five');
    var above = document.getElementById("above")
    var below = document.getElementById("below")
    var val = document.getElementById("rating_value").value;
   

    // console.log(document.getElementById('div_id'))
    // console.log(one);

    const handleSelect = (selection) => {
        switch(selection){
            case 'one': {
                one.classList.add('checked');
                two.classList.remove('checked');
                three.classList.remove('checked');
                four.classList.remove('checked');
                five.classList.remove('checked');
                above.style.display = "none";
                below.style.display = "block";
                return
            }
           

            case 'two': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.remove('checked');
                four.classList.remove('checked');
                five.classList.remove('checked');
                above.style.display = "none";
                below.style.display = "block";
                return
            }
           
            case 'three': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.add('checked');
                four.classList.remove('checked');
                five.classList.remove('checked');
                above.style.display = "none";
                below.style.display = "block"
                return
            }
           
            case 'four': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.add('checked');
                four.classList.add('checked');
                five.classList.remove('checked');
                below.style.display = "none";
                above.style.display = "block";
                return
            }
            
    
            case 'five': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.add('checked');
                four.classList.add('checked');
                five.classList.add('checked');
                below.style.display = "none";
                above.style.display = "block";
                return
            }
            
        }}

    const arr = [one, two, three, four, five]
    arr.forEach(item => item.addEventListener('click', (event)=>
    {
        handleSelect(event.target.id);
    
    }));


};

function rateValue(btn) {
  ids = btn.id
//   co

document.getElementById("rating_value").value = btn.value;

  
}
function rateValue1(btn) {
  ids = btn.id
//   co

document.getElementById("feed1").value = btn.value;

}
function rateValue2(btn) {
  ids = btn.id
//   co

document.getElementById("feed2").value = btn.value;

  
}
function rateValue3(btn) {
  ids = btn.id
//   co

document.getElementById("feed3").value = btn.value;

  
}
function rateValue4(btn) {
  ids = btn.id
//   co

document.getElementById("feed4").value = btn.value;


var closePopup1 = document.getElementById('close-popup-1')

openPopup1.addEventListener('click', () => {
	popup1.style.display = "block";
})

closePopup1.addEventListener('click', () => {
	popup1.style.display = "none";
  one3.classList.add('blur-in');

})

}



function openForm() {
  document.getElementById("myForm").style.display = "block";
    var rating_val = document.getElementById("rating_value").value
    var main = document.getElementById("main_main")
    var less = document.getElementById("less")
    var four = document.getElementById("fourstar")
    var closePopup1 = document.getElementById('close-popup-1')
    
    // closePopup1.addEventListener('click', () => {
    //   less.style.display = "none";
    //   four.style.display = "none";
      
    // })

    if (rating_val>=4){
      less.style.display = "none";

      four.style.display = "block";

    }
    else{
      less.style.display = "block";
      four.style.display = "none";

    }
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }

  function feedback() {
    document.getElementById("add_more").style.display = "block";
  }


  function checkit(){

    modal=document.getElementById("modal")
    modal_1 = document.getElementById("modal")
    modal.style.display = "block";
    modal_1.style.display="block";
    

  }

  function rateus() {
   
  var above = document.getElementById("above")
  var below = document.getElementById("below")
  var val = document.getElementById("rating_value").value;
  if (val>=4){ 
    above.style.display = "block";
    below.style.display = "none";
    
  }else{
    above.style.display = "none";
    below.style.display = "block";
  }

}