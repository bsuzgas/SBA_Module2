def calculate_total_cost(part_cost, labor_cost):
    """Calculates the total cost for car maintenance."""
    return part_cost + labor_cost

if __name__ == "__main__":
    # Demonstration of the current logic
    print(f"Sample Maintenance Cost: {calculate_total_cost(1050, 700)} PLN")