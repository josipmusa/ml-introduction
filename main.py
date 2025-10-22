import numpy as np

def calculate():
    arr = np.random.randint(1, 6, size=100)
    average_grade = np.mean(arr)
    print("Average grade is : ", average_grade)
    top_5_grades = np.partition(arr, -5)[-5:]
    print("Top 5 performing grades", top_5_grades)
    deviation = np.std(arr)
    print("Deviation is : ", deviation)

if __name__ == '__main__':
    calculate()
