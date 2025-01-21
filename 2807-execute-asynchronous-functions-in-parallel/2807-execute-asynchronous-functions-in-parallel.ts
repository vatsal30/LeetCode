type Fn<T> = () => Promise<T>

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
    const totalFn = functions.length;
    return new Promise((resolve, reject) => {
        const results = [];
        let resolvedCount = 0;
        const hasAllPromiseResolved = () => {
            if (resolvedCount == totalFn) {
                resolve(results);
            }
        }
        functions.forEach((fn, idx) => {
            fn().then((data) => {
                results[idx] = data;
                resolvedCount += 1;
                hasAllPromiseResolved();
            }).catch((err) => {
                reject(err);
            });
        });
    });

};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */