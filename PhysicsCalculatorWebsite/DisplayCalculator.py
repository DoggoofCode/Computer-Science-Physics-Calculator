import streamlit as st
from PhysicsCalculatorWebsite.Calculator import CalculateForce, CalculateRateOfWork, CalculatePivotMoments, CalculateKineticEnergy

class DisplayCalculator:
    @staticmethod
    def KineticEnergy() -> None:
        # Initialize the left and right columns for the input fields
        left_column, right_column = st.columns(2)
        # Lets the user input the velocity of the object
        velocity = left_column.number_input("Please input the velocity of the object (m/s)", key="KineticEnergy1")

        # Lets the user input the mass of the object
        # Minimum value of 0.1 because mass cannot be zero or negative, and it does not have an option have a greater of less than limit
        mass = right_column.number_input("Please input the mass of the object (kg)", min_value=0.1, key="KineticEnergy2")

        # Button to calculate the kinetic energy
        val = st.button("Calculate", key="KineticEnergy")
        if val:
            # Creates a box which displays the answer to the question
            answer_box = st.container(border=True)
            answer_box.write(f"The Kinetic Energy of the object is {CalculateKineticEnergy(mass, velocity)} Joules")

    @staticmethod
    def PivotMoments() -> None:
        # Initialize the left and right columns for the input fields
        left_column, right_column = st.columns(2)
        # Lets the user input the force exerted on the pivot
        force_on_pivot = left_column.number_input("Please input force exerted on the pivot (N)", key="Pivot1")
        # Lets the user input the distance from the pivot
        distance_from_pivot = right_column.number_input("Please input the distance from the pivot (m)", key="Pivot2")

        # Button to calculate the moment of the pivot
        val = st.button("Calculate", key="Pivot")
        if val:
            # Creates a box which displays the answer to the question
            answer_box = st.container(border=True)
            answer_box.write(f"The force of the moment is {CalculatePivotMoments(force_on_pivot, distance_from_pivot)} Newton Metres")


    @staticmethod
    def Force() -> None:
        # Initialize the left and right columns for the input fields
        left_column, right_column = st.columns(2)

        # Lets the user input the mass of the object
        # Minimum value of 0.1 because mass cannot be zero or negative, and it does not have an option have a greater of less than limit
        mass = left_column.number_input("Please input mass of the object (kg)", min_value=0.1, key="Force1")
        # Lets the user input the acceleration of the object
        acceleration = right_column.number_input("Please input the acceleration of the object (m/s^2)", key="Force2")

        # Button to calculate the force of the object
        val = st.button("Calculate", key="Force")
        if val:
            # Creates a box which displays the answer to the question
            answer_box = st.container(border=True)
            answer_box.write(f"The force of the object is {CalculateForce(mass, acceleration)} Newtons")

    @staticmethod
    def RateofWork() -> None:
        # Initialize the left and right columns for the input fields
        left_column, right_column = st.columns(2)
        # Lets the user input the total energy transferred
        total_energy = left_column.number_input("Please input the total energy transferred  (J)", key="RateOfWork1")
        # Lets the user input the total time the energy is transferred
        total_time = right_column.number_input("Please input the total time the energy is transferred (s)", min_value=0.1, key="RateOfWork2")

        # Button to calculate the rate of work
        val = st.button("Calculate", key="RateOfWork")
        if val:
            # Creates a box which displays the answer to the question
            answer_box = st.container(border=True)
            answer_box.write(f"The work done is {CalculateRateOfWork(total_energy, total_time)} watts")
