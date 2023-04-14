from pyJoules.energy_meter import measure_energy


@measure_energy
def foo():
    for i in range(1000000):
        pass

foo()