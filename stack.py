class ExtendedStack(list):
    def sum(self):
        
        self.append(self.pop(len(self)-1) + self.pop(len(self)-1))
        print(self)

    def sub(self):
        self.append(self.pop(len(self)-1) - self.pop(len(self)-1))
        print(self)

    def mul(self):
        self.append(self.pop(len(self)-1) * self.pop(len(self)-1) )
        print(self)

    def div(self):
        self.append(self.pop(len(self)-1)  // self.pop(len(self)-1) )
        print(self)



array = ExtendedStack([1,2,3,4,5,6,7,8,9])

array.sum()
array.sub()
array.mul()
array.div()