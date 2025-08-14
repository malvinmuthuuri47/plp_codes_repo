-- Task one solution
SELECT paymentDate, SUM(amount) from payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;

-- Task Two solution
SELECT customerName, country, AVG(creditLimit)
FROM customers
GROUP BY customerName, country;

-- Task Three solution
SELECT productCode, quantityOrdered, SUM(quantityOrdered * priceEach) as TotalPrice
FROM orderdetails
GROUP BY productCode, quantityOrdered;

-- Task Four solution
SELECT checkNumber, MAX(amount)
FROM payments
GROUP BY checkNumber;
