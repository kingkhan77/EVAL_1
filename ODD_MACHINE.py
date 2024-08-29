# print(sorted(("hello world".split(" ")),reverse=True))
import math,string

shopping_list = []

def add_item(new_item):
    shopping_list.append(new_item)
   
    
def remove_item(item):
    shopping_list.remove(item)
    print("After_removing-"+item+" :\n",shopping_list)
    

def search_item(item):
    if(item in shopping_list):
        return True
    else:
        return False
    
    

def binary_search(item):
    sorted(shopping_list)
    h = len(shopping_list)
    l = 0
    while(l<h):
        m = (l+h)/2
        m=int(m)
        if(shopping_list[m]==item):
            print("Item Found!! :  ", item[::-1])
            return
        elif(item > shopping_list[m]):
            l=m+1
        else:
            h=m-1
    print("NOT FOUND!!!")
    
          
    
def print_list():
    print(shopping_list)
    
nn=""
print("Enter no. of items")
n= input(nn)
n= int(n)
print(f"Enter {n} Items: ")
new_item=""
i=0
while(i<n):
    item = input(new_item)
    add_item(item)
    i=i+1


# if(search_item("bottle")==True):
#     print("Found")
# else:
#     print("Not Found")


print("Enter item to remove")
rmv =input()
remove_item(rmv)

print("Enter item to search: ")
search = input()
binary_search(search)

print_list()
 
