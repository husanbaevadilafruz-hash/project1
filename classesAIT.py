class Student():
    def __init__(self, name, id, program): 
        self.name=name
        self.id=id
        self.program=program
        self.documents={}
        self.enrollments=[]
        self.transcript=[]
        self.gpa=0.0
        self.inbox=[]
    def add_message(self, text):
        self.inbox.append(text)
    def set_document(self, kind, status ):
        
        if status.upper().split()=='MISSED':
            self.inbox.append('your document is missed')
        if status.upper().split()=='EXPIRED':
            self.inbox.append('your document is expired')
        else:
            self.documents[kind]=status
    def update_gpa(self):
        self.gpa=0.0
        self.gpa=sum(self.transcript)/len(self.transcript)



    



class Teacher():
    def __init__(self, id, name, department):
        self.id=id
        self.name=name
        self.department=department
        self.inbox=[]
    def add_message(self):

class Course():
    def __init__(self, code, title, credits):
        self.code=code
        self.title=title
        self.credits=credits
        self.prerequisites=[]

class Section():
    def __init__(self, course, teacher, capacity, kind):
        self.course=course
        self.teacher=teacher
        self.capacity=capacity
        self.kind=kind
        self.room=None
        self.start_time=None
        self.end_time=None
        self.day=None
        self.roster=[]
        self.waitlist=[]
    def enroll(self, student):
        if self.capacity>len(self.roster):
            enrollment=Enrollment(student, self.course, 'ENROLLED')
            self.roster.append(enrollment)
            student.send_message(f'vy zachisleny v {self.course}')
            self.teacher.send_message(f'{student} zachislen v {self.course}')
        else:
            enrollment=Enrollment(student, self.course, 'WAITLISTED')
            self.waitlist.append(student)
            student.send_message(f'vy v liste ojidaniya  na {self.course}')
            self.teacher.send_message(f'{student} v liste ojidaniya na {self.course}')
    def change_room(self, new_room):
        self.room=new_room
        self.teacher.add_message(f'teper vash course v cabinete {new_room}')
        for i in self.roster:
            i.add_message(f'teper vash course v cabinete {new_room}')
    
    def drop(self, student):
        for enrollment in self.roster:
            if enrollment.student==student:
                if enrollment.change_status('DROPPED'):
                    return False
                if enrollment.status=='WAITLISTED':
                    self.waitlist.remove(student)
                    enrollment.change_status('DROPPED')
                    enrollment.student.add_message(f'vy otchisleny s {self.course}')
                if enrollment.status=='ENROLLED':
                    self.roster.remove(enrollment)
                    enrollment.change_status('DROPPED')
                    enrollment.student.add_message(f'vy trchisleny s {self.course}')
                    if len(self.waitlist)>0:
                        x=self.waitlist[0]
                        enr=Enrollment(x, self.course, 'ENROLLED')
                        self.roster.append(enr)
                        
                    
    def reschedule(self, new_day, new_Stime, new_Etime):
        self.day=new_day
        self.new_Stime=new_Stime
        self.new_Etime=new_Etime
        self.teacher.add_message(f'teper vash v {new_day}, s {new_Stime} do {new_Etime}')
        for i in self.roster:
            i.add_message(f'teper vash v {new_day}, s {new_Stime} do {new_Etime}')
    def change_teacher(self, new_teacher):
        self.teacher=new_teacher
        
        
class Enrollment():
    def __init__(self, student, section, status):
        self.student=student
        self.section=section
        self.status=status
    def change_status(self, new_status):
        self.status=new_status 
class Assigment():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

class Grade():
    def __init__(self, section, student, assigment, score):
        self.section=section
        self.student=student
        self.assigment=assigment
        self.score=score

class TranscriptEntry():
    def __init__(self, course_code, letters, credits, points):
        self.coure_code=course_code
        self.letters=letters
        self.credits=credits
        self.points=points

class GraduationPolicy():
    def __init__(self, gpa_threshold):
        self.gpa_threshold=gpa_threshold
    def eligible(self, student):
        if student.gpa>self.gpa_threshold:
            return True
        else:
            return False

class NotificationCenter():
    def __init__(self):
        pass
    def notify_student( student, text):
        student.send_message(text)
    def notify_teacher(self, teacher, text):
        teacher.send_message(text)
    

class Registrar():
    def __init__(self,notify=NotificationCenter()):
        self.students=[]
        self.teachers=[]
        self.courses=[]
        self.sections=[]
        self.audit_log=[]
        self.notifier=notify
    def add_student(self, name, id, program):
        student=Student(name,id,program)
        self.students.append(student)
        self.audit_log.append(f'student {name} dobavlen')
        self.notifier.notify_student(student,"You were added")
        
    def add_teacher(self, id, name, department):
        self.teachers.append(Teacher(id, name, department))
        self.audit_log.append(f'teacher {name} dobavlen')
    def add_course(self, code, title, credits):
        self.courses.append(Course( code, title, credits))
        self.audit_log.append(f'course {title} dobavlen ')
    def change_teacher(self,section_title, new_teacher):
        if section_title==Section.title:
            Section.change_teacher(new_teacher)
        self.audit_log.append(f'u {section_title} teper teacher {new_teacher}')
    def change_room(self, section_title, new_room):
        if section_title==Section.title:
            Section



        


