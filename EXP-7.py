
import sympy as sp

# Define variables
x, y, z = sp.symbols('x y z')

print("VECTOR CALCULUS OPERATIONS")
print("1. Gradient")
print("2. Divergence")
print("3. Curl")
print("4. Analyze Vector Field")

choice = int(input("Enter your choice: "))

if choice == 1:
    # Gradient of scalar field
    f = sp.sympify(input("Enter scalar function f(x,y,z): "))

    gradient = [
        sp.diff(f, x),
        sp.diff(f, y),
        sp.diff(f, z)
    ]

    print("Gradient =", gradient)

elif choice in [2, 3, 4]:
    # Input vector field components
    P = sp.sympify(input("Enter P (i component): "))
    Q = sp.sympify(input("Enter Q (j component): "))
    R = sp.sympify(input("Enter R (k component): "))

    F = sp.Matrix([P, Q, R])

    # Calculate divergence
    divergence = (
        sp.diff(P, x) +
        sp.diff(Q, y) +
        sp.diff(R, z)
    )

    # Calculate curl
    curl = sp.Matrix([
        sp.diff(R, y) - sp.diff(Q, z),
        sp.diff(P, z) - sp.diff(R, x),
        sp.diff(Q, x) - sp.diff(P, y)
    ])

    if choice == 2:
        print("Divergence =", divergence)

    elif choice == 3:
        print("Curl =", curl)

    elif choice == 4:
        print("\nVector Field Analysis")
        print("Vector Field =", F)
        print("Divergence =", divergence)
        print("Curl =", curl)

        if divergence == 0:
            print("Field is Solenoidal")
        else:
            print("Field is not Solenoidal")

        if curl == sp.zeros(3, 1):
            print("Field is Irrotational")
        else:
            print("Field is not Irrotational")

else:
    print("Invalid choice")
