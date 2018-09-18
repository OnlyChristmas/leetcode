'''


Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

'''



class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Approach #1
        answer = []
        for i in range(1,n+1):
            ans = ''
            if i % 3 == 0:
                ans = "Fizz"
                if i % 5 == 0:
                    ans += 'Buzz'
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            answer.append(ans)
        return answer
