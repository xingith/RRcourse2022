# Exercise 2.2

#Write a function which reverses digits in an integer number (for example 7245 -> 5427). The function should be documented, with type hints, and appropriate comments.

class Solution():
    def reverse_int(self,x):
        rlist = list(str(x))     # int --> str --> list
        if rlist[0] == '-' :     # if negative
            res = int(''.join(rlist[1:][::-1])) * (-1)
        else:
            res = int(''.join(rlist[::-1]))
        return res

if __name__ == '__main__':
    num = input('number for reverse:')
    solu = Solution()
    res = solu.reverse_int(num)
    print('reverse is\n',res)
