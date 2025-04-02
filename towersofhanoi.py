def towers_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Towers of Hanoi problem.

    Parameters:
    n (int): Number of disks
    source (str): The name of the source rod
    target (str): The name of the target rod
    auxiliary (str): The name of the auxiliary rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    towers_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks from auxiliary to target
    towers_of_hanoi(n - 1, auxiliary, target, source)

# Example usage
if __name__ == "__main__":
    num_disks = 3  # Change this value for more disks
    towers_of_hanoi(num_disks, "A", "C", "B")

    
    