echo "What is your APIC IP Address: "
read apic_ip
echo "What is your APIC Username: "
read apic_username
echo "What is you APIC Password: "
read -s apic_password
echo

if
docker run -ite APIC_IP=$apic_ip \
    -e APIC_USERNAME=$apic_username \
    -e APIC_PASSWORD=$apic_password \
    3pings/chive_agent:arm
