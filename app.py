import logging
import os
from flask import Flask

from manager.manager import run_pulse
from console import log, log_debug
from manager.loop_status import loop_statuses, loop_status
from timepulse.current_day import date


def create_app():
    app = Flask(__name__)
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.DEBUG)

    @app.route('/check', methods=['GET'])
    def check():
        return {
            "message":
            f"The current date is: {date.current_date()}, loop_status:{loop_status.get_status()}"
        }

    @app.route('/start', methods=['GET'])
    def start():
        if loop_status.get_status() == loop_statuses.LOOP:
            return {"message": "The Timepulse is already running"}
        log_debug(
            f"app: before setting status, loop_status={loop_status.get_status()}"
        )
        log_debug(
            f"app: before starting pulse, loop_status={loop_status.get_status()}"
        )
        if run_pulse.start_pulse():
            return {
                "message":
                f"The Timepulse is started from day: {date.current_date()}"
            }
        return {"message": "Timepulse didn't start"}

    @app.route('/stop', methods=['GET'])
    def stop():
        if loop_status.get_status() == loop_statuses.STOP:
            return {"message": "The Timepulse has been already stopped"}
        log_debug(
            f"app: before setting status, loop_status={loop_status.get_status()}"
        )
        if run_pulse.stop_pulse():
            return {"message": "The Timepulse is stopped"}
        return {"message": "Failed to stop the Timepulse"}

    return app


if __name__ == "__main__":
    log_debug("app: before starting web service")
    port = os.environ.get('PORT') or 3000
    log(f"PORT={port}")
    app = create_app()
    app.run(host="0.0.0.0",
            port=port,
            debug=True if os.environ.get('ENV') == "debug" else False)
    log_debug("\bapp: after starting web service\n\n")
