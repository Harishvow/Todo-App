import functions
import time
num=time.strftime("%d %b %y %H:%M:%S")
print(num)
while True:
    user_action=input("enter add or show or see or edit or complete or exit:")
    user_action=user_action.strip()

    if user_action.startswith("add"):
     todo=user_action[4:] + "\n"

     todos= functions.gets_todos()

     todos.append(todo)
     functions.write_todos(todos)


    elif user_action.startswith("show"):
     todos= functions.gets_todos()

     for index,item in enumerate(todos):
        row=f"{index + 1}-{item.strip()}"
        print(row)
    elif user_action.startswith("see"):
     see_item=int(input("enter the number of todo to see:"))
     numbers=see_item-1
     show= functions.gets_todos()[numbers]
     print(show)
    elif user_action.startswith("edit"):
        try:
         number=int(user_action[4:])
         numbers=number-1
         todos = functions.gets_todos("todos.txt")
         new_todo=input("enter the new todo:")
         todos[numbers]= new_todo + "\n"
         write= functions.write_todos(todos)
        except ValueError:
            print("Your command is not vaild")
            continue
    elif user_action.startswith("complete"):
         number = int(user_action[9:])
         todos= functions.gets_todos("todos.txt")
         index=number-1
         removed_todo=todos[index].strip("\n")

         delete=todos.pop(index)
         write= functions.write_todos("todos.txt")
         msg=f"{removed_todo} this todo has been removed"
         print(msg)
    elif user_action.startswith("exit"):
     print("thank you")
     break




