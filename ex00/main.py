from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value


def main():
    model = LpProblem(name="drink-production", sense=LpMaximize)

    lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
    fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

    model += lemonade + fruit_juice, "Total_Products"

    model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
    model += 1 * lemonade <= 50, "Sugar"
    model += 1 * lemonade <= 30, "Lemon_Juice"
    model += 2 * fruit_juice <= 40, "Fruit_Puree"

    model.solve()

    print(f"Status: {LpStatus[model.status]}")
    print(f"  Lemon_Juice: {value(lemonade)} од.")
    print(f"  Fruit_Puree: {value(fruit_juice)} од.")
    print(f"  Total: {value(model.objective)} од.")

    print(f"\nUsage:")
    print(f"  Water: {2*value(lemonade) + value(fruit_juice)}/100 од.")
    print(f"  Sugar: {value(lemonade)}/50 од.")
    print(f"  Lemon_Juice: {value(lemonade)}/30 од.")
    print(f"  Fruit_Puree: {2*value(fruit_juice)}/40 од.")


if __name__ == "__main__":
    main()
