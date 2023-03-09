from information.people.students import student_information as student_info
from people import student_information, people_color

if __name__ == "__main__":
    print("Hi, I am currently in the presentation script.")
    student_info("Bill", 30)
    student_information("Joe", 40)
    people_color("Fred", color="Red")