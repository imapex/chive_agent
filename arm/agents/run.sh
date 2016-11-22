#!/usr/bin/env bash
echo "Enter your APIC IP Address: "
read apic_ip
echo "Enter your APIC Username: "
read apic_username
echo "Enter your APIC Password: "
read -s apic_password
echo "Enter your CHIVE APP IP Address or DNS Name:  "
read chive_app

docker run -ite APIC_IP=$apic_ip \
    -e APIC_USERNAME=$apic_username \
    -e APIC_PASSWORD=$apic_password \
    -e CHIVE_APP=$chive_app \
    3pings/chive_agent:arm
