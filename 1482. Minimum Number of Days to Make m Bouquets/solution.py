class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def check_flowers(day):
            num_of_bouquets = 0
            flow_num = 0
            for flow in bloomDay:
                if flow <= day:
                    flow_num += 1
                else:
                    flow_num = 0
                if flow_num >= k:
                    num_of_bouquets += 1
                    flow_num = 0
            return num_of_bouquets >= m

        left = 0
        r = max(bloomDay) + 1
        while r - left > 1:
            mid = (left + r) // 2
            if check_flowers(mid):
                r = mid
            else:
                left = mid
        if r == max(bloomDay) + 1 or (r == 1 and not check_flowers(1)):
            return -1
        return r
