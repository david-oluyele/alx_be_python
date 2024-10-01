def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1": 
            #Add an item to the list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list")
        elif choice == '2':
            #Remove an item from the list
            item = input("Enter the item to remove: ")
            if item in shopping_list: 
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} is not in the shopping list.")
        elif choice == '3':
            #Displays the Shopping List
            if shopping_list:
                print("Current Shopping List: ")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The Shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
