from mecode.devices.keyence_profilometer import KeyenceProfilometer
from mecode.devices.keyence_micrometer import KeyenceMicrometer
from mecode.devices.efd_pressure_box import EFDPressureBox
from mecode import G
from mecode.utils import profile_surface , write_cal_file
#kp = KeyenceProfilometer('COM3') 
##km = KeyenceMicrometer('COM8')
pb = EFDPressureBox('COM5')
g = G(direct_write=True, print_lines=True)
pressure_box = 5
zero=(-6.76500)


def print_LED_circuit(z, feed, dwell, pressure, axis, valve, valve_bank = True, y_negative = False):
    x_start = g.get_axis_pos(axis='x')
    y_start = g.get_axis_pos(axis='y')
    if y_negative is True:
        sign = -1
    else:
        sign = 1
    g.feed(15)
    g.move(x=8)
    pb.set_pressure(pressure = pressure)
    g.abs_move(**{axis:(z-0.7)})
    g.feed(feed)
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure()
    g.dwell(dwell)
    g.move(x=-7)
    g.move(**{axis:0.7})    
    g.move(x=-1)
    g.move(y=(-18)*sign)
    g.move(x=3.6508)
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure()
    g.move(**{axis:-0.4})
    g.feed(15)
    
    g.move(**{axis:3.4})
    g.move(x=2.6984)
    g.move(**{axis:-3.4})
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure()
    g.feed(feed)
    g.dwell(dwell)
    g.move(**{axis:0.4})
    g.move(x=7.9508)
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure()
    g.feed(15)
    g.move(**{axis:3})
    g.move(x=10.4)
    g.move(**{axis:-3})
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure()
    g.feed(feed)
    g.dwell(dwell)
    g.move(x=12.3958)
    g.move(**{axis:-0.4})
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure()
    g.feed(15)
    
    g.move(**{axis:3.4})
    g.move(x=1.8042, y=(1.9042*sign))
    g.move(**{axis:-3.4})
    if valve_bank is True:
        g.set_valve(num = valve, value = 1)
    else:
        pb.toggle_pressure()
    g.feed(feed)
    g.dwell(dwell)
    g.move(**{axis:0.4})
    g.move(y=(16.0958*sign))
    g.move(x=-5)
    if valve_bank is True:
        g.set_valve(num = valve, value = 0)
    else:
        pb.toggle_pressure()
    g.feed(20)
    g.move(**{axis:4})
    g.move(y=(10*sign))
    g.abs_move(x=x_start, y=y_start)

g.write('POSOFFSET CLEAR X Y U Z')
#
g.feed(10)
g.abs_move(Z=zero + 1)
g.set_home(Z=1)
  
            
#pb.toggle_pressure() 
print_LED_circuit(z = 0.1, feed = 2, dwell = 0.25, pressure = 8.5, axis = 'Z', valve = 0, valve_bank=False, y_negative = True) 
#pb.toggle_pressure()
g.write('POSOFFSET CLEAR X Y U Z')
pb.disconnect
g.teardown
