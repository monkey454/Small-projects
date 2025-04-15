"""
💡 Mini Projects 
🔸 1. Palindrome Checker App
Take input from user

Clean spaces and lowercase

Check if it’s a palindrome

🔸 2. Unique Words Counter
Input a sentence

Split into words

Use set() to count unique words

🔸 3. List Filter
Input a list of numbers

Create new list with even numbers using list comprehension

Sort and print

"""
text = "...🚀 Welcome to my Mini Project's Main Menu 🎯..."
print(text.center(51))
text = "This App can perform following actions: "
print(text.center(59))
text = "🧠 1. Palindrome Checker"
print(text.center(50))
text = "📊 2. Unique Words Counter"
print(text.center(51))
text = "🔢 3. List Filter"
print(text.center(41))
text = "❌ 4. Exit"
print(text.center(35))

def is_palindrome(text):
    cleaned =text.replace(" ","").lower()
    check = cleaned == cleaned[::-1]
    if check:
        print("✅ Entered sentence is Palindrome") 
    else:
        print("❌ Entered sentence is not Palindrome")
    
def is_unique(text):
    slipted_text = text.split()
    unique = set(slipted_text)
    count = len(unique)
    print(unique)
    print(f"📌 There are total {count} unique word int the sentence")
    
    
def list_filter(num):
    print(f"🧾 The entered list is:{num}")
    sorted_list = sorted(num)
    print(f"📈 The sorted list is {sorted_list}")

    even_list = [x for x in num if x%2 == 0]
    print(f"🔍 The list of even numbers are: {even_list}")

# main function
def main_function():
    while True:
        choice = input("\n➡️  Enter your choice: ")
        
        if choice == "1":
            while True:
    
                    user_input = input("✍️  Enter a sentence: ").strip()
                    if not user_input:
                        print("⚠️ Input cannot be empty. Try again.")
                    elif not any(char.isalpha() for char in user_input):
                        print("⚠️ Input must contain letters. Numbers-only input is not allowed.")
                    else:
                        is_palindrome(user_input)
                        break

        elif choice == "2":
            while True:
                user_input = input("✍️  Enter a sentence: ").strip()

                if not user_input:
                    print("⚠️ Input cannot be empty. Try again.")
                elif not any(char.isalpha() for char in user_input):
                    print("⚠️ Input must contain letters. Numbers-only input is not allowed.")
                else:
                    is_unique(user_input)
                    break

        elif choice == "3":
            limit = int(input("🔢 Enter the limit of the list: "))
            number = []
            for i in range(limit):
                elements = int(input("➕ Enter the elements in the list: "))
                number.append(elements)
            list_filter(number)

        elif choice == "4":
            print("👋 Exiting the program...")
            break
        else:
            print("⚠️  Enter a valid choice: ")

    print("✅ Thank you for using the Mini Project App. Goodbye! 🎉")

        
main_function()
