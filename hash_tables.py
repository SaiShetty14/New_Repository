'''This is a module that provide us with the concept of hash tables'''
class HashTables():
    '''This is the Hash Table Class'''
    def __init__(self):
        while True:
            try:
                choice=int(input("Enter the Number of hashes you want us to create:"))
                break
            except ValueError:
                print("Wrong Type of input,Try again.")
                continue
        self.__hash_value__=choice
        #print(self.__hash_value__)
        self.__hash_list__=[[] for x in range(choice)]
    def __gethash__(self,keys):
        index=0
        for x in keys:
            value=ord(x)
            index+=value
            #print(index%self.__hash_value__)
            return index%self.__hash_value__
    def __getitem__(self,keys):
        index=self.__gethash__(keys)
        for x,y in self.__hash_list__[index]:
            if x==keys:
                return y
        print("No Such Key Present")
    def __setitem__(self,keys,value):
        index=self.__gethash__(keys)
        for x in self.__hash_list__[index]:
            if x[0]==keys:
                x[1]=value
                return None
        self.__hash_list__[index].append([keys,value])
        return None
    def __delitem__(self,keys):
        index=self.__gethash__(keys)
        for x in self.__hash_list__[index]:
            if x[0]==keys:
                self.__hash_list__[index].remove(x)
                return None
        print("No Such Key Found.")
