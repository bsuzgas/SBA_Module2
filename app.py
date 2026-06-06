from flask import Flask, jsonify

app = Flask(__name__)

def calculate_total_cost(part_cost, labor_cost):
    """Calculates the total cost for car maintenance."""
    return part_cost + labor_cost

def calculate_brake_pad_cost(front_pads, rear_pads):
    """Calculates the cost of changing both front and rear brake pads."""
    return front_pads + rear_pads

# This section creates the web bridge to expose our API to the internet
@app.route('/')
def home():
    total = calculate_total_cost(1050, 700)
    brakes = calculate_brake_pad_cost(300, 250)
    
    return jsonify({
        "message": "Car Maintenance Cost API is Running!",
        "sample_total_cost_pln": total,
        "sample_brake_pad_cost_pln": brakes,
        "developer": "Lead Developer"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)