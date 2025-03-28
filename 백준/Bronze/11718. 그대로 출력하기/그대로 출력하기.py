while True:
    try:
        Text = input()
        print(Text)
    except EOFError:
        break