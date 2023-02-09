# Python Server Spinner

## How to use?
- First You need to export to an Executable
by installing `pyintsaller`
```
pip install pyinstaller
```
- Then run `pyinstaller server.py` to create a binary.
- You'll find `build` and `dist` folders created, Go to `dist` and copy all of its contents in th e same frontend directory
- use the next command to spin off the server if you are on linux
```
./server 8080 
```
where `8080` is the port, and you can change it to your desired port.

## How to run in development?
- Just put your python file (`server.py`) next to `index.html`
- run
```
python3 server.py 8080
```
where 8080 is t`he port, and you can change it to your desired port.