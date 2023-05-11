import threading
from console import log_debug
from .loop_status import loop_statuses, loop_status
from timepulse.timepulse import pulse


class run_pulse:
    _thread = None

    @staticmethod
    def start_pulse():
        log_debug(f"start_pulse: status={loop_status.get_status()}")
        if loop_status.get_status() == loop_statuses.STOP:
            run_pulse._thread = threading.Thread(target=pulse)
            run_pulse._thread.start()
            log_debug("start_pulse: Timepulse started")
            return True
        return False

    @staticmethod
    def stop_pulse():
        log_debug(f"stop_pulse: status={loop_status.get_status()}")
        if loop_status.get_status() != loop_statuses.STOP:
            loop_status.set_status(loop_statuses.STOP)
            if run_pulse._thread:
                run_pulse._thread.join()
                log_debug("stop_pulse: Timepulse stopped")
                return True
            return False
        return False