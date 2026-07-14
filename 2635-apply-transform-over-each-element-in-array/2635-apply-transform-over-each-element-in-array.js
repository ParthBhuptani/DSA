/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

var map = function(arr, fn) {
    for (let i = 0; i < arr.length; ++i) {
        arr[i] = fn(arr[i], i);
    }
    return arr;
};

// const map = (arr, fn) => arr.reduce((prev, curr, idx) => [...prev, fn(curr, idx)], []);