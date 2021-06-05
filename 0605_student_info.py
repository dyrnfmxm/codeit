class Student:
    # 코드를 쓰세요
    def __init__(self, name, id, major):
        self.student_info = StudentInfo(name, id, major)
        self.grade = Grade()
        
class Grade:
    
    def __init__(self):
        self.grades = []
        
    def add_grade(self, grade):
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이어야 합니다!")
            
    def get_average_gpa(self):
        return sum(self.grades) / len(self.grades)

    def print_report_grade(self):
        print("평균 학점:{}".format(self.get_average_gpa()))
    
class StudentInfo:
    
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        
    def change_student_info(self, new_name, new_id, new_major):
        self.name = new_name
        self.id = new_id
        self.major = new_major
        
    def print_report_student_info(self):
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}"
        .format(self.name, self.id, self.major))
        
# 작성한 클래스에 맞춰서 실행 코드도 바꿔보세요
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.student_info.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)

# 학생 성적표 
younghoon.student_info.print_report_student_info()
younghoon.grade.print_report_grade()
    


            
