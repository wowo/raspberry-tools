from output import PeriodicOutput
import threading

def blink_and_buzz(settings):
    for data in settings:
        periodic = PeriodicOutput(data['pin'])
        t = threading.Thread(target=getattr(periodic, data['tempo']), args=(5,))
        t.daemon = False
        t.start()


print "Red diode, fast"
blink_and_buzz(({'pin': 11, 'tempo': 'fast'}, {'pin': 15, 'tempo': 'fast'}))

#print "Green diode, medium"
#blink_and_buzz(({'pin': 12, 'tempo': 'medium'}, {'pin': 15, 'tempo': 'medium'}))
