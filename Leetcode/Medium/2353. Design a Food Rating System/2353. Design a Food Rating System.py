class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # cuisin -> list of rating
        # food -> i -> cuishin (food is unique)
        # cuisine -> sortedSet [rating, food name]

        self.name_to_food = defaultdict(list)
        self.cuisine_to_rating = defaultdict(SortedSet)
        n = len(foods)
        for i in range(n):
            self.name_to_food[foods[i]] = [foods[i], cuisines[i], ratings[i]]
            self.cuisine_to_rating[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        food_name, cuisine, rating = self.name_to_food[food]
        self.name_to_food[food] = [food, cuisine, newRating]
        self.cuisine_to_rating[cuisine].remove((-rating, food_name))
        self.cuisine_to_rating[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_to_rating[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)