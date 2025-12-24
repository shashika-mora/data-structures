# 🏗️ Data Structures: From Scratch to Systems

> **"What I cannot create, I do not understand."** — Richard Feynman

Welcome to the **Data Structures Masterclass**. This repository is not just a collection of code snippets; it is a curriculum designed to take you from a basic Python user to a **Systems Engineer** who understands how software really works under the hood.

We build every data structure **from scratch** (no `import queue` cheat codes) to understand the memory management, pointers, and algorithmic trade-offs that define high-performance computing.

---

## 📚 The Curriculum

The course is divided into 11 modules, each focusing on a core structure used in modern production systems.

### **Phase 1: The Core (Memory & Linear Structures)**
*   **[0. Core Data Structures](./0.%20Core%20Data%20Structures.ipynb)**: The "why" and "how" of memory management. Start here.
*   **[1. Arrays](./1.%20Arrays/1.%20%20Arrays.ipynb)**: Contiguous memory, CPU caching, and the reality of hardware.
*   **[2. Linked Lists](./2.%20Linked%20Lists/2.%20Linked%20Lists.ipynb)**: Nodes, pointers, and dynamic memory allocation.
*   **[3. Stacks](./3.%20Stacks/3.%20Stacks.ipynb)**: LIFO logic, the CPU Call Stack, and backtracking.
*   **[4. Queues](./4.%20Queues/4.%20Queues.ipynb)**: FIFO logic, task scheduling, and breadth-first exploration.

### **Phase 2: The Fast & The Flexible (Hashing & Scaling)**
*   **[5. Hash Tables](./5.%20Hash%20Tables/5.%20Hash%20Tables.ipynb)**: The $O(1)$ magic behind Dictionaries and Database Indexing.
*   **[8. Hashing](./8.%20Hashing/8.%20Hashing.ipynb)**: Deep dive into Hash Functions, Collisions, and Security.
*   **[11. Disjoint Sets](./11.%20Disjoint%20Sets/11.%20Disjoint%20Sets.ipynb)**: Union-Find algorithms for network connectivity.

### **Phase 3: Hierarchical Structures (Trees & Graphs)**
*   **[6. Trees](./6.%20Trees/6.%20Trees.ipynb)**: Hierarchical data, Recursion, and the DOM.
*   **[9. Heaps](./9.%20Heaps/9.%20Heaps.ipynb)**: Priority Queues, Binary Heaps, and Task Schedulers.
*   **[10. Tries](./10.%20Tries/10.%20Tries.ipynb)**: Prefix Trees, Autocomplete, and IP Routing.
*   **[7. Graph Algorithms](./7.%20Graph%20Algorithms/7.%20Graph%20Algorithms.ipynb)**: BFS, DFS, Shortest Paths, and Social Networks.

---

## 📂 Repository Structure

Each module is organized into its own folder containing the core **Notebook** and dedicated folders for implementation code.

```text
/
├── 0. Core Data Structures.ipynb  <-- Main Index / Start Here
├── 1. Arrays/
│   ├── 1. Arrays.ipynb           <-- The Lesson
│   ├── python/                   <-- Practice your Python implementation here
│   └── cpp/                      <-- Practice your C++ implementation here
...
└── 11. Disjoint Sets/
```

---

## 🚀 How to Use This Repo

1.  **Start with Notebook 0:** Open `0. Core Data Structures.ipynb`. It links to everything else.
2.  **Read & Run:** Open a module (e.g., `1. Arrays.ipynb`). Read the theory, run the code cells, and understand the mental models.
3.  **Solve the Mini-Challenge:** Each notebook ends with a "Mini-Challenge" (e.g., designing a Printer Spooler).
4.  **Implement It:** Go to the `python/` or `cpp/` folder for that module and try to build the data structure as a standalone class file without looking at the notebook.

---

## 🌟 Real-World System Map

Throughout this course, we answer the question: **"Where is this used in real life?"**

| Structure | Real-World Application |
| :--- | :--- |
| **Array** | Image Processing (Pixels), Stock Tickers |
| **Linked List** | Spotify Playlist, Blockchain Transaction Chains |
| **Stack** | Undo/Redo Buttons, Browser History, CPU Call Stack |
| **Queue** | Printer Jobs, Web Server Request Handling |
| **Hash Table** | Caching (Redis), Database Indexing |
| **Set** | Unique User Tracking, Firewall Rules |
| **Tree** | File Systems, HTML DOM, JSON |
| **Graph** | GPS Navigation, Social Networks, Internet Routing |
| **Heap** | Task Schedulers (Linux Kernel), Bandwidth Management |
| **Trie** | Autocomplete (Google Search), Spell Checkers |

---

Happy Coding! 🚀
