from target_detector import TargetDetector
from drone_controller import DroneController
from payload_dropper import PayloadDropper
from mission_executor import MissionExecutor

if __name__ == "__main__":
    connection_string = "tcp:127.0.0.1:5763"

    target_lat = -35.364500
    target_lon = 149.166500

    search_grid = [
        (-35.364000, 149.163000),
        (-35.364000, 149.167000),
        (-35.365500, 149.167000),
        (-35.365500, 149.163000),
    ]


    controller = DroneController("tcp:127.0.0.1:5763")
    detector = TargetDetector(target_lat, target_lon, threshold=8.0)
    dropper = PayloadDropper(controller, servo_chn=9)
    mission = MissionExecutor(controller, detector, dropper)
    mission.execute_mission(search_grid, alt=25)

