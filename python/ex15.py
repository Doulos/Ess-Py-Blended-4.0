import random
import re

# generate list of nsamples random integer in range 0..7 included
nsamples = 10
data = [random.randrange(0, 8) for i in range(nsamples)]
print("data = ", data)

# Create the string with the following pattern: ```n-…-n```
L = [f"{x}{x*'-'}{x}" for x in data]
print("list = ", L)

# Verify that each string in the list follows the pattern
for s in L:
    m = re.match(r"(\d)(-*)(\d)", s)
    n = int(m.group(1))
    assert len(m.group(2)) == n and int(m.group(3)) == n
print("strings in the list have the right pattern\n")

# convert to a multi-line string and replace all "00" by "*"
inputstr = "\n".join(L)
print(f"inputstr :\n{inputstr}")
str = re.sub(r"00", r"*", inputstr)
print(f"str :\n{str}")

# Verify that str has the correct pattern
"""
We check that a string is EITHER of the form (digit)(zero or more '-')(digit)
OR has exactly one `*`. As we have a multi-line string, we use of `^...$`
to delimit the start/end of the matching string.

Altough we have 4 groups per match, we get either:
* group(1)...group(3) when matching `n-..-n`, `group(4)` is empty
* group(4) when matching `*`, group(1)...group(3) are empty.

We expect to have exactly nsamples matches if the previous subsitution 
is correct.
"""
print("\nCheck substitution:")
m = re.findall(r"^(\d)(-*)(\d)$|^(\*{1})$", str, re.M)
print(m)
assert len(m) == nsamples
print("check passed :)")
