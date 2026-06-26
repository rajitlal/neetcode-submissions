class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) { const map = {};

    for (const str of strs) {
        // Sort word to create a unique key: 'eat' -> 'aet'
        const sortedKey = str.split('').sort().join('');

        // If key doesn't exist, initialize it with an empty array
        if (!map[sortedKey]) {
            map[sortedKey] = [];
        }

        // Push original word into its anagram group
        map[sortedKey].push(str);
    }

    // Return the grouped arrays
    return Object.values(map);}
}
