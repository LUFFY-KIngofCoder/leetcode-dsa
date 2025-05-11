class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri =  []

        for i in range(numRows):
            l = []
            for j in range(i+1):            
                if j!=i and j!=0:
                    print(i,j)
                    val = tri[i-1][j-1]+tri[i-1][j]
                    l.append(val)
                else:
                    print(i,j)
                    l.append(1)
            tri.append(l) 
        return tri
