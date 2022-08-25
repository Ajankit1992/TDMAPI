from faker import Faker


def TDMAPI(ssn):
    # Initialize faker
    fake = Faker('nl_NL')
    # Loop through range up to 100
    for val in range(100):
        print(f"Name: {fake.name()} phoneNumber: {fake.phone_number()}")
        return ssn


