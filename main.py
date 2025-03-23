import streamlit as st
from PhysicsCalculatorWebsite import DisplayTitle

def main():
    st.set_page_config(page_title="Physics Calculator", page_icon=":rocket:", layout="wide")
    st.title("Physics Calculator")

    TitleScreen, KineticEnergy, PivotMoments, NewtonsForce, RateOfWorkDone = st.tabs(["Title Screen", "Kinetic Energy", "Pivot Moments", "Newton’s Force", "Rate of work done"])

    with TitleScreen:
        DisplayTitle.display()
    with KineticEnergy:
        pass
    with PivotMoments:
        pass
    with NewtonsForce:
        pass
    with RateOfWorkDone:
        pass

if __name__ == "__main__":
    main()
