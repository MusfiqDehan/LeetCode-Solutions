/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    s = s.split(" ");
    console.log(s);
    s = s.map(word => word.split("").reverse().join(""));
    console.log(s);
    return s.join(" ");
};