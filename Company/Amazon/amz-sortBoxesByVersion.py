# https://www.1point3acres.com/bbs/thread-922190-1-1.html

class Solution:
    def merge_sort(self, boxes):
        ans = []
        if len(boxes) == 1:
            return boxes
        mid = len(boxes)//2
        left = self.merge_sort(boxes[:mid])
        right = self.merge_sort(boxes[mid:])
        l,r = 0,0
        ll,lr = len(left),len(right)
        while(l<ll or r<lr):
            if l == ll:
                ans.append(right[r])
                r+=1
            elif r == lr:
                ans.append(left[l])
                l+=1
            else:
                if left[l][1]<right[r][1]:
                    ans.append(left[l])
                    l+=1
                elif left[l][1]>right[r][1]:
                    ans.append(right[r])
                    r+=1
                else:
                    if left[l][0]<right[r][0]:
                        ans.append(left[l])
                        l+=1
                    else:
                        ans.append(right[r])
                        r+=1
        return ans


    def sortBoxesByVersion(self, boxList):
        new_version = []
        old_version = []

        for ind,box in enumerate(boxList):
            _box = box.split(" ")
            idt = _box[0]
            version = "".join(_box[1:])
            _box = (idt, version, ind)
            for c in version:
                if not c.isdigit():
                    old_version.append(_box)
                    break
            else:
                new_version.append(box)
        if not old_version:
            return new_version
        old_version = self.merge_sort(old_version)

        ans = []
        for _,_,ind in old_version:
            ans.append(boxList[ind])
        ans.extend(new_version)
        return ans

if __name__ == "__main__":
    boxList = [
        "ykc 82 01",
        "eo first qpx",
        "09z cat hamster",
        "06f 12 25 6",
        "az0 first qpx",
        "236 cat dog rabbit snake"
    ]
    ans = Solution().sortBoxesByVersion(boxList)
    print(ans)
    assert(ans, ["236 cat dog rabbit snake","09z cat hamster","az0 first qpx","eo first qpx","ykc 82 01","06f 12 25 6"])





