import random
from art import logo, vs
from game_data import data

def display_personality(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

def verify_answer(user_guess, a_count, b_count):
    if a_count == b_count:
        return False
    return (user_guess == 'a' and a_count > b_count) or (user_guess == 'b' and b_count > a_count)

def play_game():
    print(logo)
    score = 0
    account_b = random.choice(data)
    game_should_continue = True

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {display_personality(account_a)}")
        print(vs)
        print(f"Against B: {display_personality(account_b)}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while user_guess not in ['a', 'b']:
            user_guess = input("Invalid input. Type 'A' or 'B': ").lower()

        print("\n" * 15)
        print(logo)

        a_count = account_a["follower_count"]
        b_count = account_b["follower_count"]
        is_correct = verify_answer(user_guess, a_count, b_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Wrong. Final score: {score}")

if __name__ == "__main__":
    play_game()