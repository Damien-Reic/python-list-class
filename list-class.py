
class Liste:

    class Element:
        def __init__(self,element_before,element_after = None) -> None:
            self.element_before = element_before
            self.element_after = element_after
                    
        def __repr__(self) -> str:
            return f'{self.element_before},{self.element_after}'
        

        def __len__(chained_elements : "Liste.Element") -> int:
            return 0 if chained_elements.element_after is None else 1 + Liste.Element.__len__(chained_elements.element_after)
    
    
    def __init__(self,*args) -> None:
        last = None
        self.lenght  = -1
        for act_element in reversed(args):
            self.elements = Liste.Element(act_element,last)
            last = self.elements
            self.lenght += 1
        if len(args) == 0:
            self.elements = Liste.Element(None)
            

    def __repr__(self) -> str:
        return f'[{self.elements}]'    

    
    def __len__(self) -> int:
        return len(self.elements)
    
    
    def append(self, other) -> None:
        self.elements = Liste.Element(other,self.elements) 
        self.lenght += 1
        
    def pop(self):
        value = self.elements.element_before
        self.elements = Liste.Element(self.elements.element_after.element_before,self.elements.element_after.element_after)
        self.lenght -= 1
        return value
    
    def is_empty(self) -> bool:
        return self.elements.element_after is None

     
               
a = Liste('laa',1124,71,'asas')

print(a)
print(len(a))
         


