# -*- coding: utf-8 -*-
import requests
import json
import os
import time


# ---- sort user info from bash script section  -------
# Get user provided information from bash script and parse it


apic_ip = os.environ['APIC_IP']
apic_username = os.environ['APIC_USERNAME']
apic_password = os.environ['APIC_PASSWORD']
chive_app = os.environ['APP_PORT_5000_TCP_ADDR']


def connect_apic(apic_ip):
    # -- connect to APIC section  --
    # Generate base login URl
    # (myapic_ip variable defined by user via bash script)
    base_url = 'http://' + apic_ip + '/api/'
    return base_url


def login_apic(base_url, apic_username, apic_password):
    # Generate credentials structure
    name_pwd = {'aaaUser': {'attributes': {'name': apic_username, 'pwd': apic_password}}}
    json_credentials = json.dumps(name_pwd)

    # Generate login url
    login_url = base_url + 'aaaLogin.json'
    post_response = requests.post(login_url, data=json_credentials)
    return post_response


def get_token(post_response):
    # Get token from login response structure
    auth = json.loads(post_response.text)
    login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
    auth_token = login_attributes['token']

    # Create cookie array from token
    cookies = {}
    cookies['APIC-Cookie'] = auth_token
    return cookies


def call_api(base_url, cookies):
    # ---- make REST API Call section  -------

    # Generate URL used for REST API call to get 5minute temperature data
    # curly braces {} in string indicates a "replacement field"
    sensor_url = base_url + 'mo/{}/sys/ch/supslot-1/sup/sensor-2/CDeqptTemp5min.json'

    # Get all leaf information
    leaf_url = base_url + '/class/fabricNode.json?query-target-filter=and(eq(fabricNode.role,"leaf"))'
    leafs = requests.get(leaf_url, cookies=cookies, verify=False).json()['imdata']
    leaf_dns = []

    # for each of the objects returned by the API we will extract the dn
    for leaf in leafs:
        # this will return something like -
        # "topology/pod-1/node-101" - replaces curly braces {} in sensor_url
        dn = leaf['fabricNode']['attributes']['dn']
        leaf_dns.append(dn)

    # now we will run a query for the sensor of each node by it's dn
    for dn in leaf_dns:
        resp = requests.get(sensor_url.format(dn), cookies=cookies, verify=False).json()['imdata'][0]
        temp = resp['eqptTemp5min']['attributes']['currentMax']
        ts = resp['eqptTemp5min']['attributes']['repIntvEnd']

        # clean up dn - only save node name
        dn = dn.replace('topology/pod-1/', '')

        # temperature returned as string -
        # make it an int and assign condition
        int_temp = int(temp)

        if int_temp >= 60:         # temp is greater than 60 degrees C
            condition = "high"
        elif int_temp >= 48:       # temp between 48 and 60 degrees C
            condition = "elevated"
        else:                      # temp less than 48 degrees C
            condition = "normal"

        # take day/time returned and place into two separate variables
        date = ts.split('T')[0]    # date occurs before 'T' in  ts string
        time = ts.split('T')[1]    # time occurs after 'T' in  ts string
        time = time.split('.')[0]  # remove microseconds from time occurring after period

        obj = {"dn": dn, "attributes": {"temp": temp, "timestamp": time, "date": date, "condition": condition, "type": 'leaf'}}

        # send object to RESTAPI function
        upload = send2_RESTAPI(obj)

        # if upload:
        #    print "device successfully uploaded to api (L)"
        # else:
        #    print "error uploading device "

    # Get all spine information
    spine_url = base_url + '/class/fabricNode.json?query-target-filter=and(eq(fabricNode.role,"spine"))'
    spines = requests.get(spine_url, cookies=cookies, verify=False).json()['imdata']
    # print spines
    spine_dns = []
    # print spine_dns

    # for each of the objects returned by the API we will extract the dn
    for spine in spines:
        # this will return something like -
        # "topology/pod-1/node-101" - replaces curly braces {} in sensor_url
        dn = spine['fabricNode']['attributes']['dn']
        spine_dns.append(dn)

        # now we will run a query for the sensor of each node by it's dn
    for dn in spine_dns:
            resp = requests.get(sensor_url.format(dn), cookies=cookies, verify=False).json()['imdata'][0]
            temp = resp['eqptTemp5min']['attributes']['currentMax']
            ts = resp['eqptTemp5min']['attributes']['repIntvEnd']

            # clean up dn - only save node name
            dn = dn.replace('topology/pod-1/', '')

            # temperature returned as string -
            # make it an int and assign condition
            int_temp = int(temp)

            if int_temp >= 60:         # temp is greater than 60 degrees C
                condition = "high"
            elif int_temp >= 48:       # temp between 48 and 60 degrees C
                condition = "elevated"
            else:                      # temp less than 48 degrees C
                condition = "normal"

            # take day/time returned and place into two separate variables
            date = ts.split('T')[0]    # date occurs before 'T' in  ts string
            time = ts.split('T')[1]    # time occurs after 'T' in  ts string
            time = time.split('.')[0]  # remove microseconds from time occuring after period

            obj = {"dn": dn, "attributes": {"temp": temp, "timestamp": time, "date": date, "condition": condition, "type": 'spine'}}

            # send object to RESTAPI function
            # upload = send2_RESTAPI(obj)

            # if upload:
            #   print "device successfully uploaded to api (S)"
            # else:
            #    print "error uploading device "


def send2_RESTAPI(obj):
    # try to post a request - if web server is down just keep going
    try:
        while True:
            headers = {"Content-Type": "application/json"}
            rsp = requests.post('http://' + chive_app + '/device', headers=headers, data=json.dumps(obj))
            return rsp.ok
            # print(requests.post('http://127.0.0.1:5000/device', headers=headers, json=data))
    except:
        print "API microservice not running...keep getting data..."
        print
        pass

# run functions in a loop once every minute - until user issue break command
try:
    while True:
        base_url = connect_apic(apic_ip)
        post_response = login_apic(base_url, apic_username, apic_password)
        cookies = get_token(post_response)
        call_api(base_url, cookies)
        time.sleep(60)
# except KeyboardInterrupt:  # allow user to break loop
#    print("Manual break by user - CTRL-C")
