from models.order import Order
import datetime

date1 = datetime.datetime(2023, 6, 13)
date2 = datetime.datetime(2017, 11, 17)
date3 = datetime.datetime(2017, 12, 31)
date4 = datetime.datetime(2019, 8, 16)




order1 = Order("Euan", date1, 1, "PDA")
order2 = Order("Will", date2, 5, "Polygondwanaland")
order3 = Order("Amy", date3, 10, "Gumboot Soup")
order4 = Order("Ellie", date4, 20, "Infest The Rats Nest")

orders = [order1,order2,order3,order4]