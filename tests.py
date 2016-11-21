import unittest
import math
from stud import Students
from sub import Subjects
from school_diary import SchoolDiary


class SchoolTests(unittest.TestCase):
    
    def setUp(self):
        self.school = SchoolDiary("students.json")
        self.student1 = Students("Andrzej", "Dooda")
        self.student2 = Students("Johnny", "Ogolony")
        self.subject1 = Subjects("Religia", "prof. Pawlacz")
        self.subject2 = Subjects("Chemia", "dr Brew")
        self.student1.add_subject_to_stud([self.subject1,self.subject2])
        self.student2.add_subject_to_stud([self.subject2])
        self.student1.add_grade("Religia", [2.5, 3.5, 4.5])
        self.student1.add_grade("Chemia", [3.0, 5.0, 5.0])
        self.student2.add_grade("Chemia", [3.5, 3.5, 4.5])
        self.school.add_students([self.student1,self.student2])
        self.school.load_json_file()
           
    def test_add_student(self):
        self.assertIsNone(self.school.add_students("random_student"))
        self.assertIsNone(self.school.add_students((1, 5)))
    
    def test_add_subject_to_stud(self):
        self.assertIsNone(self.student1.add_subject_to_stud("test"))
        self.assertIsNone(self.student1.add_subject_to_stud((1, 2, 3)))
        self.assertIsNone(self.student2.add_subject_to_stud([1, 2, 3]))	
 
    def test_add_grade_to_stud(self):
        self.assertIsNone(self.student1.add_grade("test","test"))
    
    def test_add_grade_to_stud_one(self):
        self.assertIsNone(self.student1.add_grade("test",1.0))
    
    def test_add_attendace(self):
        self.student1.add_attendance("Religia", 5)
        self.assertEqual(self.student1.print_attend(), 5)
                
    def test_get_average(self):
        self.assertAlmostEquals(self.student1.average(),23.5/6)
        
    def test_get_sub_average(self):
        self.assertAlmostEquals(self.student1.sub_average("Chemia"),13./3)
            
    def test_get_student(self):
        self.assertEqual(type(self.school.get_student("Andrzej", "Dooda")), type(self.student1))
        
    def test_get_subject_name(self):
        self.assertEqual(self.subject1.get_subject_name(), "Religia")        
        
    def test_get_subject_prof(self):
        self.assertEqual(self.subject1.get_subject_prof(), "prof. Pawlacz")
    
    def test_add_students_count(self):
        self.assertNotEqual(len(self.school.students), 4)        

    
if __name__ == '__main__':
    unittest.main()