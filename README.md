# gapp-timepulse
This is a simple HTTP server with 3 endpoints. It starts or stops the Timepulse and also checks its status

## Endpoints
`/start`
`/stop`
`/check`

## The Timepulse
The Timepi]ulse module generates a new day in regular period of time, 10s by default starting from 1970-01-01
Period of time and starting date are defined by environment vars `TIMEPULSE_DAY_IN_SECS` and `GAPP_FIRST_DAY`

generated dates are sent as RabbitMQ messages to the `timepulse` exchange of `fanout` tipe.
