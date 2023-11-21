class Market:
    #private data member
    __database = {}

    #constructor of the class
    def __init__(self):
        pass

    # add method
    def add(self, data):

        self.__database.update( data )

    def search(self, key):
        pass

    def update(self, key, value):

        self.__database[key] = value

    def remove(self, key):

        self.__database.pop(key)

    #get the total of the amount
    def total(self):

        sum = 0
        for (key,value) in self.__database.items():
            sum += float(value)
        return sum

    # representation of the object
    def __repr__(self):
        out = ""
        for (key,value) in self.__database.items():
            out += str(key) + "\t\t: " + str(value) + "\n"
        return out

# main function
def main():
    print("Welcome to my MarketBase!")
    ob = Market()
    ob.add({"tomato":2})
    ob.add({"potato":1})
    ob.add({"rice":1})
    ob.add({"bread":1})
    ob.add({"yugart":1})
    print( ob )
    ch = 'n'
    while ch!="y":
        print("_"*14)
        print("MENU")
        print("ADD     1")
        print("DEL     2")
        print("UPDATE  3")
        print("Search  4")
        print("Total   5")
        print("_"*14)
        print( ob )
        if ch == '1':
            print("Add to Database:")
            key = input("Key = ")
            val = input("Value = ")
            ob.add({key:val})
        if ch == '5':
            print("Total = ", ob.total())
        if ch == '2':
            key = input("remove = ")
            ob.remove(key)
        if ch == '3':
           key = input("update key = ")
           value = input("value")
           ob.update(key,value)

        ch = input("Do you want to exit? (y/n)")
        print("Bye!")
main()
