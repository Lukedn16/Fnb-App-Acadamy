def main() :
    # Ask the user to enter their birth year
    birth_year = int(input("Enter your birth year: "))
    
    # Calculate the user's age
    current_year = 2024 
    age = current_year - birth_year
    
    # Check if the user is 18 or older
    if age >= 18:
        print("Congrats! You are old enough to enter the party.")
    else:
        print("Sorry, you are not old enough to enter the party.")

if __name__ == "__main__":
 main()   
