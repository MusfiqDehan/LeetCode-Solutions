/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let timerId = null;
    let params = null;
    let called = false;
    let func = function(...args) {
        params = args;
        if (timerId !== null){
            called = true;
            return;
        }
        fn(...params);
        timerId = setTimeout(()=>{
            timerId = null;
            if (called){
                called = false;
                func(...params);
            }

        }, t);
    }

  return func;
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */