
# Program to Calculate Probability Using Sample Space

# Create a standard deck of 52 cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = [
    "A", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K"
]

# Generate sample space
deck = [(rank, suit) for suit in suits for rank in ranks]

# Total outcomes
total = len(deck)

print("Total cards in deck:", total)

print("\nSelect an event:")
print("1. Draw a Heart")
print("2. Draw an Ace")
print("3. Draw a King")
print("4. Draw a Face Card")
print("5. Draw a Red Card")
print("6. Draw a Spade")

choice = int(input("Enter your choice: "))

# Define favourable outcomes
if choice == 1:
    event = [card for card in deck if card[1] == "Hearts"]

elif choice == 2:
    event = [card for card in deck if card[0] == "A"]

elif choice == 3:
    event = [card for card in deck if card[0] == "K"]

elif choice == 4:
    event = [card for card in deck if card[0] in ["J", "Q", "K"]]

elif choice == 5:
    event = [card for card in deck if card[1] in ["Hearts", "Diamonds"]]

elif choice == 6:
    event = [card for card in deck if card[1] == "Spades"]

else:
    print("Invalid choice")
    exit()

# Calculate probability
favourable = len(event)

probability = favourable / total

print("\nTotal possible outcomes:", total)
print("Favourable outcomes:", favourable)
print("Probability:", probability)
print("Probability in percentage:", probability * 100, "%")
