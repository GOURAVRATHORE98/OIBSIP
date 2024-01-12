def get_valid_input(prompt, input_type=float, min_value=None, max_value=None):
    while True:
        try:
            user_input = input_type(input(prompt))
            if (min_value is None or user_input >= min_value) and (max_value is None or user_input <= max_value):
                return user_input
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator!")
    
    weight = get_valid_input("Enter your weight in kilograms: ", min_value=1)
    height = get_valid_input("Enter your height in meters: ", min_value=0.5, max_value=3)

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")


if __name__ == "__main__":
    main()
