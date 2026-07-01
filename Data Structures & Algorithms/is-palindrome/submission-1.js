class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        // Convert to string, remove non-alphanumeric characters, and lowercase it
        let palString = String(s)
            .replace(/[^a-zA-Z0-9]/g, '')
            .toLowerCase(); 
        
        // Loop only through the first half of the cleaned string
        for (let i = 0; i < palString.length / 2; i++) {
            let currLetter = palString[i];
            let endLetter = palString[palString.length - i - 1];
            
            if (currLetter !== endLetter) {
                return false;
            }
        }
        return true;
    }
}
