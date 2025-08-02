-- Task One solution
SELECT checkNumber, paymentDate, amount FROM payments;

-- Task Two solution
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- Task Three solution
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- Task Four solution
SELECT * FROM offices;

-- Task Five Solution
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
