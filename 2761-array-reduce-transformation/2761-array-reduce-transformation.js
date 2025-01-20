/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let ans = init;
    nums.forEach((ele) => {
        ans = fn(ans, ele);
    });
    return ans;
};