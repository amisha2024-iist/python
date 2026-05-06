def divide(num1,num2):
    """
    num1:A number to be divided(numerator)
    num2:A number to be divided(denominator)
    :return: float(if num2 is non-zero) or str(if num2 is zero)
    """
    if num2==0:
        return "can not divide as denominator 0!"
    else:

        result=num1/num2
        return result
print((divide(90,0)))
help(len)
