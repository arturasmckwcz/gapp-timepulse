# This is HOWTOs

## Dev

1. clone repo and cd to it:
   ```
   $ git clone git@github.com:arturasmckwcz/gapp-timepulse.git
   $ cd gapp-soulforge
   ```
2. set up virtual environment for python:
   ```
   $ python3 -m venv venv
   $ source venv/bin/activate
   ```
3. install dependencies:
   ```
   $ pip3 install -r requirements.txt
   ```
4. start dev container:
   ```
   $ docker-compose -f docker-compose.dev.yml -p gapp up
   ```
And voilà!

## WSGI
to run in a container for production:
```
$ docker-compose -p gapp up --build
```
