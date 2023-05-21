import os
import get_k8s_client


##first get input from the xml files (will do this later) and put it into a list


def input():
    pass

##then use the list to start pushing kubectl commands to the cluster.
##list name is "input_list"

def kube():
    input_list = input().split()  # Split input by spaces to create a list of arguments
    if not input_list:  # Check if the list is empty
        print("All jobs have been scheduled")
        return

    while True:  # Infinite loop
        # Perform actions inside the loop
        for arg in input_list:
            os.system("kubectl create job job --image=(variable) --args=(variable)")
        # Check if the list is still empty
        if not input_list:
            print("All jobs have been scheduled")
            break

kube()

