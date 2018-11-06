
''' to concatenate two numbers'''

print("Enter 'x' for exit.");
string1 = raw_input("Enter first string to concatenate: ");
if string1 == 'x':
    exit();
else:
    string2 = raw_input("Enter second string to concatenate: ");
    string3 = string1 + string2;
    print("\nString after concatenation =",string3);
    print("String 1 =",string1);
    print("String 2 =",string2);
    print("String 3 =",string3);

