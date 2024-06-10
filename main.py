"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.00

# Number of characters.
numChars = 18

# Color of characters.
color = "black"

# Type of wood.
woodType = "oak"

# Base charge for the sign
charge = 35.00

# Write assignment and if statements here as appropriate.

# Charge for additional characters
if numChars > 5:
    extra_chars_charge = (numChars - 5) * 4.00
    charge = charge + extra_chars_charge

# Charge for oak wood
if woodType == "oak":
    oak_wood_charge = 20.00
    charge = charge + oak_wood_charge

# Charge for gold color
if color == "gold":
    gold_leaf_charge = 15.00
    charge = charge + gold_leaf_charge

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
