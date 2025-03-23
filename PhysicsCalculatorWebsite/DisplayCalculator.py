import streamlit as st

class DisplayCalculator:
    @staticmethod
    def KineticEnergy() -> None:
        left_column, right_column = st.columns(2)
        value_1 = left_column.number_input("Placeholder Prompt", max_value=100.0, min_value=0.0, key="KineticEnergy1")
        value_2 = right_column.number_input("Placeholder Prompt", max_value=100.0, min_value=0.0, key="KineticEnergy2")
        # value_2 = right_column.number_input("Placeholder", step=0.1, max_value=100.0, min_value=0.0)

    @staticmethod
    def PivotMoments() -> None:
        pass

    @staticmethod
    def Force() -> None:
        pass

    @staticmethod
    def RateofWork() -> None:
        pass
