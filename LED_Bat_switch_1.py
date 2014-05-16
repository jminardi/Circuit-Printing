from mecode.devices.keyence_profilometer import KeyenceProfilometer
from mecode.devices.keyence_micrometer import KeyenceMicrometer
from mecode.devices.efd_pressure_box import EFDPressureBox
from mecode import G
from mecode.utils import profile_surface , write_cal_file
kp = KeyenceProfilometer('COM3') 
km = KeyenceMicrometer('COM8')
pb = EFDPressureBox('COM4')
g = G(direct_write=True, print_lines=True)
pressure_box = 4


 #g.set_valve(num = 0, value = 0)
   #pb.set_pressure(com_port = 4, value = 5)
   #pb.toggle_pressure(4)
g.abs_move(x=10)
g.move(x=10)

def print_LED_circuit(z, feed, dwell, pressure, axis, valve, valve_bank = True):
    g.feed(15)
    g.move(x=8)
    pb.set_pressure(com_port = pressure_box, value = pressure)
    g.abs_move(**{axis:z})
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(feed)
    g.move(x=-8)
    g.move(y=-18)
    g.move(x=3.4508)
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure(pressure_box)
    g.feed(15)
    g.move(**{axis:3})
    g.move(x=3.0984)
    g.move(**{axis:-3})
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure(pressure_box)
    g.feed(feed)
    g.dwell(dwell)
    g.move(x=7.7508)
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure(pressure_box)
    g.feed(15)
    g.move(**{axis:3})
    g.move(x=10.4)
    g.move(**{axis:-3})
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure(pressure_box)
    g.feed(feed)
    g.dwell(dwell)
    g.move(x=12.5958)
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure(pressure_box)
    g.feed(15)
    g.move(**{axis:3})
    g.move(x=1.9042, y=1.9042)
    g.move(**{axis:-3})
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure(pressure_box)
    g.feed(feed)
    g.dwell(dwell)
    g.move(y=16.0958)
    g.move(x=-5)
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure(pressure_box)
    g.feed(30)
    g.move(**{axis:30})
    g.move(y=10)
    
    
pb.toggle_pressure(pressure_box) 
print_LED_circuit(z = 0.2, feed = 2, dwell = 0.1, pressure = 5, axis = 'Z', valve = 0, valve_bank=False) 
pb.toggle_pressure(pressure_box)
