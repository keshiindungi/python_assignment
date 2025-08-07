#Medication Dispensing -Last-In-First-Out (LIFO) for efficient medicine access
# Pharmacy Medication Stack
medication_stack = []

# Stock medications (newest on top)
medication_stack.append("Antibiotics")
medication_stack.append("Painkillers")
medication_stack.append("Insulin")
medication_stack.append("Centrizine")
medication_stack.append("Vitamins")
medication_stack.append("suppliments")
medication_stack.append("Antiacids")

print("Pharmacy Stock:", medication_stack)  

# Dispense medications
for _ in range(4):
    dispensed = medication_stack.pop()
    print(f"Dispensed: {dispensed} → Remaining: {medication_stack}")