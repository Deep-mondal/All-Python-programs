# compile string source to code  
code_str = 'x=5\ny=10\nprint("sum =",x+y)'  
code = compile(code_str, 'sum.py', 'exec')  
print(type(code))  
exec(code)  
exec(x)  