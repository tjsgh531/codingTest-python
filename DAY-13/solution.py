class BT:
    def __init__(self):
        self.bt = [None,0]
        self.level = 1
        self.count = 0

    def add(self,item):
        self.level *= 2
        temp = [item * ((-1)**i) for i in range(self.level)]
        self.bt += temp

    def search(self, target):
        for i in range(self.level, len(self.bt)):
            sum = 0
            current = i
            while current > 1:
                sum += self.bt[current]
                current = current // 2
            print(f'sum: {sum}')
            if sum == target: self.count += 1
        return self.count

def solution(numbers, target):
    numTree = BT()
    for value in numbers:
       numTree.add(value)
    print(numTree.bt)
    return numTree.search(target)