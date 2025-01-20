type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const memory = new Map();
    return function(...args) {
        const arg_str = JSON.stringify(args);
        if (memory.has(arg_str)) {
            return memory.get(arg_str);
        }
        memory.set(arg_str, fn(...args)); 
        return memory.get(arg_str);
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */