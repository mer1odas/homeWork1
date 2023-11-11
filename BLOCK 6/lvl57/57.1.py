def text(text : str):
    text = text.split()
    text.sort()
    text1 = ""
    for i in text:
        text1 = text1 + i + " "
    return text1

print(text("a b d a"))