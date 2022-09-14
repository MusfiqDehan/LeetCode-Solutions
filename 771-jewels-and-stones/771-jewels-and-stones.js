/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */

var numJewelsInStones = function(J, S) {
    let pattern = new RegExp(J.split('').join('|'), 'g');
    return (S.match(pattern) || []).length;
};
    
