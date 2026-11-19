from decision_tree import ANIMAL_TREE

def play_game():
    while True:
        print("\nThink of an animal.")
        guess = walk_tree(ANIMAL_TREE)
        right = input(f"Is it {guess}? (yes/no): ").strip().lower()
        if right in ("yes", "y"):
            print("I knew it!")
        else:
            print("Nice, you got me")

        again = input("Play again?").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing")
            break


def walk_tree(node):
    while "question" in node:
        answer = input(f"{node['question']} (yes/no): ".strip().lower())
        if answer in ("yes", "y"):
            node = node["yes"]
        elif answer in ("no", "n"):
            node = node["no"]
        else:
            print("Please type 'yes' or 'no'.")
    return node["guess"]

if __name__ == "__main__":
    print("Welcome to Jacob's 20 question v1")
    play_game()
