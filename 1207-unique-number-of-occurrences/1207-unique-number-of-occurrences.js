/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    const myObj = {};
    
    for(let item of arr) {
        myObj[item] = myObj[item] ? ++myObj[item] : 1;
    }
    
    const result = Object.values(myObj);
    
    return result.length == new Set(result).size
};
