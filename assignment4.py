# Use a stack or a queue (or both!) to determine if a given input is a palindrome or not.A palindrome is a sequence of characters that reads the same thing in both directions: Example of palindromes: “mom” “Neveroddoreven”

class Stack:
    def __init__(self):
        self.sequence = []

    def push(self, val):
        self.sequence.append(val)

    def pop(self):
        if len(self.sequence) == 0:
            return None
        return self.sequence.pop()

    def is_empty(self):
        return len(self.sequence) == 0


class Queue:
    def __init__(self):
        self.sequence = []

    def enqueue(self, val):
        self.sequence.append(val)

    def dequeue(self):
        if len(self.sequence) == 0:
            return None
        return self.sequence.pop(0)

    def is_empty(self):
        return len(self.sequence) == 0


seq = input("Enter a string to check if it's a palindromique sequence: ")


def is_palind(seq):
    seq = seq.replace(" ", "").lower()
    stack = Stack()
    queue = Queue()

    for i in seq:
        stack.push(i)
        queue.enqueue(i)

    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            return False
    return True


print(is_palind(seq))

# Use a stack or a queue (or both!) to determine if a given expression is balanced.The expression will contain a combination of these types of parenthesis: (), {}, or [] You have to make sure that for every opening parenthesis, there is a valid closing one.
# Ex:
# Input: (1+2)-3*[41+6} output: False
# Input: (1+2)-3*[41+6 output: False
# Input: (1+2)-3*]41+6[output: False
# Input: (1+[2-3]*4{41+6}) output: True


# You work for the MIB(men in black) and would like to decode the messages that they send you. The message contains alphabetical characters, white spaces, and Asterix. To decode the message, you need a stack. You start looping through the message pushing each alphabetical character and white space to your stack. Once you reach an Asterix, you pop one character out of your stack. Sometimes, you receive an incomplete message. Therefore, if you reach the end of the string and you still have characters in your stack, pop all of them out.
def decode_message(message):
    stack = []

    for char in message:
        if char == '*':
            if stack:
                stack.pop()
        else:
            stack.append(char)

    return ''.join(reversed(stack))


def decode_full_message(message):
    parts = message.split('*')
    result = []

    for part in parts:
        decoded_part = decode_message(part).strip()
        if decoded_part:
            result.append(decoded_part)

    return ' '.join(result)


message = "SIVLE ****** DAED TNSI ***"
decoded_message = decode_full_message(message)
print(decoded_message)

# Write deleteAtLocation function for a LL that takes as input an integer and deletes the node at that given location.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, position):
    temp = head
    prev = None
    if head is None:
        print("List is empty")
        return head
    if position == 1:
        head = temp.next
        return head
    for i in range(1, position-1):
        temp = temp.next
        if temp is None or temp.next is None:
            print("Data not present")
            return head
    temp.next = temp.next.next
    return head


def printList(head):
    while head:
        print(f'{head.data} ->', end=" ")
        head = head.next
    print("None")
