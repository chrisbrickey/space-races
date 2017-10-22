def is_int(self, str):
    try:
        int(str)
        return True
    except ValueError:
        return False
