guests = ["Alice", "Bob", "Charlie"]
print("Original guests:", guests)

# 1. Use .append() to add David to the end
guests.append("David")
print("After append:", guests)

# 2. Use .insert() to put 'Zoe' at the very front (Index 0)
guests.insert(0, "Zoe")
print("After insert at 0:", guests)  

# 3. Use .remove() to kick 'Bob' off the list
guests.remove("Bob")
print("After removing Bob:", guests)  
