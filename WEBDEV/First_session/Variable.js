// for (var i =0 ; i <2 ; i++){
//     console.log(i);
// }

// {
//     let i = 0;
//     console.log(i);
// }
// {
//     let i = 1 ;
//     console.log(i);
// }                //This is the demonstration of above for loop when we run that how the loop will be executed ; 


// for (var i = 0  ; i<2 ; i++){
//     setTimeout(()=>{
//         console.log(i);
//     },1000)
// }




// if any ASync function takes the callback fucntion will not take promises . e.g.:- settimeout(()=>{
    // console.log("something");
// });


// if theere is two callback with sametimeout then anyone can execute first 
    


// function sayHi(){
//     console.log(name);
//     console.log(age);
//     var name = "chandan";
//     var age = 21;
// }
// sayHi();


// console.log(typeof(new String ("something")))


// if we never mention a keyword before variable the defaut keyword is "var"

//  what is the meaning of Deep copy and shalow Copy . 




// console.log(Number('abc'))


// function sum(...args) {
//     console.log(args);
// }
// sum(1,2,3,4,5);

array = [10,20,30,40,50,60,70];

for(let i = 0 ; i <array.length; i++){
    function forEach(element,index){
        console.log(element);
        console.log(index);
        return; 
    }
    forEach(array[i],i)
}