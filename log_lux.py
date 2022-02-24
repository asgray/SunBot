# log_lux.py
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import adafruit_tsl2561
import gspread
import board
import busio

# setup sensor read
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)

# setup sheet update
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
key = 'sunbotkey.txt'
creds = ServiceAccountCredentials.from_json_keyfile_name(key, scope)
worksheet = gspread.authorize(creds).open('SunBot Log').get_worksheet(0)

time = datetime.now().strftime("%m/%d/%Y %H:%M").split(' ')

lux_val = round(sensor.lux, 5) if sensor.lux else 0

# append row
worksheet.append_row([time[0], time[1], lux_val])
