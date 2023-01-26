class NumbersList(list):
    def __init__(self, *args):
        for arg in args:
            if type(arg) not in (int, float):
                raise TypeError('Only int and float values allowed to init')
        super().__init__(args)

    def append(self, arg):
        if type(arg) not in (int, float):
            raise TypeError('Only int and float values allowed to append')
        super().append(arg)
        
    def extend(self, args):
        for arg in args:
            if type(arg) not in (int, float):
                raise TypeError('Only int and float values allowed to extend')
        super().extend(args)

    def get_sum(self):
        return sum(self)

    def get_average(self):
        return sum(self) / len(self)
    
num = NumbersList(1,2,3,4,5,6.7)
print(str(num))
num.append(6)
print(str(num))
num.extend([3,4,5])
print(str(num))

#num2 = NumbersList(1,2,3,"o",5) - da eroarea
#num2 = NumbersList(1,2,3,5) - e bine
#num2.append("o") - da eroarea
#num2.extend(["o",3,5]) - da eroarea

print(num.get_sum())
print(num.get_average())
