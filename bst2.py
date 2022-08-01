class BST: 
    def __init__ ( self ,data): 
        self.data = data 
        self.left = None
        self.right = None 
    
    # insert elements 
    def insert_element( self , data): 
        if self.data  == data: 
            return
        if data < self.data: 
            if self.left : 
                self.left.insert_element(data) 
            else: 
                self.left  = BST( data)
        else : 
            if self.right : 
                self.right.insert_element(data) 
            else: 
                self.right  = BST( data)

    # inorder traversal
    def inorder( self): 
        elements = [ ]
        if self.left:
            elements += self.left.inorder()
        elements.append( self.data)
        if self.right :
            elements += self.right.inorder()
        return elements

    # preorder traversal
    def preorder( self): 
        elements = [ ]
        elements.append( self.data)
        if self.left:
            elements += self.left.inorder()
        if self.right :
            elements += self.right.inorder()
        return elements
    
    # postorder traversal
    def postorder( self): 
        elements = [ ]
        if self.left:
            elements += self.left.inorder()
        if self.right :
            elements += self.right.inorder()
        elements.append( self.data)
        return elements
    
    # search if the element is present of not
    def search ( self , val): 
        if self.data == val : 
            return True
        if self.data > val: 
            if self.left:
                return self.left.search( val)
            else : return False
        else: 
            if self.right: 
                return self.right.search( val)
            else: return False

    # find min value from the tree
    def find_min ( self): 
        if self.left is None:
            return self.data
        else :
            return self.left.find_min( )

    # find max value from the tree
    def find_max ( self): 
        if self.right is None:
            return self.data
        else:
            return self.right.find_max( )
    
    # calculate the sum of all the members of the tree
    def calculate_sum(self ): 
        all = self.inorder()
        return sum(all)

    # delete node from the tree
    def delete_node(self, val): 
        if val < self.data: 
            if self.left: 
                self.left =self.left.delete_node(val)
        elif val > self.data: 
            if self.right :
                self.right = self.right.delete_node(val)
        else: 
            if self.left is None and self.right is None: 
                return None
            if self.left is None : 
                return self.right
            if self.right is None: 
                return self.left

            # taking successor from the right tree
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete_node( min_val)

            # taking successor from the left tree
            min_val = self.left.find_max()
            self.data = min_val
            self.left = self.left.delete_node( min_val)

        return self 


def build_tree( elements ): 
    root = BST( elements[0])
    for i in range( 1 , len ( elements)):
        root.insert_element( elements[i])
    return root

if __name__ == "__main__": 
    elements  = [45,7,2,49,75,12,16,84] 
    # elements  = [17,4,1,20,9,23,18,34] 
    root  = build_tree( elements)
    # print('in =', root.inorder())
    # print('pre =', root.preorder())
    # print('post =', root.postorder())
    # data  = root.search( 72)
    # print ('min =',root.find_min())
    # print ('max =',root.find_max())
    # print ( 'sum =',root.calculate_sum())
    # root.delete_node( 45)

# LINKS 
# https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10
# https://www.youtube.com/watch?v=JnrbMQyGLiU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=11