class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self,x):
        if(x>0):
            super().append(x)
        else:
            raise NonPositiveError( x + 'is not positive')
        

positive_list = PositiveList()

positive_list.append(2)