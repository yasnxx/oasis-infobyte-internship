import ipywidgets as widgets
from IPython.display import display, clear_output

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_weight_range(height):
    lower_limit = 18.5 * (height ** 2)
    upper_limit = 24.9 * (height ** 2)
    return lower_limit, upper_limit

def get_height_range(weight):
    lower_limit = (weight / 24.9) ** 0.5
    upper_limit = (weight / 18.5) ** 0.5
    return lower_limit, upper_limit

def calculate_button_clicked(b):
    clear_output(wait=True)
    
    try:
        weight = float(weight_input.value)
        height = float(height_input.value)

        if weight_unit_dropdown.value == "lbs":
            weight *= 0.453592
        if height_unit_dropdown.value == "feet":
            height *= 0.3048

        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)
        weight_range = get_weight_range(height)
        height_range = get_height_range(weight)

        display(widgets.HTML(f"<h3 style='color: blue;'>Your BMI: {bmi:.2f} ({bmi_category})</h3>"))
        display(widgets.HTML(f"<p>Suggested Weight Range: {weight_range[0]:.2f} - {weight_range[1]:.2f} kg</p>"))
        display(widgets.HTML(f"<p>Suggested Height Range: {height_range[0]:.2f} - {height_range[1]:.2f} meters</p>"))

    except ValueError:
        display(widgets.HTML("<p style='color: red;'>Please enter valid numeric values for weight and height.</p>"))

weight_input = widgets.FloatText(description="Weight:")
weight_unit_dropdown = widgets.Dropdown(options=["kgs", "lbs"], value="kgs", description="Unit:")
height_input = widgets.FloatText(description="Height:")
height_unit_dropdown = widgets.Dropdown(options=["meters", "feet"], value="meters", description="Unit:")

calculate_button = widgets.Button(description="Calculate BMI", button_style="success")
calculate_button.on_click(calculate_button_clicked)

display(widgets.HTML("<h2>BMI Calculator</h2>"))
display(weight_input, weight_unit_dropdown)
display(height_input, height_unit_dropdown)
display(calculate_button)
