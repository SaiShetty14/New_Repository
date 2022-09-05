'''This is a program for binary search tree'''
import os
import time
import ctypes
from random import randint
import User_input_requirements
class Node():
    '''Creating a node'''
    def __init__(self,data,left=None,right=None,parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent
class BinarySearchTree():
    '''This is a class for binary tree'''
    def __init__(self):
        self.__root_node__=None
    def insert(self,data):
        '''Inserting New element'''
        return self.__insert__(data)
    def __insert__(self,data):
        if self.__root_node__==None:
            node=Node(data)
            self.__root_node__=node
            return None
        self.__recursive_insert__(data,self.__root_node__)
    def __recursive_insert__(self,data,current_node):
        if current_node.data==data:
            print("Value already Present")
            return None
        if current_node.data>data:
            if current_node.left==None:
                current_node.left=Node(data,parent=current_node)
                return
            else:
                self.__recursive_insert__(data,current_node.left)
        else:
            if current_node.right==None:
                current_node.right=Node(data,parent=current_node)
                return
            else:
                self.__recursive_insert__(data,current_node.right)
    @property
    def height(self):
        '''checking the height of the tree'''
        return self.__height__()
    def __height__(self):
        height_=0
        if self.__root_node__==None:
            print("The Tree is Empty")
            return height_
        return self.__recursive_height__(height_,self.__root_node__)
    def __recursive_height__(self,height,current_node):
        if current_node==None:
            return height
        left_height=self.__recursive_height__(height+1,current_node.left)
        right_height=self.__recursive_height__(height+1,current_node.right)
        return max(left_height,right_height)
    def search(self,data):
        '''Searching an element'''
        return self.__search__(data)
    def __search__(self,data):
        if self.__root_node__==None:
            print("The List is Empty")
            return None
        return self.__recursive_search__(data,self.__root_node__)
    def __recursive_search__(self,data,current_node):
        if current_node.data==data:
            return current_node
        if current_node.data<data and current_node.right!=None:
            return self.__recursive_search__(data,current_node.right)
        if current_node.data>data and current_node.left!=None:
            return self.__recursive_search__(data,current_node.left)
        print("The data is not present")
        return None
    def find(self,data):
        '''Finding New element'''
        return self.__find__(data)
    def __find__(self,data):
        result=self.__search__(data)
        if result!=None:
            print("Found the data in the tree")
            return result.data
        print("Kahi tari gochi ahe")
    def number_of_childs(self,data):
        '''Checking Number of childs'''
        return self.__number_of_childs__(data)
    def __number_of_childs__(self,data):
        node=self.__search__(data)
        if node!=None:
            childs=self.__number_of_childs__using__node(node)
            return childs
        return node
    def __number_of_childs__using__node(self,node):
        childs=0
        if node.left!=None:
            childs+=1
        if node.right!=None:
            childs+=1
        return childs
    def delete(self,data):
        '''Deleting a node'''
        return self.__delete__(data)
    def __delete__(self,data):
        node=self.__search__(data)
        if node!=None:
            #print("Here")
            return self.__delete_node__(node)
        return None
    def __delete_node__(self,node):
        #print("Here,in delete_node")
        #print("Trying to delete",node.data)
        child=self.__number_of_childs__using__node(node)
        #print("Baccha",child)
        def smallest(node):
            c_node=node
            while c_node.left!=None:
                c_node=c_node.left
            return c_node
#         def largest(node):
#             c_node=node
#             while c_node.right!=None:
#                 c_node=c_node.right
            #return c_node
        if child==0:
            #print("Idhar aaya")
            if node.parent!=None:
                #print("Baap hai")
                if node.parent.left==node:
                    node.parent.left=None
                else:
                    node.parent.right=None
            else:
                print("Baap nahi hai")
                self.__root_node__=None
        elif child==1:
            if node.parent!=None:
                if node.left!=None:
                    if node.parent.left==node:
                        node.parent.left=node.left
                        node.left.parent=node.parent
                    else:
                        node.parent.right=node.left
                        node.left.parent=node.parent
                else:
                    if node.parent.left==node:
                        node.parent.left=node.right
                        node.right.parent=node.parent
                    else:
                        node.parent.right=node.right
                        node.right.parent=node.parent        
            else:
                if node.left!=None:
                    self.__root_node__=node.left
                    node.left.parent=None
                else:
                    self.__root_node__=node.right
                    node.right.parent=None
        elif child==2:
            successor=smallest(node)
            node.data=successor.data
            self.__delete_node__(successor)
    def __inorder__(self,lst,current_node):
        if current_node.left!=None:
            self.__inorder__(lst,current_node.left)
        lst.append(current_node.data)
        if current_node.right!=None:
            self.__inorder__(lst,current_node.right)
        return lst
    def __preorder__(self,lst,current_node):
        lst.append(current_node.data)
        if current_node.left!=None:
            self.__preorder__(lst,current_node.left)
        if current_node.right!=None:
            self.__preorder__(lst,current_node.right)
        return lst
    def __postorder__(self,lst,current_node):
        if current_node.left!=None:
            self.__postorder__(lst,current_node.left)
        if current_node.right!=None:
            self.__postorder__(lst,current_node.right)
        lst.append(current_node.data)
        return lst
    @property
    def display(self):
        '''Displaying the elements'''
        return self.__print__()
    def __print__(self):
        if self.__root_node__==None:
            print("The Tree is Empty")
            return
        print("1.Preorder\n2.Postorder\n3.Inorder")
        while True:
            try:
                choice=int(input("Enter/Select the choice from above:"))
                if choice in [1,2,3]:
                    break
                continue
            except ValueError:
                print("Wrong type of input,Try again.")
                continue
        lst=[]
        if choice==1:
            res=self.__preorder__(lst,self.__root_node__)
            print(res)
            return res
        elif choice==2:
            res=self.__postorder__(lst,self.__root_node__)
            print(res)
            return res
        else:
            res=self.__inorder__(lst,self.__root_node__)
            print(res)
            return res
    def __str__(self):
        return self.__print__()
    def parent_node(self,data):
        '''Checking the parent Node'''
        node=self.__search__(data)
        if node!=None:
            print(node.parent)
            if node.parent!=None:
                return node.parent.data
        #print("Hag diya bhai")
        return None
    @property
    def level_wise_print(self):
        '''Printing the tree levelwise'''
        lst=[]
        level=0
        ans=self.__printing_style__(lst,self.__root_node__,level)
        for x in ans:
            print(x)
    def __printing_style__(self,res,current_node,l):
        if l!=0:
            res.append("\t"*(l-1)+"|-------"+str(current_node.data)+"\n")
        else:
            res.append("\t"*l+str(current_node.data))
        #print(res)
        if current_node.left!=None:
            self.__printing_style__(res,current_node.left,l+1)
        #print(res)
        if current_node.right!=None:
            self.__printing_style__(res,current_node.right,l+1)
        return res
    @property
    def bfs(self):
        '''This will print the result in bfs manner'''
        if self.__root_node__==None:
            print("The List is Empty")
            return None
        queue_list=[self.__root_node__]
        visited_list=[]
        final=self.__bfs__(queue_list[0],queue_list,visited_list)
        result=[str(x.data) for x in final]
        answer="--->".join(result)
        print(answer)
    def __bfs__(self,current_node,queue_lst,visited_lst):
        if current_node.left!=None:
            queue_lst.append(current_node.left)
        if current_node.right!=None:
            queue_lst.append(current_node.right)
        element=queue_lst.pop(0)
        visited_lst.append(element)
        if len(queue_lst)==0:
            return visited_lst
        else:
            return self.__bfs__(queue_lst[0],queue_lst,visited_lst)
    '''The Concept of heapify will work for a normal binary tree but not for a Binary search tree'''
    # @property
    # def heapify(self):
    #     '''This Will heapify the tree'''
    #     if self.__root_node__==None:
    #         print("The Tree is Empty")
    #         return None
    #     while True:
    #         try:
    #             print("1.Max Heap\n2.Min Heap")
    #             option=int(input("Enter the action to perform:"))
    #             if option in [1,2]:
    #                 break
    #             else:
    #                 print("Out of bounds,Try again")
    #                 continue
    #         except ValueError:
    #             print("Wrong type of input.")
    #             continue
    #     q=[self.__root_node__]
    #     v=[]
    #     result=self.__bfs__(self.__root_node__,q,v)
    #     result_data=[x.data for x in result]
    #     if option==1:
    #         result_data.sort(reverse=True)
    #     else:
    #         result_data.sort()
    #     for x in range(len(result)):
    #         result[x].data=result_data[x]
    @property
    def random_tree_generator(self):
        '''Generating a random tree'''
        def inp_oper(statement):
            while True:
                try:
                    data=int(input(statement))
                    return data
                except ValueError:
                    print("Wrong Type of input,Try again.")
                    continue
        while True:
            try:
                os.system('cls')
                print("1.Create a Complete new tree\n2.Add to the existing tree")
                o_or_t=int(input("Enter the action to be performed:"))
                if o_or_t in [1,2]:
                    break
                print("Out of bounds")
                time.sleep(3)
                continue
            except ValueError:
                print("Wrong Type of input,Try again.")
                time.sleep(3)
                continue
        while True:
            os.system('cls')
            max_number=inp_oper("Enter the Number of Values to be included in Tree:")
            ran=inp_oper("Enter the range within which the number should be selected:")
            if ran>max_number:
                break
            else:
                print("Range Provided",ran)
                print("The Numbers to be entered",max_number)
                print("Range Can't be less than number of elements to be printed.")
                time.sleep(4)
                continue
        if o_or_t==1:
            self.__root_node__=None
        already_present=0
        new_added=0
        while max_number!=0:
            val=randint(1,ran)
            os.system('cls')
            print("The Value that we are trying to enter is",val)
            time.sleep(3)
            present=self.search(val)
            time.sleep(3)
            if present==None:
                self.__insert__(val)
                new_added+=1
            else:
                already_present+=1
            max_number-=1
        print("Since",already_present," randomly generated numbers were already present,we added",new_added,"numbers")
if __name__ == '__main__':
    import logging
    log_variable=logging.getLogger(__name__)
    
    log_variable.setLevel(logging.DEBUG)
    import os
    name=os.path.basename(__file__).split(".")
    name=name[0]+".txt"
    fh=logging.FileHandler(name)
    formatter=logging.Formatter('%(asctime)s:%(filename)s:%(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    log_variable.addHandler(fh)
    
    log_variable.info("Executed")
    execute=True
    obj=BinarySearchTree()
    def input_operation(statement):
        while True:
            try:
                os.system('cls')
                data=int(input(statement))
                return data
            except ValueError:
                print("Wrong Type of input,Try again.")
                time.sleep(3)
                continue

    def choices(lst_elements):
        chance=5
        while chance!=0:
            if chance==1:
                print("You have last chance left.")
                time.sleep(3)
            else:
                print("You have",chance,"chances left")
                time.sleep(3)
            try:
                os.system('cls')
                for x,y in enumerate(lst_elements):
                    print(x+1,y)
                choice=int(input("Enter the Operation to be performed:"))
                if choice in range(len(lst_elements)+1):
                    return (choice-1,lst_elements[choice-1])
                else:
                    chance-=1
            except ValueError:
                print("Wrong type of input,")
                chance-=1
        print("You are out of chance")
        return (None,None)
    def operation(action,obj_,dictionary):
        _object=ctypes.cast(id(obj_),ctypes.py_object).value
        function=eval("_object."+action)
        if action in d:
            value=input_operation(dictionary[action])
            result=eval("function(value)")
            return result
        return eval('function')
    options=[]
    for x in dir(obj):
        if not x.startswith("_"):
            options.append(x)
    d={}
    d["delete"]="Enter the Node Value to be deleted:"
    d["parent_node"]="Enter the Node whose parent is to be checked:"
    d["search"]="Enter the Node value to be searched in the tree:"
    d["find"]="Enter the Node Value to Find:"
    d["insert"]="Enter the Value to insert:"
    d["number_of_childs"]="Enter the Node Value wjose Childs are to be checked"
    while execute:
        number,action=choices(options)
        if action!=None:
            operation(action,obj,d)
        execute=User_input_requirements.repeat_condition()
    print("Thank You For Running this code.")
