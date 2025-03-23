import streamlit as st
from PhysicsCalculatorWebsite import DisplayTitle, DisplayCalculator

def main():
    st.set_page_config(page_title="Physics Calculator", page_icon=":rocket:", layout="wide")
    st.title("Physics Calculator")

    TitleScreen, KineticEnergy, PivotMoments, NewtonsForce, RateOfWorkDone = st.tabs(["Title Screen", "Kinetic Energy", "Pivot Moments", "Newton’s Force", "Rate of work done"])

    with TitleScreen:
        DisplayTitle.display()
    with KineticEnergy:
        DisplayCalculator.KineticEnergy()
    with PivotMoments:
        DisplayCalculator.PivotMoments()
    with NewtonsForce:
        DisplayCalculator.Force()
    with RateOfWorkDone:
        DisplayCalculator.RateofWork()

if __name__ == "__main__":
    main()
