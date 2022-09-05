import time
class Sorting_Algorithms(object):       
    def bubble_sort(self,elements=[]):
        t1=time.time()
        if elements==sorted(elements):
            print(time.time()-t1)
            return elements
        if len(elements)==0:
            print("Empty")
            return elements
        if len(elements)==1:
            return elements
        for x in range(len(elements)):
            for y in range(len(elements)-1):
                if elements[y]>elements[y+1]:
                    elements[y+1],elements[y]=elements[y],elements[y+1]
        print(time.time()-t1)
        return elements
    def merge_sort(self,elements=[]):
        t1=time.time()
        if len(elements)==0 or len(elements)==1:
            return elements
        if elements==sorted(elements):
            print(time.time()-t1)
            return elements
        result=self.__merge_sort__(elements)
        print(time.time()-t1)
        return result
    def __merge_sort__(self,elements=[]):
        #print(elements)
        if len(elements)==0 or len(elements)==1:
            return elements
        #print("\nLeft Subpart",elements[:len(elements)//2:])
        #print("Right Subpart",elements[len(elements)//2::])
        
        left_subpart=self.__merge_sort__(elements[:len(elements)//2:])
        right_subpart=self.__merge_sort__(elements[len(elements)//2::])
        
        final_=self.__merge_properly__(left_subpart,right_subpart)
        #print("Final Part",final_)
        return final_
    def __merge_properly__(self,a,b):
        #print("\na",a)
        #print("b",b)
        spare_list=[]
        i,j=0,0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                spare_list.append(a[i])
                i+=1
            else:
                spare_list.append(b[j])
                j+=1
        if i==len(a):
            spare_list.extend(b[j::])
        if j==len(b):
            spare_list.extend(a[i::])
        #print("spare",spare_list)
        return spare_list
    def insertion_sort(self,elements=[]):
        t1=time.time()
        if len(elements)==0:
            print("Empty")
            return
        if len(elements)==1:
#             print(time.time()-t1)
            return elements
        if elements==sorted(elements):
            print(time.time()-t1)
            return elements
        for i in range(1,len(elements)):
            while elements[i-1]>elements[i] and i>0:
                elements[i-1],elements[i]=elements[i],elements[i-1]
                i-=1
        print(time.time()-t1)
        return elements
    def shell_sort(self,elements=[]):
        t1=time.time()
        if len(elements)==0 or len(elements)==1:
            return elements
        if elements==sorted(elements):
            print(time.time()-t1)
            return elements
        gap=len(elements)//2
        #print(len(elements))
        while gap!=1:
            length=len(elements)-1
            while length-gap>=0:
                if elements[length]<elements[length-gap]:
                    elements[length],elements[length-gap]=elements[length-gap],elements[length]
                length-=1
            gap//=2
        for i in range(1,len(elements)):
            while elements[i-1]>elements[i] and i>0:
                elements[i-1],elements[i]=elements[i],elements[i-1]
                i-=1
        print(time.time()-t1)
        return elements
    def selection_sort(self,elements):
        t1=time.time()
        if len(elements)==0 or len(elements)==1:
            return elements
        if elements==sorted(elements):
            print(time.time()-t1)
            return elements 
        for outer in range(len(elements)-1):
            for inner in range(outer,len(elements)):
                if elements[outer]>elements[inner]:
                    elements[outer],elements[inner]=elements[inner],elements[outer]
        print(time.time()-t1)
        return elements
    def radix_sort(self,elements=[]):
        from copy import deepcopy
        t1=time.time()
        if len(elements)<=1:
            print(time.time()-t1)
            return elements
        big=max(elements)
        count=0
        while big!=0:
            big//=10
            count+=1
        counting=0
        while count!=0:
            spare_list=deepcopy(elements)
#             print("\nSpare",spare_list)
            if counting>0:
                temp=counting
#                 print(temp)
#                 print("Temp",temp)
                while temp!=0:
                    spare_list=[x//10 for x in spare_list]
#                     print("Spare wala",spare_list)
                    temp-=1
#             print("ELEMENTS",elements)
#             print("Spare",spare_list)
            dictionary={x:[] for x in range(10)}
            for i in range(len(spare_list)):
                index=spare_list[i]%10
#                 print(index)
                dictionary[index].append(elements[i])
            elements=[]
#             print(dictionary)
#             print()
            for keys in dictionary.keys():
                elements.extend(dictionary[keys])
            counting+=1
            count-=1
        print(time.time()-t1)
        return elements
    def bucket_sort(self,elements=[]):
        t1=time.time()
        if len(elements)<=1:
            print(time.time()-t1)
            return elements
        if elements==sorted(elements):
            print(time.time()-t1)
            return elements
        big=max(elements)
        round_=big%10
        big=big+(10-round_)
        buckets={(x,x+10):[] for x in range(0,big,10)}
        for element in elements:
            for lower,upper in buckets:
                if element>=lower and element<=upper:
                    buckets[(lower,upper)].append(element)
                    break
        final_list=[]
        for keys in buckets:
            if len(buckets[keys])>1:
#                 print(buckets[keys])
                for index in range(1,len(buckets[keys])):
                    while buckets[keys][index-1]>buckets[keys][index] and index>0:
                        buckets[keys][index-1],buckets[keys][index]=buckets[keys][index],buckets[keys][index-1]
                        index-=1
#                 print(buckets[keys],"\n")
            final_list.extend(buckets[keys])
#         print(buckets)
        print(time.time()-t1)
        return final_list
    def quick_sort(self,elements=[]):
        t1=time.time()
        result=self.__quick_sort__(elements)
        print(time.time()-t1)
        return result
    def __quick_sort__(self,elements):
#         print("\nElements initially",elements)
        if len(elements)<=1:
            return elements
        pivot=0
        left=1
        right=len(elements)-1
        while left<=right:
            while left<len(elements) and elements[left]<elements[pivot]:
                left+=1
            while right>pivot and elements[right]>elements[pivot]:
                right-=1
            if left<=right:
#                 print("Swapping",elements[left],elements[right])
                elements[left],elements[right]=elements[right],elements[left]
#                 print("Left",left)
#                 print("Right",right)
        elements[right],elements[pivot]=elements[pivot],elements[right]
        pivot=right
#         print('Elements After sort operations',elements)
#         if left<len(elements):
#             print("Left",left,elements[left])
#         else:
#             print("Left",left)
#         print("Right",right,elements[0])
#         print("Pivot",elements[pivot])
        left_subpart=self.__quick_sort__(elements[:pivot:])
#         print("Left Subpart",left_subpart)
        if pivot+1 in range(len(elements)):
            right_subpart=self.__quick_sort__(elements[pivot+1:])
        else:
            right_subpart=[]
        
#         print("Right_subpart",right_subpart)
        final_element=left_subpart+[elements[pivot]]+right_subpart
#         print("Returning",final_element)
        return final_element
    def quick_sort2(self,elements):
        t1=time.time()
        result=self.__quick_sort2__(elements)
        print(time.time()-t1)
        return result
    def __quick_sort2__(self,elements):
#         print("\nElements initially",elements)
        if len(elements)<=1:
            return elements
        pivot=len(elements)-1
#         print(pivot)
        left=0
        right=pivot-1
        while left<=right:
            while left<pivot and elements[left]<elements[pivot]:
                left+=1
            while right>-1 and elements[right]>elements[pivot]:
                right-=1
            if left<=right:
#                 print("Swapping",elements[left],elements[right])
                elements[left],elements[right]=elements[right],elements[left]
#                 print("Left",left)
#                 print("Right",right)
        elements[left],elements[pivot]=elements[pivot],elements[left]
        pivot=left
#         print('Elements After sort operations',elements)
#         if left<len(elements):
#             print("Left",left,elements[left])
#         else:
#             print("Left",left)
#         print("Right",right,elements[0])
#         print("Pivot",elements[pivot])
        left_subpart=self.__quick_sort2__(elements[:pivot:])
#         print("Left Subpart",left_subpart)
        if pivot+1 in range(len(elements)):
            right_subpart=self.__quick_sort2__(elements[pivot+1:])
        else:
            right_subpart=[]
        
#         print("Right_subpart",right_subpart)
        final_element=left_subpart+[elements[pivot]]+right_subpart
#         print("Returning",final_element)
        return final_element