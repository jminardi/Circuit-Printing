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

PRESSURE_ON = 'M400 \nM42 P32 S255'
PRESSURE_OFF = 'M400 \nM42 P32 S0'



def print_LED_circuit(z, feed, fast_feed, dwell, pressure, axis, valve, valve_bank = True, y_negative = False):
    #x_start = g.get_axis_pos(axis='x')
    #y_start = g.get_axis_pos(axis='y')
    
    top = 5                            #Z height of the top of the circuit (channel filling height)
    travelHeight=9                     #Z height to travel at
    x_start, y_start = 13.20, 104.70   #hand calibrated reference position of ink nozzle above the upper left corner trace
    padFillingZOffzet= -0.7            #height of the nozzle relative whle filling pads relative to their top
    dabHeight = -0.4                   #height of the nozzle relative to the top of the channels for "dapping" the trace at their ends (avoid stringing)

    #flip Y dir
    if y_negative is True:
        sign = -1
    else:
        sign = 1

    #safe travel to start position
    g.write("\n;Travel to start position")
    g.feed(fast_feed)
    g.abs_move(**{axis:(travelHeight)})           #raise to safe travel height
    g.abs_move(x_start+8, y_start)                #move nozzle above starting position, 8mm to the right of the reference position
    g.abs_move(**{axis:(top+padFillingZOffzet)})  #move down just below the top of the pad (nozzle is closer to make a flatter, wel-adhered trace in the pad)
         
    #First trace segment going left from the battery's left pad
    g.write("\n;First Segment Lpad -> resistor")
    g.write(PRESSURE_ON)
    g.dwell(dwell)
    g.feed(feed)
    g.move(x=-7)#go from the left side to the right side of the battery's left pad
    g.abs_move(**{axis:(top)})   #go to channel filling height    
    g.move(x=-1)        #the first small channel segment leading in the the top left corner from the pad
    g.move(y=(-18)*sign)#the left down trace
    g.move(x=3.6508)    #the bottom left horizontal trce going to the resistor
    g.abs_move(**{axis:(top+dabHeight)})
    g.write(PRESSURE_OFF)
    
    #jump over the resistor
    g.write("\n;Jump resistor")
    g.feed(fast_feed)
    g.abs_move(**{axis:(travelHeight)})
    g.move(x=2.6984)
    g.abs_move(**{axis:(top+dabHeight)})
    
    #Second trace segment between resistor and reed switch
    g.write("\n;Second Segment - resistors -> reed")
    g.feed(feed)
    g.write(PRESSURE_ON)  
    g.dwell(dwell)
    g.abs_move(**{axis:(top)})
    g.move(x=7.9508)
    g.abs_move(**{axis:(top+dabHeight)})
    g.write(PRESSURE_OFF)
    
    #jump over reed switch
    g.write("\n;Jump reed switch")
    g.feed(fast_feed)
    g.abs_move(**{axis:(travelHeight)})
    g.move(x=11.4)
    g.abs_move(**{axis:(top+dabHeight)})
    
    #Third trace between reed switch and LED
    g.write("\n;Third Segment reed -> LED")
    g.feed(feed)
    g.write(PRESSURE_ON)
    g.dwell(dwell)
    g.abs_move(**{axis:(top)})
    g.move(x=11.3958)
    g.abs_move(**{axis:(top+dabHeight)})
    g.write(PRESSURE_OFF)
    
    #jump over LED
    g.write("\n;Jump LED")
    g.feed(fast_feed)
    g.abs_move(**{axis:(travelHeight)})
    g.move(x=1.8042, y=(1.9042*sign))
    g.abs_move(**{axis:(top+dabHeight)})
    
    #Final trace from LED to Battery's right pad
    g.write("\n;Final Segment LED -> Rpad")
    g.feed(feed)
    g.write(PRESSURE_ON)
    g.dwell(dwell)
    g.abs_move(**{axis:(top)})
    #g.move(**{axis:0.4})
    g.move(y=(16.0958*sign))#up top top right corner
    g.move(x=-1)
    g.abs_move(**{axis:(top+padFillingZOffzet)})
    g.move(x=-4)            #from top right corner to left side of battery's right pad
    g.abs_move(**{axis:(top+dabHeight)})
    g.write(PRESSURE_OFF)
    
    #end code
    g.write("\n;End Code")
    g.feed(fast_feed)
    g.abs_move(**{axis:(travelHeight)})
    #g.move(y=(10*sign))
    g.abs_move(x=0, y=150)    #Move to manual circuit population waiting position
    g.abs_move(**{axis:(top)})#move back to the original z height
    g.write("M100")#finish all current moves
    g.write("M226")   #Pause
    g.write("M1")    #Marlin Pause
    g.write("M0")    #Marlin Pause
          
    g.write("\n;Paused")          
#pb.toggle_pressure() 
print_LED_circuit(z = 0.1, feed = 2*60, fast_feed=15*60, dwell = 0.25, pressure = 8, axis = 'Z', valve = 0, valve_bank=False, y_negative = False) 
g.view()
#pb.toggle_pressure()
#g.write('POSOFFSET CLEAR X Y U Z')
#pb.disconnect
#g.teardown
