class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        trying to create all the ingredients first with all the supplies we have in current
        -> use queue to keep track of the supplies that we have
        this is DAG
        """
        n = len(recipes)
        indegree = defaultdict(int)
        q = deque(supplies)
        adj = defaultdict(list)
        res = []

        for i in range(n):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                indegree[recipe] += 1
                adj[ingredient].append(recipe)

        while q:
            ingredient = q.popleft()

            for recipe in adj[ingredient]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)
                    res.append(recipe)

        return res

