from faker import Faker


class CheckoutAddressModel:
    FULL_NAME: str
    ADDRESS_LINE_1: str
    ADDRESS_LINE_2: str
    CITY: str
    STATE: str
    ZIP_CODE: str
    COUNTRY: str


class CheckoutPaymentModel:
    CARD_NUMBER: str
    EXPIRATION_DATE: str
    CVV: str
    CARDHOLDER_NAME: str


def generate_address() -> CheckoutAddressModel:
    """Generates a random checkout address using the Faker library."""
    faker = Faker(locale="pl_PL")
    checkout_address = CheckoutAddressModel()
    checkout_address.FULL_NAME = faker.name()
    checkout_address.ADDRESS_LINE_1 = faker.street_address()
    checkout_address.ADDRESS_LINE_2 = f"{faker.street_name()} Apt. {faker.building_number()}"
    checkout_address.CITY = faker.city()
    checkout_address.STATE = faker.administrative_unit()
    checkout_address.ZIP_CODE = faker.zipcode()
    checkout_address.COUNTRY = faker.country()
    return checkout_address


def generate_payment_info() -> CheckoutPaymentModel:
    """Generates random payment information using the Faker library."""
    faker = Faker()
    checkout_payment = CheckoutPaymentModel()
    checkout_payment.CARD_NUMBER = faker.credit_card_number(card_type="visa")
    checkout_payment.EXPIRATION_DATE = faker.credit_card_expire()
    checkout_payment.CVV = faker.credit_card_security_code()
    checkout_payment.CARDHOLDER_NAME = faker.name()
    return checkout_payment
