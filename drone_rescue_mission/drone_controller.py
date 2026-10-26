from pymavlink import mavutil
import time
import math
class DroneController:
    def __init__(self, connection_string):
        self.master = mavutil.mavlink_connection(connection_string)
        self.master.wait_heartbeat()
        # ten element jest potrzebny poniewaz ardupilot nie wysylal informacji o wysokosci
        self.master.mav.request_data_stream_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_DATA_STREAM_POSITION,
            1,
            1,
        )

    def set_mode(self, mode_string, timeout=8):
        if not mode_string in self.master.mode_mapping():
            print("Niepoprawna nazwa trybu")
            return False

        mode_id = self.master.mode_mapping()[mode_string]

        self.master.mav.set_mode_send(
            self.master.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id
        )
        # while loop prevents from reading HEARTBEAT from before the mode change
        # or missing the HEARTBEAT
        start_time = time.time()
        while time.time() - start_time < timeout:
            msg = self.master.recv_match(type="HEARTBEAT", blocking=True, timeout=1.0)
            if msg:
                if msg.custom_mode == mode_id:
                    print("autopilot potwierdzil zmiane trybu lotu")
                    return True
            time.sleep(0.1)
        print("autopilot nie potwierdzil zmiany trybu lotu")
        return False



    def arm_takeoff(self, alt):

        change_success = self.set_mode("GUIDED")

        if not change_success:
            return False

        self.master.arducopter_arm()
        print("czekam na uzbrojenie silnikow")
        self.master.motors_armed_wait()
        print("silniki uzbrojone")

        print("wysyłam komende startu")
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            alt
        )

        start_time = time.time()
        while time.time() - start_time < 20:
            msg = self.master.recv_match(type="GLOBAL_POSITION_INT", blocking=True)
            if msg:
                current_alt = msg.relative_alt / 1000.0
                if current_alt >= alt*0.95:
                    print("osiagnieto docelowa wysokosc")
                    return True
            time.sleep(0.5)
        print("autopilot nie potwierdzil zmiany trybu lotu")
        return False

    def get_current_position(self):
        msg = self.master.recv_match(
            type="GLOBAL_POSITION_INT", blocking=True, timeout=1.0
        )
        if msg:
            lat = msg.lat / 1e7
            lon = msg.lon / 1e7
            alt = msg.relative_alt / 1000.0
            return lat, lon, alt
        return None

    def goto_position(self, lat, lon, alt):
        print(f"Lot do punktu {lat}, {lon}")
        self.master.mav.set_position_target_global_int_send(
            0,  # time_boot_ms (not used)
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
            int(
                0b110111111000
            ),  # ignoruj predkosc i przyspieszenie
            int(lat * 1e7),
            int(lon * 1e7),
            alt,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )

    def return_to_home(self):
        print("Rozpoczynam procedure powrotu do startu")
        success = self.set_mode("RTL")
        if success:
            print("dron wraca do startu")
        else:
            print("Nie udalo się wlaczyć trybu RTL")
        return success


