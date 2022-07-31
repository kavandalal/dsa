from collections import deque
import time
import threading

class Queue : 
    def __init__ (self): 
        self.buffer = deque()

    def enqueue( self , val ): 
        self.buffer.appendleft(val)

    def dequeue( self  ): 
        return self.buffer.pop()

    def is_empty( self ): 
        return len ( self.buffer) == 0 
    
    def size( self  ): 
        return len ( self.buffer)

q = Queue()

def provider_func (orders): 
    for i in orders:
        q.enqueue( i)
        print( f'+ enqueue ( ordering ) = {q.buffer}')
        time.sleep( 0.5)

def consumer_func():
    while True: 
        if q.is_empty(): 
            break
        q.dequeue( )
        print( f'- dequeue ( serving ) = {q.buffer}')
        time.sleep( 2)

    
if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']

    provider = threading.Thread( target=provider_func , args=( orders ,))
    consumer = threading.Thread( target=consumer_func )

    provider.start()
    time.sleep( 1)
    consumer.start()


# LINKS 
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md
# https://www.youtube.com/watch?v=rUUrmGKYwHw&t=11s

