def automate(auto, perform, done):

    if auto < (perform * done):
        print("Do it!")
    else:
        print("Not worth the time!")


automate(2400, 10, 240)
