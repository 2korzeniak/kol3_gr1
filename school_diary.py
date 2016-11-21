import jsonpickle

from stud import Students
from sub import Subjects

class SchoolDiary(object):
    """School diary"""
    def __init__(self, json_fname, students = []):
        self.students = students
        self.json_fname = json_fname
        
    def add_students(self, students):
        """Adds students and saves to json file"""
        for i in students:
            if not isinstance(i, Students):				
                return
        self.students.extend(students)
        self.save_json_file()
        
    def get_student(self, fname, lname):
        """Gets student"""
        for stud in self.students:
            print stud
            return stud
        return
        
    def print_studs(self):
        """Prints students list"""
        print("Students:")
        print("\n".join(str(s) for s in self.students))
        
    def load_json_file(self):
        """Loads json file"""
        with open(self.json_fname, 'rb') as file:
            self.students = jsonpickle.decode(file.read())
            
    def save_json_file(self):
        """Saves json file"""
        with open(self.json_fname, 'wb') as file:
           file.write(jsonpickle.encode(self.students))
           

if __name__ == "__main__":           
    student1 = Students("Andrzej", "Duda")
    student2 = Students("Johnny", "Bravo")
    subject1 = Subjects("Religia", "prof. Wojtyla")
    subject2 = Subjects("Chemia", "dr Oetker")
    subject3 = Subjects("ZTI", "dr inz. Antonio")
    student1.add_subject_to_stud([subject1,subject2])
    student2.add_subject_to_stud([subject2,subject3])
    student1.add_grade("Religia", [2.0, 3.0, 4.0])
    student1.add_grade("Chemia", [4.0, 5.0, 5.0])
    student2.add_grade("Chemia", [3.0, 3.0, 4.0])
    student2.add_grade("ZTI", [4.0, 4.0, 5.0])
    e = SchoolDiary("students.json")
    e.add_students([student1,student2])
    d = SchoolDiary("students.json")
    d.load_json_file()
    d.print_studs()
    print "\n"
    andrzej = d.get_student("Andrzej", "Duda")
    andrzej.average().sub_average("Chemia").add_attendance("Religia", 5)
    andrzej.print_attend()