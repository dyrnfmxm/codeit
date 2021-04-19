class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

user1.count = 5         # 같은 이름의 클래스변수 보다 인스턴스 변수가 읽어와짐
                        # 그렇기에 설정 할 때는 꼭 클래스 이름으로 설

print(User.count)
print(user1.count)
print(user2.count)
