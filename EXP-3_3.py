
# Program to check Injective, Surjective and Bijective Functions

# Input set of domain and codomain
A = set(map(int, input("Enter domain elements: ").split()))
B = set(map(int, input("Enter codomain elements: ").split()))

# Input function mapping
n = int(input("Enter number of mappings: "))
f = {}

print("Enter input-output pairs:")

for i in range(n):
    x, y = map(int, input().split())
    f[x] = y

# Check Injective (One-to-One)
injective = len(set(f.values())) == len(f)

# Check Surjective (Onto)
surjective = set(f.values()) == B

# Check Bijective
bijective = injective and surjective

# Display results
if injective:
    print("Function is Injective")
else:
    print("Function is not Injective")

if surjective:
    print("Function is Surjective")
else:
    print("Function is not Surjective")

if bijective:
    print("Function is Bijective")
else:
    print("Function is not Bijective")
