"""
print diamond's upper part using variable field width, and * for padding
lower diamond's part is left as an exercise to the reader ;) 
"""
empty = ""
for i in range(9):
    print(f"{empty:^{9-i}}{empty:*^{2*i+1}}")

