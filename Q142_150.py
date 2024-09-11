# 142 Ask subject name and marks from the user and keep adding it to dictionary.
marks= {}
sub_count=int(input("Enter the number of subject :"))
for _ in range(0,sub_count):
    sub_name=input("Enter the subject name: ")
    sub_marks = int(input("Enter your Marks for "+sub_name+": "))
    marks[sub_name]=sub_marks

print(marks)

# 143 Convert two lists into a dictionary. Make two list on your own of same length, and convert them to dictionary.
lst1=["math","english","odia","hindi"]
lst2=[89,98,87,89]
dic={}
i=0
j=0
while i<len(lst1) and j<len(lst2):
    dic[lst1[i]]=lst2[j]
    i+=1
    j+=1
    
print(dic)

# 144 Write a Python program to sum all the items in a dictionary.
marks={"phy":98,"che":89,"Math":78}
total=0
for v in marks.values():
    total=total+v

print(total)

#or print(sum(list(marks.values()))) one line ans

#145 Write a Python program to multiply all the items in a dictionary.
marks={"phy":89,"math":67,"sci":69,"che":90}
mul=1
for v in marks.values():
    mul=mul*v

print(mul)


# 146 Ask a string from user. Display the dictionary where each key is a character and value is the 
#frequency of that character that comes in that string.

my_string=str(input("Please Enter Your String:"))
dic={}
for ch in my_string:
    if ch in dic:
        dic[ch]+=1
    else:
        dic[ch]=1

print(dic)

# 147 Store “name” of a student as Key, “list of 5 marks” of that student as a Value. Store atleast 5 student 
# names. Print the sum and percentage of all the students.

student_data={
    "student1":[56,76,80,78,89],
    "student2":[56,76,80,78,89],
    "student3":[56,76,80,78,89],
    "student4":[56,76,80,78,89],
    "student5":[56,76,80,78,89],
}
for name,marks in student_data.items():
    total=sum(marks)
    percentage=total/500*100
    print(name,'- sum :',total,"Percentage:",percentage)

# 148 Store marks of 5 diff erent subjects in a dictionary. Ask subject name as an input from the User. 
# Print the marks of that subject entered by User. If subject does not exist, print “Invalid”.
student_data={
    "Math":89,
    "Science":76,
    "odia":80,
    "Englisg":56,
    "Hindi":78
}
"""
subject_name=input("Enter the subject name :")
for subject,marks in student_data.items():
    if subject==subject_name:
        print('Marks for',subject,":",marks)
    else:
        print("Invalid")
"""
subject_name=input("Enter the subject name :")

if subject_name in student_data:
    print(student_data[subject_name])
else:
    print("Invalid")

# 149 Store name as a Key, and 5 marks in a List as a value in dictionary. Store details of at least 5 students.
# Print the name of the student who got highest marks.

student_data={
    "student1":[56,76,80,78,89],
    "student2":[56,76,80,78,89],
    "student3":[56,76,80,78,89],
    "student4":[56,76,80,78,89],
    "student5":[56,76,80,78,89]
}
heighest_mark=0
heighest_student_name=""

for name,marks in student_data.items():
    total=sum(marks)
    if total>heighest_mark:
        heighest_mark=total
        heighest_student_name=name

print(heighest_student_name)
print(heighest_mark)

# 150 Write a Python program to combine two dictionary by adding values for common keys.

d1={"a":300,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}

result={}

for k,v in d1.items():
    result[k]=v

for k,v in d2.items():
    if k in result:
        result[k]=result[k]+v
    else:
        result[k]=v

print(result)





















