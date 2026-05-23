"""fh=open("file4.txt","rt") #rt=rad text
contents=fh.read()
fh.close()
print(contents)"""
"""with open("practice_1.txt","rt") as fh:
    contents=fh.read()
print(contents)"""
with open("practice_2.txt","xt") as fh:
    fh.write("new file creation\n")
    fh.write("bye")
