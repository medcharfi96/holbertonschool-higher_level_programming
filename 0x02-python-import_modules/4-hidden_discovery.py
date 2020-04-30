#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for tes in dir(hidden_4):
        if tes[0:2] != "__":
            print("{}".format(tes))
