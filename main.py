import algorithms
import BinaryHeap
import BinarySearchTree
import BookStore
import Calculator
import DLList
import SLLStack
import SLLQueue


def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
               1 Assign variable and value for expression
               2 Introduce expression
               3 Show expression
               4 Evaluate expression
               0 Return to main menu
                """)
        option = input()
        expression = ""
        if option == "2":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression.")
            else:
                print(f"{expression} is an invalid expression")
        if option == "1":
            variable = str(input("Introduce the variable: "))
            value = float(input("Introduce the value: "))
            calculator.set_variable(variable, value)
        if option == "3":
            print(calculator.printExpression())
        if option == "4":
            print(f"{calculator.printExpression()} = {calculator.evaluate(expression)}")


def bookstoreSystemMenu():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
                b Search best selling books  
                s FIFO shopping cart
                m Best Selling Book
                r Random shopping cart
                v Reverse shopping cart
                1 Load book catalog
                2 Remove a book by index from catalog
                3 Add a book by index to shopping cart
                4 Remove from the shopping cart
                5 Search book by infix
                6 Search book by index
                7 Search sorted book titles by prefix
                8 MergeSort book catalog
                9 QuickSort book catalog
                10 Search prefix (Binary Search)
                11 Search prefix (Binary Search, Extra Credit, using DLList)
                12 Search using BFS2 up to k degree
                13 Check degree of separation using DFS2
                0 Return to main menu
                """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "b":
            print("Enter an infix: ")
            infix = input()
            print("How many books would you like to see?")
            num_of_books = input()
            while num_of_books.isnumeric() is False:
                num_of_books = int(input("Please enter a number: "))
            bookStore.bestSellingBooks(infix, num_of_books)
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "v":
            bookStore.printShoppingCart()
            bookStore.reverseShoppingCart()
            bookStore.printShoppingCart()
        elif option == "m":
            print(bookStore.getBestSellingBook())
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 15981)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option == "6":
            index = str(input("Enter the index of the book: "))
            bookStore.searchBookTitleIndex(index)
        elif option == "7":
            prefix = str(input("Enter the title of the book:"))
            bookStore.searchIndexSortedTitle(prefix)
        elif option == "8":
            algorithms.merge_sort(bookStore.bookSortedCatalog)
            print(f"merge_sort complete")
        elif option == "9":
            print(algorithms.quick_sort(bookStore.bookSortedCatalog))
            print(f"quick_sort complete")
        elif option == "10":
            prefix = str(input("Introduce the prefix to search: "))
            if len(prefix) is None:
                print(f"Can't search for an empty title.")
            else:
                bookStore.binarySearchByTitle(prefix)
        elif option == "11":
            prefix = str(input("Introduce the prefix to search: "))
            if len(prefix) is None:
                print(f"Can't search for an empty prefix.")
            else:
                bookStore.binarySearchByTitle2(prefix)
        elif option == "12":
            r1 = int(input("Enter the 1st index: "))
            r2 = int(input("Enter the 2nd index: "))
            bookStore.search_to_k_degree(r1, r2)
        elif option == "13":
            r1 = int(input("Enter the 1st index: "))
            r2 = int(input("Enter the 2nd index: "))
            bookStore.degree_of_separation(r1, r2)


def sllStackMenu():
    stack = SLLStack.SLLStack()
    option = ""
    while option != "0":
        print("""
                1 Add element to SLLStack
                2 Remove element from SLLStack
                3 Print SLLStack
                4 Reverse SLLStack
                0 Exit/Quit
                """)
        option = input()
        if option == "1":
            e = int(input("Enter an element to add to SLLStack: "))
            stack.push(e)
        elif option == "2":
            print(f"{stack.pop()} removed from SLLStack")
        elif option == "3":
            print(f"SLLStack: ", stack)
        elif option == "4":
            stack.reverse()


def dlListMenu():
    dlList = DLList.DLList()
    option = ""
    while option != "0":
        print("""
                1 Add element to DLList
                2 Remove element from DLList
                3 Print DLList
                4 Check Palindrome DLList
                0 Exit/Quit
                """)
        option = input()
        if option == "1":
            e = input("Enter an element to add to DLList: ")
            dlList.append(e)
        elif option == "2":
            i = int(input("Enter the index to remove the DLList: "))
            print(f"{dlList.remove(i)} at index {i} removed from DLList")
        elif option == "3":
            print(f"DLlist: ", dlList)
        elif option == "4":
            word = ""
            if dlList.isPalindrome():
                print(f"{word.join(dlList)} is palindrome")
            else:
                print(f"{word.join(dlList)} is not palindrome")


def sllQueueMenu():
    queue = SLLQueue.SLLQueue()
    option = ""
    while option != "0":
        print("""
                1 Add element to SLLQueue
                2 Remove element from SLLQueue
                3 Print SLLQueue
                4 Reverse SLLQueue
                0 Exit/Quit
                """)
        option = input()
        if option == "1":
            e = int(input("Enter an element to add to SLLQueue: "))
            queue.add(e)
        elif option == "2":
            print(f"{queue.remove()} removed from SLLQueue")
        elif option == "3":
            print(f"SLLQueue: ", queue)
        elif option == "4":
            queue.reverse()


def bstMenu():
    bst = BinarySearchTree.BinarySearchTree()
    # bt = BinaryTree.BinaryTree()
    option = ""
    while option != "0":
        print("""
                1 Add element 
                2 Remove element
                3 In-order
                4 Pre-order
                5 Post-order
                6 Bf Traversal
                7 Height
                0 Exit/Quit
                """)
        option = input()
        if option == "1":
            variable = input("Introduce the position as an integer: ")
            while variable.isdigit() is False:
                print("I said an integer, a number, not a decimal, not letters, not special characters. Try again.")
                variable = input()
            value = str(input("Introduce the value: "))
            if bst.add(variable, value):
                print(f"Successfully added: {variable} which was set to: {value}.")
        elif option == "2":
            key = input("Introduce the position: ")
            while key.isdigit() is False:
                print("A position is a digit. Please insert a digit, not a decimal, not letters or special chars.")
                key = input()
            print(f"Successfully removed {key}.")
        elif option == "3":
            print(f"In order traversal: {', '.join(map(str, bst.in_order(bst.r, [])))}")
        elif option == "4":
            print(f"Pre order traversal: {', '.join(map(str, bst.pre_order(bst.r, [])))}")
        elif option == "5":
            print(f"Post order traversal: {', '.join(map(str, bst.post_order(bst.r, [])))}")
        elif option == "6":
            print(f"Breadth first traversal: {', '.join(map(str, bst.bf_traverse()))}")
        elif option == "7":
            print(f"Height of tree: {bst.height()}")


def bhMenu():
    bh = BinaryHeap.BinaryHeap()
    option = ""
    while option != 0:
        print("""
                1 Add element
                2 Remove element
                3 Check size
                4 Print list
                0 Return to main menu
                """)
        option = input()
        if option == "1":
            print("Value of element to input:")
            choice = input()
            if bh.add(choice):
                print(f"Successfully added: {choice} to the binary heap")
            else:
                print(f"Could not add: {choice} to the binary heap. Try again.")
        elif option == "2":
            if bh.remove() is not False:
                print(f"Successfully removed {bh.remove()} from the Binary Heap")
            else:
                print(f"Could not remove element from binary heap. It might be empty")
        elif option == "3":
            print(f"Size of Binary Heap is: {bh.size()}")
        elif option == "4":
            print(bh)


def algorithmsMenu():
    algo = algorithms.algorithms()
    option = ""
    while option != 0:
        print("""
                1 merge_sort
                2 quick_sort
                3 binary_search
                0 Quit
                """)
        option = input()
        array = []
        if option == "1":
            ele = ""
            while ele != 0:
                ele = input("Add an element: ")
                array.append(ele)
            print(algo.merge_sort(array))
        elif option == "2":
            ele = ""
            while ele != 0:
                ele = input("Add an element: ")
                array.append(ele)
            print(algo.quick_sort(array))
        elif option == "3":
            ele = ""
            while ele != 0:
                ele = input("Add an element: ")
                array.append(ele)
            search = False
            while search.isdigit() is False:
                search = input("Enter the number you would like to search for in the array: ")
            algo.binary_search(algo.merge_sort(array), search)


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
                1 Bookstore System
                2 SLLQueue
                3 SLLStack
                4 DLList
                5 Calculator
                6 Binary/Binary Search Tree
                7 BinaryHeap
                8 Algorithms
                0 Exit/Quit
                """)
        option = input()
        if option == "1":
            bookstoreSystemMenu()
        elif option == "2":
            sllQueueMenu()
        elif option == "3":
            sllStackMenu()
        elif option == "4":
            dlListMenu()
        elif option == "5":
            menu_calculator()
        elif option == "6":
            bstMenu()
        elif option == "7":
            bhMenu()
        elif option == "8":
            algorithmsMenu()


if __name__ == "__main__":
    main()
