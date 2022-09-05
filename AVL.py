import os
import ctypes
import time
from random import randint
from User_input_requirements import repeat_condition
class Node():
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent
        self.height=None
        self.bf=None
class AVLTree():
    def __init__(self):
        self.__root_node__=None
    def insert(self,data):
        if self.__root_node__ is None:
            self.__root_node__=Node(data)
            self._set_height()
            self.height
            return None
        res=self.__insert__(data,self.__root_node__)
        self.__set_height__(self.__root_node__,0)
        return res
    def __insert__(self,data,node):
        if node.data==data:
            print("The Value is already present")
            return None
        if data>node.data:
            if node.right is None:
                node.right=Node(data,parent=node)
                self._set_height()
                self.height
                self.__balance_factor__(node.right)
                return None
            return self.__insert__(data,node.right)
        else:
            if node.left is None:
                node.left=Node(data,parent=node)
                self._set_height()
                self.height
                self.__balance_factor__(node.left)
                return None
            return self.__insert__(data,node.left)
    def delete(self,data):
        if self.__root_node__==None:
            print("The Tree is Empty")
            return None
        node=self.search(data)
        if node!=None:
            self.__delete__(node)
    def __smallest__(self,node):
        current_node=node
        while current_node.left!=None:
            current_node=current_node.left
        return current_node
    def __biggest__(self,node):
        current_node=node
        while current_node.right!=None:
            current_node=current_node.right
        return current_node
    def __delete__(self,current_node):
        if current_node.parent!=None:
            current_node_parent=current_node.parent
        childrens=self.__number_of_childs__(current_node)
        if childrens==0:
            if current_node.parent!=None:
                if current_node.parent.left==current_node:
                    current_node.parent.left=None
                    current_node=current_node.parent
                else:
                    current_node.parent.right=None
                    current_node=current_node.parent
            else:
                self.__root_node__=None
        if childrens==1:
            if current_node.parent!=None:
                if current_node_parent.left==current_node:
                    if current_node.left!=None:
                        current_node.left.parent=current_node_parent
                        current_node_parent.left=current_node.left
                        current_node=current_node.left
                    else:
                        current_node.right.parent=current_node_parent
                        current_node_parent.left=current_node.right
                        current_node=current_node.right
                else:
                    if current_node.left!=None:
                        current_node.left.parent=current_node_parent
                        current_node_parent.right=current_node.left
                        current_node=current_node.left
                    else:
                        current_node.right.parent=current_node_parent
                        current_node_parent.right=current_node.right
                        current_node=current_node.right
            else:
                if current_node.left!=None:
                    self.__root_node__=current_node.left
                    current_node.left.parent=None
                else:
                    self.__root_node__=current_node.right
                    current_node.right.parent=None
            self.height
        if childrens==2:
            successor=self.__biggest__(current_node.left)
            current_node.data=successor.data
            self.__delete__(successor)
        self.height
        self.__rebalance_tree__(current_node)
    def search(self,data):
        if self.__root_node__ is None:
            print("The Tree is Empty")
            return None
        return self.__search__(self.__root_node__,data)
    def __search__(self,current_node,data):
        if current_node.data==data:
            return current_node
        if current_node.data>data and current_node.left!=None:
            return self.__search__(current_node.left,data)
        if current_node.data<data and current_node.right!=None:
            return self.__search__(current_node.right,data)
        print("No Such data present")
        return None
    def find(self,data):
        res=self.search(data)
        if res!=None:
            print(res.data,"is present")
            return res
    def __number_of_childs__(self,node):
        childs=0
        if node.left!=None:
            childs+=1
        if node.right!=None:
            childs+=1
        return childs 
    def number_of_childs(self,data):
        res=self.search(data)
        if res!=None:
            return self.__number_of_childs__(res)
        return None
    @property
    def height(self):
        if self.__root_node__ is None:
            print("The tree is Empty")
            return None
        return self.__height__(self.__root_node__,0)
    def __height__(self,node,height=0):
        if node==None:
            return height
        left_height=self.__height__(node.left,height+1)
        right_height=self.__height__(node.right,height+1)
        node.bf=left_height-right_height
        return max(left_height,right_height)
    def _set_height(self):
        if self.__root_node__ is None:
            print("The Tree is Empty")
            return None
        self.__set_height__(self.__root_node__,0)
    def __set_height__(self,node,height):
        if node==None:
            return height
        left_subtree=self.__set_height__(node.left,height+1)
        right_subtree=self.__set_height__(node.right,height+1)
        node.height=height
    def __balance_factor__(self,node):
        if self.__root_node__ is None:
            print("The Tree s Empty")
            return None
        if node is None:
            self.height
            return
        if abs(node.bf)>1:
            self.__rebalance_tree__(node)
        self.__balance_factor__(node.parent)
    def __rebalance_tree__(self,node):
        balance_factor=node.bf
        current_node_parent=node.parent
        current_node=node
        if balance_factor==2:
            child_node=current_node.left
            self.__select_operation_lhs__(current_node,current_node_parent,child_node)
        elif balance_factor==-2:
            child_node=current_node.right
            self.__select_operation_rhs__(current_node,current_node_parent,child_node)
    def __select_operation_lhs__(self,current_node,current_node_parent,child_node):
        if child_node.bf==1:
            self.__right_rotation__(current_node,current_node_parent,child_node)
        elif child_node.bf==-1:
            right=child_node.right
            self.__left_rotation__(child_node,current_node,child_node.right)
            self.__right_rotation__(current_node,current_node_parent,right)
    def __select_operation_rhs__(self,current_node,current_node_parent,child_node):
        if child_node.bf==1:
            left=child_node.left
            self.__right_rotation__(child_node,current_node,child_node.left)
            self.__left_rotation__(current_node,current_node_parent,left)
        elif child_node.bf==-1:
            self.__left_rotation__(current_node,current_node_parent,child_node)
    def __right_rotation__(self,current_node,current_node_parent,child_node):
        right_child=child_node.right
        current_node.left=right_child
        child_node.right=current_node
        if current_node_parent!=None:
            if current_node_parent.left==current_node:
                current_node_parent.left=child_node
            else:
                current_node_parent.right=child_node
            child_node.parent=current_node_parent
        else:
            self.__root_node__=child_node
            child_node.parent=None
        current_node.parent=child_node
        if right_child!=None:
                right_child.parent=current_node
        self.height
    def __left_rotation__(self,current_node,current_node_parent,child_node):
        left_child=child_node.left
        current_node.right=left_child
        child_node.left=current_node
        if current_node_parent!=None:
            if current_node_parent.left==current_node:
                current_node_parent.left=child_node
            else:
                current_node_parent.right=child_node
            child_node.parent=current_node_parent
        else:
            self.__root_node__=child_node
            child_node.parent=None
        current_node.parent=child_node
        if left_child!=None:
            left_child.parent=current_node
        self.height
    @property
    def display(self):
        if self.__root_node__ is None:
            print("The Tree is Empty")
            return None
        while True:
            try:
                print("1.Inorder\n2.Preorder\n3.Postorder")
                choice=int(input("Enter the Manner in which the output should be displayed(1,2 or 3)"))
                if choice in [1,2,3]:
                    break
                else:
                    print("Out of Bounds,Try again.")
                    continue
            except ValueError:
                print("Wrong type of input")
                continue
        lst=[]
        if choice==1:
            res=self.__inorder__(lst,self.__root_node__)
            print(res)
            return res
        elif choice==2:
            res=self.__preorder__(lst,self.__root_node__)
            print(res)
        else:
            res=self.__postorder__(lst,self.__root_node__)
            print(res)
    def __inorder__(self,lst_elements,current_node):
        if current_node.left!=None:
            self.__inorder__(lst_elements,current_node.left)
        lst_elements.append(current_node.data)
        if current_node.right!=None:
            self.__inorder__(lst_elements,current_node.right)
        return lst_elements
    def __preorder__(self,lst_elements,current_node):
        lst_elements.append(current_node.data)
        if current_node.left!=None:
            self.__inorder__(lst_elements,current_node.left)
        if current_node.right!=None:
            self.__inorder__(lst_elements,current_node.right)
        return lst_elements
    def __postorder__(self,lst_elements,current_node):
        if current_node.left!=None:
            self.__inorder__(lst_elements,current_node.left)
        if current_node.right!=None:
            self.__inorder__(lst_elements,current_node.right)
        lst_elements.append(current_node.data)
        return lst_elements
    @property
    def display_level_wise(self):
        if self.__root_node__ is None:
            print("The Tree is Empty")
            return None
        return self.__level_wise_print__(self.__root_node__,0)
    def __level_wise_print__(self,node,level,tag=None):
        if level==0:
            print(str(node.data)+"\t"+" balance factor:-",str(node.bf))
            print()
        else:
            print("\t"*(level-1)+"|-----"+str(node.data)+" "+tag+"\t"+" balance factor:-",str(node.bf))
            print()
        if node.left!=None:
            self.__level_wise_print__(node.left,level+1,"(left of "+str(node.data)+")")
        if node.right!=None:
            self.__level_wise_print__(node.right,level+1,"(right of "+str(node.data)+")")
    @property
    def bfs(self):
        if self.__root_node__ is None:
            print("The Tree is Empty.")
            return None
        queue_list=[self.__root_node__]
        visited_list=[]
        self.__bfs__(queue_list,visited_list)
        result="-->".join(visited_list)
        print(result)
    def __bfs__(self,queue,visited):
        if len(queue)==0:
            return visited
        current_node=queue[0]
        if current_node.left!=None:
            queue.append(current_node.left)
        if current_node.right!=None:
            queue.append(current_node.right)
        visited.append(str(current_node.data))
        queue.pop(0)
        self.__bfs__(queue,visited)
    @property
    def dfs(self):
        if self.__root_node__ is None:
            print("The Tree is Empty")
            return None
        lst=[]
        res=self.__dfs__(lst,self.__root_node__)
        result="-->".join(res)
        print(result)
    def __dfs__(self,lst_elements,current_node):
        lst_elements.append(str(current_node.data))
        if current_node.left!=None:
            self.__dfs__(lst_elements,current_node.left)
        if current_node.right!=None:
            self.__dfs__(lst_elements,current_node.right)
        return lst_elements
    @property
    def random_tree_generator(self):
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
            max_number=inp_oper("Enter the Number of Values to be included in Tree:")
            ran=inp_oper("Enter the range within which the number should be selected:")
            if ran>max_number:
                break
            else:
                print("Range Provided",ran)
                print("The Numbers to be entered",max_number)
                print("Range Can't be less than number of elements to be printed.")
                time.sleep(3)
                os.system("cls")
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
            if present==None:
                self.insert(val)
                new_added+=1
            else:
                already_present+=1
            max_number-=1 
        if already_present==0:
            already_present="No"
        if already_present==1:
            already_present="only one"
        print("Since",already_present," randomly generated number were already present,we  added",new_added,"new numbers")
import logging
log_variable=logging.getLogger(__name__)

log_variable.setLevel(logging.DEBUG)
import os
name=os.path.basename(__file__).split(".")[0]+".txt"
fh=logging.FileHandler(name)
formatter=logging.Formatter('%(asctime)s:%(filename)s:%(levelname)s:%(message)s')
fh.setFormatter(formatter)
log_variable.addHandler(fh)

if __name__ == '__main__':
    log_variable.info("Executed")
    obj=AVLTree()
    def input_value():
        while True:
            try:
                os.system('cls')
                value=int(input("Enter The Value:-"))
                return value
            except ValueError:
                print("Wrong type of input,Try again.")
                time.sleep(2)
                continue
    def action_(lst):
        chance=5
        while chance!=0:
            if chance==1:
                time.sleep(3)
                os.system('cls')
                print("You have last chance left")
            else:
                time.sleep(3)
                os.system('cls')
                print(f"You have {chance} chance left")
            try:
                for x,y in enumerate(lst):
                    print(x+1,".",y)
                choice=int(input("Enter the Operation to be performed:"))
                if choice in range(len(lst)+1):
                    return choice-1
                chance-=1
            except ValueError:
                print("Wrong type of input,Try again.")
                chance-=1
                continue
        print("Out of chances...")
    def operation(action,lst,obj):
        _object=ctypes.cast(id(obj),ctypes.py_object).value
        function=eval("_object."+lst[action])
        try:
            if function.__code__.co_argcount>1:
                val=input_value()
                return eval("function(val)")
        except:
            return eval("function")
    execute=True
    lst_elements=[x for x in dir(obj) if not x.startswith("_")]
    while execute:
        choice=action_(lst_elements)
        operation(choice,lst_elements,obj)
        execute=repeat_condition()
    print("Thank You for using this Code")
else:
    log_variable.info(f'This Script was Imported')