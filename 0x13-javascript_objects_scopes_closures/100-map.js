#!/usr/bin/node
// maps an array, multiplying each element by its index
const list = require('./100-data').list;
const mapped = list.map(function (value, index) { return value * index; });
console.log(list);
console.log(mapped);
