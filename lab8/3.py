import unittest

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_bikes(students, bikes):
    n = len(students)
    m = len(bikes)
    
    distances = []  
    assigned_bikes = [-1] * n       
    bike_taken = [False] * m        

    for i in range(n):
        for j in range(m):
            distance = manhattan_distance(students[i], bikes[j])
            distances.append((distance, i, j))

    distances.sort(key=lambda x: (x[0], x[1], x[2]))

    for distance, student, bike in distances:
        if assigned_bikes[student] == -1 and bike_taken[bike] == False:
            assigned_bikes[student] = bike  
            bike_taken[bike] = True         

    return assigned_bikes

class TestBikeAssignment(unittest.TestCase):
    def test_(self):
        students = [(0, 0), (1, 1)]
        bikes = [(0, 1), (4, 3), (2, 1)]
        expected_result = [0, 2]
        self.assertEqual(assign_bikes(students, bikes), expected_result)

    def test_1(self):
        students = [(0, 0), (2, 3)]
        bikes = [(0, 1), (2, 1)]
        expected_result = [0, 1]
        self.assertEqual(assign_bikes(students, bikes), expected_result)

    def test_2(self):
        students = [(1, 2), (1, 2)]
        bikes = [(0, 1), (2, 3), (1, 2)]
        expected_result = [2, 0]  
        self.assertEqual(assign_bikes(students, bikes), expected_result)

    def test_3(self):
        students = [(0, 0), (1, 1), (2, 2)]
        bikes = [(0, 1), (1, 0), (2, 2)]
        expected_result = [0, 1, 2]
        self.assertEqual(assign_bikes(students, bikes), expected_result)

    def test_4(self):
        students = [(3, 3), (0, 0)]
        bikes = [(1, 1), (3, 3), (0, 1), (2, 2)]
        expected_result = [1, 2]
        self.assertEqual(assign_bikes(students, bikes), expected_result)

if __name__ == "__main__":
    unittest.main()
