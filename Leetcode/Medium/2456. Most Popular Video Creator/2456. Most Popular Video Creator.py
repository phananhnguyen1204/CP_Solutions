from heapq import heappush, heappop
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        """
        popularity of creator = sum (views from all videos)
        creator -> (views, video_ids) (sorted by highest view)
        """
        # creator_to_infors = defaultdict(list) # (-views, video_ids)
        # n = len(creators)

        # for i in range(n):
        #     heappush(creator_to_infors[creators[i]], [-views[i], ids[i]])
        
        # res = []
        # max_popularity = 0
        # for creator, movies in creator_to_infors.items():
        #     popularity = 0
        #     for view, _ in movies:
        #         view *= -1
        #         popularity += view
        #     if popularity > max_popularity:
        #         max_popularity = popularity
        #         res = [[creator]]
        #     elif popularity == max_popularity:
        #         res.append([creator])
        # print(res)
        # for i in range(len(res)):
        #     creator = res[i][0]
        #     id = creator_to_infors[creator][0][1]
        #     res[i].append(id)
        # return res

        # 2nd approach: no sort
        n = len(creators)
        infors = defaultdict(list) # [popularity, view_of_most_video, id_of_most_view]

        max_views = max_popularity = 0
        total_views = 0

        for i in range(n):
            creator, id, view = creators[i], ids[i], views[i]
            if creator not in infors:
                infors[creator] = [0, 0, id]
            infors[creator][0] += view
            if infors[creator][1] < view:
                infors[creator][1] = view
                infors[creator][2] = id
            elif infors[creator][1] == view:
                if infors[creator][2] > id:
                    infors[creator][2] = id
            max_popularity = max(infors[creator][0], max_popularity)

        res = []
        for creator in infors:
            if infors[creator][0] == max_popularity:
                res.append([creator, infors[creator][2]])

        return res

        