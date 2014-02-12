-- What customers are from the UK
SELECT * FROM customers WHERE country = 'UK'

-- What is the name of the customer who has the most orders?
SELECT customers.customername, COUNT(*) AS total_orders 
FROM orders 
LEFT JOIN customers ON orders.customerid = customers.customerid
GROUP BY orders.customerid 
ORDER BY total_orders DESC 
LIMIT 1

-- What supplier has the highest average product price?
SELECT suppliers.suppliername, avg(price) AS average_price 
FROM [Products] 
LEFT JOIN suppliers ON products.supplierid = suppliers.supplierid
GROUP BY products.supplierid
ORDER BY average_price DESC 
LIMIT 1

-- What category has the most orders?
SELECT categories.categoryname, count(*) AS total_orders 
FROM [OrderDetails] 
LEFT JOIN products ON orderdetails.productid = products.productid
LEFT JOIN categories ON products.categoryid = categories.categoryid
GROUP BY products.categoryid 
ORDER BY total_orders 
DESC LIMIT 1


-- What employee made the most sales (by number of sales)?
SELECT employees.employeeid, employees.firstname, employees.lastname, sum(orderdetails.quantity) AS total_orders
FROM orders 
LEFT JOIN employees ON orders.employeeid = employees.employeeid
LEFT JOIN orderdetails ON orderdetails.orderid = orders.orderid
GROUP BY employees.employeeid 
ORDER BY total_orders DESC LIMIT 1

-- What employee made the most sales (by value of sales)?
SELECT employees.employeeid, employees.firstname, employees.lastname, sum(products.price*orderdetails.quantity) AS total_sales 
FROM orderdetails 
LEFT JOIN products ON products.productid = orderdetails.productid 
LEFT JOIN orders ON orderdetails.orderid = orders.orderid
LEFT JOIN employees ON employees.employeeid = orders.employeeid
GROUP BY employees.employeeid
ORDER BY total_sales DESC LIMIT 1

			
-- What employees have BS degrees? (Hint: Look at LIKE operator)
SELECT * FROM employees WHERE notes LIKE '%BS%'

-- What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)
SELECT suppliers.suppliername, avg(price) AS average_price FROM [Products] 
LEFT JOIN suppliers ON products.supplierid = suppliers.supplierid
GROUP BY products.supplierid
HAVING COUNT(products.productid) >= 2
ORDER BY average_price DESC LIMIT 1


