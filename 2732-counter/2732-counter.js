/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let counter = n;
    return function() {
        let temp = counter;
        counter += 1;
        return temp;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */