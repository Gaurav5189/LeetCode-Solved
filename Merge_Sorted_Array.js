// 88. Merge Sorted Array (easy)
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    for (let i = nums1.length-1; i>=0; i--) {
        if (nums1[i] !== 0 || i === m-1) {
            break;
        } else {
            nums1.pop()
        }
    }
    nums1.push(...nums2);

    nums1.sort((a, b) => a-b);
};

// alternative solution
var merge = function(nums1, m, nums2, n) {
    nums1.length = m;
    nums1.push(...nums2);

    nums1.sort((a, b) => a-b);
};
