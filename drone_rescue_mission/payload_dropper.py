"""
ta klasa zaklada ze do drona jest zamontowane urządzenie ktore
moze upuscic ladunek przy pomocy silnika serwo który jest sterowany
przez kanal 9
"""
import time
from pymavlink import mavutil

class PayloadDropper:
    def __init__(self, controller, servo_chn, open_pwm=2000, closed_pwm=1000):
        self.controller = controller
        self.servo_chn = servo_chn
        # 2000 is max pwm value for servo and 1000 is the min value
        self.open_pwm = open_pwm
        self.closed_pwm = closed_pwm
    def drop(self):
        print("zwalnianie ladunku")
        self.controller.master.mav.command_long_send(
            self.controller.master.target_system,
            self.controller.master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0,
            self.servo_chn,
            self.open_pwm,
            0,
            0,
            0,
            0,
            0,
        )
        print("ladunek zostal upuszczony")
        time.sleep(3)
        self.controller.master.mav.command_long_send(
            self.controller.master.target_system,
            self.controller.master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0,
            self.servo_chn,
            self.closed_pwm,
            0,
            0,
            0,
            0,
            0,
        )
        return True

