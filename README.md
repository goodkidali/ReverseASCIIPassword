# ReverseASCIIPassword

#### Problem:
Aman, who is working at a software company forgot his password of his LinkedIn account, but he knows the ASCII values of his password in reverse order. Help Aman to find his password.

#### Solution:
To decode the password, first reverse the string of digits, then successively pick valid values from the string and convert them to their ASCII equivalents. 
Some of the values will have two digits, and others three. Use the ranges of valid values when decoding the string of digits.

#### Constraints:
- 1 <= |s| <= 10^5
- s[i] is an ascii character in the range [A-Za-z] or a space character

The password only has alphabets and blank spaces.

- The ASCII value of 'A-Z' is 65-90
- The ASCII value of 'a-z' is 97-122
- The ASCII value of 'space' is 32
