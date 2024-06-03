def create_operation(operation):
    if operation == 'add':
        def add(num_1, num_2):
            return num_1 + num_2
        return add
    elif operation == 'subtract':
        def subtract(num_1, num_2):
            return num_1 - num_2
        return subtract
