my_file = open('input.txt', 'w')
name=input("""In    the beginning  there  was    chaos.
Out of  the chaos  came order.
The universe  began to take shape.
Stars  formed  and galaxies were  born.
Life   emerged  in the  vast  expanse.""")
print("no. of bytes ",len(name))
my_file.close()

