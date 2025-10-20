items_list=["milk","chocolates","biscuit"]
def add_item(item):
   items_list.append(item)
   print("updated List:",items_list)

def remove_item(item):
  if item in items_list:
    items_list.remove(item)
    print("Updated List:", items_list)
  else:
     print(f"{item} item  not found in the list")
 

def view_list():
   print("current_list:",items_list)

task=input("Enter a task(add/view/remove):").lower()
if task=="add":
   items=input("Enter a item to add :").lower()
   add_item(items)
elif task=="remove":
    items=input("Enter a item to remove :").lower()
    remove_item(items)
elif task=="view":
   view_list()
else:
   print("please enter a valid task (add/remove/view)")
