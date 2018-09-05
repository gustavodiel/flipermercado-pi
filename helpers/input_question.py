
def input_default(message, default):
    message_with_default = default and "{} (default: {})".format(message, str(default)) or message
    formated_message = "{:110} ".format(message_with_default)
    return input(formated_message) or default
