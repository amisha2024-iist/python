n=1#global variable

def fn():
    n=8 #local variable
    print('in',n)
fn()

print('out',n)
#aleays local variable prefer first then the global variable.
