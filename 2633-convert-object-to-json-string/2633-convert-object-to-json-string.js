/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (typeof object === 'string') {
    return `"${object}"`;
  } else if (typeof object === 'number' || typeof object === 'boolean' || object === null) {
    return `${object}`;
  } else if (Array.isArray(object)) {
    const arrayElements = object.map((element) => jsonStringify(element));
    return `[${arrayElements.join(',')}]`;
  } else if (typeof object === 'object') {
    const keys = Object.keys(object);
    const keyValuePairs = keys.map((key) => `"${key}":${jsonStringify(object[key])}`);
    return `{${keyValuePairs.join(',')}}`;
  }
    
};