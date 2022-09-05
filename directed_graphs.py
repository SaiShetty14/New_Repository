import os
import ctypes
import time
from User_input_requirements import repeat_condition
from copy import deepcopy
from itertools import permutations

class Directed_Graph():
    def __init__(self):
        self.__Vertices__=set()
        self.__edges__=set()
        self.__directed__={}
        self.__inward__={}
        self.__edge_value__={}
    def insert_vertex(self,data=None):
        if data is None:
            while True:
                data=input("Enter the Name Of the vertex:")
                if data.isalnum():
                    if data.isalpha():
                        data=data.upper()
                else:
                    print("This is not a proper node name type,please change it")
                    print("(Either use Alphabets or numbers or alphanums)")
                    continue
        else:
            if data.isalnum():
                if data.isalpha():
                    data=data.upper()
            else:
                print("Can't Name a node using this name(Either use Alphabets or numbers or alphanums)")
                print("Node Not created")
                return None
        if data not in self.__Vertices__:
            self.__Vertices__.add(data)
            self.__directed__[data]=[]
            self.__inward__[data]=[]
        else:
            print("The Vertex is already present")
            return None
    def __input_function__(self,tag,previous_vertex=None):
        chance=3
        while chance!=0:
            if chance!=1:
                print("You have",chance,"chances left")
            else:
                print("You have last chance left")
            time.sleep(3)
            os.system('cls')
            vertex=input("Enter the "+tag)
            if vertex.isalnum():
                if vertex.isalpha():
                    vertex=vertex.upper()
            if vertex==previous_vertex:
                print("This vertex was chosen as the directing vertex")
                print("Choose Some other vertex")
                chance-=1
                continue
            if vertex not in self.__Vertices__:
                print("The Vertex",vertex,"is not present")
                chance-=1
                continue
            else:
                return vertex
        print("Sorry You are out of chance,can't proceed further.")
        return None
    def __authorization__(self,vertex1,previous_vertex=None):
        if vertex1.isalnum():
                if vertex1.isalpha():
                    vertex1=vertex1.upper()
                if vertex1 not in self.__Vertices__:
                    print(vertex1,"is not present")
                    print("Can't continue further.")
                    return(vertex1,None)
                if vertex1==previous_vertex:
                    print("The Vertex already used.")
                    return(vertex1,None)
                else:
                    return(vertex1,True)
        else:
            print("The Vertex is not of an appropriate type for a node")
            print("Can't continue further.")
            return(vertex1,None)
    def create_directed_edge(self,directing_vertex=None,inward_vertex=None,value=None):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty")
            time.sleep(2)
            return None
        if len(self.__Vertices__)<2:
            print("Can't create an Edge as there are insufficient vertices")
            return None
        if directing_vertex is None or inward_vertex is None:
            if directing_vertex is None:
                directing_vertex=self.__input_function__("Directing Vertex:")
                if directing_vertex is None:
                    return directing_vertex
            if inward_vertex is None:
                inward_vertex=self.__input_function__("Inward Vertex:",directing_vertex)
                if inward_vertex is None:
                    return inward_vertex
        else:
            if type(directing_vertex)!=str:
                directing_vertex,condition=self.__authorization__(str(directing_vertex))
            else:
                directing_vertex,condition=self.__authorization__(directing_vertex)
            if condition is None:
                return condition
            if type(inward_vertex)!=str:
                inward_vertex,condition=self.__authorization__(str(inward_vertex),directing_vertex)
            else:
                inward_vertex,condition=self.__authorization__(inward_vertex,directing_vertex)
            if condition is None:
                return condition
 
        if directing_vertex+"--->"+inward_vertex in self.__edges__:
            print("The Edge is already present")
            return None
        if value is None:
            chance=5
            while chance!=0:
                if chance!=1:
                    print("You have",chance,"chances left to enter the edge value")
                else:
                    print("You have last chance  left to enter the edge value")
                try:
                    value=int(input("Enter the directed edge value:"))
                    break
                except ValueError:
                    print("Not a proper type of input")
                    chance-=1
                    continue
            if chance==0:
                print("No Proper value provided for the edge")
                print("Thus can't proceed further")
                return None
        else:
            if type(value)==bool:
                print("Wrong type of input,can't create an edge")
                return
            try:
                value=int(value)
            except:
                print("Wrong type of input,can't create an edge")
                return
        self.__directed__[directing_vertex].append(inward_vertex)
        self.__inward__[inward_vertex].append(directing_vertex)
        self.__edges__.add(directing_vertex+"--->"+inward_vertex)
        self.__edge_value__[directing_vertex+"--->"+inward_vertex]=value
    def delete_edge(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty.")
            return None
        if len(self.__Vertices__)<2:
            print("Can't create an Edge as there are insufficient vertices.")
            return None
        directing_vertex=self.__input_function__("Directing Vertex:")
        if directing_vertex is None:
            return directing_vertex
        inward_vertex=self.__input_function__("Inward Vertex:",directing_vertex)
        if inward_vertex is None:
            return inward_vertex
        if inward_vertex not in self.__directed__[directing_vertex]:
            print("No Such edge present.")
            return None
        
        self.__edges__.discard(directing_vertex+"--->"+inward_vertex)
        del(self.__edge_value__[directing_vertex+"--->"+inward_vertex])
        
        self.__directed__[directing_vertex].remove(inward_vertex)
        self.__inward__[inward_vertex].remove(directing_vertex)
        
    def delete_vertex(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty.")
            return None
        vertex=self.__input_function__("Vertex to Delete:")
        if vertex is None:
            return None
        all_edges=[]
        for edges in self.__edges__:
            for node in edges.split("--->"):
                if vertex==node:
                    all_edges.append(edges)
        for edge in all_edges:
            self.__edges__.discard(edge)
        directed_list=self.__directed__[vertex]
        inward_list=self.__inward__[vertex]
        for v in directed_list:
            self.__inward__[v].remove(vertex)
        for v in inward_list:
            self.__directed__[v].remove(vertex)
        del(self.__directed__[vertex])
        del(self.__inward__[vertex])
        if len(all_edges)!=0:
            for edge in all_edges:
                del(self.__edge_value__[edge])
        self.__Vertices__.discard(vertex)
        print("Shayad Sab Ho Gaya.")
    @property
    def display(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty")
            return None
        pointing_list=[]
        for vertex in self.__directed__:
            print("The Vertex is:",vertex)
            if len(self.__directed__[vertex])==0:
                print(vertex,"Doesn't point to any node.\n")
                continue
            for x,y in enumerate(self.__directed__[vertex]):
                print(x+1,".",y,self.__edge_value__[vertex+"--->"+y])
            print()
    def dfs(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty")
            return None
        visited=set()
        final_family=[]
        for vertices in self.__directed__:
            temp=[]
            if vertices not in visited:
                res=self.__dfs_traversal__(vertices,visited,temp)
            if res not in final_family:
                final_family.append(res)
        if len(final_family)==1:
            print(final_family[0])
            return
        #print(final_family)
        for index,lst in enumerate(final_family):
            print(index+1,".",lst)
    def __dfs_traversal__(self,node,visited,family=[]):
        family.append(node)
        visited.add(node)
        for vertex in self.__directed__[node]:
            if vertex not in visited:
                self.__dfs_traversal__(vertex,visited,family)
        return family
    @property
    def bfs(self):
        if len(self.__Vertices__)==0:
            print("The Tree is Empty")
        visited=set()
        final_list=[]
        for vertex in self.__directed__:
            if vertex not in visited:
                if len(self.__directed__[vertex])==0:
                    result=[vertex]
                else:
                    temporary=[vertex]
                    visited_order=[]
                    result=self.__bfs_traversal__(vertex,visited,visited_order,temporary)
                if result not in final_list:
                    final_list.append(result)
        if len(final_list)==1:
            print(final_list[0])
            return
        for x,y in enumerate(final_list):
            print(x+1,"--->",y)
        
    def __bfs_traversal__(self,node,visited_set,visited_list,family):
        if node not in visited_list:
            visited_list.append(node)
        visited_set.add(node)
        for vertices in self.__directed__[node]:
            if vertices not in visited_set:
                family.append(vertices)
        family.pop(0)
        if len(family)!=0:
            self.__bfs_traversal__(family[0],visited_set,visited_list,family)
        return visited_list
        
    @property
    def check_for_cyclic(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty.")
            return None
        if len(self.__Vertices__)==1:
            print("Can't determine whether its cyclic or not with just one node in the Graph")
            return
        visited=set()
        final_family=[]
        for vertex in self.__directed__:
            branching=[]
            backtracking=[]
            if vertex not in visited:
                #print("\nIdhar se nikla")
                result,family_list=self.__cyclic_or_acyclic__(vertex,visited,branching,backtracking)
            if [family_list,result] not in final_family:    
                final_family.append([family_list,result])       
#         if len(final_family)==1:
#             print(final_family[0][0])
#             if final_family[0][1]==True:
#                 #print("Here")
#                 print("The Graph is Cyclic.")
#             else:
#                 print("The Graph is Acyclic")
        
        for x,y in final_family:
            print(x)
            if y is True:
                print("The Graph is Cyclic\n")
            else:
                print("The Graph is Acyclic\n")
        return final_family
    def __cyclic_or_acyclic__(self,node,visited,sequence_list,backtracking):
        result=None
        #print("Current_Node",node)
        
        sequence_list.append(node)
        #print("Seq_list",sequence_list)
        
        visited.add(node)
        #print("VISITED LIST-",visited)
        
        for vertex in self.__directed__[node]:
            if vertex not in backtracking:
                if vertex in sequence_list and len(self.__directed__[vertex])>0:
                    #print("The vertex is",vertex)
                    #print("Sequence list is",sequence_list)
                    return (True,sequence_list)
                result,lst=self.__cyclic_or_acyclic__(vertex,visited,sequence_list,backtracking)
                #print("Result Currently",result)
#                 if result==True:
#                     return (result,sequence_list)
        #print("BackTRAcking with")
        backtracking.append(node)
        #print(backtracking,"\n")
        
        return (result,sequence_list)
    def generate_edges(self,lst):
            edges_list=[]
            for x in lst:
                for y in self.__directed__[x]:
                    edges_list.append(x+"--->"+y)
            return edges_list
    @property
    def bellman_ford_check(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty.")
            return None
        if len(self.__Vertices__)==1:
            print("Can't perform this operation as there is only one node/vertex in the Graph")
            return 
        visited=set()
        final_result=[]
        for vertex in self.__directed__:
            if vertex not in visited:
                if len(self.__directed__[vertex])==0:
                        result=[vertex]
                else:
                    temporary=[vertex]
                    visited_order=[]
                    result=self.__bfs_traversal__(vertex,visited,visited_order,temporary)
                if len(result)>0 and result not in final_result:
                    final_result.append(result)
        
               
#         if len(final_result)==1:
#             edge_list=self.generate_edges(final_result[0])
#             number_of_repetitions=len(final_result[0])-1
#             if len(final_result[0])==1:
#                 print(final_result[0][0],"0")
#                 return
#             print("We will start from",final_result[0][0])
#             distance={}
#             distance[final_result[0][0]]=0
#             for vertex in final_result[0][1::]:
#                 distance[vertex]=float("inf")
            
#             final_distance,negative_weight_cycle=self.__sssp_operation__(distance,number_of_repetitions,edge_list)
#             print("For the Graph--->",final_result[0])
#             print("The distances from",final_result[0][0],"is:")
#             for keys,values in sorted(distance.items()):
#                 print(keys,"--->",values)
#             print("Negative Weight Cycle",negative_weight_cycle)
#             return
        for elements in final_result:
            edge_list=self.generate_edges(elements)
            number_of_repetitions=len(elements)-1
            if len(elements)==1:
                print(elements[0],"0")
                return
            print("We Will Start From",elements[0])
            distance={}
            distance[elements[0]]=0
            for vertex in elements[1::]:
                distance[vertex]=float("inf")
            final_distance,negative_weight_cycle=self.__sssp_operation__(distance,number_of_repetitions,edge_list)
            print("For Graph--->",elements)
            print("The distances from",elements[0],"is:")
            for keys,values in sorted(distance.items()):
                print(keys,"--->",values)
            print("Negative Weight Cycle",negative_weight_cycle)
    
    def __sssp_operation__(self,distance_dictionary,number_of_reps,edges_list):
        import copy
        iteration=0
        while number_of_reps!=0:
            iteration+=1
            #print("Iteration",str(iteration),":")
            previous_round=copy.deepcopy(distance_dictionary)
            for edge in edges_list:
                #print("Edge-->",edge)
                vertex1,vertex2=edge.split("--->")
                #print(vertex1,vertex2)
                if distance_dictionary[vertex1]+self.__edge_value__[edge]<distance_dictionary[vertex2]:
                    #print("Yes")
                    #print(distance_dictionary[vertex2],">",distance_dictionary[vertex1],"+",self.__edge_value__[edge])
                    distance_dictionary[vertex2]=distance_dictionary[vertex1]+self.__edge_value__[edge]
            if previous_round.items()==distance_dictionary.items():
                #print("There is No Change in Value thus we stop.")
                return (distance_dictionary,"Absent")
            number_of_reps-=1
        d=copy.deepcopy(distance_dictionary)
        for edge in edges_list:
            vertex1,vertex2=edge.split("--->")
            if d[vertex1]+self.__edge_value__[edge]<d[vertex2]:
                d[vertex2]=d[vertex1]+self.__edge_value__[edge]
        if d.items()!=distance_dictionary.items():
            return(distance_dictionary,"Present")
        return (distance_dictionary,"Absent")
    @property
    def Topological_sort(self):
        result=self.check_for_cyclic
        for lst,res in result:
            if res is not True:
                if len(lst)>1:
                    new_list,inward_list=self.__topological__(lst)
                    if new_list!=None:
                        print("For",lst,"The topological order is:")
                        print(new_list)
                        print("\nInwards for",new_list[0],"is:\nNone\n")
                        for x in new_list[1::]:
                            print("Inwards for",x,"is:")
                            for inwards in inward_list[x]:
                                print(inwards)
                            print()
                    else:
                        pass
                else:
                    print("For",lst,"it will be",lst)
            else:
                print("Can't perform topological sort on",lst)
    def __topological__(self,element_list):
        from copy import deepcopy
        final_order=[]
        second_spare=deepcopy(self.__inward__)
        for x in second_spare:
            second_spare[x]=[x for x in self.__inward__[x] if x in element_list]
        #print(second_spare)
        spare_inward=deepcopy(second_spare)
        queue_list=sorted([[x,len(second_spare[x])] for x in element_list],key=lambda y:y[1])
        while len(queue_list)!=0:
            #print("Quelist is",queue_list)
            if queue_list[0][1]!=0:
                print(queue_list)
                print("Can't perform further operation on this")
                return (None,None)
            multiple_zeros=[[x[0],queue_list.index(x)] for x in queue_list if x[1]==0]
            if len(multiple_zeros)>1:
                #print(multiple_zeros)
                indexes=[x[1] for x in multiple_zeros]
                values=sorted(x[0] for x in multiple_zeros)
                new=list(zip(indexes,values))
                for x,y in new:
                    queue_list[x][0]=y
            final_order.append(queue_list[0][0])
            for vertex,lengths in queue_list:
                if queue_list[0][0] in spare_inward[vertex]:
                    spare_inward[vertex].remove(queue_list[0][0])
            queue_list.pop(0)
            if len(queue_list)!=0:
                queue_list=sorted([[x,len(spare_inward[x])] for x,y in queue_list],key=lambda y:y[1])
        return (final_order,second_spare)
    @property
    def dijkstras_algorithm(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty")
            return 
        if len(self.__Vertices__)==1:
            print("Can't perform this operation on Graph with just one vertex/node")
            return 
        for edge in self.__edge_value__:
            if self.__edge_value__[edge]<0:
                print("Can't perform Dijkstras algorithm on this Graph as it has a negative edge")
                return
        visited=set()
        final_list=[]
        for vertex in self.__directed__:
            if vertex not in visited:
                if len(self.__directed__[vertex])==0:
                    result=[vertex]
                else:
                    temporary=[vertex]
                    visited_order=[]
                    result=self.__bfs_traversal__(vertex,visited,visited_order,temporary)
                if result not in final_list:
                    final_list.append(result)
#         if len(final_list)==1:
#             edge_list=self.generate_edges(final_list[0])
#             if len(final_list[0])==1:
#                 print(final_list[0][0],"0")
#                 return
#             number_of_repetitions=len(final_list[0])-1
#             distance={}
#             distance[final_list[0][0]]=0
#             for vertex in final_list[0][1::]:
#                 distance[vertex]=float("inf")
#             distance_dict=self.__sssp_for_dijkstras__(number_of_repetitions,distance,edge_list)
#             print("For Graph",final_list[0])
#             for key,value in distance_dict.items():
#                 print(key,"--->",value)
#             return
        for lst in final_list:
            #print("Here")
            edge_list=self.generate_edges(lst)
            if len(lst)==1:
                print(lst[0],"0")
                return
            number_of_repetitions=len(lst)-1
            distance={}
            distance[lst[0]]=0
            for vertex in lst[1::]:
                distance[vertex]=float("inf")
            distance_dict=self.__sssp_for_dijkstras__(number_of_repetitions,distance,edge_list)
            print("For Graph",lst)
            for key,value in distance_dict.items():
                print(key,"--->",value)
            print()
    def __sssp_for_dijkstras__(self,number_of_reps,distance_dict,edge_list):
        from copy import deepcopy
        while number_of_reps!=0:
            temp_dict=deepcopy(distance_dict)
            for edge in edge_list:
                vertex1,vertex2=edge.split("--->")
                if distance_dict[vertex1]+self.__edge_value__[edge]<distance_dict[vertex2]:
                    distance_dict[vertex2]=distance_dict[vertex1]+self.__edge_value__[edge]
            number_of_reps-=1
            if temp_dict.items()==distance_dict.items():
                return distance_dict
        return distance_dict
    @property
    def Warshals_algorithm(self):
        if len(self.__Vertices__)==0:
            print("The Graph is Empty.")
            return
        if len(self.__Vertices__)==1:
            print("Can't perform this operation on Graph with just one vertex/node")
            return 
        dictionary={}
#         edges=[]
        for vertex in self.__directed__:
            for vertices in self.__directed__:
                if vertex==vertices:
                    default=0
                else:
                    default=float("inf")
                edge=vertex+"--->"+vertices
                edge_value=self.__edge_value__.get(edge,default)
                dictionary[vertex+"--->"+vertices]=edge_value
#                 edges.append([edge,edge_value])
#         print(dictionary)
        number_of_repetitions=(len(self.__Vertices__))
        final_result=self.__Warshall_algorithm__(dictionary,number_of_repetitions)
        val=[x for x in final_result.values()]
        final_list=[[] for x in range(len(self.__Vertices__))]
        count=0
        row_elements=len(final_result)/len(self.__Vertices__)
        for x in range(len(final_result)):
            if x==0:
                final_list[0].append(val[x])
            elif x%row_elements!=0:
                final_list[count].append(val[x])
            else:
                count+=1
                final_list[count].append(val[x])
        for x in final_list:
            print(x)
    def __Warshall_algorithm__(self,dictionary,number_of_reps):
#         while number_of_reps!=0:
        for x in self.__directed__:
#             print()
#             print(x,"is the mediator")   
            for edges in dictionary:
                
                vertex1,vertex2=edges.split("--->")
#                 print("\nEdge is:",edges,"\tvertex1 + x is:",vertex1+"--->"+x,"\t x + vertex2 is:",x+"--->"+vertex2)
#                 print(dictionary[edges],"\t"*3,dictionary[vertex1+"--->"+x],"\t"*3,dictionary[x+"--->"+vertex2])
                if dictionary[edges]>dictionary[vertex1+"--->"+x]+dictionary[x+"--->"+vertex2]:
                    dictionary[edges]=dictionary[vertex1+"--->"+x]+dictionary[x+"--->"+vertex2]
#             number_of_reps-=1
        return dictionary
    def __start__(self,list_):
        chance=5
        while chance!=0:
            if chance==1:
                print("You have last chance left.")
            else:
                print("You have",chance,"chances left.")
            try:
                time.sleep(3)
                os.system('cls')
                for x,y in enumerate(list_):
                    print(x+1,"--->",y)
                choice=int(input("Enter the Starting node based on the Serial No.:"))
                if choice in range(1,len(list_)+1):
                    return list_[choice-1]
                print("Out of Bounds")
                chance-=1
            except:
                print("Wrong type of Input,Try again.")
                chance-=1
        return None
    @property
    def travelling_salesman(self):
        from itertools import permutations
        
        if len(self.__Vertices__)==0:
            print("The Graph is Empty")
            return
        if len(self.__Vertices__)==1:
            print("Can't perform this operation on Graph with just one vertex/node")
            return 
        if len(self.__edges__)<(len(self.__Vertices__)-1)*len(self.__Vertices__):
            print("Can't perform this operarion")
            return 
        
        first=self.__start__(list(self.__Vertices__))
        if first is None:
            return first
        element_list=[x for x in self.__Vertices__ if x!=first]
        other_elements=[list(x) for x in list(permutations(element_list))]
        print("Start",first)
        print("Other elements are",element_list)
        print("Permutations",other_elements)
        result=self.__travelling_salesman__(first,other_elements)
        lst=min(result,key=lambda x:x[1])
        print(lst)
        return
    def __travelling_salesman__(self,start,element_list):
        final_result=[]
        for lst in element_list:
            total=0
            visited=[start]
            for element in lst:
                total+=self.__edge_value__[visited[-1]+"--->"+element]
                visited.append(element)
            total+=self.__edge_value__[visited[-1]+"--->"+start]
            lst.insert(0,start)
            lst.append(start)
            final_result.append([lst,total])
        return final_result
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
if __name__ == '__main__':
    
    log_variable.info("Executed")
    _obj_=Directed_Graph()
    operations=[x for x in dir(_obj_) if not x.startswith("__") and x not in ["Vertices","neighbour",'edge_length_value','edges']]

    def operation(operations,obj,action):
        if action is None:
            print("Can't perform the operation further.")
            return None
        import ctypes
        object_=ctypes.cast(id(obj),ctypes.py_object).value
        function=eval("object_."+action)
        try:
            if function.__code__.co_argcount>1 or callable(function):
                return eval('function()')
        except:
            return eval('function')
    execute=True
    while execute:
        result=_obj_.__start__(operations)
        operation(operations,_obj_,result)
        execute=repeat_condition()
    print("Thank you for using the code.")
else:
    log_variable.info(f"This is imported ")