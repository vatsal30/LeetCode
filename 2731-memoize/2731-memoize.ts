type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const memory = new Map<string, number>();
    return function(...args) {
        const arg_str: string = JSON.stringify(args);
        if (memory.has(arg_str)) {
            return memory.get(arg_str);
        }
        const result: number = fn(...args)
        memory.set(arg_str, result); 
        return result;
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