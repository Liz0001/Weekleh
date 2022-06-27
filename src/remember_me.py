"""Remember the user for next time."""


def remember_user(email, pwd):
    """Save the data."""
    with open("src/remember_me.txt", "w") as remember_user:
        remember_user.write(email)
        remember_user.write("\n")
        remember_user.write(pwd)


def check_if_user_remembered():
    """."""
    try:
        with open("src/remember_me.txt", "r") as remembered:
            is_remembered = remembered.readline()
    except Exception as err:
        return False
    if not is_remembered == "":
        return True
    else:
        return False

def get_name_pwd():
    """."""
    email = ""
    password = ""
    try:
        with open("src/remember_me.txt", "r") as remembered_yes:
            email = remembered_yes.readline()
            password = remembered_yes.readline()
            email = email.rstrip('\n')
    except Exception as err:
        return False
    
    return email, password


def forget_me():
    """Forget the user."""
    try:
        with open("src/remember_me.txt", "w") as forget_user:
            forget_user.write("")
    except Exception as err:
        pass
        