#There are n cities. Some of them are connected, while some are not. 
#If city a is connected directly with city b, and city b is connected directly with city c,
#then city a is connected indirectly with city c.
#
#A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
#You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
#Return the total number of provinces.

#Constraints:
#
#1 <= n <= 200
#n == isConnected.length
#n == isConnected[i].length
#isConnected[i][j] is 1 or 0.
#isConnected[i][i] == 1
#isConnected[i][j] == isConnected[j][i]


#Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
#Output: 2
# 0 - 2 
# 3
#
#Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
#Output: 3
#
# 0 1 3
#
#Input: isConnected = [[1,1,1],[1,1,0],[1,0,1]]
#Output: 1
# 
# 1 - 2
#  \
#   3
#Input: isConnected = [[1,1,0],[1,1,1],[0,2,1]]
#Output: 1
# 
# 1-2
#  \
#   3
#
# [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0], [0,0,0,0,1]]
#
# 1-2 
# 3-4 
# 5
#

class Solution:
    def find_circle(self, is_connected):
        print("Start")
        # Init control variablies
        number_of_cities = len(is_connected) # Space complexity O(n) Time complexity O(n)
        visited_cities = [False] * number_of_cities # Space complexity O(n) Time complexity O(n)
        provinces = 0

        def map_city_connections(city):
            visited_cities[city] = True
            for neighbor in range(number_of_cities): # Space complexity O(n^2) Time complexity O(n)
                if not visited_cities[neighbor] and is_connected[city][neighbor]:
                    map_city_connections(neighbor)

        for city in range(number_of_cities): # Space complexity O(n) Time complexity O(n)
            print(f"Checking city {city}")
            if not visited_cities[city]:
                provinces+=1
                map_city_connections(city)

        return provinces

class Solution2:
    """
    For this solution I want attempt to avoid the O(nˆ2) time complexity
    The idea is to use a merge strategy, where I'll merge the parents, so 
    they became the grandparent, this way I just need to count the number of 
    grandparents to know how many comopenents there are.

    So the idea is to compare city by city, so each city will be compared to all its neighbors
    then if there is a connection between these cities I will merge their parents so:

    instead of 1-2-3-4 I'd have 1-2
                                | \
                                4  3
    
    then I just need to check if the city is its own parent, if so I can assure that is 
    a root/parent

    so in a situation like [[1,1,0],[1,1,0],[0,0,1]]

    I would first create an array that contains each city parent ->
    in this case each city starts being its own parent, but then I will compare each 
    city with all neighbors, and I will also need a rank variable to store the size of each
    component, bc I need to understand which one will be maintained while merging
    and it should be the bigger one

    parents = [0,1,2]
    rank  = [1,1,1]

    the output here should be something like: parents = [0,0,2] -> what is basically 2 
    different values, in other words 2 components

    foreach city:
        is city connected with any neighbor?:
            rank[city] > rank[neighbor]:
                parents[neighbor] = parents[city]
            else if rank[city] < rank[neighbor]:
                parents[city] = parents[neighbor]
            rank[city] += 1
            parents[neighbor] = parents[city]

    """
    def find_circle(self, is_connected):
        print("Start")
        cities_len = len(is_connected)
        parents = list(range(cities_len))
        rank = [1] * cities_len


        def find_root(city):
            if city != parents[city]:
                parents[city] = find_root(parents[city])
            return parents[city] 


        def merge_cities(city1, city2):
            root_of_city1 = find_root(city1)
            root_of_city2 = find_root(city2)

            if rank[root_of_city1] > rank[root_of_city2]:
                parents[city2] = root_of_city1
            if rank[root_of_city1] > rank[root_of_city2]:
                parents[city1] = root_of_city2
            parents[city2] = root_of_city1
            rank[root_of_city1] +=1


        for city in range(cities_len):
            print(f"Checking city: {city}")
            for neighbor in range(cities_len):
                if is_connected[city][neighbor] and parents[city] != parents[neighbor]:
                    merge_cities(city, neighbor)

        return sum(1 for city in range(cities_len) if parents[city] == city)



if __name__=="__main__":
    solution = Solution2()
    result = solution.find_circle([[1,1,0],[1,1,1],[0,2,1]])
    print(result)




