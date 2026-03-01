def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")
    print("Your sandwich is ready!")

make_sandwich("ham", "cheese", "lettuce", "tomato")
make_sandwich("turkey", "bacon", "avocado")