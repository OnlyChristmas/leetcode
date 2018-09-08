'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".


Note:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

'''



class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """



        # method one   不够简洁,输入构造麻烦
        # ref = {'a':".-",
        #        "b":"-...",
        #        "c":"-.-.",
        #        "d":"-..",
        #        "e":".",
        #        "f":"..-.",
        #        "g":"--.",
        #        "h":"....",
        #        "i":"..",
        #        "j":".---",
        #        "k":"-.-",
        #        "l":".-..",
        #        "m":"--",
        #        "n":"-.",
        #        "o":"---",
        #        "p":".--.",
        #        "q":"--.-",
        #        "r":".-.",
        #        "s":"...",
        #        "t":"-",
        #        "u":"..-",
        #        "v":"...-",
        #        "w":".--",
        #        "x":"-..-",
        #        "y":"-.--",
        #        "z":"--.."}
        # res = []
        # for word in words:
        #     s = ''
        #     for i in  word:
        #         s += ref.get(i)
        #     res.append(s)
        # return len(set(res))



        # method two   用ord()函数求出a的ASCII值, chr() 是将ASCII值变为字符.  ord('a') = 97 ,   ord("A") = 65


        ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        return len(set("".join(ref[ord(s) - 97] for s in word) for word in words))
