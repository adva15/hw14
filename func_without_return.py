#a
from audioop import avgpp
from msilib import make_id


def my_ascending(x:int=-12,y:int=7):
 if x<y:
  print(x,y)
 else:
  print(y,x)

my_ascending(-12,7)

#b
def my_details(string:str):
 if len(string):
  string1: str = string[0]
  string2: str = string[7]
  string3: str = string[-1]

my_details("AI is the best")

#c
def say_bool(say:bool):
 if say:
      print("yes")
 else:
     print("no")

say_bool(True)
say_bool(False)

#d
def print_zugi(list_zugi:list[int]):
 for list_zugi in list_zugi:
    if list_zugi % 2==0:
        print("even")
    else:
        print("odd")

print_zugi([5,3,2,10,15,14,14])


#e

def my_statistics(scores:list[int]):
 if scores:
    high= max(scores)
    low=  min(scores)
    amount= len(scores)
    avg= sum(scores) / amount
    print(f"The highest score:{high} the lowest score:{low} the number of scores are:{amount} the average score is:{avg}")


score=[]
while True:
    try:
        scories:int=int(input("whts is your score?"))
        if scories==-99:
            break
        if scories > 0 or scories > 100 :
         continue
        else:
         score.append(scories)
    except ValueError:
        print("give me number")

my_statistics(score)
my_statistics([98,99,100,89,95])
