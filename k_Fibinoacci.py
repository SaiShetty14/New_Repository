import logging
import os
class KFibonacci:
    def __init__(self,k,initials):
        self.memo=dict(zip(range(k),initials))
        self.k=k
        print(self.memo)
    def __call__(self,n):
        if n not in self.memo:
            result=0
            for i in range(1,self.k+1):
                result+=self.__call__(n-i)[0]
            self.memo[n]=result
        return (self.memo[n],list(self.memo.values()))

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
filename=os.path.basename(__file__).split(".")[0]
Handler=logging.FileHandler(filename)
Formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
Handler.setFormatter(Formatter)
logger.addHandler(Handler)


if __name__ == '__main__':
    logger.info(f"{filename} Executed")
    def call(text):
        chance=5
        while chance!=0:
            try:
                os.system('cls')
                inp=int(input(f"{text}:"))
                return inp
            except:
                print("Wrong type")
                chance-=1
        return None
    res=call("Enter the Nacci series")
    if res is None:
        print("Sorry,try again")
    else:
        tup=tuple([0]*(res-1)+[1])
        obj=KFibonacci(res,tup)
        result=call("Enter the Number/Index")
        if result is None:
            print("Sorry,try again")
        else:
            print(obj(result))
else:
    logger.info(f"{__name__} Imported")