/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    let ans = {};

     for( let item of this ) {
          let key = fn(item);
          if( ans.hasOwnProperty(key)) {
            ans[key].push(item);
          }else {
             ans[key] = [item]
          }
     }

     return ans;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */