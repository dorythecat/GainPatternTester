import pynanovna

try:
    vna = pynanovna.VNA()
    vna.is_connected() # Trigger Exception if not connected
except Exception:
    print("Could not connect to NanoVNA!")
    exit(1)

print(vna.info())

test_freq = float(input("What frequency should we test? (MHz) ")) * 1000000

vna.set_sweep(test_freq, test_freq, 101)

# Calibration
print("""
Calibrate open.
Please connect the open standard to port 1 of the NanoVNA.

Either use a supplied open, or leave the end of the cable unconnected if desired.

Press enter when you are ready to continue."
""")
input()
vna.calibration_step("open")

print("""
Calibrate short.
Please connect the short standard to port 1 of the NanoVNA.

Press enter when you are ready to continue.
""")
input()
vna.calibration_step("short") #  The calibration is done in several steps as usual.

print("""
Calibrate load.
Please connect the "load" standard to port 1 of the NanoVNA.

Press enter when you are ready to continue.
""")
input()
vna.calibration_step("load")

print("""
Calibrate isolation
Please connect the load standard to port 2 of the NanoVNA.

If available, also connect a load standard to port 1.

Press enter when you are ready to continue."
""")
input()
vna.calibration_step("isolation")

print("""
Calibrate through.
Please connect the "through" standard between port 1 and port 2 of the NanoVNA.

Press enter when you are ready to continue.
""")
input()
vna.calibration_step("through")

data0, data1, freq = vna.sweep()
print("Single sweep done:", data0[0])