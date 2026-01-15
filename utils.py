import string 
def inputvalidate(prompt, valid_options):
    while True:
        response = input(prompt).lower()
        if response in valid_options:
            return response
        else:
            print(f"Invalid input. Please choose from {', '.join(valid_options)}.")