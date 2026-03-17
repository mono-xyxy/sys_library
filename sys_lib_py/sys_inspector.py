import sys

def main():
    print("DEBUG: Inside main()")
    print("Args:", sys.argv)

    print("Waiting for input...")
    user_input = sys.stdin.read()

    print("You entered:", user_input)
    print("Python version :",sys.version)

    print("Command-Line args: ",sys.argv)

    print("\n Module search paths: ")
    for p in sys.path[:3]:
        print(" ",p)

    print("\nEnter some text:")
    user_input = input()  

    sys.stdout.write("\nYou entered:\n" + user_input + "\n")

    if not user_input.strip():
        print("No input provided!", file=sys.stderr)
    
    size = sys.getsizeof(user_input)
    print(f"\nMemory size of input: {size} bytes")

    print("\nLoaded modules (first 5):")
    for name in list(sys.modules.keys())[:5]:
        print(" ",name)
    
    if len(sys.argv)>1 and sys.argv[1]=="exit":
        sys.exit("Exiting program via sys.exit()")

    if __name__ == "__main__":
        main()