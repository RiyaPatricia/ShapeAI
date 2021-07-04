import hashlib
hash=input("Enter Input:")
last = hashlib.md5(hash.encode())
print("This is md5 Hash :",last.hexdigest())