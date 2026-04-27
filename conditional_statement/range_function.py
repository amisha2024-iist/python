#range()-built-in function
#it generate the sequence of integer in a given interval.
#range(start,stop,step) stop is not included
"""
for i in range(start,stop,step):
    statement"""
for i in range(0,50,5):
    print(i)

    #generate even number between (1 to 10) and 10 exclude.
for i in range(2,10,2):
    print(i)

#reverse => 20 to 10 (excluding 10)
for i in range(20,10,-1):
    print(i)

profits=[9,30,40,50]
for index in range(0,len(profits)):
    q=index+1
    print(f"profit for quarter {q} is {profits[index]} ")
