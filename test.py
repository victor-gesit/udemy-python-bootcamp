class Node():
    def __init__(self, value):
        self.value = value # Every node has a value that should be initialized when the node is created
        self.next = None # This is assigned a value later in the lifecycle of the node
        
    def loop_size(self):
        count = 0 # Counter to get the size of the loop
        node = self # The counting is done using an iteration that starts with the current loop
        found_values = [] # Hold the values of all nodes up to this point
        while node.next != None:
            if node.value in found_values:
                size = count - found_values.index(node.value)
                return size
            count += 1
            found_values.append(node.value)
            node = node.next
        else:
            print("This linked list has no loop")
            return -1
        