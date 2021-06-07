def problem1():
  filename = "inputs/Prob01.in.txt"
  with open(filename) as f:
    for line in f:
      print(line.rstrip("\n"))
      number = int(line.rstrip("\n"))
      #what to do with each number
      if number >= 70:
        print ("PASS")
      elif number < 70:
        print ("FAIL")

problem1()

def problem7():
  filename = "inputs/Prob07.in.txt"
  with open(filename) as f:
    for line in f:
      print(line.rstrip("\n") + " is a palindrome?") 
      s = str(line.rstrip("\n"))
      stringlength = len(s) 
      reversedString = s[stringlength::-1] 
      if s == reversedString:
        print ("True")
      elif s != reversedString: 
        print ("False")
        
problem7()
