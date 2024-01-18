import matplotlib.pyplot as plt
from pandas.plotting import table

def main():
    # Define the initial asset holdings
    assets = {
        "AAPL": 15,
        "NVDA": 50,
        "VTI": 20,
        "VOO": 10,
        "AMZN": 10,
        "AMD": 20,
        "VUG": 20,
        "MU": 15,
    }

    # Calculate the total invested amount
    total_invested = sum(assets.values())

    # Get user input for the target invested amount
    target_investment = float(input(f"Current amount invested: ${total_invested}\nEnter how much money you want to have invested: "))

    # Calculate the initial ratios of assets
    assets_ratios = {key: value / total_invested for key, value in assets.items()}

    # Initialize an empty dictionary to store user-provided weights
    user_weights = {}

    # Get user input for weights, ensuring they are between 0.5 and 1.5
    for key in assets:
        while True:
            try:
                user_input = float(input(f"Choose a weight for {key} between 0.5 and 1.5: "))
                if 0.5 <= user_input <= 1.5:
                    user_weights[key] = user_input
                    break
                else:
                    print("Choose a number between 0.5 and 1.5")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Calculate new ratios based on user-provided weights
    new_ratios = {key: assets_ratios[key] * user_weights[key] for key in assets}

    # Calculate the sum of new ratios
    ratios_sum = sum(new_ratios.values())

    # Normalize new ratios to ensure they sum up to 1
    new_ratios = {key: value / ratios_sum for key, value in new_ratios.items()}

    # Calculate new investments based on target investment and normalized ratios
    new_investments = {key: round((target_investment - total_invested) * value, 2) for key, value in new_ratios.items()}
    
    # Create a table with adjusted cell height
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")

     # Set the title for the table
    ax.set_title(f"Recommended New Investments with Target: ${target_investment:.2f}", fontsize=16)

    # Define the table data with formatted values
    table_data = [
        (key, f"{assets_ratios[key] * 100:.2f}%", f"{new_ratios[key] * 100:.2f}%", f"${new_investments[key]}") 
        for key in assets
    ]

    # Insert column headers at the beginning of the table data
    table_data.insert(0, ("Assets", "Old Ratios(%)", "New Ratios(%)", "New Investments($)"))

    # Create the table
    table = ax.table(
        cellText=table_data, 
        colLabels=None, 
        cellLoc="center", 
        loc="center", 
        cellColours=[["#f0f0f0", "#f0f0f0", "#f0f0f0", "#f0f0f0"]] * (len(assets) + 1), 
        bbox=[0, 0, 1, 1]
    )

    # Display the table
    plt.show()

if __name__ == "__main__":
    main()