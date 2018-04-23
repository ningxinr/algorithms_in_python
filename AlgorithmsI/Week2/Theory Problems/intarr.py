import sys

class inv_cnt:
##    int_arr=[]
##    cnt=0
    def __init__(self,int_array=[],count=0):
        self.int_arr=int_array
        self.cnt=count
##        self.Left=int_array[:len(int_array)/2]
##        self.Right=int_array[len(int_array)/2:]

def MandC(Left,Right):
        i,j=0,0
        result=inv_cnt([],Left.cnt+Right.cnt)
        while i<len(Left.int_arr) and j<len(Right.int_arr):
            if Left.int_arr[i]<Right.int_arr[j]:
                result.int_arr.append(Left.int_arr[i])
                i+=1
            else:
                result.int_arr.append(Right.int_arr[j])
                result.cnt+=len(Left.int_arr)-i
                j+=1
        result.int_arr+=Left.int_arr[i:]
        result.int_arr+=Right.int_arr[j:]
##        result.Left=result.int_arr[:len(result.int_arr)/2]
##        result.Right=result.int_arr[len(result.int_arr)/2:]
        return result
        
def SandC(array):
    if len(array.int_arr)==1:
        array.cnt=0
        return array
    else:
        Left=inv_cnt(array.int_arr[:len(array.int_arr)/2],0)
        Right=inv_cnt(array.int_arr[len(array.int_arr)/2:],0)
        Left=SandC(Left)
        Right=SandC(Right)
        return MandC(Left,Right)

def main():
##    f_int=open('IntegerArray.txt','r')
    f_int=open('Integer10.txt','r')
    array=inv_cnt([],0)
    for line in f_int:
        array.int_arr.append(int(line))
    array=SandC(array)
    print array.int_arr
    print len(array.int_arr)
    print array.cnt
    print "Press any key to continue"
    raw_input()

   
    f_int.close()

main()
