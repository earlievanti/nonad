visited = {(0, 0): True, (1, 2): True, (2, 3): True}

r, c = 1, 2
if (r, c) in visited:
    print(f"({r}, {c}) exists in visited")
else:
    print(f"({r}, {c}) does not exist in visited")

# Output: (1, 2) exists in visited

r, c = 3, 4
if (r, c) in visited:
    print(f"({r}, {c}) exists in visited")
else:
    print(f"({r}, {c}) does not exist in visited")

# Output: (3, 4) does not exist in visited
