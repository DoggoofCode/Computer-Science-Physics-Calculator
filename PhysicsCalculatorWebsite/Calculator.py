def CalculateKineticEnergy(mass, velocity):
    # Calculates the kinetic energy of an object
    return 0.5 * mass * velocity ** 2

def CalculatePivotMoments(distance_from_pivot, force_exerted):
    # Calculates the pivot moments of an object
    return distance_from_pivot * force_exerted

def CalculateForce(mass, acceleration):
    # Calculates the force exerted on an object
    return mass * acceleration

def CalculateRateOfWork(energy_transferred, time_transferred):
    # Calculates the rate of work done on an object
    return energy_transferred / time_transferred
