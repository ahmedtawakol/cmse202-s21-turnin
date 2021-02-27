# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    year: this is how many years the student has been in college
    '''
    
    def __init__(self, name='', gpa=0.0, year=0, courses = []):
        self.name = name
        self.gpa = gpa
        self.year = year
        self.courses = courses
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)

    def enroll(self, courses):
        '''
        This function takes an input of a list of courses and adds them as an attribute to the student
        '''
        self.courses.append(courses)
    def display_courses(self, courses):
        '''
        This function prints out enrolled courses
        '''
        print("I am enrolled in:", courses)
        
    def years_until_graduation(self):
        '''
        This function returns the number of years left until the student graduates (assuming that a student typically graduates           after 4 years)
        '''
        return("I will graduate in", 4-self.year, "years.")

class Spartan(Student):
    
    def set_motto(self,motto = ''):
        '''
        This takes a string as an input and sees it to set a new class attribute, called motto
        '''
        self.motto = motto
    
    def school_spirit(self):
        '''
        prints name and motto
        '''
        print("My name is:", self.name)
        print("I am a spartan. My motto is", self.motto)