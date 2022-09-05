# A little Bit updation of the Graph class
#IT IS AN UNDIRECTED GRAPH
import os
import ctypes
import time
from User_input_requirements import repeat_condition
from copy import deepcopy
#from itertools import permutations
class Graph1():
    def __init__(self):
        self.Vertices=set()
        self.edges=set()
        self.neighbour={}
        self.edge_length_value={}
    def insert_vertex(self,data=None):
        if data is None:
            while True:
                data=input("Enter the Node Name:")
                if data.isalnum():
                    if data.isalpha():
                        data=data.upper()
                else:
                    print("This is Not a proper type of input for a node")
                    continue
                break
        else:
            if data.isalnum():
                if data.isalpha():
                    data=data.upper()
            else:
                print("Can't Name a node using this name(Either use Alphabets or numbers or alphanums)")
                print("Node Not created")
                return None
        if data not in self.Vertices:
            self.Vertices.add(data)
            self.neighbour[data]=[]
        else:
            print("The Vertex is Already Present")            
    def __input_value__(self,tag,previous_vertex=None):
        chance=3
        while chance!=0:
            if chance!=1:
                print("There are",chance,"chance  left")
            else:
                print("You have last chance left")
            time.sleep(3)
            os.system('cls')
            data=input("Enter the "+tag+" name:")
            if data.isalnum():
                if data.isalpha():
                    data=data.upper()
                if data==previous_vertex:
                    print("Already Selected this Vertex,can't choose it again.")
                    chance-=1
                    continue
                if data not in self.Vertices:
                    print("The Vertex",data,"is not present in the Graph")
                    chance-=1
                    continue
                else:
                    return data
        print("Sorry Can't proceed to further step")
        return None
    def __authorization__(self,vertex1,previous_vertex=None):
        if vertex1.isalnum():
                if vertex1.isalpha():
                    vertex1=vertex1.upper()
                if vertex1 not in self.Vertices:
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
    def add_edges(self,vertex1=None,vertex2=None,edge_value=None):
        def edge_input():
            chance=5
            while chance!=0:
                try:
                    time.sleep(2)
                    os.system('cls')
                    value=int(input("Enter the Edge length:"))
                    return value
                except ValueError:
                    print("Wrong type of input,Try again")
                    chance-=1
            print("Sorry You are Out of chances\nCan't proceed further")
            return None
        if vertex1 is None and vertex2 is None:
            if len(self.Vertices)==0:
                print("The Graph is Empty")
                return None
            if len(self.Vertices)<2:
                print("Can't create an Edge as there are insufficient vertices")
                return None
            vertex1=self.__input_value__("First vertex")
            if vertex1 is None:
                return vertex1
            vertex2=self.__input_value__("Second vertex",vertex1)
            if vertex2 is None:
                return vertex2
            if vertex1+"--->"+vertex2 in self.edges and vertex2+"--->"+vertex1 in self.edges:
                print("Edge already Present.")
                return None
        
        else:
            if type(vertex1)!=str:
                vertex1,condition=self.__authorization__(str(vertex1))
            else:
                vertex1,condition=self.__authorization__(vertex1)
            
            if condition is None:
                return None
            if type(vertex2)!=str:
                vertex2,condition=self.__authorization__(str(vertex2),vertex1)
            
            else:
                vertex2,condition=self.__authorization__(vertex2,vertex1)
            if condition is None:
                return None
                
        if vertex1+"--->"+vertex2 in self.edges and vertex2+"--->"+vertex1 in self.edges:
            print("The Edge is already present")
            return
        if edge_value is None:
            edge_value=edge_input()
            if edge_value is None:
                return edge_value
        else:
            if type(edge_value)==bool:
                print("Wrong type of input,can't create an edge")
                return
            try:
                edge_value=int(edge_value)
            except:
                print("Wrong type of input,can't create an edge")
                return
        self.neighbour[vertex1].append(vertex2)
        self.neighbour[vertex2].append(vertex1)
        self.edges.add(vertex1+"--->"+vertex2)
        self.edges.add(vertex2+"--->"+vertex1)
        self.edge_length_value[vertex1+"--->"+vertex2]=edge_value
        self.edge_length_value[vertex2+"--->"+vertex1]=edge_value
        print("Successfully created the edge with edge length",edge_value)
    @property
    def delete_edge(self):
        if len(self.Vertices)==0:
            print("The Graph is Empty")
            return None
        vertex1=self.__input_value__("First vertex")
        if vertex1 is None:
            return vertex1
        vertex2=self.__input_value__("Second vertex",vertex1)
        if vertex2 is None:
            return vertex2
        if vertex1+"--->"+vertex2 not in self.edges or vertex2+"--->"+vertex1 not in self.edges:
            print("There is No Such Edge present")
            return None
        self.edges.discard(vertex1+"--->"+vertex2)
        self.edges.discard(vertex2+"--->"+vertex1)
        del(self.edge_length_value[vertex1+"--->"+vertex2])
        del(self.edge_length_value[vertex2+"--->"+vertex1])
        self.neighbour[vertex1].remove(vertex2)
        self.neighbour[vertex2].remove(vertex1)
        print("Successfully deleted the Edge")
    def delete_vertex(self):
        if len(self.Vertices) ==0:
            print("The Graph is Empty.")
            return None
        vertex=self.__input_value__("Vertex")
        self.Vertices.discard(vertex)
        if vertex is None:
            return None
        neighbours_list=self.neighbour[vertex]
        del(self.neighbour[vertex])
        for vertices in neighbours_list:
            self.neighbour[vertices].remove(vertex)
            self.edges.discard(vertices+"--->"+vertex)
            self.edges.discard(vertex+"--->"+vertices)
            del(self.edge_length_value[vertices+"--->"+vertex])
            del(self.edge_length_value[vertex+"--->"+vertices])
        print("Successfully deleted the Vertex")
    @property
    def display(self):
        if len(self.Vertices)==0:
            print("The Graph is Currently Empty")
            return None
        for vertex in self.neighbour:
            print("Vertex",vertex)
            if len(self.neighbour[vertex])==0:
                print("It has No neighbours\n")
                continue
            else:
                print("\nThe Neighbours are:")
                for x in self.neighbour[vertex]:
                    print(x,"with edge length->",self.edge_length_value[vertex+"--->"+x])
                print()
    @property
    def dfs_traversal(self):
        if len(self.Vertices)==0:
            print("The Graph is Empty")
            return None
        visited=set()
        if len(self.edges)==0:
            print("Can't print through dfs as there are No edges present")
        family_forest=[]
        for vertexes in self.neighbour:
            if vertexes not in visited:
                if len(self.neighbour[vertexes])==0:
                    fam=[vertexes]
                else:
                    temp=[]
                    fam=self.__dfs__(vertexes,visited,temp)
            if fam not in family_forest:
                family_forest.append(fam)
        if len(family_forest)==1:
            print(family_forest[0])
        else:
            for x,y in enumerate(family_forest):
                print(x+1,"--->",y)
            #print("\n\n")
            #print(family_forest)
    def __dfs__(self,node,visited,family=[]):
        family.append(node)
        visited.add(node)
        for vertices in self.neighbour[node]:
            if vertices not in visited:
                self.__dfs__(vertices,visited,family)
        return family
    @property
    def bfs(self):
        if len(self.Vertices)==0:
            print("The List is Empty.")
            return
        visited=set()
        final_list=[]
        for vertex in self.neighbour:
            if vertex not in visited:
                if len(self.neighbour[vertex])==0:
#                     print("Ther vertex",vertex)
                    result=[vertex]
                else:
                    temporary=[vertex]
                    order=[]
#                     print("Vertex passed",vertex)
                    result=self.__bfs__(vertex,visited,temporary,order)
                if result not in final_list:
                    final_list.append(result)
        if len(final_list)==1:
            print(final_list[0])
            return 
        for x,y in enumerate(final_list):
            print(x+1,"--->",y)
    def __bfs__(self,node,visited,family,visited_order):
#         print("Currently the node is:",node)
        if node not in visited_order:
            visited_order.append(node)
        visited.add(node)
        for vertex in self.neighbour[node]:
            if vertex not in visited:
                family.append(vertex)
        family.pop(0)
        if len(family)!=0:
            self.__bfs__(family[0],visited,family,visited_order)
        return visited_order
    @property
    def cyclic_or_acyclic(self):
        if len(self.Vertices)==0:
            print("The Graph is Empty")
            return None
        if len(self.Vertices)==1:
            print("Can't determine whether it is cyclic or acyclic with just one node")
            return None
        visited=set()
        final_tree=[]
        for vertexes in self.neighbour:
            if vertexes not in visited:
                if len(self.neighbour[vertexes])==0:
                    lst=[vertexes]
                    result=None
                else:
                    temporary=[]
                    backtracking=[]

                    result,lst=self.__cyclic_or_acyclic__(vertexes,visited,temporary,backtracking,None)
                if [lst,result] not in final_tree:
                    final_tree.append([lst,result])
        if len(final_tree)==1:
            print(final_tree[0][0])
            if final_tree[0][1] is True:
                print("The Tree is Cyclic")
            else:
                print("The Tree is Acyclic")
            return
        for x,y in final_tree:
            print(x)
            if y is True:
                print("The Above Tree is Cyclic\n")
            else:
                print("The Above Tree is Acyclic\n")
        return
    def __cyclic_or_acyclic__(self,node,visited,temporary,backtracking,previous_node):
        result=None
        #print("Previous Node is",previous_node)
        visited.add(node)
        if node not in temporary:
            temporary.append(node)
        for vertice in self.neighbour[node]:
            #print("For",vertice,"in",node)
            if vertice!=previous_node:
                if vertice not in backtracking:
                    if vertice in temporary and len(self.neighbour[vertice])>0:
                        return(True,temporary)
                    result,lst=self.__cyclic_or_acyclic__(vertice,visited,temporary,backtracking,node)
        backtracking.append(node)
        return (result,temporary)
    @property
    #This is basically graph colouring problem
    def check_bipartite(self):
        if len(self.Vertices)==0:
            print("The Graph is Empty")
            return
        if len(self.Vertices) is None:
            print("Can't determine whether it is Bipartite or not based on Single node")
            return True
        visited=set()
        final_graph=[]
        for vertex in self.neighbour:
#             print("Here")
            if vertex not in visited:
                if len(self.neighbour[vertex])==0:
                    result=None
                    lst=[vertex]
                else:
                    temporary=[]
                    colour={}
                    result,lst=self.__check_bipartite__(vertex,visited,temporary,colour,1,None)
                if [lst,result] not in final_graph:
                    final_graph.append([lst,result])
        if len(final_graph)==1:
            print(final_graph[0][0])
            if final_graph[0][1] is False:
                print("The Graph is not Bipartiate")
            else:
                print("The Graph is Bipartiate")
            return
        for x,y in final_graph:
            print(x)
            if y is False:
                print("The Graph is not Bipartiate\n")
            else:
                print("The Graph is Bipartiate\n")
    def __check_bipartite__(self,vertex,visited,family,colour_dict,colour,previous):
        result=None
#         print("Current Node",vertex)
#         print("Previous Node",previous)
        visited.add(vertex)
        if vertex not in family:
            family.append(vertex)
        colour_dict[vertex]=colour
        new=colour^0
        
#         print("Colour is",colour)
#         print("Colour dict here",colour_dict,"\n")
#         print("New_colour",new)
        for child in self.neighbour[vertex]:
#             print("Child node",child)
            if child not in visited:
#                 print("Not in Visited")
                result,lst=self.__check_bipartite__(child,visited,family,colour_dict,colour^1,vertex)
            else:
                if colour_dict[child]==colour_dict[vertex]:
#                     print("Else Mein")
                    return (False,family)
        return(result,family)
    def __generate_edges__(self,lst):
            edges_list=[]
            for x in lst:
                for y in self.neighbour[x]:
                    edges_list.append(x+"--->"+y)
            return edges_list
    def __first__(self,lst):
        chance=5
        while chance!=0:
            if chance==1:
                print("You have last chance left")
            else:
                print("You have",chance,"chances left")
            try:
                time.sleep(3)
                os.system('cls')
                for x,y in enumerate(lst):
                    print(x+1,"--->",y)
                choice=int(input("Enter the serial number of the node that you want to start from:"))
                if choice in range(1,len(lst)+1):
                    return lst[choice-1]
                print("Out of bounds")
                chance-=1
            except:
                print("Wrong type of Input Try again")
                chance-=1
        print("You are out of chance.")
        return None
    @property
    def dijkstras_algorithm(self):
        if len(self.Vertices)==0:
            print("The Graph is Empty")
            return None
        if len(self.Vertices)==1:
            print("Can't perform this operation with just one vertex")
            return
        for vertex in self.edge_length_value:
            if self.edge_length_value[vertex]<0:
                print("Can't perfrom Dijkstras or Bellman algorithm on undirected weighted graph as there is a negative edge present")
                return
        visited=set()
        final_list=[]
        for vertex in self.neighbour:
            if vertex not in visited:
                if len(self.neighbour[vertex])==0:
#                     print("Ther vertex",vertex)
                    result=[vertex]
                else:
                    temporary=[vertex]
                    order=[]
#                     print("Vertex passed",vertex)
                    result=self.__bfs__(vertex,visited,temporary,order)
                if result not in final_list:
                    final_list.append(result)
        for lst in final_list:
            edge_list=self.__generate_edges__(lst)
            if len(lst)==1:
                print(lst[0],"0")
                return
            number_of_repetitions=len(lst)-1
            distance={}
            start=self.__first__(lst)
            if start is None:
                return
            distance[start]=0
            for vertex in lst:
                if vertex!=start:
                    distance[vertex]=float("inf")
#             print(start)
#             print(distance)
            distance_dictionary=self.__dijkstras_algo__(number_of_repetitions,distance,edge_list)
            print("For Graph:",lst)
            print("Starting vertex is",start)
            for key,value in sorted(distance_dictionary.items(),key=lambda y:y[1]):
                print(key,"--->",value)
            print()
        return
    def __dijkstras_algo__(self,number_of_repetitions,distance,edge_list):
        from copy import deepcopy
        while number_of_repetitions!=0:
            temp_dict=deepcopy(distance)
#             print(distance)
            for edge in edge_list:
                vertex1,vertex2=edge.split("--->")
                if distance[vertex1]+self.edge_length_value[edge]<distance[vertex2]:
                    distance[vertex2]=distance[vertex1]+self.edge_length_value[edge]
            number_of_repetitions-=1
            if temp_dict.items()==distance.items():
                return distance
        return distance
    @property
    def bellman_ford(self):
        self.dijkstras_algorithm
    @property
    def prims_algorithm(self):
        if len(self.Vertices)==0:
            print("The Graph is Empty")
            return
        if len(self.Vertices)==1:
            print("Can't perform this opertaion with just one vertex in the Graph")
            return
        visited=set()
        final_list=[]
        for vertex in self.neighbour:
            if vertex not in visited:
                if len(self.neighbour[vertex])==0:
                    result=[vertex]
                else:
                    temporary=[vertex]
                    visited_order=[]
                    result=self.__bfs__(vertex,visited,temporary,visited_order)
                if result not in final_list:
                    final_list.append(result)
        for lst in final_list:
            minimum_spanning_edges=len(lst)-1
            first=self.__first__(lst)
            if first is None:
                return
            minimum_spanning_list=[first]
            spanning_edge_list=[]
            final_result=self.__prims_algorithm__(minimum_spanning_edges,minimum_spanning_list,spanning_edge_list)
            mst=0
            for edge,value in final_result:
                print(edge,"is the edge with value",value)
                mst+=value
            print("\nFinal MST is:",mst)
    def __prims_algorithm__(self,number_of_edges,spanning_list,final_edge_list):
        from copy import deepcopy
        while number_of_edges!=0:
            #print("\nIteration",number_of_edges)
            temp=[]
            for x in spanning_list:
                for vertex in self.neighbour[x]:
                    temp.append([x,vertex,x+"--->"+vertex,self.edge_length_value[x+"--->"+vertex]])
                    
            while True:
                #print("Temp List",temp)
                value=min(temp,key=lambda x:x[3])
                #print("Value Selected",value)
                if value[1] in spanning_list:
                    #print("Value is present")
                    temp.remove(value)
                elif value[2] in final_edge_list:
                    print("Dikkat")
                else:
                    break
            spanning_list.append(value[1])
            final_edge_list.append([value[2],value[3]])
            number_of_edges-=1
        return final_edge_list
    @property
    def kruskal_algorithm(self):
        if len(self.Vertices)==0:
            print("The Graph is Empty")
            return
        if len(self.Vertices)==1:
            print("Can't perform this opertaion with just one vertex in the Graph")
            return
        visited=set()
        final_list=[]
        for vertex in self.neighbour:
            if vertex not in visited:
                if len(self.neighbour[vertex])==0:
                    result=[vertex]
                else:
                    temporary=[vertex]
                    visited_order=[]
                    result=self.__bfs__(vertex,visited,temporary,visited_order)
                if result not in final_list:
                    final_list.append(result)
        
        for lst in final_list:
            edge_list=[]
            for vertex in lst:
                for v in self.neighbour[vertex]:
                    if v+"--->"+vertex not in edge_list and vertex+"--->"+v not in edge_list:
                        edge_list.append([vertex+"--->"+v,self.edge_length_value[vertex+"--->"+v]])
            MST=set()
            visited_order=[]
            number_of_reps=len(lst)-1
            result,discarded=self.__kruskal_algorithm__(lst,edge_list,MST,visited_order,number_of_reps)
            total=0
            for x in sorted(result,key=lambda x:x[1]):
                print(x,"with edge value",self.edge_length_value[x])
                total+=self.edge_length_value[x]
            print("MST Cost is",total)
            if len(discarded)>0:
                print("Discarded edges are:")
                for x in discarded:
                    print(x,"--->",self.edge_length_value[x])
    def __kruskal_algorithm__(self,element_list,edge_list,MST,visited_order,number_of_reps):
        from copy import deepcopy
        edges_discarded=set()
        edges_selected=[]
        while number_of_reps!=0:
            execute=True
            while execute:
#                 print("Here1")
                temp=set(deepcopy(visited_order))
                edge=min(edge_list,key=lambda x:x[1])
                vertex1,vertex2=edge[0].split("--->")
                if edge[0] in MST or vertex2+"--->"+vertex1 in MST:
                    edge_list.remove(edge)
                    continue
                edges_selected.append(edge[0])
                edges_selected.append(vertex2+"--->"+vertex1)
                temp.add(vertex1)
                temp.add(vertex2)
                spare={}
                for x in self.neighbour:
                    spare[x]=[y for y in self.neighbour[x] if y in temp and x+"--->"+y in edges_selected ]
                visited=set()
                tree=[]
                for vertexes in temp:
                    if vertexes not in visited:
                        if len(self.neighbour[vertexes])==0:
                            lst=[vertexes]
                            result=None
                        else:
                            temporary=[]
                            backtracking=[]
                            edges_only=[]
                            for x in edge_list:
                                result,lst=self.__check_the_cycle__(vertexes,visited,temporary,backtracking,None,spare)
                        if [lst,result] not in tree:
                            tree.append([lst,result])
                for x,y in tree:
                    if y is True:
#                         print("The Tree has become cyclic by inserting",edge)
                        if edge in edge_list:
                            edge_list.remove(edge)
                        spare[vertex1].remove(vertex2)
                        spare[vertex2].remove(vertex1)
                        if vertex1+"--->"+vertex2 in edges_selected:
                            edges_selected.remove(vertex1+"--->"+vertex2)
                            edges_selected.remove(vertex2+"--->"+vertex1)
                        edges_discarded.add(edge[0])
                        set_val=True
                        break
                    else:
                        visited_order.append(vertex1)
                        visited_order.append(vertex2)
                        if edge in edge_list:
                            edge_list.remove(edge)
                        MST.add(edge[0])
                        execute=False
                        set_val=None
                if set_val is True:
                    continue
            number_of_reps-=1
        return (MST,edges_discarded)
    def __check_the_cycle__(self,node,visited,temporary,backtracking,previous,spare_dict):
        
        result=None
        visited.add(node)
        if node not in temporary:
            temporary.append(node)
        for vertex in spare_dict[node]:
            if vertex!=previous:
                if vertex not in backtracking:
                    if vertex in temporary and len(spare_dict[vertex])>0:
                        return(True,temporary)
                    result,lst=self.__check_the_cycle__(vertex,visited,temporary,backtracking,node,spare_dict)
                    if result is True:
                        return(True,temporary)
        backtracking.append(node)
        return(result,temporary)
#     @property
#     def travelling_salesman(self):
#         from itertools import permutations
#         if len(self.Vertices)==0:
#             print("The Graph is Empty")
#             return None
#         if len(self.Vertices)==1:
#             print("Can't perform this opertaion with just one vertex in the Graph")
#             return
#         if len(self.edges)<len(self.edges)*(len(self.edges)-1):
#             print("Can't perform this operation on this Graph")
#             return
#         first=self.__first__(list(self.Vertices))
#         if first is None:
#             return
#         other_elements=[x for x in self.neighbour if x!=first]
#         element_list=[list(x) for x in list(permutations(other_elements))]
#         result=self.__travelling_salesman__(first,element_list)
#         answer=min(result,key=lambda x:x[1])
#         print()
#         print(answer)
#     def __travelling_salesman__(self,start,other_elements):
#         all_elements=[]
#         for lst in other_elements:
#             visited=[start]
#             total=0
#             for elements in lst:
#                 total+=self.edge_length_value(visited[-1]+"--->"+elements)
#                 visited.append(elements)
#             total+=self.edge_length_value(visited[-1]+"--->"+start)
#             visited.append(start)
#             all_elements.append([visited,total])
#         return all_elements
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
    _obj_=Graph1()
    log_variable.info("Executed")
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
        result=_obj_.__first__(operations)
        operation(operations,_obj_,result)
        execute=repeat_condition()
    print("Thank You for using this Code")
else:
    log_variable.info(f"This has been imported ")