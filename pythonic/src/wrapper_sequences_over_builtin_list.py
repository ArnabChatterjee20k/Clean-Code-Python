from collections.abc import Sequence

class Item(Sequence):
    def __init__(self,*values):
        self._values = list(values)
    
    def __len__(self) -> int:
        return len(self._values)

    def __getitem__(self,item):
        return self._values.__getitem__(item)
    
item = Item(1,2,3,4,5)
print(type(item[:2]))