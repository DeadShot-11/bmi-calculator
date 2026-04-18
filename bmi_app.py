import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0)
height_cm = st.number_input("Enter your height (cm)", min_value=1.0)

if st.button("Calculate BMI"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI is: {round(bmi, 2)}")

    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif bmi < 24.9:
        st.success("Category: Normal weight")
    elif bmi < 29.9:
        st.info("Category: Overweight")
    else:
        st.error("Category: Obese")