class HashTable: # HashMap / HashTable is the same
    def __init__ (self): 
        self.MAX_LEN = 10
        self.arr = [None for i in range( self.MAX_LEN)]
    
    def get_hash( self , key): 
        h = 0 
        for char in key :
            h+= ord ( char)
        return h % self.MAX_LEN

    # t['march 9']  = 304
    def __setitem__ ( self , key , value ): 
        h = self.get_hash( key)
        if self.arr[h ] == None:
            self.arr[h ] = ( key , value)
            return
        if self.arr[h ][0 ] == key:
            self.arr[h ] = ( key, value)
            return
        x = self.get_index_linear_probing( h)
        self.arr[x] = ( key,value)
        
    # get the available index after main hash value in not empty
    def get_index_linear_probing( self , h): 
        x = h
        for _ in range( self.MAX_LEN):
            x = (x+1) % self.MAX_LEN
            if self.arr[x] == None:
                return x 
        raise Exception( "No Index Is Empty")

    # t['march 9']
    def __getitem__( self , key ): 
        h = self.get_hash( key)
        print( '111')
        if self.arr[h][0 ] == key:
            return self.arr[h]
        else: 
            i = self.find_element_after_index( h , key)
            return self.arr[i]

    # find the element location after it was not found in the hash function postion
    def find_element_after_index(self , h , key):
        x = h 
        for _ in range( self.MAX_LEN):
            x = (x + 1 )% self.MAX_LEN
            if self.arr[x] != None and self.arr[x][0] == key:
                return x
        raise Exception( 'Element Not Found')

    # del t['mar 9']
    def __delitem__( self , key): 
        h = self.get_hash( key)
        if self.arr[h][0] == key:
            self.arr[h] = 0 
        else: 
            i = self.find_element_after_index( h , key)
            self.arr[i] = None

    # get the total number of location that is left in arr
    def get_empty_location( self):
        c = 0 
        for i in self.arr:
            if i == None:
                c+=1
        return c

    # get the total number of location that is filled
    def get_filled_location( self):
        c = 0 
        for i in self.arr:
            if i != None:
                c+=1
        return c


if __name__ == "__main__": 
    t= HashTable( )
    t['mar 9']  = 1
    t['mar 9']  = 2
    t['mar 10']  = 3
    t['apr 10']  = 4
    t['aug 6']  = 5
    t['aug 25']  = 6
    t['aug 17']  = 7
    t['aug 20']  = 8
    t['sep 20']  = 9
    t['dec 7']  = 10
    t['dec 10'] = 11
    # print( t.get_hash('dec 10'))
    # print( t.get_filled_location() ) 
    # print( t.get_empty_location() ) 
    # print( t['aug 25'])
    # del t['dec 7']
    print( t.arr)

# LINKS https://www.youtube.com/watch?v=54iv1si4YCM&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=6