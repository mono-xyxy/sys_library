import json

print("Json formatter")

file_name = input("Enter JSON file name: ")

try:
    with open(file_name, "r",encoding="utf-8") as f:
        data = json.load(f)
    
    formatted = json.dumps(data,indent=4)
    output_file = "formatted.json"

    with open(output_file,"w", encoding="utf-8") as f:
        f.write(formatted)

    print(f"\nFormatted JSON saved to {output_file}")

except Exception as e:
    print("Error:", e)