class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        numStudents = len(students)
        numSand = len(sandwiches)
        studentQueue = deque(students)
        sandwichQueue = deque(sandwiches)
        retries = 0

        while sandwichQueue:
            student, sand = studentQueue.popleft(), sandwichQueue[0]
            if student == sand:
                sandwichQueue.popleft()
                numSand -= 1
                numStudents -= 1
                retries = 0
            else:
                studentQueue.append(student)
                retries += 1
                if retries == numStudents:
                    return numStudents
        
        return numStudents
            
