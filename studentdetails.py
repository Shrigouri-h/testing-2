import sys
def sum(x, y):
    return x + y

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print("User provided two numbers:")
else:
    script_name = sys.argv[0]
    num1 = 10.0    
    print("No input given - using default values:")


result = num1 + num2

print("Script Name:", script_name)
print("Number 1:", num1)
print("Number 2:", num2)
print("Sum:", result)

  
