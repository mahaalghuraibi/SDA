class Node {
    constructor(data) {
        // a Node starts with a given data property
        // a Node also has a .next property initialized as null

        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        // a Linked List starts with a "head" property intialized as null
        this.head = null;
    }
    appendNode(data) {
        // creates a new node with the given data and adds it to back of the list
        const newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
            return;
        }

        let current = this.head;
        while (current.next) {
            current = current.next;
        }

        current.next = newNode;
    }
    prependNode(data) {
        // creates a new node with the given data and adds it to the front of the list
        const newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }

    pop() {
        // removes the last node from the list and returns it
        if (!this.head) return null;
        if (!this.head.next) {
            const out = this.head;
            this.head = null;
            return out;
        }
        let prev = null;
        let current = this.head;
        while (current.next) {
            prev = current;
            current = current.next;
        }
        prev.next = null;
        return current;

    }
    removeFromFront() {
        // remove the head node from the list and return it
        // the next node in the list is the new head node
        if (!this.head) return null;
        const out = this.head;
        this.head = this.head.next;
        return out;
    }
    insertAt(X, data) {
        // insert a new node into the list with the given data
        // place it after X nodes in the list
        // if X exceeds the bounds of the list, put the node at the end
        // insertAt(0, 7) would add the new node as the head
    }
    removeAt(X) {
        // remove the Xth node from the list, considering 0 to be the first node
        // return the node that has been removed
    }
    search(data) {
        // searches the list for a node with the given data
        // if it is found, return the "index" of the node, considering 0 to be the first node
        // if not, return false
    }
    sort() {
        // sort the Linked List in ascending order of data values
    }
}

module.exports = {
    Node,
    LinkedList
}