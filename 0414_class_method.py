class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def __str__(self):
        return f"User: {self.name}, E-mail: {self.email}, Password: {self.pw}"

    @classmethod
    def number_of_users(cls):
        print(f"total users number:{cls.count}")   # cls.count == User.count
"""
    def number_of_users(self):
        print(f"total users number:{User.count}")
        # self는 사용하지 않지만 User라는 클래스 변수를 사용하기 때문에
        # 굳이 인스턴스 메소드를 사용할 필요가 없
"""

user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

User.number_of_users()
user1.number_of_users()
