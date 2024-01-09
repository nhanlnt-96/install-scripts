import os
import json
import sys

# JSON file path
FILE_PATH = "./scripts.json"

scripts_json_file = open(FILE_PATH)
scrips_data = json.load(scripts_json_file)

# Create option_scripts variable
option_scripts = []

# Add scripts from JSON file to option_scripts
for script in scrips_data:
    option_object = {
        "name": script["name"],
        "script_string": script["script_string"]
    }
    option_scripts.append(option_object)

scripts_json_file.close()


def menu():
    print("--------------------\n")
    print("Run command script\n")

    for index, script_option in enumerate(option_scripts):
        print(f"[{index + 1}]. {script_option['name']}")

    print("[0]. Add new script")
    print("[A]. Run all scripts")
    print("[X]. Exit")
    print("--------------------")


def add_new_script():
    print("--------------------")
    print("Add new script")
    script_name = input("Enter script name: ")
    command_line = input("Enter command: ")
    option_scripts.append({
        "name": script_name,
        "script_string": command_line
    })

    with open(FILE_PATH, "w") as json_file:
        json.dump(option_scripts, json_file, indent=2)

    print("Add script success")
    print("--------------------")

    menu()


def main():
    # run menu for use select
    menu()

    input_option = input("Select one of the options: ")

    if input_option.lower() == "x":
        print("--------------------")
        print("See you later.")
        exit()

    if input_option.lower() == "a":
        print("--------------------")
        print("Running all of the scripts...")
        for script_item in option_scripts:
            print("--------------------\n")
            print(f"Running command line: {script_item['script_string']}")
            os.system(script_item["script_string"])

        os.execv(sys.executable, ['python3'] + sys.argv)

    if int(input_option) == 0:
        add_new_script()

    if len(option_scripts) and option_scripts[int(input_option) - 1]:
        print("--------------------\n")
        print(f"Running command line: {option_scripts[int(input_option) - 1]['script_string']}")
        os.system(option_scripts[int(input_option) - 1]["script_string"])
        os.execv(sys.executable, ['python3'] + sys.argv)


main()