grades = [3, 4, 2, 5, 5]
grades.append(4)
grades.extend([[2, 2, 4]])
grades.remove([2, 2, 4])
grades.insert(1, 10)
print(grades)
print(grades.count(2))
grades.sort()
print(grades)