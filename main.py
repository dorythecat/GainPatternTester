import pynanovna
import time
import os

try:
    vna = pynanovna.VNA()
    vna.is_connected() # Trigger Exception if not connected
except Exception:
    print("Could not connect to NanoVNA!")
    exit(1)

print(vna.info())

test_freq = float(input("What frequency should we test? (MHz) ")) * 1000000

vna.set_sweep(test_freq, test_freq, 2)

# Calibration
ans = input("Do you wish to load a calibration file? [y]/n: ")
if not ans.lower().startswith("n"):
    if not os.path.isfile("./latest.cal."):
        print("Couldn't open calibration file!")
        exit(1)
    vna.load_calibration("./latest.cal")
else:
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

    vna.calibrate()

    ans = input("Do you wish to save this calibration to a file? [y]/n: ")
    if not ans.lower().startswith("n"):
        print("Saving calibration to ./latest.cal.")
        vna.save_calibration("./latest.cal")
    else:
        print("Discarding calibration.")

while True:
    data0, data1, freq = vna.sweep()
    print("Single sweep done:", data0[0])
    time.sleep(1)