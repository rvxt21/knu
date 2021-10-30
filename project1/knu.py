##a,b,c=[int (d) for d in input().split()]
##if (a==b) and (b==c) and (a==c):
  ## print('1')
##elif (a!=b) and (b!=c) and (a!=c):
##    print('3')
##else:
##    print('2')

##x1,y1,x2,y2,a=[float (d) for d in input().split()]
##x=(x1+a*x2)/(1+a)
##y=(y1+a*y2)/(1+a)
##print("%.2f" % x,"%.2f" % y)

##n=int(input())
##i=0
##new_n=0
##last_digit=0
##while n>0:
     ##if n%2==0:
        ##last_digit=n%10+1
     ##else:
        ##last_digit=n%10-1
     ##new_n+=last_digit*10**i
     ##i+=1
     ##n//=10
##print(new_n)

##n=int(input())
##arr= []
##for a in input().split():
    ##arr.append(float(a) )
##min=arr[0]
##for i in range(n):
    ##if arr[i]<min:
        ##min=arr[i]
##min*=2
##print("%.2f" % min)

##n=int(input())
##list=[]
##for i in range(0,n):
    ##elem=int(input())
    ##list.append(elem)
##for i in range(0,n):
    ##if list[i]%2==0:
        ##print(list[i],"is even")
    ##else:
        ##print(list[i],"is odd")

##n=input()
##new=sorted(n)
##d=''.join(new)
##print(d)

##word=input()
##n=input()
##a=set(word)
##b=set(n)
##if b.issubset(a):
    ##print("Yes")
##else:
    ##print("No")

##def perevod(num, base):
    ##alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ##b = alphabet[num % base]
    ##while num >= base:
        ##num = num // base
        ##b += alphabet[num % base]
    ##return b[::-1]

##m,k=[int (d) for d in input().split()]
##n=input()
##res = int(n,m)
##res = perevod(res,k)
##print(res)

import collections
a=input()
b=input()
count=0
d_a=dict(collections.Counter(a))
d_b=dict(collections.Counter(b))
mn=set(b)
for key in d_b:
    if d_b.get(key)==d_a.get(key):
        count+=1
if count==len(mn):
    print("Ok")
else:
    print("No")


