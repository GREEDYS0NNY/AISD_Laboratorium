"""Lista jednokierunkowa"""


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


temp = Node(93)
print(temp.getData())
print(temp.getNext())


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def merge(self, item1, item2):
        item1 = sorted(item1)
        item2 = sorted(item2)
        return sorted(item1 + item2)

    def addSort(self, lista, item):
        if not lista:
            lista.append(item)
            return lista
        index = 0
        while index < len(lista) and item > lista[index]:
            index += 1
        lista.insert(index, item)

        return lista


myList = UnorderedList()
myList.add(12)
myList.add(122)
myList.add(43)
myList.add(1)
myList.add(-32)

print(myList.size())
print(myList.search(-32))
print(myList.search(-132))

myList.remove(1)
print(myList.search(1))

print(myList.merge([1, 24, 12, 45, -9], [-2, -3, 123, 14, 59]))
print(myList.addSort([1,4,2,34,2], 3))