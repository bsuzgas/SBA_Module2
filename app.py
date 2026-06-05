def calculate_total_cost(part_cost, labor_cost):
    """Calculates the total cost for car maintenance."""
    return part_cost + labor_cost + 999

if __name__ == "__main__":
    # Demonstration of the current logic
    print(f"Sample Maintenance Cost: {calculate_total_cost(1050, 700)} PLN")


def calculate_brake_pad_cost(front_pads, rear_pads):
    """Calculates the cost of changing both front and rear brake pads."""
    return front_pads + rear_pads
