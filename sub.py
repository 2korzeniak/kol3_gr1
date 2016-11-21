class Subjects(object):
    """School subject"""
    
    def __init__(self, subname, tname):
        self.subname = subname
        self.tname = tname
    
    def get_subject_name(self):
        return self.subname    
    
    def get_subject_prof(self):
        return self.tname
    
    @property
    def subname(self):
        return self.__subname
    
    @subname.setter
    def subname(self, subname):
        self.__subname = subname
        
    @property
    def tname(self):
        return self.__tname 
        
    @tname.setter
    def tname(self, tname):
        self.__tname = tname      
        
