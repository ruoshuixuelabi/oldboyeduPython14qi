
class MyStack(object):
    def __init__(self):
        self.data = []
        
    def push(self,item):
        self.data.append(item)
        
    def pop(self):
        return self.data.pop()
    
    def top(self):
        return self.data[-1]

ms = MyStack()
ms.push("123")

print(ms.pop())
print(ms.data)