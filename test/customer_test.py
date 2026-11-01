from model.customer import Customer
from tools.validation import Validator
customer_1=Customer(1,"ali","alipour","09123726503")
customer_1.phone="09127777777"
print(customer_1)
print(customer_1.to_tuple())