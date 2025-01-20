/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filteredArr = [];
    arr.forEach((ele, idx) => {
        if (fn(ele, idx)) {
            filteredArr.push(ele);
        }
    });
    return filteredArr;
};