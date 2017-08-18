text = "all zip files are zipped"

# ENTER CODE BELOW HERE
po1 = text.find("zip")
po2 = text[po1 + 1:].find("zip")

print (text[po1 + 1:])
print (po1)
print (po2)
