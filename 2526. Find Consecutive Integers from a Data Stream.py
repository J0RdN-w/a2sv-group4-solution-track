from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        # to track a number which equals to self.vaue
        self.eqValue = 0   

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.eqValue += 1
        else:
            self.eqValue = 0
        return self.eqValue >= self.k



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
