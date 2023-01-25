class Order:

    def __init__(self, products):
        self.products = products

    def get_total_cost(self):
        pass


class PurchaseOrder(Order):

    def __init__(self, products, supplier):
        super().__init__(products)
        self.supplier = supplier

    def get_supplier(self):
        return


class SaleOrder(Order):

    def __init__(self, products, customer):
        super().__init__(products)
        self.customer = customer


def get_total_cost_for_orders(orders_list):
    if not all([isinstance(order, Order) for order in orders_list]):
        raise Exception('Only allowed for order')
    return sum([order.get_total_cost() for order in orders_list])


PurchaseOrder([], None)
