var TimeLimitedCache = function() {
     this.memo=new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
        let time=Date.now()
        if(this.memo.has(key))
        {
                this.memo.set(key,{value:value,exp:time+duration})
                return true;
        }
        else{
                this.memo.set(key,{value:value,exp:time+duration})
                return false; 
        }
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    let time=Date.now();

    if(this.memo.has(key))
        if(this.memo.get(key).exp>time)
             return this.memo.get(key).value;
        else{
            this.memo.delete(key);
            return -1;
        }
     return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let co=0;
    let time=Date.now();
                for(key of this.memo.values())
                        if(key.exp>time)co++
    return co;
};
