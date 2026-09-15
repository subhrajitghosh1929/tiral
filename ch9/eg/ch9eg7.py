string='#'
pattern=""
for a in range(5):
    pattern+=string
    print(pattern)

print()
print('#2')
string='ABCDE'
pattern=""
for a in range(5):
    pattern+=string[a]+' '
    print(pattern)

print()
print('#3')
string='A B C D E'
pattern=""
for a in range(9):      # practice for output 
    print(string[:a])


print()
print('#3A')
for a in range(65,71):      # printing pattern using ASCII value
    pattern+=chr(a)+' '
    print(pattern)
    


print()
print('#3B')
string='A B C D E'
for a in range(0,9,2):      #  printing pattern using string
    for b in range(a):      #  printing pattern using nested loop
        print(string[b],end="")     # prints the character at the position b  
    print()


print()
print('#4')
string='ABCDE'
pattern=""
for a in range(5):
    pattern=(string[a]+' ')*(a+1)
    print(pattern)


print()
print('#5')
string='ABCDE'
pattern=""
for a in range(5):
    pattern=(string[a]*(a+1)+'#')
    print(pattern)


print()
print('#7')
word='amazing'
print('1:  '+word[0:7])
print('2:  '+word[0:3])
print('3:  '+word[2:5])
print('4:  '+word[-7:-3])
print('5:  '+word[-5:-1])
print('6:  '+word[:7])
print('7:  '+word[:5])
print('8:  '+word[3:])
print('9:  '+word[5:])
print('10:  '+word[3:],word[:3])
print('11:  '+word[3:]+word[:3])
print('12:  '+word[-7:],word[:-7])
print('13:  '+word[-7:]+word[:-7])
print('14:  '+word[1:6:2])      # word[] starting:ending+1:step(increament/decreament)
print('15:  '+word[-7:-3:3])      # word[] starting:ending+1:step(increament/decreament)
print('16:  '+word[::])     # by default starting value=0:ending value=len of string:step value=positive 1
print('17:  '+word[:])      # same as above(16)
print('18:  '+word[6])          # will print only the (6+1)th character

print()
print('#8')
print(ord('A'))    # ord('string(CHAR) value') gives the ASCII/unicode value of a string(SINGLR CHARACTER)
print(chr(65))      # chr(ASCII value)  gives the CHARACTER of the corrosponding ASCII/unicode value
