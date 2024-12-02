from netmiko import ConnectHandler
#les informations de connexion
router = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22 
}

#connexion au router
conn = ConnectHandler(**router)
#afffiche l'heure
clock = conn.send_command("show clock")
print(clock)
#afficher les interfaces
interface = conn.send_command("sh ip int br")
with open("interfaces.txt", "w") as file:
    file.write(interface)
print('interfaces.txt') 
#configuration une interface loopback avec ip address 
commands = {
    "interface loopback 8",
    "ip address 10.8.8.8 255.255.255.240",
    "no shutdown"
}
configuration = conn.send_config_set(commands)
print(configuration)
