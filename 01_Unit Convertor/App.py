import streamlit as st


st.title(" Unit Convertor") 

category = st.selectbox("Select category", ["distance","Temperature","Weight"])


# For Distance

def distance_convertor(From_unit,To_unit,value):
  unit = {
    "Meter" : 1,
    "Kilometer" : 1000,
    "feet" : 0.3048,
    "Mile" : 1609.34,
  }  
  result = value * unit[From_unit] / unit[To_unit]
  return result

if category == "distance":
  From_unit = st.selectbox ("From",["Meter","Kilometer","feet","Mile"])
  To_unit = st.selectbox ("To", ["Meter","Kilometer","feet","Mile"])
  value = st.number_input("Enter the value")
  if st.button("Convert"):
    result = distance_convertor(From_unit,To_unit,value)
    st.success(f"{value} {From_unit} = {result:2f} {To_unit}")


# For Temperature

# def Temperature_convertor(From_unit, To_unit, value):
#    if From_unit == "Celsius" and To_unit == "Fahrenhiet":
#         result = (value * 9/5) + 32
#    elif From_unit == "Fahrenhiet" and To_unit == "Celsius":
#         result = (value *9/5) + 32 

#    return value
  

# if category == "Temperature":
#     From_unit = st.selectbox ("From",["Celsius","Fahrenhiet"])
#     To_unit = st.selectbox ("To", ["Celsius","Fahrenhiet"])
#     value = st.number_input("Enter the value")
#     if st.button("Convert"): 
#         result = Temperature_convertor(From_unit ,To_unit, value)
#         st.success(f"{value} {From_unit} = {result:2f} {To_unit}")

def Temperature_convertor(From_unit, To_unit, value):
    if From_unit == "Celsius" and To_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif From_unit == "Fahrenheit" and To_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value  # When units are the same
    return result

category = "Temperature"  # Set this explicitly or let user select

if category == "Temperature":
    From_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    To_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter the value")
    if st.button("Convert"): 
        result = Temperature_convertor(From_unit, To_unit, value)
        st.success(f"{value} {From_unit} = {result:.2f} {To_unit}")




# For Weight


def Weight_convertor(From_unit,To_unit,value):
  unit = {
    "Grams" : 0.001,
    "Kilograms" :1 ,
    "Pounds" : 0.453592,
    "Ounces" : 0.02,
  }  
  result = value * unit[From_unit] / unit[To_unit]
  return result

if category == "Weight":
    From_unit = st.selectbox ("From",["Grams","Kilograms","Pounds","Ounces"])
    To_unit = st.selectbox ("To", ["Grams","Kilograms","Pounds","Ounces"])
    value = st.number_input("Enter the value")
    if st.button("Convert"): 
        result = Weight_convertor(From_unit ,To_unit, value)
        st.success(f"{value} {From_unit} = {result:2f} {To_unit}")


