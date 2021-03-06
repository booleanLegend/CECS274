Calculator 

The calculator exemplifies the use of Stacks, HashTables and BinaryTrees. It allows defining mathematical expressions
    with variables, assigning values to the variables and evaluating it.

BookStore

BookStore uses a fraction of the Amazon database to exemplify the use of several data structures
    such as Queues, Lists, HashTables, BinarySearch Trees, Heaps, Graphs and sorting. The program
    allows adding books to a shopping cart.

Installation

Install Python 3.8 or higher and numpy. A highly recommended IDE is PyCharm 
https://www.jetbrains.com/pycharm/.


The entry point (main program) is the file main.py. That is done using the 
    following lines:

if __name__ == "__main__":
    main()

To run the program in command line use:

% python3.8 main.py

In Pycharm you can use the options in the "run" tab.

The program will present the main menu with three options:
        1 Calculator
        2 Bookstore System
        0 Exit/Quit
Pressing 1 or 2 and the enter will take you to a second menu with different 
    options. The python function that allows to accept an input from the keyboard
    is input(). Use the same pattern to add new options accordingly.

The project is organized in different files (modules):
main.py: The main entry point of the program. It will present the menu that executes the assignments
Calculator.py: The calculator system to be done in Lab 1, lab 3 and Lab  4
BookStore.py: The book store system to be done during the semester
Book.py: Data class that holds the attributes of a book. The class allows to compare ranks using the operator < or >
SortableBook.py: Data class that holds the attributes of a book. The class allows to compare by alphabetical order using
    the operator < or >
Interfaces.py: The interfaces to be implemented during the semester: Stack, Queue, Deque, List, Set, Graph
ArrayStack.py: It will implement the interface Stack in lab 1
ArrayQueue.py: It will implement the interface Queue in lab 1
ArrayList.py: It will implement the interface List in lab 1
ArrayDeque.py: It implements the interface Deque. It is a specialization (Inheritance) of ArrayList
RandomQueue.py: It will implement the interface Queue. It is a specialization (Inheritance) of ArrayQueue
MaxQueue.py: It will implement the interface Queue. It is a specialization (Inheritance) of ArrayQueue. 
SLLStack.py: It will implement the interface Stack in lab 2
SLLQueue.py: It will implement the interface Queue in lab 2
DLList.py: It will implement the interface List in lab 2
DLLDeque.py: It implements the interface Deque. It is a specialization (Inheritance) of DLLList
ChainedHashTable.py: It will implement the interface USet in lab 3
BinarySearchTree.py: It will implement the interface Sorted Set in lab 4
BinaryHeap.py: It will implement the interface Queue in lab 5. It removes the element with highest priority
algorithms.py: It will implement the sorting algorithms in lab 6
AdjacencyList.py: It will implement the Graph interface in Lab 7 using the adjacency list
AdjacencyMatrix.py: It will implement the Graph interface in Lab 7 using the adjacency matrix
RedBlackTree.py: It will implement the interface Sorted Set in lab 8 using a balance tree.


Stack
    |- ArrayStack
    |- SLLStack     
Queue   
    |- ArrayQueue
            |- RandomQueue
            |- MaxQueue
    |- SLLQueue
    |- BinaryHeap
List                            Dequeue
    |- ArrayList                 |
                |-  ArrayDeque  -|
    |- DLList                    |
                |-   DLLDeque   -|
Set
    |- ChainedHashTable
    |- BinarySearchTree
Graph
    |- AdjacencyMatrix
    |- AdjacencyList

