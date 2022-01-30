let fs = require("fs");

const readFileLines = (filename) =>
    fs.readFileSync(filename).toString("UTF8").split("\n");

let arr = readFileLines("MachineLearningModel/rules.txt");
//To make array of objects
var arr_obj = [];
var len = arr.length;
for (var m = 0; m < len; m++) {
    let obj={FirstMovie:1,RecommendedMovie:1,lift:1};
    // To extract FirstMovie
    let temp;
    for(let i=2; i<arr[m].length-1; i++) {
        if(arr[m].substr(i,4)===`', '`||arr[m].substr(i,4)===`', "`||arr[m].substr(i,4)===`", '`||arr[m].substr(i,4)===`", "`)
        {
            temp=i;
            // console.log(i);
            break;
        }
    }
    obj.FirstMovie=arr[m].substr(2,temp-2);
    // To extract SecondMovie
    let temp2;
    for(let i=temp+1; i<arr[m].length-1; i++) {
        if(arr[m].substr(i,3)===`', `||arr[m].substr(i,3)===`", `)
        {
            temp2=i;
            // console.log(i);
            break;
        }
    }
    obj.RecommendedMovie=arr[m].substr(temp+4,temp2-temp-4);
    //To extract lift
    obj.lift=arr[m].substr(temp2+3,arr[m].length-temp2-5);
    // console.log(obj);
    arr_obj.push({
        FirstMovie: obj.FirstMovie,
        RecommendedMovie: obj.RecommendedMovie,
        lift: obj.lift
    });
}
console.log(arr_obj);
module.exports = arr_obj;
