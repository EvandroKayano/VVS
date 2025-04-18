import re

def validate(email):
    if not email or not isinstance(email, str):
        return False

    if len(email) > 320 or email.count('@') != 1:
        return False

    local_part, domain = email.split('@')

    if not local_part:
        return False
    
    if not domain:
        return False
    
    if len(local_part) > 64 or len(domain) > 255:
        return False

    # Local part rules
    if '..' in local_part or local_part.endswith('.') or ' ' in local_part:
        return False

    # Domain part rules
    domain_labels = domain.split('.')
    if any(len(label) > 63 for label in domain_labels):
        return False

    # Use a safe regex to confirm valid characters and structure
    local_pattern = r'^[A-Za-z0-9!#$%&\'*+/=?^_`{|}~.-]+$'
    domain_pattern = r'^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not re.match(local_pattern, local_part):
        return False

    if not re.match(domain_pattern, domain):
        return False

    return True