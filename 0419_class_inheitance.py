class Employee:
    """직원 클래스"""
    company_name = "Burger King"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """시급 인상 메소드"""
        self.wage = *= self.raise_percentage

    def __str__(self):
        """직원 정보 문자열로 리턴하는 메소드"""
        return Employee.conpany_name + " 직원: " + self.name


class Cashier(Employee):    #Cashier가 자식 Employee가 부모인 클래스 생성
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold):
        """self.name = name
        self.wage = wage""" 
        super().__init__(name, wage)    #위 두 줄과 같은 뜻
        self.number_sold = number_sold

    def take_order(self, money_received):
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " +self.name"

class Delivery(Employee):
