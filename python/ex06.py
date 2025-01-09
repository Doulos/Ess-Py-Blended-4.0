try:
    for l in open(__file__):
        print(f"{l}", end="")  # try removing end=''
except:
    print("Something went wrong...")
    raise  # do not continue (by re-raising the exception)

# Copy the contents of a file to another file,
# reversing the order of the characters in each line
try:
    output = open("reversed.txt", "w")
    for line in open(__file__):
        output.write(line[-2::-1] + "\n")
    output.close()
except:
    print("Error opening file")
