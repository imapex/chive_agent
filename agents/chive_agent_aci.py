import json
import re
import requests
# import MySQLdb as mdb
# import sys
import time
import getpass

# ---- sort user info from bash script section  -------
# Get user provided information from bash script and parse it
# bash_user_info = sys.argv[1]

# bash_lst = (bash_user_info.split(','))
myapic_ip = raw_input('Enter your APIC IP Address:  ')
myapic_usr = raw_input('Enter your APIC Administrative Username:  ')
myapic_pwd = getpass.getpass('Enter APIC Apssword:  ')

# ---- connect to APIC section  -------
# Generate base login URl (myapic_ip variable defined by user via bash script)
base_url = 'http://' + myapic_ip + '/api/'

# Generate credentials structure
name_pwd = {'aaaUser': {'attributes': {'name': myapic_usr, 'pwd': myapic_pwd}}}
json_credentials = json.dumps(name_pwd)

# Generate login url
login_url = base_url + 'aaaLogin.json'
post_response = requests.post(login_url, data=json_credentials)

# Get token from login response structure
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']

# Create cookie array from token
cookies = {}
cookies['APIC-Cookie'] = auth_token

# ---- make REST API Call section  -------
try:
    while True:
        # Generate URL used for REST API call to get 5minute temperature data
        node_url = base_url + 'class/eqptTemp5min.json'

        get_nodes = requests.get(node_url, cookies=cookies, verify=False).json()

        rootNodeList = get_nodes["imdata"]

        # ---- parse data collected from REST API call section  -------
        # Create variables to be used to sort data
        dn_cnt = 0  # counter for dn attribute in rootNodeList
        device_lst = []  # list for device names
        curr_temp_lst = []  # list for tempature readings
        day_time_lst = []  # list for day/time of readings

        for device in rootNodeList:
            dn = device['eqptTemp5min']['attributes']['dn']  # find dn field
            curr_temp = device['eqptTemp5min']['attributes']['currentLast']  # current temp field
            day_time = device['eqptTemp5min']['attributes']['repIntvEnd']   # day/time field

            # change to ascii - type is now string
            dn_ascii = dn.encode("utf8")
            # change to ascii - type is now string
            curr_temp_ascii = curr_temp.encode("utf8")
            # change to ascii - type is now string
            day_time_ascii = day_time.encode("utf8")

            sensor = re.findall(r'sup/sensor-(.*?)/', dn_ascii)

            if '3' in sensor:  # Interested in only sensor-3
                # this will find ['node-x'] ex . topology/pod-1/node-101/sys/ch/supslot-1/sup/sensor-3/CDeqptTemp5min
                devname = re.findall(r'.*/.*/(.*?)/.*/.*/.*/.*./.*/.*', dn_ascii)
                dn_cnt += 1  # Add 1 to dn_cnt

                device_lst.append(devname)
                curr_temp_lst.append(curr_temp_ascii)
                day_time_lst.append(day_time_ascii)

        # Display to standard output for testing - visualize data exists
        i = 0
        print "----                 TABLE                   ----"
        print " Node                Temp               Day/Time "
        while i < dn_cnt:
            print device_lst[i], '       ', curr_temp_lst[i], '     ', day_time_lst[i]
            i += 1  # Add 1 to variable i
        time.sleep(60)
except KeyboardInterrupt:
    print('Manual break by user - CTRL-C')

# ---- mySQL section  -------

#con = mdb.connect('localhost', 'mydbuser', 'mydbpassword', 'mydatabase')

#with con:
#    cur = con.cursor()
#    cur.execute("DROP TABLE IF EXISTS aciTable")
#    cur.execute("CREATE TABLE aciTable(Id INT PRIMARY KEY AUTO_INCREMENT, \
#                Node_Name VARCHAR(25),Temp VARCHAR(25),Date_Time VARCHAR(50))")
#    x = 0
#    while x < dn_cnt:
#        cur.execute("INSERT INTO aciTable (Node_Name,Temp,Date_Time) VALUES(%s,%s,%s)",
#                    (device_lst[x], curr_temp_lst[x], day_time_lst[x]))
#        x += 1  # Add 1 to variable x

        # Fetch data
#    cur.execute("SELECT * FROM aciTable")

#    rows = cur.fetchall()

# Display to standard output for testing - visualize data exists in database
#   for row in rows:
#        print "This is from mySQL : ", row
