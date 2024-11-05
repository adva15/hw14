#2
#a
def my_avg(a:int,b:int) -> float:
   return (a+b)/2

avg1=my_avg(90,99)
print("the average is:",avg1)

#b
def my_headline(string:str) ->str :
    return string.upper()

head1=my_headline("python has concurred the word")
print(head1,"!")
print(head1,"!")

#c
def concat_list(list1:list[int],list2:list[int],list3:list[int])->list[int]:
    """Print the three functions together and their length together"""
    return list1+list2+list3

res_con=concat_list([1,2],[3,4 ,5 ,6],[7,8,9])
print(res_con,"Length-",len(res_con))
help(concat_list)

