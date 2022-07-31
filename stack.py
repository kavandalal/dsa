from collections import deque

class Stack : 
    def __init__ (self): 
        self.container = deque()

    def push( self , val ): 
        self.container.append(val)

    def pop( self  ): 
        return self.container.pop()

    def peek( self ): 
        return self.container[-1]
    
    def is_empty( self ): 
        return len ( self.container) == 0 
    
    def size( self  ): 
        return len ( self.container)
    
    def print_stack ( self ):
        print( self.container)

    def is_balanced(self, s):
        opening =  {'(': 1 ,'[': 2 ,'{': 3  }
        closing =  {')': 1 ,']': 2 ,'}': 3  }
        for i in s: 
            if i in opening:
                self.push(i)
            elif i in closing :
                if self.size() > 0 and opening[ self.peek()]  == closing[i]:
                    try:
                        self.pop()
                    except : 
                        return False
                else: return False
        return True if self.is_empty() else False


if __name__ == '__main__':
    s = Stack()
    # print( s.is_balanced('([{[{[A+B]}]}])'))
    print( s.is_balanced('(a+b){b+c}[x+y]'))


# LINKS https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=7