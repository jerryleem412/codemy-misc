import serial

s = serial.Serial(port='COM4', baudrate=9600)
s.write(b"\r\n")
res = s.read_all()
print(res.decode("ASCII"))