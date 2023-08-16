import requests


def get_area_names(pin_code):
    api_url = f"https://api.postalpincode.in/pincode/{pin_code}"
    response = requests.get(api_url)
    data = response.json()

    if data and data[0]['Status'] == 'Success':
        return [area['Name'].lower() for area in data[0]['PostOffice']]
    return []


def validate_address(address, pin_code):
    area_names = get_area_names(pin_code)

    for area_name in area_names:
        if area_name in address.lower():
            return True
    return False


# Test cases
test_cases = [
    ("2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka",
     "560050", True),
    ("2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka",
     "560050", True),
    ("374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore.", "560050", True),
    ("2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka",
     "560095", False),
    ("Colony, Bengaluru, Karnataka", "560050", False),
]

for address, pin_code, expected_result in test_cases:
    result = validate_address(address, pin_code)
    if result == expected_result:
        status = "Pass"
    else:
        status = "Fail"
    print(f"Address: {address}, PIN Code: {pin_code}, Expected: {expected_result}, Result: {result}, Status: {status}")
