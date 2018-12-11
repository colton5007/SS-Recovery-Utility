import datetime
import subprocess
from datetime import timedelta

print('     Welcome to the SS Data Recovery Utility     ')
print('Please enter the day this report is running for: ')
print('-------------------------------------------------')
ds = datetime.datetime.today().strftime('%Y-%m-%d')
dsy = (datetime.datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
print('(0) Today: ' + ds)
print('(1) Yesterday:' + dsy)
print('Custom: YYYY-MM-DD')
print('-------------------------------------------------')
d_selection = input('Enter Selection: ')
date_s = None
if d_selection == '0':
	date_s = ds
elif d_selection == '1':
	date_s = dsy
else:
	year,month,day = d_selection.split('-')
	try :
		datetime.datetime(int(year),int(month),int(day))
	except:
		print('Invalid date selection, exitting program')
		sys.exit(1)
	date_s = d_selection

year,month,day = date_s.split('-')
subprocess.call(['sed', '-n', ('/%s\\-%s\\-%s/,' % (year, month, day)) + '%' + 'p', '/var/log/strem.log', '|', 'sudo', 'tee', 'data_log', '2>&1', '>/dev/null'])

with open("data_log") as infile:
    for line in infile:
        if "b'" in line:
        	with open('data_log.csv', 'a+') as f:
        		t = line.replace("\\r\\n'", '').replace(":b'", ',')
        		f.write(t)
        		f.close()