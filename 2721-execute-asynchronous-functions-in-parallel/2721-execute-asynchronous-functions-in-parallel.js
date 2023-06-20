/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */

var promiseAll = async function(functions) {
    const a = functions.map(e=> e())
    return  Promise.all(a).then(data => data).catch(err=> {
        throw err
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */