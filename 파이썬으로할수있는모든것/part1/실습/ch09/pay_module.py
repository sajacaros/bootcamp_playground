version = 2.0


def printAuthor():
    print("start coding")


class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time

    def get_pay_info(self):
        return f"{self.id} {self.price} {self.time}"

if __name__ == "__main__":
    print("pay module 실행")
    pay = Pay(10,20,30)
    print(pay.get_pay_info())
