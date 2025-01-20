/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const new_arr = [];
    arr.forEach((ele, idx) => {
        new_arr.push(fn(ele, idx));
    });
    return new_arr;
};