# README

## Project Overview
This project is a simple Python script that demonstrates basic usage of dictionaries, loops, input validation, and formatted string output. The script collects user input, validates certain fields (such as cohort number), and displays the information both from a pre-defined profile and the user input.

### Features:
- **Profile Data:** A predefined dictionary called `profile` contains some initial user information such as name, cohort, track, and the organization behind it.
- **User Input:** The script takes input from the user for their name, cohort, and learning track.
- **Input Validation:** A `while` loop is used to ensure the cohort number is entered as an integer. If the user inputs anything other than a number, an error message prompts them to try again.
- **Formatted Output:** Both the predefined profile and user input are displayed using Python’s f-string for formatted text, which outputs the data neatly on separate lines.

## Files
There is only one file in this project:
- `script.py`: This is the main Python file containing all the code to run the project.

## Code Explanation
### Profile Display:
```python
profile = {
    'name': 'Isaac Menegbe',
    'cohort': '4',
    'track': 'Software Development ',
    'powered_by': 'PORA Academy'
}

for key, value in profile.items():
    print(f'{key}: {value}\n')
```
- A dictionary called `profile` is defined with key-value pairs that describe the user. The for loop is used to iterate over the dictionary and print each key-value pair on a new line.

### User Input:
```python
name = input("what is your fullname?" )

while True:
    try:
        cohort = int(input( "which cohort are you (enter a number) :"))
        break
    except ValueError:
        print("invalid input.  Please enter a number for this cohort")
```
- `name`: The script prompts the user to enter their full name.
- `cohort`: This asks the user to input their cohort number. A `try-except` block is used to catch invalid inputs (e.g., if the user inputs a string instead of a number). If the input is invalid, it will prompt the user to try again.

### Final Output:
```python
learning_track = input ("what is your learning track")

print(f'my name is {name}, \ni am in cohort {cohort} \nand my learning track is {learning_track}')
```
- After collecting the `learning_track`, the script uses formatted strings to print the collected information in a user-friendly format.

## How to Run
1. Install Python on your computer (version 3.x or above is recommended).
2. Copy the code into a Python file, such as `script.py`.
3. Open a terminal or command prompt and navigate to the folder containing `script.py`.
4. Run the script using the command:
   ```
   python script.py
   ```
5. Follow the prompts to input your full name, cohort number, and learning track.

## Requirements
- Python 3.x or above

## Sample Output:
```
name: Isaac Menegbe

cohort: 4

track: Software Development

powered_by: PORA Academy


what is your fullname? John Doe
which cohort are you (enter a number) :abcd
invalid input.  Please enter a number for this cohort
which cohort are you (enter a number) :5
what is your learning track? UI/UX
my name is John Doe,
i am in cohort 5
and my learning track is UI/UX
```￼Enter
