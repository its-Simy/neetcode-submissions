class Solution:
    def kClosest(self, points, k):
        res = []
        distance = []
        dic = {}

        for x,y in points:
            dist = (math.pow((x - 0),2) + math.pow((y-0),2))**.5
            distance.append(dist)
            if dic.get(dist,False):
                dic[dist].append([x,y])
            else:
                dic[dist] = [[x,y]]
        
        heapq.heapify(distance)
        

        for _ in range(k):
            dist = heapq.heappop(distance)
            item = dic[dist].pop()
            res.append(item)
        
        return res
        