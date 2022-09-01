# https://www.1point3acres.com/bbs/thread-921833-1-1.html

# matrix, 里面包含"F", ".", "#", F会往下滑, 遇到"#"会停止, F可以连成不规则的现状, 类似与俄罗斯方块.

class Solution:
    def tetris(self, matrix):
        row,col = len(matrix),len(matrix[0])
        dis = row
        obj = []
        for j in range(col):
            block = row-1
            for i in range(row-1,-1,-1):
                if matrix[i][j] == "#":
                    block = row-1
                elif matrix[i][j] == "F":
                    obj.append((i,j))
                    dis = min(dis,i-block)
                    if dis == 0:
                        return matrix

        for x,y in obj:
            matrix[x][y] = "."
        
        for x,y in obj:
            matrix[x+dis][y] = "F"
        
        return matrix

if __name__ == "__main__":
    matrix = [
        ["F","F",".","."],
        [".","F",".","."],
        ["F","F",".","."],
        [".","F","F","F"],
        ["#","F",".","."],
        [".","F",".","."],
        ["F","F",".","#"],
        [".",".","#","."],
        [".",".",".","."]
    ]

    ans = Solution().tetris(matrix)
    print(ans)
