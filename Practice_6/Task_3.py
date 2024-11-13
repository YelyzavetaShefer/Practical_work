list_of_names = ["John Doe", "Jane Smith", "Emily Johnson", "Michael Brown"]
list_of_initials = [name.split()[0][0] + name.split()[1][0] for name in list_of_names]
print(list_of_initials)