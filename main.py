import pynanovna
from pynanovna.utils import stream_from_csv
from pynanovna.vis import plot, polar

# Create a VNA object to control your NanoVNA.
vna = pynanovna.VNA()


# Get and print some information about your device.
print(vna.info())

# Load a premade calibration file. See example_calibration.py for info on calibration.
#vna.load_calibration("./cal_file.cal")


# Set the sweep range and number of points to measure.
vna.set_sweep(430e6, 440e6, 1001)

data0, data1, freq = vna.sweep()
print("Single sweep done:", data0)