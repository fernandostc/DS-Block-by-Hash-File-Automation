import json
import getpass

from dsp3.models.manager import Manager

#Interactive ask information to dont use the hardcode information
tenant_info = str(input("Tenant: "))
user_info = str(input("Username: "))
password_info = getpass.getpass("Password: ")
host_info = str(input("DSM Hostname or IP (if you are using DSaaS just Press Enter): "))

if (host_info == None):
	dsm = Manager(tenant=tenant_info,username=user_info, password=password_info) #DSaaS example
else:
	port_info = str(input("DSM port: "))
	if (tenant_info == None):
		dsm = Manager(username=user_info, password=password_info, host=host_info, port=port_info)   #On Prem DSM Example
	else:
		dsm = Manager(tenant=tenant_info, username=user_info, password=password_info, host=host_info, port=port_info) #On Prem DSM Example with Tenant enable


#You could hard code the tenant, user and password if you would like, following example:
#dsm = Manager(tenant="tenant",username="user", password="password")

print ("\n" * 100)

case = 0

while (case != 6):
	print ("##########################################################################################################################" + '\n')
	print ("Welcome to Deep Security Security Automation tool for Global Trusted Hash Files" + '\n')
	print ("Following below the actions allowed today from this tool:" + '\n')
	print('1 - Add Hashes through TEXT file')
	print('2 - Search by Hash')
	print('3 - Delete File Hash by hash')
	print('4 - Delete File Hash by text file')
	print('5 - List File Hash')
	print('6 - Close the session' + '\n')
	print ("##########################################################################################################################" + '\n')
	case = int(input("Please enter with one option: "))


	if (case == 1):
		with open('add_file_hash.txt') as f:
   			hashes = f.readlines()	
		for info in hashes:
			info = info.split('\0')[0].strip()
			print (info)
			hash,description = info.split(' - ')
			detail = json.dumps(dsm.add_block_by_hash_rule(hash, description))
			message = json.loads(detail)
			print (message)
			print ('\n')
		
		input("Press Enter to continue...")
		print ("\n" * 100)
		
		case = 0

	elif case == 2:
		data = dsm.list_block_by_hash_rules()
		data = data['DescribeGlobalRulesetResponse']['ruleset']['rules']
		hash = str(input("Pleas enter the hash that you would like to search: "))
		for into in data:
			if (into['sha256']) == hash:
				print ('\n' + "RULE ALREADY EXIST WITH THIS SHA 265")
				print ("Rule ID: " + str(into['ruleID']))
				print ("SHA 265: " + into['sha256'])
				print ("Description: " + into['description'])
				print ("Action: " + into['action'] + '\n')
		
		input("Press Enter to continue...")
		print ("\n" * 100)
		
		case = 0

	elif case == 3:
		hash = str(input("Pleas enter the hash that you would like to delete: "))
		data = dsm.list_block_by_hash_rules()
		data = data['DescribeGlobalRulesetResponse']['ruleset']['rules']
		for into in data:
			if (into['sha256']) == hash:
				ruleid = into['ruleID']
				dsm.delete_block_by_hash_rule(ruleid)
				print ("The hash was deleted with successful")
		
		input("Press Enter to continue...")
		print ("\n" * 100)
		
		case = 0

	elif case == 4:
		with open('delete_file_hash.txt') as f:
   			hashes = f.readlines()
		for hash in hashes:
			hash = hash.split(' - ')[0].strip()
			data = dsm.list_block_by_hash_rules()
			data = data['DescribeGlobalRulesetResponse']['ruleset']['rules']
			for into in data:
				if (into['sha256']) == hash:
					print (hash)
					ruleid = into['ruleID']
					dsm.delete_block_by_hash_rule(ruleid)
					print ("The hash was deleted with successful" + '\n')
		
		input("Press Enter to continue...")
		print ("\n" * 100)
		
		case = 0


	elif case == 5:
		parsed = dsm.list_block_by_hash_rules()
		print (json.dumps(parsed, indent=4, sort_keys=True))
		print ('\n')
		
		input("Press Enter to continue...")
		print ("\n" * 100)
		
		case = 0
	
	elif case == 6:
		print ("Thank you! We will close the session with Deep Security." + '\n')
		dsm.end_session()
		exit
