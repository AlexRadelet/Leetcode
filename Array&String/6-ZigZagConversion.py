class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i =0
        d = 1 #Going down ( -1 to going up)
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i == 0:
                d =1
            elif i == numRows - 1:
                d = -1
            i +=d

        ret = ''
        for i in range(numRows):
            ret += ''.join(rows[i])

        return ret



# Time : O( r * n)
# Space : O( n+ r)