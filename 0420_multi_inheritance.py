class Engineer:
    """엔지니어 클래스"""
    def __init__(self, gavorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print(f"{self.favorite_language}(으)로 프로그래밍 합니다.")


class TennisPlayer:
    """테니스 선수 클래스"""
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print(f"{tennis_level} 반에서 테니스를 칩니다.")


class EngineerTennisPlayer(Engineer, TennisPlayer):
    """다중 상속 클래스"""
    def __init__(self, favorite_language, tennis_level):
        Engineer.__init__(self, favorite_language)
        TennisPlayer.__init__(self, tennis_level)       #super()를 사용할 경우 명확하지 않음

        
