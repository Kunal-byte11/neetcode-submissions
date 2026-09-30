class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0

        r = len(heights) - 1

        while l < r :
            width =  r - l

            h = min(heights[l] , heights[r])

            area = width * h

            res = max(res,area)

            if heights[l] < heights[r]:
                l+=1

            else:
                r-=1

        return res
        