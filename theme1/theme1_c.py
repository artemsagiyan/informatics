class Basket:
    def __init__(self, cnt_peoples, cnt_apples):
        self.cnt_peoples = cnt_peoples
        self.cnt_apples = cnt_apples

    def avg_cnt_apples(self):
        return self.cnt_peoples // self.cnt_apples


N = int(input())
K = int(input())
basket = Basket(K, N)
print(basket.avg_cnt_apples())
