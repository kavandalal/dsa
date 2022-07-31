class HashTable: # HashMap / HashTable is the same
    def __init__ (self): 
        self.MAX_LEN = 10
        self.arr = [[] for i in range( self.MAX_LEN)]
    
    def get_hash( self , key): 
        h = 0 
        for char in key :
            h+= ord ( char)
        return h % self.MAX_LEN

    # t['march 9']  = 304
    def __setitem__ ( self , key , value ): 
        h = self.get_hash( key)
        found = False
        for ind , val in enumerate(self.arr[h] ):
            if val[0] == key and len ( val) == 2 :
                self.arr[h][ind] =  ( key , value ) 
                found = True
                break
        if not found:
            self.arr[h].append( ( key , value))
            
    
    # t['march 9']
    def __getitem__( self , key ): 
        h = self.get_hash( key)
        return self.arr[h]
    
    # del t['mar 9']
    def __delitem__( self , key): 
        h = self.get_hash( key)
        for ind , val in enumerate( self.arr[h]):
            if val[0] == key :
                del self.arr[h][ind] 

if __name__ == "__main__": 
    t= HashTable( )
    t['mar 9']  = 111
    t['mar 9']  = 222
    t['mar 10']  = 333
    t['apr 10']  = 444
    t['aug 6']  = 555
    t['dec 7']  = 666
    # print( t['dec 6'])
    # del t['mar 10']
    print( t.arr)
    
# LINKS https://www.youtube.com/watch?v=54iv1si4YCM&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=6