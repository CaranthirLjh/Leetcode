# https://www.1point3acres.com/bbs/thread-921924-1-1.html

# 给一个列表的paragraphs [ ["word1", "word2"], ["word3", "word4"], ... ] 和整数 width， 返回一个列表类似于：
# ["**********",
# "*   word1 word2   *",
# "*   word3 word4   *",
# "**********"]
# 就是output每个元素的string长度为width + 2，最开始和最后都是填满星号，中间的句子的词用空格相接 然后左右空格填平； 如果paragraph长度超出了，则会新建一行，新建的这行不跟后面的paragraphs元素相连
# 比如word1 +空格 + word2 > width: 那么结果就是
# ["**********",
# "*     word1     *",
# "*     word2     *",
# "*   word3 word4   *",
# "**********"]

class Solution:
    def formParagraphs(self, paragraphs, width):
        ans = []
        for paragraph in paragraphs:
            cur = ""
            for word in paragraph:
                if not cur:
                    if len(word) <= width:
                        cur = word
                else:
                    if len(cur) + 1 + len(word) <= width:
                        cur += " "+word
                    else:
                        gap = width-len(cur)
                        cur = "*"+" "*(gap//2)+cur+" "*(gap-gap//2)+"*"
                        ans.append(cur)
                        cur = word
            if cur:
                gap = width-len(cur)
                cur = "*"+" "*(gap//2)+cur+" "*(gap-gap//2)+"*"
                ans.append(cur)
                cur = word
        return ans

if __name__ == "__main__":
    paragraphs = [ ["word1", "word2"], ["word33", "word4"], ["word555", "word666"] ]
    width = 13
    ans = Solution().formParagraphs(paragraphs,width)
    print(ans)


                

