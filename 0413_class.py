class User:
    def say_hello(some_user):
        print(f"안녕하세요! 저는 {some_user.name}입니다!")

    def login(some_user, my_email, my_password):
        if (some_user == my_email and some_user.password == my_password):
            print("로그인 성공")
        else:
            print("로그인 실패")

user1 = User()
user2 = User()
user3 = User()      # 세개의 변수는 각자 다 다른 변수

user1.name = "조건희"
user1.email = "dyrnfmxm9@naver.com"
user1.password = "12345"

print(user1.email)
print(user1.name)

User.say_hello(user1)
user1.say_hello()       # 두 줄은 같은 표현

user1.login("dyrnfmxm9@naver.com", "12345")
