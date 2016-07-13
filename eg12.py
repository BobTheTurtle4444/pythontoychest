# 12.py - This program demonstrates sets.
items = {"arrow", "spear", "arrow", "arrow", "rock"}

# Print set.
print(items)
print(len(items))

# Use in-keyword.
if "rock" in items:
    print("Rock exists")

# Use not-in keywords.
if "clock" not in items:
    print("Cloak not found")
