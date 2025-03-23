import streamlit as st
from PhysicsCalculatorWebsite import DisplayTitle, DisplayCalculator

def main():
    # Initialize the Streamlit, by showing an always present title, and sets the page layout / configuration
    st.set_page_config(page_title="Physics Calculator", page_icon=":rocket:", layout="wide")
    st.title("Physics Calculator")

    # Creates tabs for the user to choose from
    TitleScreen, KineticEnergy, PivotMoments, NewtonsForce, RateOfWorkDone = st.tabs(["Title Screen", "Kinetic Energy", "Pivot Moments", "Newton’s Force", "Rate of work done"])

    with TitleScreen:
        # Displays the title screen
        DisplayTitle.display()
    with KineticEnergy:
        # Displays the kinetic energy calculator
        DisplayCalculator.KineticEnergy()
    with PivotMoments:
        # Displays the pivot moments calculator
        DisplayCalculator.PivotMoments()
    with NewtonsForce:
        # Displays the force calculator
        DisplayCalculator.Force()
    with RateOfWorkDone:
        # Displays the rate of work done calculator
        DisplayCalculator.RateofWork()

if __name__ == "__main__":
    main()
