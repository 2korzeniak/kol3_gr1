from __future__ import division
from array import *


#
# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student

# The default interface for interaction should be python interprete
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


class Student(object):
    def __init__(self, id, name, surname, class_id, attendance=0, scores=[]):
        self._id = id
        self._class_id = class_id
        self._name = name
        self._surname = surname
        self._scores = scores
        self._attendance = attendance

    @property
    def class_id(self):
        return self._class_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def attendance(self):
        return self._attendance

    @property
    def scores(self):
        return self._scores

    @property
    def average(self):
        if len(self._scores) == 0:
            return 0
        else:
            return sum(self._scores) / len(self._scores)
