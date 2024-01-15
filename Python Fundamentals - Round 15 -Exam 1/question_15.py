# Remove Duplicates From a List of Tuples : Make it unique List

ips_List = [

    ('192.168.0.15', 'y'),

    ('192.168.0.22', 'y'),

    ('192.168.0.14', 'y'),

    ('192.168.0.24', 'n'),

    ('192.168.0.15', 'y'),

    ('192.168.0.11', 'y')]

company_list_2 = []

for item in ips_List:
    if item not in company_list_2:
        company_list_2.append(item)


print(company_list_2)