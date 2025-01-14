// ob = new Object();
// ob.name = "harshdeep";
// ob.age = 21;
// ob.address= "moraj riverside park takka panvel";

// // for(x in ob){
// //     console.log(ob[x]);
// // }

// console.log(JSON.stringify(ob));


// let name = "harshdeep singh"
// console.log(`Hello ${name}`)


// let name = "harshdeep";
// console.log(name.slice(2,3));


// functions
// let name = "harsh";
// function myfunc(name){
//     console.log(name);
// };

// // arrow functiono

// const f = (name)=>{
//     console.log(name);
// }
//
// console.log(((name)=>name+"deep")(name));


// function Person(name,age,location){
//     this.name = name,
//     this.age = age,
//     this.location = location,
//     this.sayname = ()=>this.name
// };

// var p1 = new Person("harshdeep",21,"Mumbai");
// console.log(p1.sayname());


// class Person{
//     constructor(name,age,location){
//         this.name = name,
//         this.age =age,
//         this.location
//     }
//     sayname(){
//         return this.name;
//     };
// }
// class alive{
//     constructor()
// }
// var add = (function(){
//     let x =0;
//     return function(){x++;return x;}
// })();
// var fetchData = ()=>{
//     return "harshdeep singh";
// };
// function getdata(time,func,func2){
//     let x = setTimeout(time,func2);
//     func(x);
// }
// function printName(str){
//     console.log(str)
// }
// function getData(){
//     return"    harshdeep singh      ";
// }
// //simulating sever response
// function server(t,callback){
//     setTimeout(()=>{
//         let result = getData();
//         callback(result);
//     },t)
// }

// function processing(time,callback){
//     setTimeout(()=>{
//         callback(output.trim);
//     },time)
// }

// function printing(time){
//     setTimeout(()=>{
//         console.log(result)
//     },time)
// }

// server(100,(result)=>{
//     processing(100,(result)=>{
//         printing(100,result);
//     })
// })


//promise chaining


// const p2 = new Promise((resolve)=>{
//     resolve(" I am learning")
// })

// const p3 = new Promise((resolve)=>{
//     resolve(" promises in JavaScript")
// })

// p.then((val)=>{
//     let res = val
//     p2.then((val)=>{
//         res+=val
//         p3.then((val)=>{
//             console.log(res+val)
//         })
//     })
// })

// const p = new Promise((resolve)=>{
//     resolve("hi there")
// })

// console.log(p)



// const p1 = new Promise((resolve)=>{
//     resolve("hi There")
// })

// const p2 = new Promise((resolve)=>{
//     resolve(" I am learning")
// })

// const p3 = new Promise((resolve)=>{
//     resolve(" promises in JavaScript")
// })


// p1.then((val)=>{
//     return p2.then((val1)=>{
//         return val+val1
//     })
// })
// .then((intres)=>{
//     return p3.then((val)=>{
//         intres+val
//     })
// })
// .then

// const p1 = new Promise((resolve)=>{
//     resolve("harsh")
// })

// p1.then((val)=>{
//     return val+" deep"
// })
// .then((val)=>{
//     reject("harsh")
// })
// .then((val)=>{
//     console.log(val)
// },(val)=>{console.log(val)})



// const promise1 = Promise.resolve(3);
// const promise2 = 42;
// const promise3 = new Promise((resolve, reject) => {
//   setTimeout(resolve, 100, 'foo');
// });
// const megaPromise = Promise.all([promise1, promise2, promise3]).then((values) => {
//   return values
// });

// console.log(megaPromise)
// setTimeout(()=>console.log(megaPromise),2000)


//Create a promise that simulates fetching user data (e.g., { name: "Alice", age: 25 }) after 3 seconds.

// function Fetch(){
//     return new Promise((resolve)=>{
//         setTimeout(()=>{
//             resolve({ name: "Alice", age: 25 })
//         },3000)
//     })
// }

// const result = Fetch()
// result.then((val)=>{
//     console.log(val?.name)
//     console.log(val?.age)
// })

// function meh(){
//     let count=0;
//     if(count<3){
//         return ()=>{
//             console.log(count)

//             count+=1;
//         }
//     }
//     else{
//         console.log("no retry")
//     }
// }
// const func = meh()
// func()
// func()
// func()
// func()
// func()
// func()

// function netReq(){
//     return new Promise((reject)=>{
//         reject("naah")
//     })
// }    

// function retryHandler(netReq){
//     let count=0;
//     const innerFunction=()=>{
//         if(count<3){
//             count+=1
//             return netReq()
//                 .then((val)=>{
//                     return val;
//                 },(val)=>{
//                     setTimeout(innerFunction,2000)
//                 })
//         }
//         else{
//             return "retries exceeded";
//         }
//     }
//     return innerFunction
// }

// const request = retryHandler(netReq);
// request().then((val)=>{
//     console.log(val)
// }).catch((val)=>{
//     console.log(val)
// })

// const np = new Promise((resolve)=>{
//     setTimeout(()=>{
//         console.log("heheh")
//         resolve("done")
//     },2000)
// })

// np.then((val)=>{
//     console.log(val)
// })

