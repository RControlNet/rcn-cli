def getInput(message, defaultValue):
    text = input(f"{message} ({defaultValue}): ")
    if text.strip() == "":
        return defaultValue
    else:
        return text
