import threading
from console import log_debug
from .loop_status import Statuses, get_loop_status
from timepulse.timepulse import pulse

thread = None


def start_loop():
    status = get_loop_status()
    log_debug(f"start_loop: status={status}")
    if status == Statuses.STOP:
        thread = threading.Thread(target=pulse)
        thread.start()
        log_debug("start_loop: Timepulse loop started")


def stop_loop():
    status = get_loop_status()
    log_debug(f"stop_loop: status={status}")
    if status == Statuses.LOOP:
        thread.join()
        log_debug("stop_loop: Timepulse loop stopped")