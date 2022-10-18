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


def ping(picam_ip):
    # Configure subprocess to hide the console window
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    picam_status = []
    # For each IP address in the subnet, 
    # run the ping command with subprocess.popen interface
    for i in range(len(picam_ip)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(picam_ip[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
        
        if "Destination host unreachable" in output.decode('utf-8'):
            picam_status.append("Offline")
        elif "Request timed out" in output.decode('utf-8'):
            picam_status.append("Offline")
        else:
            picam_status.append("Online")
    return picam_status

print(ping(PICAM_IP))