# chive_agent
Cisco Heat Indication Visualization Explorer Agent

# Background
High temperatures are the enemy of network equipment. This application leverages the Application Policy Infrastructure Controller (APIC) REST APIs, to gather near near real-time  operating temperature of both spine and leaf switches in the Cisco Application Centric Infrastructure (ACI) fabric.


This application was developed based on microservice architecture and is wrapped in a Docker container.

One image is designed so that it can be deployed on a ARM (Raspberry Pi) device, another image exists that can be deployed on an x86 device. 

# Diagram

Inline-style: 
![alt text]( https://github.com/imapex/chive_agent/blob/master/diagrams/CHIVE_AGENT.gif "CHIVE_AGENT")

