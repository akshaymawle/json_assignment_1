import json

# Dictionary of Indian states and their capitals
indian_states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Delhi": "New Delhi",
    "Rajasthan": "Jaipur",
    "Uttar Pradesh": "Lucknow"
}

# Write the dictionary to a JSON file
with open('indian_states_and_capitals.json', 'w') as json_file:
    json.dump(indian_states_and_capitals, json_file, indent=4)

print("JSON file 'indian_states_and_capitals.json' created successfully.")
