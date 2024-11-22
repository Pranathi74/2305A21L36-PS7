import streamlit as st
import math

def Tran_OC(V0, I0, W0):
    """
    Calculate the resistance (R0) and reactance (X0) of a transformer based on open circuit test measurements.

    Parameters:
        V0 (float): Open circuit voltage (Volts)
        I0 (float): Open circuit current (Amperes)
        W0 (float): Open circuit power (Watts)

    Returns:
        tuple: R0 (ohms), X0 (ohms)
    """
    # Calculate power factor
    NP_F = W0 / (V0 * I0)

    # Calculate magnetizing and core loss components of the current
    Iw = I0 * NP_F
    Im = I0 * math.sqrt(1 - NP_F**2)

    # Calculate resistance (R0) and reactance (X0)
    R0 = V0 / Iw
    X0 = V0 / Im

    return R0, X0

# Streamlit application
def main():
    st.title("Transformer Open Circuit Test Calculator")

    st.write("This application calculates the resistance (R0) and reactance (X0) of a transformer based on open circuit test measurements.")

    # Input fields
    V0 = st.number_input("Enter Open Circuit Voltage (V0) [Volts]", min_value=0.0, value=230.0, step=1.0)
    I0 = st.number_input("Enter Open Circuit Current (I0) [Amperes]", min_value=0.0, value=1.0, step=0.01)
    W0 = st.number_input("Enter Open Circuit Power (W0) [Watts]", min_value=0.0, value=100.0, step=1.0)

    if st.button("Calculate R0 and X0"):
        if I0 == 0:
            st.error("Open Circuit Current (I0) must be greater than zero.")
        else:
            R0, X0 = Tran_OC(V0, I0, W0)
            st.success(f"Calculated Results:")
            st.write(f"Resistance (R0): {R0:.2f} ohms")
            st.write(f"Reactance (X0): {X0:.2f} ohms")

if __name__ == "__main__":
    main()
    
