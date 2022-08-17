window.onload = function() {

    

    var one = document.getElementById('one');
    var two = document.getElementById('two');
    var three = document.getElementById('three');
    var four = document.getElementById('four');
    var five = document.getElementById('five');
    
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
                
                
                return
            }
           

            case 'two': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.remove('checked');
                four.classList.remove('checked');
                five.classList.remove('checked');
                
                
                return
            }
           
            case 'three': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.add('checked');
                four.classList.remove('checked');
                five.classList.remove('checked');
                
               
                return
            }
           
            case 'four': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.add('checked');
                four.classList.add('checked');
                five.classList.remove('checked');
              
                return
            }
            
    
            case 'five': {
                one.classList.add('checked');
                two.classList.add('checked');
                three.classList.add('checked');
                four.classList.add('checked');
                five.classList.add('checked');
               
                return
            }
            
        }}

    const arr = [one, two, three, four, five]
    arr.forEach(item => item.addEventListener('click', (event)=>
    {
        handleSelect(event.target.id);
    
    }));

    var s1 = document.getElementById('s1');
    var s2 = document.getElementById('s2');
    var s3 = document.getElementById('s3');
    var s4 = document.getElementById('s4');
    var s5 = document.getElementById('s5');
    
    var val1 = document.getElementById("rating_value1").value;
   

    // console.log(document.getElementById('div_id'))
    // console.log(one);

    const handleSelect1 = (selection) => {
        switch(selection){
            case 's1': {
                s1.classList.add('checked');
                s2.classList.remove('checked');
                s3.classList.remove('checked');
                s4.classList.remove('checked');
                s5.classList.remove('checked');
               
                return
            }
           

            case 's2': {
                s1.classList.add('checked');
                s2.classList.add('checked');
                s3.classList.remove('checked');
                s4.classList.remove('checked');
                s5.classList.remove('checked');
                
                
                return
            }
           
            case 's3': {
                s1.classList.add('checked');
                s2.classList.add('checked');
                s3.classList.add('checked');
                s4.classList.remove('checked');
                s5.classList.remove('checked');
                
               
                return
            }
           
            case 's4': {
                s1.classList.add('checked');
                s2.classList.add('checked');
                s3.classList.add('checked');
                s4.classList.add('checked');
                s5.classList.remove('checked');
              
                return
            }
            
    
            case 's5': {
                s1.classList.add('checked');
                s2.classList.add('checked');
                s3.classList.add('checked');
                s4.classList.add('checked');
                s5.classList.add('checked');
                
                return
            }
            
        }}

    const arr1 = [s1, s2, s3, s4, s5]
    arr1.forEach(item => item.addEventListener('click', (event)=>
    {
        handleSelect1(event.target.id);
    
    }));

    var r1 = document.getElementById('r1');
    var r2 = document.getElementById('r2');
    var r3 = document.getElementById('r3');
    var r4 = document.getElementById('r4');
    var r5 = document.getElementById('r5');
    
    var val2 = document.getElementById("rating_value2").value;
   

    // console.log(document.getElementById('div_id'))
    // console.log(one);

    const handleSelect2 = (selection) => {
        switch(selection){
            case 'r1': {
                r1.classList.add('checked');
                r2.classList.remove('checked');
                r3.classList.remove('checked');
                r4.classList.remove('checked');
                r5.classList.remove('checked');
                
                
                return
            }
           

            case 'r2': {
                r1.classList.add('checked');
                r2.classList.add('checked');
                r3.classList.remove('checked');
                r4.classList.remove('checked');
                r5.classList.remove('checked');
                
                
                return
            }
           
            case 'r3': {
                r1.classList.add('checked');
                r2.classList.add('checked');
                r3.classList.add('checked');
                r4.classList.remove('checked');
                r5.classList.remove('checked');
                
                
                return
            }
           
            case 'r4': {
                r1.classList.add('checked');
                r2.classList.add('checked');
                r3.classList.add('checked');
                r4.classList.add('checked');
                r5.classList.remove('checked');
                
                return
            }
            
    
            case 'r5': {
                r1.classList.add('checked');
                r2.classList.add('checked');
                r3.classList.add('checked');
                r4.classList.add('checked');
                r5.classList.add('checked');
               
                return
            }
            
        }}

    const arr2 = [r1, r2, r3, r4, r5]
    arr2.forEach(item => item.addEventListener('click', (event)=>
    {
        handleSelect2(event.target.id);
    
    }));
    
    var c1 = document.getElementById('c1');
    var c2 = document.getElementById('c2');
    var c3 = document.getElementById('c3');
    var c4 = document.getElementById('c4');
    var c5 = document.getElementById('c5');
    
    var val3 = document.getElementById("rating_value3").value;
   

    // console.log(document.getElementById('div_id'))
    // console.log(one);

    const handleSelect3 = (selection) => {
        switch(selection){
            case 'c1': {
                c1.classList.add('checked');
                c2.classList.remove('checked');
                c3.classList.remove('checked');
                c4.classList.remove('checked');
                c5.classList.remove('checked');
                
                
                return
            }
           

            case 'c2': {
                c1.classList.add('checked');
                c2.classList.add('checked');
                c3.classList.remove('checked');
                c4.classList.remove('checked');
                c5.classList.remove('checked');
                
                
                return
            }
           
            case 'c3': {
                c1.classList.add('checked');
                c2.classList.add('checked');
                c3.classList.add('checked');
                c4.classList.remove('checked');
                c5.classList.remove('checked');
                
               
                return
            }
           
            case 'c4': {
                c1.classList.add('checked');
                c2.classList.add('checked');
                c3.classList.add('checked');
                c4.classList.add('checked');
                c5.classList.remove('checked');
               
                return
            }
            
    
            case 'c5': {
                c1.classList.add('checked');
                c2.classList.add('checked');
                c3.classList.add('checked');
                c4.classList.add('checked');
                c5.classList.add('checked');
                
                return
            }
            
        }}

    const arr3 = [c1, c2, c3, c4, c5]
    arr3.forEach(item => item.addEventListener('click', (event)=>
    {
        handleSelect3(event.target.id);
    
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

document.getElementById("rating_value1").value = btn.value;

}
function rateValue2(btn) {
  ids = btn.id
//   co

document.getElementById("rating_value2").value = btn.value;

  
}
function rateValue3(btn) {
  ids = btn.id
//   co

document.getElementById("rating_value3").value = btn.value;

  
}





// $(document).ready(function() {
//     $("#one").hover(function() {
        
//         $("#one").css("color", "yellow");

//     });
//     $("#two").hover(function() {
        
//         $("#one, #two").css("color", "yellow");

//     });
//     $("#three").hover(function() {
        
//         $("#one, #two, #three").css("color", "yellow");

//     });
//     $("#four").hover(function() {
        
//         $("#one, #two, #three, #four").css("color", "yellow");

//     });
//     $("#five").hover(function() {
        
//         $("#one, #two, #three, #four, #five").css("color", "yellow");

//     });
//   });
