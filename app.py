class Students:
    def __init__(self,name,s_class,roll_number):
        self.name = name
        self.s_class = s_class
        self.roll_number = roll_number
      
        
        
        
student_1 = Students("ram","10th",1025,'B')
student_2 = Students('arjun','10th',72,'A')
student_3 = Students('vikram',"12th",1234,'C')

print(student_1.name)