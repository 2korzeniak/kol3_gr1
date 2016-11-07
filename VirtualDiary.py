from __future__ import division
from itertools import groupby
from Student import Student


class VirtualDiary(object):
    def __init__(self):
        self._students = [Student(1, "Janusz", "Tytanowy", "A", 3, [2, 3, 4]),
                          Student(2, "Adam", "Mleko", "A", 7, [4, 4, 4]),
                          Student(3, "Ania", "Podsiadlo", "B", 17, [2])]

        self._classes = groupby(self._students, lambda s: s.class_id)

    def total_attendance(self):
        value = sum(s.attendance for s in self._students)
        print value
        return value

    def attendance_by_class(self):
        self._classes = groupby(self._students, lambda s: s.class_id)
        for class_id, students in self._classes:
            print "    Class " + class_id + ": " + str(sum(s.attendance for s in students))
            

    def average_by_class(self):
        self._classes = groupby(self._students, lambda s: s.class_id)
        for class_id, students in self._classes:
            scores = [score for subScores in [s.scores for s in students] for score in subScores]
            print "    Class " + class_id + ": " + str(sum(scores) / len(scores))

    def total_average(self):
        scores = [score for subScores in [s.scores for s in self._students] for score in subScores]
        print str(sum(scores) / len(scores))

    def print_students(self):
        self._classes = groupby(self._students, lambda s: s.class_id)
        for class_id, students in self._classes:
            print "Class " + class_id
            for student in students:
                print " -- " + student.name + " " + student.surname

    def add_score(self, student_id, value):
        if self.index_validation(student_id, len(self._students)):
            self._students[student_id].scores.append(value)

    def add_attendance(self, student_id):
        if self.index_validation(student_id, len(self._students)):
            self._students[student_id].attendance += 1

    @staticmethod
    def index_validation(index, size):
        if index < 0 or index >= size:
            print "Incorrect index, please try again";
            return False
        else:
            return True

    @staticmethod
    def is_number(number):
        try:
            int(number)
        except ValueError:
            return False
        else:
            return True

    def menu(self):
        while True:
            operation = raw_input("""
                    Please select the number of operations
                    [1] get students total average score (average across classes)
                    [2] get students average score in class
                    [3] print students
                    [4] count total attendance of student
                    [5] count total attendance of student by class
                    [6] exit

                    Operation: """)
            if not self.is_number(operation):
                print "Incorrect operation, please try again"
                continue

            operation = int(operation)

            if operation < 0 or operation > 6:
                print "Incorrect number of operation, please try again"
                continue

            if operation == 1:
                self.total_average()
            elif operation == 2:
                self.average_by_class()
            elif operation == 3:
                self.print_students()
            elif operation == 4:
                self.total_attendance()
            elif operation == 5:
                self.attendance_by_class()
            elif operation == 6:
                break
