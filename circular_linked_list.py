'''This is a Modeule which is used to work with a circular linked list'''
import time
import os
import ctypes
import User_input_requirements
class Node():
    '''This Class Creates a node object'''
    def __init__(self,left=None,right=None,data=None):
        self.left=left
        self.right=right
        self.data=data

class LinkedList():
    '''this is the main circular linked list class'''
    def __init__(self):
        self.first=None
    def insert_at_start(self,value):
        '''To insert a value at start'''
        return self.__insert_at_start__(value)
    def __insert_at_start__(self,value):
        if self.first==None:
            node=Node(data=value)
            self.first=node
            return
        node=Node(right=self.first,data=value)
        self.first=node
        node.right.left=node
    def insert_at_end(self,value):
        '''to insert a value at end and to insert values'''
        return self.__insert_at_end__(value)
    def __insert_at_end__(self,value):
        if self.first==None:
            self.first=Node(data=value)
            return
        elements=self.first
        while elements.right:
            elements=elements.right
        elements.right=Node(left=elements,data=value)
        return
    def search_value(self,value):
        '''to search a Node from the linked list'''
        if self.first==None:
            print("The Linked List is Empty.")
            return
        return self.__search_value__(value)
    def __search_value__(self,value):
        if self.first.data==value:
            return self.first
        elements=self.first
        if elements.data==value:
            return elements
        while elements.right:
            elements=elements.right
            if elements.data==value:
                return elements
        print("The Value is not present")
        return
    def find_value(self,value):
        '''to find a value from the linked list'''
        return self.__find_value__(value)
    def __find_value__(self,value):
        result=self.search_value(value)
        if result==None:
            print("Try other operation")
        else:
            print("Value is ",result.data)
            return result
    @property
    def length(self):
        '''This is to check the length of LL'''
        return self.__len__
    @property
    def __len__(self):
        if self.first==None:
            print("The List is Empty")
            return None
        length=1
        ele=self.first
        while ele.right:
            ele=ele.right
            length+=1
        return length
    def insert_before_value(self,value,data):
        '''insering before a value'''
        return self.__insert_before_value__(value,data)
    def __insert_before_value__(self,value,data):
        node_element=self.search_value(value)
        if node_element==None:
            print("Try Some Other value or operation")
            return
        new_node=Node(node_element.left,node_element,data)
        if node_element.left!=None:
            node_element.left.right=new_node
        node_element.left=new_node
        return
    def insert_after_value(self,value,data):
        '''inserting after a value'''
        return self.__insert_after_value__(value,data)
    def __insert_after_value__(self,value,data):
        node_element=self.search_value(value)
        if node_element==None:
            print("Try Some Other value or operation")
            return
        new_node=Node(node_element,node_element.right,data)
        if node_element.right!=None:
            node_element.right.left=new_node
        node_element.right=new_node
    def delete_by_value(self,value):
        '''deleting a node using value'''
        return self.__delete_by_value__(value)
    def __delete_by_value__(self,value):
        node_element=self.search_value(value)
        print(node_element,node_element.data)
        if node_element==None:
            print("Try Some Other value or operation")
            return
        if node_element==self.first:
            self.first.right.left=None
            self.first=self.first.right
            return
        if node_element.left!=None:
            node_element.left.right=node_element.right
        if node_element.right!=None:
            node_element.right.left=node_element.left
    def insert_at_position(self,index,value):
        '''inserting at position'''
        return self.__insert_at_position__(index,value)
    def __insert_at_position__(self,index,value):
        if index<0 or index>self.__len__:
            print("Out Of Bounds")
            return
        index-=1
        elements=self.first
        while index!=0:
            elements=elements.right
            index-=1
        new_node=Node(elements.left,elements,value)
        if elements.left!=None:
            elements.left.right=new_node
        elements.left=new_node
    def delete_from_position(self,index):
        '''deleting using position'''
        return self.__delete_from_position__(index)
    def __delete_from_position__(self,position):
        if position<0 or position>self.__len__:
            print("Out Of Bounds")
            return
        position-=1
        elements=self.first
        while position!=0:
            elements=elements.right
            position-=1
        if elements==self.first:
            self.first.right.left=None
            self.first=self.first.right
            return
        if elements.left!=None:
            elements.left.right=elements.right
        if elements.right!=None:
            elements.right.left=elements.left
        return
    def replace(self,value,data):
        '''Replace a data value with other value'''
        return self.__replace__(value,data)
    def __replace__(self,value,data):
        node_element=self.search_value(value)
        if node_element==None:
            print("Try Some Other value of different operation.")
            return
        node_element.data=data
        return
    @property
    def display(self):
        '''Display the linked list'''
        return self.__display__
    @property
    def __display__(self):
        if self.first==None:
            print("The List is Empty")
            return
        lst=[]
        elements=self.first
        lst.append(str(elements.data))
        while elements.right:
            elements=elements.right
            lst.append(str(elements.data))
        element_list="--->".join(lst)
        #print(element_list)
        return element_list
    def __str__(self):
        action=self.__display__
        if action==None:
            return "Nothing to print"
        return action
    def insert_multiple_values(self):
        '''To Insert Multiple Values at a Time'''
        chance=5
        while chance!=0:
            if chance==1:
                print("You have Last chance left")
                time.sleep(3)
            else:
                print("You have",chance,"chances left")
                time.sleep(3)
            try:
                inp=int(input("Enter the Number of values to be entered:"))
                break
            except ValueError:
                print("This is Not a Valid Input type")
                chance-=1
        if inp==None:
            print("Out of chances")
            return
        values=[]
        while inp!=0:
            try:
                v=int(input("Enter the Value:"))
                inp-=1
                values.append(v)
            except ValueError:
                print("Try Proper type of Value")
                continue
        for x in values:
            self.insert_at_end(x)
    # def __repr__(self):
    #     action=self.__display__
    #     if action==None:
    #         return "Nothing to print"
    #     return action
if __name__ == '__main__':
    obj=LinkedList()
    lst=[]
    for x in dir(obj):
        if not x.startswith("_"):
            lst.append(x)
    if 'first' in lst:
        lst.remove('first')
    def choice(lst_elements):
        '''This takes the input from the user'''
        chance=5
        while chance!=0:
            if chance==1:
                print("You have Last chance left")
                time.sleep(3)
            else:
                print("You have",chance,"chances left")
                time.sleep(3)
            try:
                os.system('cls')
                for sr_no,oper_names in enumerate(lst):
                    print(str(sr_no+1)+".",oper_names)
                option=int(input("Enter the choice:"))
                if option in range(len(lst_elements)+1):
                    return option-1
                print("This is not a valid input")
                chance-=1
                continue
            except ValueError:
                print("This is Not a Valid Input type")
                chance-=1
    def value_input(string):
        '''Take value and data from user'''
        req=string
        while True:
            try:
                os.system('cls')
                val=int(input("Enter the "+req+":"))
                break
            except ValueError:
                print("Not a Proper type of Input.")
                time.sleep(3)
                continue
        return val
    def index_position():
        '''Takes the Index Position'''
        while True:
            try:
                os.system('cls')
                index=int(input("Enter the Index Position:"))
                break
            except ValueError:
                print("Not a proper type of input.")
                time.sleep(3)
                continue
        return index
    def operation(lst,choice,obj_):
        '''This Performs the main operation'''
        oper=lst[choice]
        value_variable=None
        index_variable=None
        data_variable=None
        object_address=id(obj_)
        _object=ctypes.cast(object_address,ctypes.py_object).value
        func=eval("_object."+oper)
        try:
            arguments=func.__code__.co_varnames
            if "value" in arguments:
                value_variable=value_input("Value")
            if "data" in arguments:
                data_variable=value_input("data to be Entered or inserted")
            if "index" in arguments:
                index_variable=index_position()
            value=value_variable
            data=data_variable
            index=index_variable
            args=[index,value,data]
            args1=[]
            for x in args:
                if x==None:
                    pass
                else:
                    args1.append(x)
            x=eval("_object."+oper+"(*args1)")
            if x!=None:
                return x
            print("Done")
        except:
            if callable(func):
                print(oper)
                return eval("_object."+oper+"()")
            return func
    execute=True
    while execute:
        action=choice(lst)
        operation(lst,action,obj)
        execute=User_input_requirements.repeat_condition()
    print("Thank You For Using Our Code")
