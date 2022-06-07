carbon=float(input("Enter the number of carbon atoms:"))
hydrogen=float(input("Enter the number of hydrogen atoms:"))
oxygen=float(input("Enter the number of oxygen atoms:"))
carbon_weight=carbon*12.0107
hydrogen_weight=hydrogen*1.00794
oxygen_weight=oxygen*15.9994
molecular_weight=carbon_weight+hydrogen_weight+oxygen_weight
print("the molecular weight is:",molecular_weight)
