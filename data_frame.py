student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76,98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#  print(key) #student
                 #score
    # print(value) # ['Angela', 'James', 'Lilly']
                 # [56, 76, 98]

import pandas 
student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    # print(row.student)
#loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

    if row.student == "Angela":
        print(row.score)