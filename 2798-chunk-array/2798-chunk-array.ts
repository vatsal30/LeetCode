type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    const ans = [];
    // arr.reduce((acc: any, ele: any, idx) => {
    //     acc.push(ele);
    //     if (acc.length === size || idx == arr.length - 1){
    //         ans.push(acc);
    //         acc = [];
    //     }
    //     return acc;
    // }, []);
    for (let i = 0; i < arr.length; i += size) {
        ans.push(arr.slice(i, i + size));
    }
    return ans;
};
