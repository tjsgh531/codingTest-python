#리스트 -> 선형 검색 O(n)
def listSearch(arr, key):
    for index, value in enumerate(arr) :
        if value == key: 
            print(f"arr[{index}]에 있습니다.")
            return 0
    print(f"arr안에 {key}가 없습니다")
    return -1
         
# 이진 탐색 트리 -> O(logn) 최악 = 한쪽으로 쏠린 경우 O(n)
# 단순구현 vs 재귀적 구현

class Node :
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root) :
        self.root = root

    def insert(self, value):
        self.current_node = self.root
        while(True):
            if value < self.current_node.value:
                if not(self.current_node.left == None):
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left =  Node(value)
                    break
            else:
                if not(self.current_node.right == None):
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delte(self, value):
        # value node를 찾고 - search쓰면 안됨???
        # 그 노드가 자식을 두마리 들고 있을 경우 / 왼쪽만 들고 있을 경우 / 오른쪽만 들고 있을 경우 / 없을 경우
        self.current_node = self.root;
        while self.current_node == value:


