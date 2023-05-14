/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    let params = []
    return function curried(...args) {
        params.push(...args);
        if (params.length == fn.length) {
            return fn(...params);
        }
        return curried;
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
