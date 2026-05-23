class Students:
    def __init__(self,name,s_class,roll_number,section):
        self.name = name
        self.s_class = s_class
        self.roll_number = roll_number
        self.section = section
        
        
        
student_1 = Students("ram","10th",1025,'B')
student_2 = Students('arjun','10th',72,'A')

print(student_1.name)