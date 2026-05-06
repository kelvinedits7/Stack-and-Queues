📚 Stack and Queue Implementation in Python
📌 Overview

This project demonstrates the implementation of two fundamental data structures in computer science: Stack and Queue using Python.

These structures are essential for understanding how data is stored, accessed, and managed in programs.

🧠 Concepts Covered
🔹 Stack (LIFO - Last In, First Out)

A stack follows the principle where the last element added is the first one to be removed.

Operations:

push() → Add an element to the stack
pop() → Remove the top element
peek() → View the top element
is_empty() → Check if the stack is empty
🔹 Queue (FIFO - First In, First Out)

A queue follows the principle where the first element added is the first one to be removed.

Operations:

enqueue() → Add an element to the queue
dequeue() → Remove the front element
peek() → View the front element
is_empty() → Check if the queue is empty
🛠️ Implementation Details
The stack is implemented using a Python list.
The queue is also implemented using a list (or optionally collections.deque for efficiency).
Basic operations are defined as methods inside classes.
📂 Project Structure
project-folder/
│
├── stack.py      # Stack implementation
├── queue.py      # Queue implementation
└── README.md     # Project documentation
▶️ How to Run
Make sure you have Python installed (Python 3.x recommended)
Clone or download the project
Run the files:
python stack.py
python queue.py
💻 Example Usage
# Stack Example
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # Output: 20

# Queue Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  # Output: 10
