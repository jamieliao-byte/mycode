#!/usr/bin/env python3`

def test1():
    # create the string hostname
    hostname = "MTG"
    # test logic with the `if` statement
    # what to do if this statement is found to be true
    if hostname == "MTG":
        print("The hostname was found to be mtg")

def test2():
    #!/usr/bin/env python3
    hostname = input("What value should we set for hostname?")
    if hostname == "MTG":
        print("The hostname was found to be mtg")

def test3():
    ## Collect input from user
    hostname = input("What value should we set for hostname?")
    
    ## use the lower method to test if input value matches expected value
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    ## Always print out to the user
        print("Exiting the script")


def main():
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()
