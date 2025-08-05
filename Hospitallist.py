#Hospital Ward Management List - Ordered collections for patient beds
# Ward 4A Patient Beds (Ordered by proximity to nurses' station)
ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]

# New admission
ward_4a.append("Bed4: Aisha")
ward_4a.append("Bed5: keshii")
print("Ward 4A:", ward_4a)  

# Discharge patient
discharged = ward_4a.pop(1)
discharged = ward_4a.pop(3)
discharged = ward_4a.pop(2)
print(f"Discharged: {discharged} → Remaining: {ward_4a}")  
