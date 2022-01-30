let fs = require("fs");

const readFileLines = (filename) =>
    fs.readFileSync(filename).toString("UTF8").split("\n");

let arr = readFileLines("MachineLearningModel/rules.txt");

module.exports = arr;
