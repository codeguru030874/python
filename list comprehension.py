''''
odd_list=[]
for i in range(1,11):
    if(i%2==1):
        odd_list.append(i*i)
print(odd_list)'''
odd_square=[x**2 for x in range(10)if x%2==1]
print(odd_square)
