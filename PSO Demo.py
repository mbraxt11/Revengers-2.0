import pandas as pd

# Database
database = [
    {
        "material": "Brick",
        "price": 1.50,
        "maxload": 200,
        "quantity_available": 400,
        "vendor": "Vendor A",
    },
    {
        "material": "Brick",
        "price": 2.00,
        "maxload": 150,
        "quantity_available": 500,
        "vendor": "Vendor B",
    },
    # Algorithm generates more entries as needed.
]

def main():
    # Get user input
    material = input("Enter the material or part: ")
    quantity = int(input("Enter the quantity: "))
    load= int(input("Enter the max load of your project:"))

    # Filter database based on user input
    filtered_data = [
        entry for entry in database
        if entry["material"] == material and entry["quantity_available"] >= quantity and entry["maxload"]>=load
    ] 
    
    # Convert to DataFrame
    df = pd.DataFrame(filtered_data)

    # Calculate total cost
    df["total_cost"] = quantity * df["price"]

    # Scoring function
    def score(row):
        cost_weight = 0.5
        availability_weight = 0.5
        score = cost_weight * (1 / row["total_cost"]) + availability_weight * (row["quantity_available"] / quantity)
        return score

    # Calculate scores and sort by best fit
    df["score"] = df.apply(score, axis=1)
    df_sorted = df.sort_values(by="score", ascending=False)

    # Get the top 10 best fits
    top_10_fits = df_sorted.head(10)

    print("\nTop 10 Options:")
    print(top_10_fits)

if __name__ == "__main__":
    main()
