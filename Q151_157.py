# 151 Given a list and dictionary, map each element of list with each item
# of dictionary, forming nested dictionary as value.
test_dict={"anirudh":23,"satya":45,"Soumya":90}
test_list=[11,14,17]
result_dict = {}

for i in test_list:
    
    nested_dict = {}
    
    for key, value in test_dict.items():
        nested_dict[key] = value

    result_dict[i] = nested_dict 

print(result_dict)

# Create a dictionary like this given below and solve the questions based on that.
# 152 Add a new student named "Eva" with marks [95, 91, 89] to the student_marks dictionary.

student_mark={"jhon":{"Marks":[80,85,90]},
              "Alice":{"Marks":[75,88,92]},
              "Bob":{"Marks":[90,92,88]}
              }
student_mark["Eva"]=[95,91,89]
print(student_mark)

# 153 Write a python program that prints all the students name along with their average marks.

student_mark={"jhon":{"Marks":[80,85,90]},
              "Alice":{"Marks":[75,88,92]},
              "Bob":{"Marks":[90,92,88]}
              }
for key,value in student_mark.items():
    total=sum(value['Marks'])
    avg=total/len(value['Marks'])
    print("Student Name : ",key,"\nAverage Marks : ",avg)

# 154 Update the marks of "John" to [85, 88, 92] in the student_marks dictionary.
student_mark={"jhon":{"Marks":[80,85,90]},
              "Alice":{"Marks":[75,88,92]},
              "Bob":{"Marks":[90,92,88]}
              }
student_mark["jhon"]= {"Marks":[85, 88, 92]}
print(student_mark)

# 155 Write a program that displays the name of the student that has scored highest marks overall.
student_mark={"jhon":{"Marks":[80,85,90]},
              "Alice":{"Marks":[75,56,92]},
              "Bob":{"Marks":[90,92,88]}
}
heighest_mark=0
heighest_student_name= {}
for student,marks in  student_mark.items():
    total=sum(marks['Marks'])
    if total>heighest_mark:
        heighest_mark=total
        heighest_student_name=student

print (heighest_student_name,"has scored heighest marks is",heighest_mark)
# 156 Remove the entry for the student "John" from the student_marks dictionary.
student_mark={"jhon":{"Marks":[80,85,90]},
              "Alice":{"Marks":[75,56,92]},
              "Bob":{"Marks":[90,92,88]}
}
del student_mark["jhon"]

print(student_mark)


# 157  Create another nested dictionary named additional_marks with information for two more students. 
#      Merge this dictionary with the student_marks dictionary.
student_mark={"jhon":{"Marks":[80,85,90]},
              "Alice":{"Marks":[75,56,92]},
              "Bob":{"Marks":[90,92,88]}
}
additional_mark={
              "Alex":{"Marks":[15,55,33]},
              "Devid":{"Marks":[39,72,48]},
}

student_mark.update(additional_mark)
print(student_mark)




































