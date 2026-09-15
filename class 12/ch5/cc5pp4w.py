
#ans
to_count = 0
the_count = 0
with open("Poem.txt", 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word.lower() == 'to':
                to_count += 1
            elif word.lower() == 'the':
                the_count += 1

print("count of 'to': ", to_count)
print("count of 'the': ", the_count)
