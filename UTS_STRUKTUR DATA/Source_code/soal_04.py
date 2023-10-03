class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")
    
    def is_empty(self):
        return len(self.items) == 0 

#contoh penggunaan
    def print_stack(self):
        #mencetak isi stack dari atas ke bawah
        for item in reversed(self.items):
            print(item)
#membuat objek stack
my_stack = Stack()

#menambahkan beberapa elemen ke dalam stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.pop()

print("Isi Stack : ")
my_stack.print_stack()