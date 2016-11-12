#! /bin/bash

echo
echo "###############################################"
echo "Thank you for using the CHIVE Demo Application."
echo "This script will install the chive agent aci app"
echo "###############################################"
echo
# commands to brind up docker container :  chive_agent_aci.py
# < STUFF HERE >


echo "Press Enter to continue..."
read confirm
echo

echo "Please enter the IP ADDRESS of your APIC : "
read myapic_ip

echo "Please enter the USERNAME for your APIC : "
read myapic_usr

echo "Please enter the PASSWORD of your APIC : "
read -s myapic_pwd

echo
echo "The IP address of your APIC is : ${myapic_ip}"
echo "The IP address of your APIC is : ${myapic_usr}"
echo
echo "Press Enter to continue..."
read confirm

python chive_agent_aci.py $myapic_ip,$myapic_usr,$myapic_pwd
#python -c "import chive-agent_aci1; chive-agent_aci1.apic_connect('$myapic_ip','$myapic_usr','$myapic_pwd')"

