num1=int(input('enter the number:'))
operator=(input('enter the operator: '+','-','/','*''))
num2=int( input('ENTER THE SECOND NUMBER:'))
# to simply calculate the numbers
if operator == "+":
    print("result:" , num1+num2)
if operator == "-":
    print("result:" , num1-num2)
if operator == "*":
    print("result:" , num1*num2)
if operator == "/":
    print("result:" , num1/num2)