
# Program to implement Set Operations without map()

# Input Set A
A = set()
n = int(input("Enter number of elements in Set A: "))

for i in range(n):
    x = int(input("Enter element: "))
    A.add(x)

# Input Set B
B = set()
n = int(input("Enter number of elements in Set B: "))

for i in range(n):
    x = int(input("Enter element: "))
    B.add(x)
 
print("\nSet A:", A)
print("Set B:", B)

# 1. Union
print("\nUnion (A U B):", A | B)

# 2. Intersection
print("Intersection (A ∩ B):", A & B)

# 3. Difference
print("Difference (A - B):", A - B)

# 4. Cartesian Product
print("Cartesian Product (A x B):")

for x in A:
    for y in B:
        print("(", x, ",", y, ")")
