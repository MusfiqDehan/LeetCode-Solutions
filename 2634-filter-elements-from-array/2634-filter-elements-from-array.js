/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

var filter = function(arr, fn) {
    let newArr = [];
    arr.forEach((element,index)=>{
        if(fn(element,index)){
            newArr.push(element);
        }
    })
    return newArr;
};