import streamlit as st
from PhysicsCalculatorWebsite.Calculator import CalculateForce, CalculateRateOfWork, CalculatePivotMoments, CalculateKineticEnergy

class DisplayCalculator:
    @staticmethod
    def KineticEnergy() -> None:
        left_column, right_column = st.columns(2)
        velocity = left_column.number_input("Please input the velocity of the object (m/s)", key="KineticEnergy1")
        # Minimum value of 0.1 because mass cannot be zero or negative, and it does not have an option have a greater of less than limit
        mass = right_column.number_input("Please input the mass of the object (kg)", min_value=0.1, key="KineticEnergy2")

        val = st.button("Calculate", key="KineticEnergy")
        if val:
            answer_box = st.container(border=True)
            answer_box.write(f"The Kinetic Energy of the object is {CalculateKineticEnergy(mass, velocity)} Joules")

    @staticmethod
    def PivotMoments() -> None:
        left_column, right_column = st.columns(2)
        force_on_pivot = left_column.number_input("Please input force exerted on the pivot (N)", key="Pivot1")
        distance_from_pivot = right_column.number_input("Please input the distance from the pivot (m)", key="Pivot2")

        val = st.button("Calculate", key="Pivot")
        if val:
            answer_box = st.container(border=True)
            answer_box.write(f"The force of the moment is {CalculatePivotMoments(force_on_pivot, distance_from_pivot)} Newton Metres")


    @staticmethod
    def Force() -> None:
        left_column, right_column = st.columns(2)
        # Minimum value of 0.1 because mass cannot be zero or negative, and it does not have an option have a greater of less than limit
        mass = left_column.number_input("Please input mass of the object (kg)", min_value=0.1, key="Force1")
        acceleration = right_column.number_input("Please input the acceleration of the object (m/s^2)", key="Force2")

        val = st.button("Calculate", key="Force")
        if val:
            answer_box = st.container(border=True)
            answer_box.write(f"The force of the object is {CalculateForce(mass, acceleration)} Newtons")

    @staticmethod
    def RateofWork() -> None:
        left_column, right_column = st.columns(2)
        total_energy = left_column.number_input("Please input the total energy transferred  (J)", key="RateOfWork1")
        total_time = right_column.number_input("Please input the total time the energy is transferred (s)", min_value=0.1, key="RateOfWork2")

        val = st.button("Calculate", key="RateOfWork")
        if val:
            answer_box = st.container(border=True)
            answer_box.write(f"The work done is {CalculateRateOfWork(total_energy, total_time)} watts")
