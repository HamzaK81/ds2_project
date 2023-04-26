# PROJECT GUI
# Script Author: Hamza Khurram

import tkinter as tk
import random
from tkinter import messagebox
from timeit import default_timer as timer
from datastructures.AVL import AVLTree, TreeNode
from datastructures.bst import Node
from datastructures.skiplist import SkipList, SkipNode

class ProjectGUI:


    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("700x300")
        self.root.title("Project GUI")

        self.titleLabel = tk.Label(text="Project GUI", font=('Arial', 16), padx=20, pady=20)
        self.titleLabel.pack()

        self.dropmenuFrame = tk.Frame(self.root)
        self.dropmenuFrame.columnconfigure(0, weight=1)
        self.dropmenuFrame.columnconfigure(1, weight=1)
        self.dropmenuFrame.columnconfigure(2, weight=1)

        self.optionsDS = [
            "            AVL            ",
            "     Binary Search Tree    ",
            "          Skiplist         "
        ]

        self.optionsOperations = [
            "          Search           ",
            "          Insert           ",
            "          Delete           "
        ]

        self.optionsNum = [
            "            10             ",
            "            100            ",
            "            1000           "
        ]

        self.clickedDS = tk.StringVar()
        self.clickedOperations = tk.StringVar()
        self.clickedNum = tk.StringVar()
        self.clickedDS.set("   Choose Data Structure   ")
        self.clickedOperations.set("     Choose Operation      ")
        self.clickedNum.set("Choose Number of Iterations")

        # Create dropdown menus
        self.dropDS = tk.OptionMenu(self.dropmenuFrame, self.clickedDS, *self.optionsDS)
        self.dropDS.grid(row=0, column=0, sticky=tk.W+tk.E, padx=20, pady=20)

        self.dropOperations = tk.OptionMenu(self.dropmenuFrame, self.clickedOperations, *self.optionsOperations)
        self.dropOperations.grid(row=0, column=1, sticky=tk.W + tk.E, padx=20, pady=20)

        self.dropNum = tk.OptionMenu(self.dropmenuFrame, self.clickedNum, *self.optionsNum)
        self.dropNum.grid(row=0, column=2, sticky=tk.W + tk.E, padx=20, pady=20)

        self.dropmenuFrame.pack()

        self.btn = tk.Button(self.root, text="Execute", command=self.buttonPress)
        self.btn.pack()

        self.root.mainloop()


    def buttonPress(self):

        chosenDS = self.clickedDS.get()
        chosenOperation = self.clickedOperations.get()
        chosenNum = self.clickedNum.get()


        # Ensure all relevant options have been chosen
        try:
            assert chosenNum != "Choose Number of Iterations"
            assert chosenDS != "   Choose Data Structure   "
            assert chosenOperation != "     Choose Operation      "

            chosenNum = int(chosenNum)

            start = end = 0

            # CHOSEN STRUCTURE = AVL
            if chosenDS == "            AVL            ":
                avl = AVLTree()
                root = TreeNode(50)
                # OPERATION = SEARCH
                if chosenOperation == "          Search           ":
                    start = timer()
                    for i in range(chosenNum):
                        avl.search(root=root, key=50)
                    end = timer()
                # OPERATION = INSERT
                if chosenOperation == "          Insert           ":
                    start = timer()
                    for i in range(chosenNum):
                        avl.insert_node(root, random.randint(0,100000))
                    end = timer()
                # OPERATION = DELETE
                if chosenOperation == "          Delete           ":
                    start = timer()
                    for i in range(chosenNum):
                        avl.delete_node(root, 50)
                    end = timer()

            # CHOSEN STRUCTURE = BINARY SEARCH TREE
            elif chosenDS == "     Binary Search Tree    ":
                bst = Node(50)
                # OPERATION = SEARCH
                if chosenOperation == "          Search           ":
                    start = timer()
                    for i in range(chosenNum):
                        bst.find(random.randint(1, 100000))
                    end = timer()
                # OPERATION = INSERT
                if chosenOperation == "          Insert           ":
                    start = timer()
                    for i in range(chosenNum):
                        bst.insert(random.randint(1, 100000))
                    end = timer()
                # OPERATION = DELETE
                if chosenOperation == "          Delete           ":
                    start = timer()
                    for i in range(chosenNum):
                        bst.delete(random.randint(1, 100000))
                    end = timer()

            # CHOSEN STRUCTURE = SKIPLIST
            elif chosenDS == "          Skiplist         ":
                skiplist = SkipList()
                # OPERATION = SEARCH
                if chosenOperation == "          Search           ":
                    start = timer()
                    for i in range(chosenNum):
                        skiplist.find(random.randint(1, 100000))
                    end = timer()
                # OPERATION = SEARCH
                if chosenOperation == "          Insert           ":
                    start = timer()
                    for i in range(chosenNum):
                        skiplist.insert(random.randint(1, 100000))
                    end = timer()
                # OPERATION = SEARCH
                if chosenOperation == "          Delete           ":
                    start = timer()
                    for i in range(chosenNum):
                        skiplist.remove(random.randint(1, 100000))
                    end = timer()


            time = end - start

            messagebox.showinfo(title="Output", message=f"Time Taken = {time} s")

        except AssertionError:
            messagebox.showwarning(title="Error", message="Please choose all the relevant options.")



ProjectGUI()
