import random
import string


def generate_random():
    """Generate random string"""
    length = random.randint(1, 10)
    random_symbols = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return random_symbols


def generate_random_email():
    """Generate random valid email"""
    characters = string.ascii_lowercase + string.digits
    name = ''.join(random.choice(characters) for _ in range(random.randint(1, 10)))
    dom = ''.join(random.choice(characters) for _ in range(3))
    email = f"{name}@{dom}.{dom}"
    return email


valid_user = {'login': 'qa.ajax.app.automation@gmail.com', 'password': 'qa_automation_password'}
