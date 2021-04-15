class User:
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, my_email, my_password):
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공")
        else:
            print("로그인 실패")

    def check_name(self, name):
        return self.name == name

user1 = User()      # 세개의 변수는 각자 다 다른 변수

user1.name = "조건희"
user1.email = "dyrnfmxm9@naver.com"
user1.password = "12345"


User.say_hello(user1)
user1.say_hello()       # 두 줄은 같은 표현

user1.login("dyrnfmxm9@naver.com", "12345")

print(user1.check_name("조건희"))
print(user1.check_name("김율희"))
