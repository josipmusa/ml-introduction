import numpy as np

def basic_array_manipulation():
    num_students = 5
    num_subjects = 4
    grades = np.random.randint(1, 6, size=(num_students, num_subjects))
    print(grades)
    average_per_subject = np.mean(grades, axis=0)
    average_per_student = np.mean(grades, axis=1)
    top_student_index = np.argmax(average_per_student)
    top_student_grades = grades[top_student_index]
    vertical_flip = np.flip(grades, axis=0)
    horizontal_flip = np.flip(grades, axis=1)
    print("Average per subject: ", average_per_subject)
    print("Average per student: ", average_per_student)
    print("Top student grades: ", top_student_grades)
    print("Vertical flip: ", vertical_flip)
    print("Horizontal flip: ", horizontal_flip)


if __name__ == '__main__' :
    basic_array_manipulation()