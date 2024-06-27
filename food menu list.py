food_menu = {
    "Appetizers": {
        "Soup of the Day": 5.99,
        "Bruschetta": 7.99,
        "Wings": 9.99
    },
    "Entrees": {
        "Margherita Pizza": 12.99,
        "Spaghetti Bolognese": 14.99,
        "Grilled Salmon": 21.99
    },
    "Desserts": {
        "Tiramisu": 6.99,
        "Cheesecake": 7.99,
        "Gelato": 5.99
    }
}

for category, items in food_menu.items():
    print(f"{category.title()}:")
    for item, price in items.items():
        print(f"{item.title()}: ${price:.2f}")
    print()
