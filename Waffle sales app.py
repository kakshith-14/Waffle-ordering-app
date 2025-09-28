import time
import random

waffles = {
    1: {"name": "Classic Butter Waffle", "price": 120, "flavor": "Golden crisp with creamy butter"},
    2: {"name": "Chocolate Chip Waffle", "price": 150, "flavor": "Melty chips in every bite"},
    3: {"name": "Strawberry Delight", "price": 180, "flavor": "Fresh berries and whipped cream"},
    4: {"name": "Nutella Banana Waffle", "price": 200, "flavor": "Rich Nutella with banana slices"}
}

cart = []

def intro():
    print("🎉 Welcome to Waffle World 🎉")
    print("Where waffles aren't just food—they're a vibe.\n")
    time.sleep(1)

def show_menu():
    print("📜 Today's Waffle Specials 📜")
    for id, item in waffles.items():
        print(f"{id}. {item['name']} - ₹{item['price']}")
        print(f"   🍴 Flavor: {item['flavor']}")
        print("   🔥 Sizzling hot and ready to serve!\n")
        time.sleep(0.5)
    print("0. Checkout")

def add_to_cart(choice):
    if choice in waffles:
        selected = waffles[choice]
        cart.append(selected)
        print(f"\n✅ Added {selected['name']} to your cart.")
        print("✨ Flavor burst: " + selected['flavor'])
        print("🎵 *sizzle sizzle crunch* 🎵\n")
        time.sleep(1)
    else:
        print("❌ That waffle isn't on the menu.\n")

def checkout():
    print("\n🛍️ Finalizing your order...")
    time.sleep(1)
    print("🧾 Your Waffle Receipt 🧾")
    total = 0
    for item in cart:
        print(f"- {item['name']} ₹{item['price']}")
        total += item['price']
    print(f"\n💸 Total Bill: ₹{total}")
    print("🎁 Bonus: You earned a free topping next time!")
    print("🙏 Thanks for vibing with Waffle World!")

def run_app():
    intro()
    while True:
        show_menu()
        try:
            choice = int(input("👉 Choose your waffle (0 to checkout): "))
            if choice == 0:
                checkout()
                break
            add_to_cart(choice)
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

run_app()