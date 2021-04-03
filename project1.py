from statistics import mean as m
admin={"admin":"admin123","user1":"santhu"}
data={'santhu':[90,80,70],'reddy':[99,89,90]}

def entergrades():
    name=input("enter the student name")
    enter=input("enter the grade:")
    if name in data:
        print("adding grades")
        data[name].append(enter)
    else:
        print('name is not found')
    print(data)
def removestudent():
    n=input('enter the name')
    if n in data:
        del data[n]
    else:
        print('name doesnot exit')
    print(data)
def avgrades():
    for student in data:
        grade=data[student]
        avg=m(grade)
        print(avg)


def main():
    print("""welcome to grade central
      [1]- enter the Grades
      [2]- remove the student
      [3]-student average grade
      [4]-exit""")

    option=int(input("enter the number:"))
    if option == 1:
        entergrades()
        
    elif option == 2:
        removestudent()
    elif  option == 3:
        avgrades()
    elif option == 4:
        print("thank you see you again")
    else:
        print('invalid number')

login=input("enter the username:")
passwd=input("enter the password:")
if login in admin:
    if admin[login] == passwd:
        print("hello welcome",login)
        while True:
            main()
    else:
        print("oops... you entered wrong password Please try again! ")
else:
    print("username is doesnot exit")



