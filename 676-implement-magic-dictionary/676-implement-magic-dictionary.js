/**
 * Initialize your data structure here.
 */
var MagicDictionary = function() {
    this.set = new Set();
};

/** 
 * @param {string[]} dictionary
 * @return {void}
 */
MagicDictionary.prototype.buildDict = function(dictionary) {
    for (const word of dictionary) {
        this.set.add(word);
    }
};


/** 
 * @param {string} searchWord
 * @return {boolean}
 */
MagicDictionary.prototype.search = function(searchWord) {
    
    for (const compareWord of this.set) {
        if (compareWord.length != searchWord.length) continue;
        
        let count = 0;
        
        for (let i = 0; i < searchWord.length; i++) {
            const searchChar = searchWord.charAt(i);
            const compareChar = compareWord.charAt(i);

            if (searchChar != compareChar) count++;
            if (count > 1) continue;
        }
    
        if (count === 1) return true;
    }
   
    return false;
};

/** 
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */