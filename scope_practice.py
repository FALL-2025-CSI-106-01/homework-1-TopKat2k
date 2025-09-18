for i in range(3,11):
    print(i)

print("\n")

#letters = ["a","b","d"]

def print_abcs():
    for number in range(2):
        print(number)

    for i in ["a","b","d"]:
        print(i)

print_abcs()


var1 = "hello"

def my_function(var1):
  var1 = 'goodbye'
  return var1

var1 = my_function(var1)
print(var1)
