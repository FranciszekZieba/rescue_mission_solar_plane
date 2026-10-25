import math
import time

class MissionExecutor:
    def __init__(self, controller, detector, dropper):
        self.controller = controller
        self.detector = detector
        self.dropper = dropper

    def execute_mission(self, waypoints, alt):
        print("rozpoczynam misje")
        if not self.controller.arm_takeoff(alt):
            print("blad startu misja nie rozpoczeta")
            return False
        found = False

        for wp_lat, wp_lon in waypoints:
            self.controller.goto_position(wp_lat, wp_lon, alt)
            while True:
                current_pos = self.controller.get_current_position()
                if current_pos is None:
                    time.sleep(0.3)
                    continue
                curr_lat, curr_lon, _ = current_pos

                if self.detector.detection(curr_lat, curr_lon):
                    print("cel namierzony")
                    found = True
                    break

                d_lat = (curr_lat - wp_lat) * 111111
                d_lon = (curr_lon - wp_lon) * 111111 * math.cos(
                    math.radians(wp_lat)
                )
                distance_to_waypoint = math.sqrt(d_lat ** 2 + d_lon ** 2)

                if distance_to_waypoint <= 3.0:
                    break
                time.sleep(0.5)
            if found:
                break
        #
        if found:
            print("zmiana trybu na zwis")
            self.controller.set_mode("LOITER")
            time.sleep(2)
            self.dropper.drop()
            time.sleep(2)
        else:
            print("nie znaleziono celu")

        self.controller.return_to_home()
        return True