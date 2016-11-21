FROM hypriot/rpi-python



ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "python", "./agents/chive_agent_aci.py" ]