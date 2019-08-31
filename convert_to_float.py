def convert(num):
    """
    Convert string number to float.
    """
    if len(num) == 0:
        return 0
    num = num.replace(",", ".")
    num = float(num)
    return num