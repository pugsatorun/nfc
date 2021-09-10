import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('../python-write-test-325506-04f791ddf6a9.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('python 書き込みテスト').sheet1

wks.update_acell('A1', 'Hello World!')
print(wks.acell('A1'))
