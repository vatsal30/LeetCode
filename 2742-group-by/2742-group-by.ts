interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>
}


Array.prototype.groupBy = function(fn) {
    const obj = {};
    this.forEach((ele) => {
        const id = fn(ele);
        if (id in obj) {
            obj[id].push(ele);
            
        } else {
            obj[id] = [ele];
        }
    });
    return obj;
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */