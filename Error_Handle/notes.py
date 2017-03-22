try:
    f = open("simple.txt", 'r')
    f.write("Test write to simple text!")
    f.write("\n")
    f.write("Test write to simple text again!")

except IOError:
    print("Error could not find file or read data")
else:
    print("Success!")
    f.close()
finally:
    print("Always get to this line!")
