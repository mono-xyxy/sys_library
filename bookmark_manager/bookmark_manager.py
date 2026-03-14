import json

FILE = "bookmarks.json"

# load bookmarks

def load_bookmarks():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

#save bookmarks
def save_bookmarks(bookmarks):
    with open(FILE,"w") as f:
        json.dumps(bookmarks,f,indent=4)

bookmarks = load_bookmarks()

while True:
    print("\nBookmark Manager")
    print("1. Add Bookmark")
    print("2. View Bookmarks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter bookmark name: ")
        url = input("Enter URL: ")

        bookmarks.append({"name": name, "url": url})
        save_bookmarks(bookmarks)

        print("Bookmark saved!")

    elif choice == "2":
        if not bookmarks:
            print("No bookmarks saved.")
        else:
            print("\nSaved Bookmarks:")
            for i, b in enumerate(bookmarks, 1):
                print(f"{i}. {b['name']} - {b['url']}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
