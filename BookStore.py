import AdjacencyList
import algorithms
import ArrayList
import BinaryHeap
import BinarySearchTree
import Book
import ChainedHashTable
import DLList
import MaxQueue
import RandomQueue
import SLLQueue
# import SortableBook
import time


class BookStore:
    """
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    """

    def __init__(self):
        self.bookCatalog = None
        self.indexKeys = None
        self.shoppingCart = SLLQueue.SLLQueue()
        self.bestSellingBook = MaxQueue.MaxQueue()
        self.indexTitle = ChainedHashTable.ChainedHashTable()
        self.indexSortedTitle = BinarySearchTree.BinarySearchTree()
        self.bestSellers = BinaryHeap.BinaryHeap()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.bookSortedCatalog2 = DLList.DLList()
        self.similar_graph = None

    def loadCatalog(self, fileName: str):
        """
            loadCatalog: Read the file fileName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        """
        self.bookCatalog = ArrayList.ArrayList()
        self.indexKeys = ChainedHashTable.ChainedHashTable()
        with open(fileName, encoding='UTF-8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                # s = SortableBook.SortableBook(key, title, group, rank, similar)
                # self.bookSortedCatalog.append(s)
                # self.bookSortedCatalog2.append(s)
                # self.bookCatalog.append(b)
                # self.indexTitle.add(b.title, b)
                self.bookCatalog.append(b)
                self.indexKeys.add(b.key, i)
                i += 1
        self.similar_graph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        with open(fileName, encoding='UTF-8') as f:
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                l = similar.split()
                for k in range(1, len(l)):
                    j = self.indexKeys.find(l[k])
                    if j is not None:
                        self.similar_graph.add_edge(i, j)
                i += 1
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove)
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove)
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        """
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        """
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        """
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        """
        # Validating the index. Otherwise it  crashes
        if (i >= 0) or (i < self.bookCatalog.size()):
            start_time = time.time()
            ls = []
            s = self.bookCatalog.get(i)
            for j in range(self.bookCatalog.size()):
                ls.append(s)
                if len(ls) >= 0:
                    print("Which would you like to add: " + str(ls))
                    choice = input()
                    self.shoppingCart.add(choice)
                else:
                    self.shoppingCart.add(s)
            # add to bestSelling
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str):
        """
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        """
        start_time = time.time()
        elapsed_time = time.time() - start_time
        for i in range(self.bookCatalog.size()):
            if infix in self.bookCatalog.get(i).title:
                print(self.bookCatalog.get(i).key, self.bookCatalog.get(i).title)
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        """
        removeFromShoppingCart: remove one book from the shopping cart
        """
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def printShoppingCart(self):
        for i in range(self.bookCatalog.size() - 1):
            print(self.bookCatalog.get(i))

    def printBookCatalog(self):
        for i in range(self.bookCatalog.size() - 1):
            print(self.bookCatalog.get(i))

    def reverseShoppingCart(self):
        return self.shoppingCart.reverse()

    def getBestSellingBook(self):
        for i in range(self.bookCatalog.size()):
            s = self.bookCatalog.get(i)
            self.bestSellingBook.add(s)
        return self.bestSellingBook.max()

    def searchBookTitleIndex(self, title: str):
        hashmap = {}
        if title is None:
            print("Invalid input")
        else:
            for i in range(self.bookCatalog.size()):
                while self.indexTitle.find(int(title)):
                    hashmap[i].append(self.indexTitle.find(int(title)))
            if len(hashmap) is None:
                print("Book not found!")
            else:
                if len(hashmap) > 1:
                    for j in hashmap:
                        print(j, hashmap[j])
                    choice = int(input("Please enter the index number of the book you would like to add: "))
                    start_time = time.time()
                    self.shoppingCart.add(choice)
                    elapsed_time = time.time() - start_time
                    print(f"Added book {hashmap[choice]} by index in {elapsed_time} s")
                else:
                    start_time = time.time()
                    self.shoppingCart.add(hashmap.values())
                    elapsed_time = time.time() - start_time
                    print(f"Added book {hashmap.values()} by index in {elapsed_time} s")

    def searchIndexSortedTitle(self, prefix: str):
        bList = self.indexSortedTitle.bookStoreList(prefix)
        for i in range(len(bList) - 1):
            if len(bList) > 1:
                for ele in range(len(bList)):
                    print(f"Book: {ele}")
                choice = input("Which would you like to choose?")
                while choice.isdigit() is False:
                    print("Please input an index, an integer to choose the book you would like to choose.")
                    input()
                self.shoppingCart.add(choice)
            elif len(bList) == 0:
                print("No books with such prefix found.")
            else:
                print(f"Unique book: was found.")

    def bestSellingBooks(self, infix: str, k: int):
        for i in range(self.bookCatalog.size()):
            if infix in self.bookCatalog.get(i).title:
                self.bookCatalog.get(i).rank *= -1
                self.bestSellers.add(self.bookCatalog.get(i))
        for y in range(int(k)):
            x = self.bestSellers.remove()
            if x is False:
                break
            else:
                print(f"{x.rank * -1}: {x.title}")

    def binarySearchByTitle(self, title: str):
        titleCatalog = ArrayList.ArrayList()
        for i in range(self.bookSortedCatalog.size()):
            titleCatalog.append(self.bookSortedCatalog.get(i).title)
        sortedTitleCatalog = algorithms.merge_sort(titleCatalog)
        index = not None
        firstIndex = index
        j = 0
        while index is not None:
            index = algorithms.binary_search(sortedTitleCatalog, title)
            if j == 0:
                firstIndex = index
                j += 1
            if index is not None:
                print(f"{firstIndex}: {sortedTitleCatalog.get(index)}")
                sortedTitleCatalog.remove(index)
                firstIndex += 1
            else:
                print(f"Finished searching for title: {title}")

    def binarySearchByTitle2(self, title: str):
        titleCatalog = ArrayList.ArrayList()
        for i in range(self.bookSortedCatalog2.size()):
            titleCatalog.append(self.bookSortedCatalog2.get(i).title)
        sortedTitleCatalog = algorithms.merge_sort(titleCatalog)
        index = not None
        j = 0
        while index is not None:
            index = algorithms.binary_search(sortedTitleCatalog, title)
            if j == 0:
                firstIndex = index
                j += 1
                if index is not None:
                    print(f"{firstIndex}: {sortedTitleCatalog.get(index)}")
                    sortedTitleCatalog.remove(index)
                    firstIndex += 1
            else:
                print(f"Finished searching for title: {title}")

    def search_to_k_degree(self, r1: int, r2: int):
        books = self.similar_graph.bfs2(r1, r2)
        for i in range(0, len(books) - 1):
            print(self.bookCatalog.get(books[i]))

    def degree_of_separation(self, r1: int, r2: int):
        print(self.similar_graph.dfs2(r1, r2))
