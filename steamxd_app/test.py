# Import modules
import subprocess

PICAM1 = "192.168.1.23"
PICAM2 = "8.8.8.8"
PICAM3 = "192.168.1.23"
PICAM4 = "192.168.1.23"
PICAM5 = "192.168.1.23"
PICAM6 = "192.168.1.23"
PICAM7 = "192.168.1.23"
PICAM8 = "192.168.1.23"
PICAM9 = "192.168.1.23"
PICAM10 = "192.168.1.23"
PICAM_IP = [PICAM1, PICAM2, PICAM3, PICAM4, PICAM5, PICAM6, PICAM7, PICAM8, PICAM9, PICAM10]

import platform    # For getting the operating system name

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

print(ping("8.8.8.8"))
print(ping("192.168.1.23"))




