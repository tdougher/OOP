import StudentClass as sc


dob = input('What is your date of birth? ')
studentid = 1001
name = 'John'
classification = 'junior'


student1 = sc.Student(studentid, name, dob, classification, '', 0)


student1.calc_age()
student1.calc_register()

print(f"Student age is: {student1.get_age()} and they can register between {student1.get_register()}")


