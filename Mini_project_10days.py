#Student Management Mini Project
print("****Student Management Mini Project****")

#Welcome Message
print("---Welcome Message---")
name=input("Enter your name:")
age=int(input("Enter your age:"))
branch=input("Enter your branch:")
college_name=input("Enter your college name:")
print("Student name:",name)
print("Age:",age)
print("Branch:",branch)
print("College name:",college_name)

#Marks Calculation
print("---Marks Calculation using operators---")
sub1=int(input("Enter your sub1 marks:"))
sub2=int(input("Enter your sub2 marks:"))
sub3=int(input("Enter your sub3 marks:"))
print("Maths:",sub1)
print("Physics:",sub2)
print("Chemistry:",sub3)
total_marks=sub1+sub2+sub3
print("Total marks:",total_marks)
average_marks=total_marks/3
print("Average marks",average_marks)

#Grade Checker
print("---Grade Checker using conditions---")
marks=int(input("Enter your marks:"))
if marks>90:
    print("A grade")
elif marks>75:
    print("B grade")
elif marks>50:
    print("C grade")
elif marks>35:
    print("D grade")
else:
    print("Fail")
    
#Even or Odd
print("---Even or Odd using functins---")
def even_odd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
even_odd(67)

#Loop Practice
print("---Loop Practice---")
print("Print 1 to 10 numbers:")
i=0
while i<=10:
    print(i)
    i=i+1
print("Print Even numbers:")
for i in range(0,21,2):
    print(i)
    

#String Practice
print("---String Practice---")
favorite_pl=input("Enter your Favorite Programming Language:")
print(favorite_pl)
print("Uppercase:",favorite_pl.upper())
print("Lowercase:",favorite_pl.lower())
print("Lenght of string:",len(favorite_pl))

#List Practice
print("---List Practice---")
movies=["Amaran","Leo","Beast"]
print(movies)
movies.append("Kubera")
print("Add movie:",movies)
movies.remove("Beast")
print("Remove movie:",movies)
print("Lenght of movie:",len(movies))

#Tuple Practice
print("---Tuple Practice---")
subjects=("Maths","Physics","Chemistry","C","C++")
print(subjects)
print("First subject:",subjects[0])
print("Last subject:",subjects[-1])

#Dictionary Practice
print("---Dictionary Practice---")
student={
    "name":"Vasavi",
    "Branch":"DS"
}
print(student)
student["Age"]=19
print("Add Age:",student)
student["Branch"]="AIDS"
print("Update branch:",student)

#Function Practice
print("---Function Practice---")
def student_details(name,age,branch,percentage):
    print("name:",name)
    print("Age:",age)
    print("branch:",branch)
    print("percentage:",percentage)
student_details("Vasavi",19,"AIDS","73%")






