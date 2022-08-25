import pasword

def encode(password):
    password = password.encode()
    pas = pasword.sha256(password).hexdigest()
    return pas