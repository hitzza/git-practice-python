'''
line_counter = 0
data_header = []
customer_list = []

with open("customers.csv") as customer_data:
    while True:
        data = customer_data.readline()
        if not data: break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer_list.append(data.split(","))
        line_counter += 1
print("Header : \t", data_header)
for i in range(0,10):
    print("Data", i, ": \t\t", customer_list[i])
print(len(customer_list))
'''
line_counter = 0
data_header = []
employee = []
customer_USA_only_list = []
customer = None

with open("customers.csv") as customer_data:
    while 1:
        data = customer_data.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer = data.split(",")
            if customer[10].upper() == "USA":#customer 데이터의 offset 10번째 값
                customer_USA_only_list.append(customer)#즉 country의 필드가 "USA"인 것만 customer_USA_only_list에 저장
        line_counter += 1
print("Header : \t", data_header)
for i in range(0,10):
    print("Data", i, ": \t\t", customer_USA_only_list[i])
print(len(customer_USA_only_list))

with open("customers_USA_only_list.csv", "w") as customers_USA_only_csv:
    for customer in customer_USA_only_list:
        customer_USA_only_list.write(",".join(customer).strip("\n")+"\n")
        #customer_USA_only_list에 있는 데이터를 customers_USA_only_csv파일에 쓰기