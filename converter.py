import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔹 Select Conversion Type")
conversion_type = st.sidebar.radio("Choose an option:", 
                                   ["Length Converter", "Weight Converter", "Temperature Converter"])

st.sidebar.markdown("---")
st.sidebar.write("📜 **Conversion History**")
st.sidebar.write("Recent conversions will be displayed here.")

st.sidebar.markdown("---")
st.sidebar.markdown("👩‍💻 Made with ❤️ by **Sidra**")

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "grams": 1,
        "kilograms": 0.001,
        "milligrams": 1000,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        return value * 9/5 + 32 if to_unit == "fahrenheit" else value + 273.15
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32
    return value

# Unit Converter Function
def unit_converter(value, from_unit, to_unit):
    if from_unit in ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]:
        return length_converter(value, from_unit, to_unit)
    elif from_unit in ["grams", "kilograms", "milligrams", "pounds", "ounces"]:
        return weight_converter(value, from_unit, to_unit)
    elif from_unit in ["celsius", "fahrenheit", "kelvin"]:
        return temperature_converter(value, from_unit, to_unit)
    else:
        return "Invalid unit"

# Main Page Title
st.title("🔄 Unit Converter")

# Conversion Type Logic
if conversion_type == "Length Converter":
    st.subheader("📏 Length Converter")
    available_units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
elif conversion_type == "Weight Converter":
    st.subheader("⚖️ Weight Converter")
    available_units = ["grams", "kilograms", "milligrams", "pounds", "ounces"]
else:
    st.subheader("🌡️ Temperature Converter")
    available_units = ["celsius", "fahrenheit", "kelvin"]

# User Input
value = st.number_input("Enter Value:", min_value=0.0, step=0.1)
from_unit = st.selectbox("From Unit:", available_units)
to_unit = st.selectbox("To Unit:", available_units)

# Convert Button
if st.button("Convert"):
    result = unit_converter(value, from_unit, to_unit)
    st.success(f"✅ {value} {from_unit} is equal to {result} {to_unit}")
