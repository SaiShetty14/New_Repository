import copy
import os
import time
import ctypes
from User_input_requirements import repeat_condition
from ordinal import ordinal
class Graph():
    def __init__(self):
        self.__vertex__=set()
        self.__Edges__=set()
        self.__neighbours__={}
        self.__edge_length_value__={}
    def insert_multiple_values(self):
        while True:
            try:
                numbers=int(input("Enter the Number of values to be Entered:."))
                if numbers>=1:
                    break
                else:
                    print("That is Not a proper type of Input.")
                    continue
            except ValueError:
                print("Wrong type of Input,Try again.")
                continue
        value=0
        while value!=numbers:
            value+=1
            num=ordinal(value)
            data=input(f"Enter the {num} node.:")
            res=self.__insert__(data)
            if res==None:
                print("You should try some other element.")
                value-=1
                continue
    def insert_vertex(self,data):
        return self.__insert__(data)
    def __insert__(self,data):
        d=data.upper() if data.isalpha() else data
        if d in self.__vertex__:
            print("The vertex is already present")
            return None
        self.__vertex__.add(d)
        self.__neighbours__[d]=set()
        return "Chutiya"
    def __node_input__(self,node):
        while True:
            value=input("Enter the "+node+" vertex:")
            if value.isalpha():
                value=value.upper()
            if value not in self.__vertex__:
                print("The vertex",value,"is not present")
                return None
            return value
    def create_edge(self):
        return self.__create_edge__()
    def __create_edge__(self):
        first=self.__node_input__("first")
        if first==None:
            return first
        second=self.__node_input__("second")
        if second==None:
            return second
        #print("Idhar")
        while True:
            try:
                #print("Here")
                length=int(input("Enter the Edge Length between "+str(first)+" and "+str(second)+" :"))
                break
            except:
                print("Wrong Type of Input.")
                continue
        self.__Edges__.add(first+second)
        self.__Edges__.add(second+first)
        self.__edge_length_value__[first+second]=length
        self.__edge_length_value__[second+first]=length
        self.__neighbours__[first].add(second)
        self.__neighbours__[second].add(first)
    def delete_vertex(self,data):
        return self.__delete_vertex__(data)
    def __delete_vertex__(self,data):
        if len(self.__vertex__)==0:
            print("The Graph is already Empty")
            return
        d=data.upper() if data.isalpha() else data
        if d not in self.__vertex__:
            print("No such vertex Present")
        #deleting from __vertex__
        self.__vertex__.discard(d)
        lst_to_remove=[]
        temporary=copy.deepcopy(self.__Edges__)
        #deleting from __Edges__ list
        for x in temporary:
            if d in x:
                lst_to_remove.append(x)
                self.__Edges__.discard(x)
        #deleting edge length of those deleted __Edges__
        for x in lst_to_remove:
            del self.__edge_length_value__[x]
        __neighbours___lst=list(self.__neighbours__[d])
        #deleting the __vertex__s neighbour list
        del self.__neighbours__[d]
        #deleting the __vertex__ from all the neighbour list
        for x in __neighbours___lst:
            #print(self.__neighbours__[x])
            self.__neighbours__[x].discard(d)
    def delete_edge(self):
        return self.__delete_edge__()
    def __delete_edge__(self):
        first=self.__node_input__("first")
        if first==None:
            return first
        second=self.__node_input__("second")
        if second==None:
            return second
        edge1=first+second
        edge2=second+first
        if edge1 not in self.__Edges__ and edge2 not in self.__Edges__:
            print("There is No Such Edge Present")
            return None
        self.__Edges__.discard(edge1)
        self.__Edges__.discard(edge2)
        del(self.__edge_length_value__[edge1])
        del(self.__edge_length_value__[edge2])
        self.__neighbours__[first].discard(second)
        self.__neighbours__[second].discard(first)
    @property
    def display(self):
        if len(self.__vertex__)==0:
            print("The Graph is empty")
            return None
        for x in self.__vertex__:
            print("The vertex is",x)
            print('Its neighbours and the edge_length with it is:-')
            #print(self.__neighbours__[x])
            if len(self.__neighbours__[x])==0:
                print("None")
                print()
                continue
            for y in self.__neighbours__[x]:
                print(y,"--->",self.__edge_length_value__[x+y])
            print()
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
    obj=Graph()
    def input_value(lst):
        chance=5
        while chance!=0:
            if chance!=1:
                time.sleep(3)
                os.system('cls')
                print(f'You have {chance} chances to select the operation')
            else:
                time.sleep(3)
                os.system('cls')
                print("You have last chance to select the operation")
            try:
                for x,y in enumerate(lst):
                    print(f"{x+1}.{y}")
                choice=int(input("Enter the operation to be performed:"))
                if choice in range(len(lst)+1):
                    return lst[choice-1]
                else:
                    print("Out of bounds")
                    chance-=1
            except:
                print("Wrong type of input,Try again")
                chance-=1
        print("You are Out of chances.")
        return None
    def input_data():
        chance=7
        while chance!=0:
            try:
                os.system('cls')
                data=input("Enter the data to be Entered:")
                return data
            except ValueError:
                print("Wrong type of input Try again.")
                time.sleep(2)
                chance-=1
                continue
        print("Limit exceeded!!!")
        time.sleep(5)
        return None
    def operation(choice,obj_):
        #print(choice)
        _object=ctypes.cast(id(obj_),ctypes.py_object).value
        function=eval("_object."+choice)
        #print(function)
        #print(function.__code__.co_argcount)
        if callable(function):
            #print("Yes")
            if function.__code__.co_argcount>1:
                value=input_data()
                if value==None:
                    print("Since No Proper Input received,operation terminated.")
                    return None
                value=str(value)
                return eval("function(value)")
            return eval("function()")
        return function
    lst_elements=[x for x in dir(obj) if not x.startswith("_")]
    execute=True
    while execute:
        result=input_value(lst_elements)
        if result!=None:
            operation(result,obj)
        execute=repeat_condition()
