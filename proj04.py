# Simple Key Logger (Educational)

filename = "keylog.txt"

print("=== Simple Key Logger ===")
print("Type 'exit' to stop.\n")

with open(filename, "a") as file:
    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            print("Logging stopped.")
            break

        file.write(text + "\n")

print("Keys saved in", filename)