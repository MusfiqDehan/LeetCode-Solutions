/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    sqrtNum = Math.sqrt(num)

    if (num % sqrtNum === 0)
        return true
    else
        return false    
};