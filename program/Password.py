import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    """
    Generates a password with the specified length and character types.
    """
    # Define the character sets to use based on user input
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    lowercase_chars = string.ascii_lowercase if use_lowercase else ""
    number_chars = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special else ""

    # Combine the character sets into a single string
    all_chars = uppercase_chars + lowercase_chars + number_chars + special_chars

    # Generate a password by randomly selecting characters from the combined set
    password = "".join(random.choice(all_chars) for _ in range(length))

    return password


def user_choice():
    length = int(input("Enter password length: "))
    use_uppercase = input("Use uppercase letters? (y/n): ").lower() == "y"
    use_lowercase = input("Use lowercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Use numbers? (y/n): ").lower() == "y"
    use_special = input("Use special characters? (y/n): ").lower() == "y"
    password = generate_password(
        length, use_uppercase, use_lowercase, use_numbers, use_special
    )
    print("Your password is:", password)


def main():
    user_choice()


if __name__ == "__main__":
    main()