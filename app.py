import os
from flask import Flask

from manager.manager import start_loop, stop_loop
from console import log, log_debug
from manager.loop_status import Statuses, set_loop_status, get_loop_status

app = Flask(__name__)


@app.route('/start', methods=['GET'])
def start():
    if get_loop_status() == Statuses.LOOP:
        return {"message": "The Timepulse is already running"}
    log_debug(f"app: before setting status, loop_status={get_loop_status()}")
    set_loop_status(Statuses.STOP)
    start_loop()
    return {"message": "The Timepulse is running"}


@app.route('/stop', methods=['GET'])
def stop():
    if get_loop_status() == Statuses.STOP:
        return {"message": "The Timepulse is already stopped"}
    log_debug(f"app: before setting status, loop_status={get_loop_status()}")
    set_loop_status(Statuses.STOP)
    stop_loop()
    return {"message": "The Timepulse is stopped"}


if __name__ == "__main__":
    start_loop()

    log_debug("app: before starting web service")
    # port = 3000 if os.environ.get('PORT') == None else os.environ.get('PORT')
    port = os.environ.get('PORT') or 3000
    log(f"PORT={port}")
    app.run(host="0.0.0.0",
            port=port,
            debug=True if os.environ.get('ENV') == "develop" else False)
    log_debug("\bapp: after starting web service\n\n")
