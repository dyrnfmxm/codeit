class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}, 비밀번호: *****"

user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 1. User 인스턴스 생성
# 2. __init__ 메소드 자동 호출



print(user1)
print(user2)
