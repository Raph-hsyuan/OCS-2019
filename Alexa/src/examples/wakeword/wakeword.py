import logging
import sys
import led_controller as led
import distance_reader as dis
import motor_controller as mt
from agt import AlexaGadget
import led_controller as led

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

cled = led.Led_Controller(6)
cled.setColor(-1)
cmt = mt.Motor_Controller(7)

class WakewordGadget(AlexaGadget):

    def __init__(self):
        super().__init__()

    def on_alexa_gadget_statelistener_stateupdate(self, directive):
        for state in directive.payload.states:
            print(state.name)
            # if state.name == 'wakeword':
            #     if state.value == 'active':
            #         logger.info('Wake word active - turn on LED')
            #         cled.setColor(1)
            #     elif state.value == 'cleared':
            #         logger.info('Wake word cleared - turn off LED')
            #         cled.setColor(-1)
            if state.name == 'reminders' :
                cled.setColor(1)
                if state.value == 'active':
                    cmt.rotate(22.5)
                    logger.info('Medicine time')
                    cled.setColor(1)
                elif state.value == 'cleared':
                    logger.info('Medicine taken')
                    rdis = dis.Distance_Reader(5)
                    while (not rdis.foundSomething()):
                        cled.setBlinkBySecond(1,5)
                    cled.setColor(-1)


if __name__ == '__main__':
    try:
        WakewordGadget().main()
    finally:
        logger.debug('Cleaning up GPIO')
        cmt.cleanup()
