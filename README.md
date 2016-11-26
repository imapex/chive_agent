# C H I V E   Agent Service
Cisco Heat Indication Visualization Explorer Agent

This is the Agent microservice service for the CHIVE application

# Background
High temperatures are the enemy of network equipment. The traditional approach of setting thresholds and relying on SNMP traps to alert on environmental changes is very reactive. 
This application leverages the Application Policy Infrastructure Controller (APIC) REST APIs to continuously gather near real-time operating temperatures of both spine and leaf switches in the Cisco Application Centric Infrastructure (ACI) fabric. 
The data that is collected is then displayed on a webpage. The eventual goal of the project is to create a data center "heatmap" to show hotspots on the data center floor.

Devices are categorized into three conditions HIGH, ELEVATED and NORMAL. Each condition is defined by a temperature range and is assigned a color

* (1) HIGH     -  red   - the device has exceeded safe operating temperatures 
* (2) ELEVATED - yellow - device temperature had gone above normal temperature range
* (3) NORMAL   - green  - device is operating within expected temperature range

# Application Details
This application will was developed based on microservice architecture and is wrapped in a Docker container.

One image is designed so that it can be deployed on a ARM (Raspberry Pi) device. Another image exists that can be deployed on an x86 device. The user is able to choose the image at installation time. 

The application invokes an API GET request by sending an HTTP/1.1 GET message to the Application Policy Infrastructure Controller (APIC). The HTML body of the response message from the APIC controller contains a Javascript Object Notation (JSON) structure that contains the requested temperature data.
Once the data that was received is parsed, the JSON structured data is sent to the **chive_app** microservice ,running in the MANTL environment, via an API POST request. 

The HTML body of the POST message is JSON.

# Diagram

REST API Flow: 
![chive_agent Flow]( https://github.com/clintmann/chive_agent/blob/master/diagrams/CHIVE_flow.gif "CHIVE_flow")

# Installation

Prerequisites

* Python 2.7+


# Preparing the Raspberry Pi to run Docker
First we will install a Raspberry Pi compatible Docker Image with a minimal `Busybox httpd` web server. Once the Raspberry Pi is setup to run Docker containers we will download the CHIVE agent ARM container. 

Thank you [Hypriot](http://blog.hypriot.com/about/) for full instructions below. 

[Preparing the Raspberry Pi to run Docker](http://blog.hypriot.com/getting-started-with-docker-on-your-arm-device/)
[Getting started with Docker on your ARM device](http://blog.hypriot.com/getting-started-with-docker-on-your-arm-device/)

Type the following command into the terminal of your Raspberry Pi:

    docker run -d -p 80:80 hypriot/rpi-busybox-httpd

This will download and start the Docker image hypriot/rpi-busybox-httpd which contains a tiny webserver. 
 You can check if your container is running by typing

    docker ps

You should see the container you just started in the container list.


Now we are ready to download and start the CHIVE agent Docker image. To do this type in the following commands. 


    .....command here ....


## Downloading

< ENTER INFORMATION HERE >

## Basic Usage

In order to run, the service needs 4 pieces of information to be provided:

   * APIC Controller Address
   * Username for APIC Controller
   * Password for APIC Controller
   * DNS name of CHIVE REST API (chive_app microservice)

This information is gathered as raw input when the application is run
 < SHOW SCREEN SHOT OF QUESTIONS HERE >
 
 


 the CPU architecture here is ARM rather than x86/x64 by Intel or AMD. Thus, Docker-based apps you use have to be packaged specifically for ARM architecture! Docker-based apps packaged for x86/x64 will not work 
 
