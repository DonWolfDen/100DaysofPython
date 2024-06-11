class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class Category:

    def get_category(self, categories):
        print("--------Categories--------")
        n = 0
        for i in categories:
            n += 1
            print(f"{n}: {i}")
        print("--------------------------")
        cat_choice = int(input("\nEnter a number from the above list to select a category: "))
        cat = categories[cat_choice - 1]
        print(f"    You selected {cat}")
        return cat
