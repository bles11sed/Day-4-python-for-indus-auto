def delchar(s,c):
    if len(c) != 1:
        return s
    else:
        return s.replace(c, "")
s = "Good evening"
c = "o"
print("String after the character is removed: ",delchar(s,c))

s = "Take care"
c = "e"
print("String after the character is removed: ", delchar(s,c))

s = "123456s"
c = "6"
print("String after the character is removed: ",delchar(s,c))

s = "Red rose"
c = "e"
print("String after the character is removed: ",delchar(s,c))

s = "Flower"
c = "w"
print("String after the character is removed: ",delchar(s,c))
