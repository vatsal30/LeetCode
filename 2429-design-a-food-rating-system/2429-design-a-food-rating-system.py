class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_map = defaultdict(list)
        self.food_map = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = (cuisine, rating)
            heapq.heappush(self.cuisines_map[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_map[food]
        heapq.heappush(self.cuisines_map[cuisine], (-newRating, food))
        self.food_map[food] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = self.cuisines_map[cuisine][0]
            if self.food_map[food][1] == -rating:
                return food
            heapq.heappop(self.cuisines_map[cuisine]) 


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)