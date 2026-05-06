#filter(function,sequence)

"""seq=[1,2,3,4,5,6,7,8,9,0]
even=lambda x: True if x%2 ==0 else False
filtered_output=filter(even,seq)
print(filtered_output)
print(f"even number in the above sequence are: {list(filtered_output)}")

"""
seq=[1,2,3,4,5,6,7,8]
mapped_output=map(lambda x: x**2,seq)
print(mapped_output)
print(f"map output: {list(mapped_output)}")

