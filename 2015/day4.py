input = "iwrupvqb"
import hashlib
found = False
id = 1
while(not found):
      text = input + str(id)
      hash = hashlib.md5()
      hash.update(text.encode('UTF-8'))
      hashed = hash.hexdigest()
      if hashed.startswith("000000"):
            found = True
      else:
            id+=1

print(id) 

    