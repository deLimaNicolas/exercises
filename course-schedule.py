#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
#For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#Return true if you can finish all courses. Otherwise, return false.
#
# 
#
#Example 1:
# [0,1]
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take. 
#To take course 1 you should have finished course 0. So it is possible.
#Example 2:
#
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Input: numCourses = 3, prerequisites = [[1,0],[0,2]]
#Output: True
#  1 -> 0 -> 2
#
#Input: numCourses = 3, prerequisites = [[1,0],[0,2], [2,1]]]
#Output: True
#                  1 -> 0 -> 2
#                  3 <-> 4
#                  cria grafo
#                    0: 2
#                    1: 0
#                    2: 
#                    3: 4
#                    4: 3
#                  visited: {0, 2, 3, 4}
#                  current_visited: {3, 4}
#                  
#                  isCyclic(vertice):
#                   if vertice in visited:
#                      return false
#                   visited add vertice
#                   if vertice in current_visited:
#                       return true
#                   add current_visited
#                   for dep in grap[vertice]:
#                       iscyclic(dep)
#                   return false
#                  
#                  pra cada vertice:
#                   if vertice not in visited:
#                       current_visited: {}
#                       if isCyclic(vertice):
#                           false
#                    
#                      
#                    
# 
#
#Explanation: There are a total of 2 courses to take. 
#To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

from typing import List

class Solution0:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list representation of the graph
        # For each course, store the courses that depend on it
        graph = [[] for _ in range(numCourses)]
        
        # Fill the graph: if [a,b] is a prerequisite, it means b -> a (b must be taken before a)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        print(graph)
        
        # Keep track of visited nodes and nodes in current path
        visited = set()
        path = set()
        
        def has_cycle(node):
            # If node is in current path, we found a cycle
            if node in path:
                return True
            
            # If node is already visited and not in path, we know it's safe
            if node in visited:
                return False
            
            # Mark node as part of current path
            path.add(node)
            
            # Recursively check all neighbors
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            
            # Remove node from current path
            path.remove(node)
            
            # Mark node as visited
            visited.add(node)
            
            return False
        
        # Check for cycles from each unvisited node
        for course in range(numCourses):
            if course not in visited:
                if has_cycle(course):
                    return False
        
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [set() for _ in range(numCourses)]
        visited = set()
        current_visited = set()

        for course, prereq in prerequisites:
            graph[course].add(prereq)
        
        def is_cyclic(course):
            if course in current_visited:
                return True
            if course in visited:
                return False

            print("Checking Course ", course)

            visited.add(course)
            current_visited.add(course)
            
            for dep in graph[course]:
                if is_cyclic(dep):
                    return True

            current_visited.remove(course)
            
            return False


        for course in range(numCourses):
            if course not in visited:
                if is_cyclic(course):
                    return False
        return True



def main():
    solution = Solution()
    # Test cases
    print("Test 1:", solution.canFinish(2, [[1,0]]))  # Should be True
    print("Test 2:", solution.canFinish(2, [[1,0],[0,1]]))  # Should be False
    print("Test 3:", solution.canFinish(3, [[1,0],[0,2]]))  # Should be True
    print("Test 4:", solution.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))  # Should check if this has a cycle

if __name__ == "__main__":
    main()
