type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    let timeout;
    return function(...args) {
        if (timeout) {
            clearTimeout(timeout);
        }
        timeout = setTimeout(fn, t, ...args);
    };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */