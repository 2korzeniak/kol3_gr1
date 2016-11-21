from sub import Subjects
from numbers import Number
import numpy

class Students(object):
    """Student class"""
    def __init__(self,fname,lname):
        self.__fname = fname
        self.__lname = lname
        self.attend = {}
        self.grade = {}
        self.subjects = []
        
    def __str__(self):
        return self.__fname + " " + self.__lname
        
    def add_subject_to_stud(self, subjects):
        """Adds subject to student"""
        for s in subjects:
            if not isinstance(s,Subjects):
                return
        self.subjects.extend(subjects)
    
    def add_grade(self, subject, grade):
        """Adds new grade to student"""
        if subject in self.grade.keys():
            self.grade[subject].extend(grade)
        else:
            self.grade[subject] = grade
            
    def add_attendance(self, subject, count):
        """Adds attendace to student"""
        if subject in self.attend.keys():
            self.attend[subject] += count
        else:
            self.attend[subject] = count
            
    def average(self):
        """Computes total average"""
        avg, count = 0, 0
        for i in self.grade:
            for j in self.grade[i]:
                avg += j
                count += 1
        if count!= 0:
            aver = avg/count
            print("Total average is: " + str(avg/count))
            return aver
        return self
        
    def sub_average(self, subject):
        """Computes subject average"""
        avg = numpy.mean(self.grade[subject])
        print(subject + " avarage is: " + str(avg))        
        return avg
        return self
        
    def print_attend(self):
        """Prints student's attendace"""
        print("\nAttendance:")
        for i in self.attend:
            print(i + ": " + str(self.attend[i]))
        return self.attend[i]
	
    @property
    def fname(self):
        return self.__fname

	@fname.setter
	def fname(self, fname):
		self.__fname = fname

	@property
	def lname(self):
		return self.__lname

	@lname.setter
	def lname(self, lname):
		self.__lname = lname



    
        
    