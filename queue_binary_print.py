from collections import deque

class Queue : 
    def __init__ (self): 
        self.buffer = deque()

    def enqueue( self , val ): 
        self.buffer.appendleft(val)

    def dequeue( self  ): 
        if int( self.size())  == 0:
            print('Queue is empty')
            return
        return self.buffer.pop()

    def is_empty( self ): 
        return len ( self.buffer) == 0 
    
    def size( self  ): 
        return len ( self.buffer)
    
    def get_last( self ): 
        return self.buffer[-1]

q = Queue()

def print_binary (n): 
    q.enqueue( 1)
    for i in range( n ): 
        prefix = q.get_last() 
        print (i , ' = ',prefix)
        q.enqueue(str( prefix)+'0')
        q.enqueue(str(prefix)+'1')
        q.dequeue()

    
if __name__ == '__main__':
    print_binary( 10 )


# LINKS 
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md
# https://www.youtube.com/watch?v=rUUrmGKYwHw&t=11s

