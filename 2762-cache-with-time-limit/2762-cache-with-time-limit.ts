class TimeLimitedCache {
    keyValue: any = {};

    constructor() {
       this.keyValue = {};
    }
    
    set(key: number, value: number, duration: number): boolean {
        let isPresent = false;
        if (key in this.keyValue) {
            const data = this.keyValue[key];
            clearTimeout(data[2]);
            isPresent = true;
        }
        const timeout = setTimeout(() => {
            const data = this.keyValue[key];
            data[1] = 0;
            this.keyValue[key] = data;
        }, duration);
        this.keyValue[key] = [value, 1, timeout];
        return isPresent;
    }
    
    get(key: number): number {
        if (key in this.keyValue) {
            const data = this.keyValue[key];
            return data[1] ? data[0] : -1;
        }
        return -1;
    }
    
    count(): number {
        let cnt = 0;
        for (const key in this.keyValue) {
            if (this.keyValue[key][1]) {
                cnt += 1;
            }
        }
        return cnt;
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */