/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    var ans = [];
    var ind = 0;
    while(ind < arr.length){
        ans.push(arr.slice(ind,ind+size));
        ind+=size;
    }
    return ans;
};