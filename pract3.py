matrix = (
    (1, 2, 3),
    (4, 5, 6),  
    (7, 8, 9)
)

# Transpose the matrix
transposed_matrix = tuple(zip(*matrix))

# Find the greatest number in each row
greatest_numbers = [max(row) for row in matrix]

print("Transposed Matrix:")
print(*transposed_matrix, sep='\n')

print("\nGreatest number in each row:", greatest_numbers)
