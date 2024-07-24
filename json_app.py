import json
import re

def find_unwanted_new_lines(data):
    errors = []
    pattern = re.compile(r'":\s*[\n\t]+')  # Matches : followed by unwanted new lines or tabs

    for match in pattern.finditer(data):
        start_index = match.start()
        line_number = data.count('\n', 0, start_index) + 1
        column_number = start_index - data.rfind('\n', 0, start_index)
        errors.append((line_number, column_number))

    return errors

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()

            # Check for unwanted new lines in the JSON values
            line_number_errors = find_unwanted_new_lines(data)
            if line_number_errors:
                error_messages = [f"line {line}, column {col}" for line, col in line_number_errors]
                raise ValueError(f"The JSON file contains unwanted new lines at: {', '.join(error_messages)}")

            # Attempt to load JSON data
            json_data = json.loads(data)
        return json_data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: The file {file_path} is not a valid JSON file. {str(e)}")
    except ValueError as ve:
        print(f"Error: {ve}")
    return None

def print_details(data):
    if data:
        name = data.get("name", "N/A")
        age = data.get("age", "N/A")
        city = data.get("city", "N/A")
        email = data.get("email", "N/A")
        skills = data.get("skills", [])

        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"City: {city}")
        print(f"Email: {email}")
        print(f"Skills: {', '.join(skills) if skills else 'N/A'}")

def main():
    file_path = 'input.json'
    json_data = read_json(file_path)
    print_details(json_data)

if __name__ == "__main__":
    main()
