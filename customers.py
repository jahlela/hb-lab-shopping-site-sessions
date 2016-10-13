"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password                 
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """ Return customer information from Customer object"""

        return "Customer: {} {}, Email: {}".format(self.first_name,self.last_name,
                                            self.email)    



def read_customer_info_from_file(filepath):
    """Read customer data and populate dictionary of customer info.

    Dictionary will be {email: Customer object}
    """

    customer_info = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customer_info[email] = Customer(first_name,
                                         last_name,
                                         email,
                                         password)
    return customer_info    



def get_by_email(email):
    """ Return a Customer object, given its email """

    return CUSTOMER_INFO[email]


CUSTOMER_INFO = read_customer_info_from_file('customers.txt')













