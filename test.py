"""
Generated with ChatGPT
> Can you generate a Python code snippet to test some color styling ? Try to include as many different token types in a short code snippet.
"""
import colorama
from colorama import Back, Fore, Style

colorama.init()

def main():
    # Variables
    name = "Alice"
    age = int(30)

    # Conditional statement
    if age >= 18:
        print(f"{Fore.GREEN}Welcome, {name}! You are {age} years old.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Sorry, {name}. You are under 18.{Style.RESET_ALL}")

    # Function definition
    def greet():
        print(f"{Fore.BLUE}Hello, {name}!{Style.RESET_ALL}")

    greet()

    # Loop
    for i in range(3):
        print(f"{Fore.YELLOW}Iteration {i+1}{Style.RESET_ALL}")

    # Error handling
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"{Fore.MAGENTA}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
