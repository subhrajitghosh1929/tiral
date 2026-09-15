print(len("hello"))
name="subhrajit"
print(len(name))
print('true'.capitalize())
print("abracadabra".count('ab'))        # counts no. of times ab is present in the string
print("abracadabra".count('ab',4,8))    # counts no. of times ab is present in the string within 4th to 8th character
print("abracadabra".count('ab',6))      # counts no. of times ab is present in the string from 6th character onwards
string='it gose as - ringa ringa'
sub='ringa'
print(string.find(sub))
print(string.find(sub,15,25))
print("abracadabra".index('ab')) 
print("abracadabra".index('ab',6))
#print("abracadabra".index('ab',4,8))       #as the sub string is not in the string hence error
string="abc123"
string2="hello"
string3="12345"
string4=" "
print(string.isalnum())
print(string2.isalnum())
print(string3.isalnum())
print(string4.isalnum())
print()
print(string.isalpha())
print(string2.isalpha())
print(string3.isalpha())
print(string4.isalpha())
print(string.isdigit())
print(string2.isdigit())
print(string3.isdigit())
print(string4.isdigit())
string="hello"
string2="THERE"
string3="GOLDY"
print(string.islower())
print(string2.islower())
print(string3.islower())
string="   "
string2=""
print(string.isspace())
print(string2.isspace())
string="HELLO"
string2="There"
string3="goldy"
string4="U123"
string5="123f"
print(string.isupper())
print(string2.isupper())
print(string3.isupper())
print(string4.isupper())
print(string5.isupper())
string="HELLO"
string2="There"
string3="goldy"
string4="U123"
string5="123f"
print(string.lower())
print(string2.lower())
print(string3.lower())
print(string4.lower())
print(string5.lower())
print(string.upper())
print(string2.upper())
print(string3.upper())
print(string4.upper())
print(string5.upper())
print(" Sipo ".lstrip())
print(" Sipo ".rstrip()+'#')
print(" Sipo ".strip()+'#')
print()
print("abcd".startswith("cd"))
print("abcd".startswith("ab"))
print("abcd".endswith("b"))
print("abcd".endswith("cd"))
print("the sipo app".title())
print("COMPUTER SCINCE".title())
print("COMPUTER SCINCE".istitle())
print("Computer Scince".istitle())
print("abracadabra".replace('ab','sp'))
print("i work for you".replace('you','u'))
print("i work for you".replace('work','care'))
print("*".join("hello"))
print("***".join("hello"))
print("$$".join(["trial","hello"]))
print("$$".join(("trial","hello","new")))
#print("$$".join((123,"hello","new")))      # all three items in the argument must be string
print("I Love python".split())
print("I Love python".split(" "))
print("I Love python".split("o"))       #the string is divided from positions containing "o"
txt="I enjoy working in Python"      #it return a tuple with 3 elements
x=txt.partition("working")      #the string working acts as a seperator    
print(x)            # 1st element before seperstor
                    # 2nd element seperstor
                    # 3rd element after seperstor


