
class PurchaseOrder():
    def __init__(self, orderNumber = 0, poNumber="", purchaseDate = “”):
        self.orderNumber = int #  used as the index, incremented for each order
        self.poNumber = str # could be a mix of letters and numbers, or just numbers.
        self.purchaseDate = datetime.datetime # this is just Gregorian and doesn’t take into account other time systems, maybe the system could be configured elsewhere

class CustomerDetails():
    def __init__(self, customerName ="", companyName = “”, address=””, phone=””, emailAddress = “”):
        self.customerName = str # name of the customer
        self.companyName = str # name of the company (optional)
        self.address = str # could be different from delivery address, but the form doesn’t specify
        self.phone = str  #  String with validation, its not doing calculations
        self.emailAddress - str # needs validation on entry

class OrderItem():
    def __init__(self, productCode = “”, quantity = “”, , unitPrice = “” , productDescription = “”):
        self.productCode = str # product code, amy be a mix of numbers and letters
        self.productDescription = str # product description
        self.quantity - int # number of items ordered
        self.UnitPrice - float # unit price at time of purchase

class purchaseOrder();
    def __init__(self, PONumber, Date, CustomerNumber , formItems):

        """
        Inputs:
        CustomerNumber
        PONumber = BO4476
        Date = 28/03/2026
        formItems (an array of )
        """

        # add the purchase order details to the data structure
        PurchaseOrder(orderNumber = 0, poNumber="", purchaseDate = “”)
        # add the customer details to to the purchase order
        CustomerDetails(customerName ="", companyName = “”, address=””, phone=””, emailAddress = “”)
        # loop through the items and add them to the purchase
        # it should be a list of lists as

        self.items = []

        foreach itemNumber in formItems
            item.add(OrderItem(itemNumber))

        # count the number of items and calculate the postage

        self.PostageHandling =  # calculated just on the number of items
                                     # really it should be by size.

        self.GST  = 15 # fixed amount

        # loop through the items and calculate the total amount
        self.orderTotal = calculateTotal() # total for the order (before GST)
        # multiply by GST amount for the GST amount.
        self.GSTwithTotal = calculateGST() # total for the order (after GST)


    def calculateTotal():
        # loop through the items, add the cost up
        totalCost =int
        foreach purchase in items:
            totalCost = UnitPrice + item.UnitPrice
        return totalCost

    def calculateGST():
        return self.totalCost * self.GST

    # add a new item to the order
    def addItem():
        self.items.append(OrderItem)

     # Retrieve how many items we have in the list
    def length(self):
        return len(self.items)

	# Retrieve an item at a specific index
    def get(self, index):
        return self.items[index]

	def remove(self, index):
        return self.items.pop(index)

CustomerOrder()

# ** Purchase Order
PONumber = BO4476
Date = 28/03/2026

# ** Customer Name
Name: John Doe
Company Name: The Milkmen
Address: Some mall
         Somewhere
Phone: 5655565
Email Address jdoe@evelyn.co.zn

Product Code    Product Desc.   Quantity    Unit Price  Amount
145245






