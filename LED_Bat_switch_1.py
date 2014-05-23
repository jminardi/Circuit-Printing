from mecode import G
from mecode.utils import profile_surface , write_cal_file
#kp = KeyenceProfilometer('COM3') 
##km = KeyenceMicrometer('COM8')
#pb = EFDPressureBox('COM5')
g = G(
    print_lines=False,
    outfile=r"C:\Users\lewislab\Desktop\circuit-path.gcode",
    aerotech_include=False,
)
#pressure_box = 5
zero = 5

PRESSURE_ON = 'M400 \nM42 P32 S255'
PRESSURE_OFF = 'M400 \nM42 P32 S0'



def print_LED_circuit(z, feed, fast_feed, dwell, pressure, axis, valve, valve_bank = True, y_negative = False):
    #x_start = g.get_axis_pos(axis='x')
    #y_start = g.get_axis_pos(axis='y')
    top = 5
    x_start, y_start = 12.70, 104.00
    g.feed(fast_feed)
    g.abs_move(x_start, y_start, Z=top+3)
    g.move(Z=-4)
    if y_negative is True:
        sign = -1
    else:
        sign = 1
    g.feed(fast_feed)
    g.move(x=8)
    #pb.set_pressure(pressure = pressure)
    g.abs_move(**{axis:(z-0.7)})
    g.feed(feed)
    
    g.write(PRESSURE_ON)
    
    g.dwell(dwell)
    g.move(x=-7)
    g.move(**{axis:0.7})    
    g.move(x=-1)
    g.move(y=(-18)*sign)
    g.move(x=3.6508)
    
    g.write(PRESSURE_OFF)
    
    g.move(**{axis:-0.4})
    g.feed(fast_feed)
    
    g.move(**{axis:3.4})
    g.move(x=2.6984)
    g.move(**{axis:-3.4})
    
    g.write(PRESSURE_ON)  
    
    g.feed(feed)
    g.dwell(dwell)
    g.move(**{axis:0.4})
    g.move(x=7.9508)
    
    g.write(PRESSURE_OFF)
    
    g.feed(fast_feed)
    g.move(**{axis:3})
    g.move(x=10.4)
    g.move(**{axis:-3})
    
    g.write(PRESSURE_ON)
    
    g.feed(feed)
    g.dwell(dwell)
    g.move(x=12.3958)
    g.move(**{axis:-0.4})
    
    g.write(PRESSURE_OFF)
    
    g.feed(fast_feed)
    
    g.move(**{axis:3.4})
    g.move(x=1.8042, y=(1.9042*sign))
    g.move(**{axis:-3.4})
    
    g.write(PRESSURE_ON)
    
    g.feed(feed)
    g.dwell(dwell)
    g.move(**{axis:0.4})
    g.move(y=(16.0958*sign))
    g.move(x=-5)
    
    g.write(PRESSURE_OFF)
    
    g.feed(fast_feed)
    g.move(**{axis:4})
    g.move(y=(10*sign))
    g.abs_move(x=x_start, y=y_start)

#g.write('POSOFFSET CLEAR X Y U Z')
#
g.feed(10*60)
g.abs_move(Z=zero + 1)
g.set_home(Z=1)
  
            
#pb.toggle_pressure() 
print_LED_circuit(z = 0.1, feed = 2*60, fast_feed=15*60, dwell = 0.25, pressure = 8, axis = 'Z', valve = 0, valve_bank=False, y_negative = False) 
g.view()
#pb.toggle_pressure()
#g.write('POSOFFSET CLEAR X Y U Z')
#pb.disconnect
#g.teardown
