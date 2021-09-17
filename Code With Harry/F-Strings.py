# F-String : Fast String

# 1.
s1 = "Nikhil"
s2 = "Deore"
x = "This is me, %s %s"%(s1, s2)
print(x)

# 2.
s3 = "Nikhil"
s4 = "Deore"
y = "This is me, {} {}"
z = y.format(s3, s4)
print(z)

# 3.
s3 = "Nikhil"
s4 = "Deore"
y = "This is me, {1} {0}"
z = y.format(s3, s4)
print(z)

# 4. F-String
i = f"This is me, {s1} {s2}"
print(i)