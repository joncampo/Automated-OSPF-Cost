import pandas as pd

from netmiko import ConnectHandler


def send_command(ip, username, password, interface):
    ssh_connection = ConnectHandler(
        device_type='cisco_ios',
        ip=ip,
        username=username,
        password=password)

    command=ssh_connection.send_config_set(['interface '+interface,'ip ospf cost 1000']) # for config commands

    print(command)

    verify = ssh_connection.send_command('show run | inc ospf') # for run commands

    print(verify)

    ssh_connection.disconnect()

    return verify



if __name__ == "__main__":

	df = pd.read_csv('ospf.csv', delimiter = ',', names = ['hostname','ip','interface'])

	total=len(df)

	num=0

	while num < total:

		try:
			print (df['hostname'][num]+" Starting!")

			excel_ip=df['ip'][num]
			print (excel_ip)
			excel_interface=df['interface'][num]
			print (excel_interface)

			command = send_command(
	            ip=excel_ip,
	            username="XXXXXXXXXX",  #device username
	            password="XXXXXXXXXX",  #device password
	            interface=excel_interface)
		

			print(command)
			print (df['hostname'][num]+" Success!")
			num=num+1

		except:
			print (df['hostname'][num]+" Failed!")
			num=num+1
			pass


