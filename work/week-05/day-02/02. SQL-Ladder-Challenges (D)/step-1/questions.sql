-- this will allow us to connect to the database
-- this will format the information being printed in the console to make it easier.. try it without if you want!
\connect ladder  
\x off         

-- 1.1 Select the names of all the products in the store.
-- Your query goes here:
SELECT name
FROM products;

-- 1.2 Select the names and the prices of all the products in the store.
-- Your query goes here:
SELECT name , price
FROM Products;

-- 1.3 Select the name of the products with a price less than or equal to $200.
-- Your query goes here:
SELECT name, price
FROM products
WHERE price <= 200;

-- 1.4 Select all the products with a price between $60 and $120.
-- Your query goes here:
SELECT name, price
FROM products
WHERE price BETWEEN 60 AND 120;

-- 1.5 Select the name and price in cents (i.e., the price must be multiplied by 100).
-- Your query goes here:
SELECT name, price * 100 AS price_in_cents
FROM products;

-- 1.6 Compute the average price of all the products.
-- Your query goes here:
SELECT AVG(price) 
FROM products;


-- 1.7 Compute the average price of all products with manufacturer code equal to 2.
-- Your query goes here:
SELECT AVG(price) 
FROM products
WHERE manufacturer = 2;


-- 1.8 Compute the number of products with a price larger than or equal to $180.
-- Your query goes here:
SELECT COUNT(price)
FROM products
WHERE price >= 180;

-- 1.9 Select the name and price of all products with a price larger than or equal to $180, and sort first by price (in descending order), and then by name (in ascending order).
-- Your query goes here:
SELECT name, price
FROM products
WHERE price >= 180
ORDER BY price DESC, name ASC;

-- 1.10 Select all the data from the products, including all the data for each product's manufacturer.
-- Your query goes here:
SELECT *
FROM products
JOIN manufacturers
  ON products.manufacturer = manufacturers.code;


-- 1.11 Select the product name, price, and manufacturer name of all the products.
-- Your query goes here:
SELECT p.name AS product_name,
       p.price,
       m.name AS manufacturer_name
FROM products p
JOIN manufacturers m
  ON p.manufacturer = m.code;

-- 1.12 Select the average price of each manufacturer's products, showing only the manufacturer's code.
-- Your query goes here:
SELECT manufacturer, AVG(price)
FROM products
GROUP BY manufacturer;

-- 1.13 Select the average price of each manufacturer's products, showing the manufacturer's name.
-- Your query goes here:
SELECT manufacturers.name, AVG(products.price) AS avg_price
FROM products
JOIN manufacturers
ON products.manufacturer = manufacturers.code
GROUP BY manufacturers.name;

-- 1.14 Select the names of manufacturer whose products have an average price larger than or equal to $150.
-- Your query goes here:
SELECT m.name
FROM products p
JOIN manufacturers m
  ON p.manufacturer = m.code
GROUP BY m.name
HAVING AVG(p.price) >= 150;


-- 1.15 Select the name and price of the cheapest product.
-- Your query goes here:
SELECT name, price
FROM products
ORDER BY price ASC
LIMIT 1;


-- 1.16 Select the name of each manufacturer along with the name and price of its most expensive product.

SELECT m.name AS manufacturer,
       p.name AS product,
       p.price
FROM products p
JOIN manufacturers m
  ON p.manufacturer = m.code
WHERE p.price = (
    SELECT MAX(p2.price)
    FROM products p2
    WHERE p2.manufacturer = p.manufacturer
);

-- 1.17 Add a new product: Loudspeakers, $70, manufacturer 2.
-- Your query goes here:
INSERT INTO products (code, name, price, manufacturer)
VALUES (11, 'Loudspeakers', 70, 2);



-- 1.18 Update the name of product 8 to "Laser Printer".
-- Your query goes here:
UPDATE products
SET name = 'Laser Printer'
WHERE code = 8;



-- 1.19 Apply a 10% discount to all products.
-- Your query goes here:
UPDATE products
SET price = price * 0.9;



-- 1.20 Apply a 10% discount to all products with a price larger than or equal to $120.
-- Your query goes here:
UPDATE products
SET price = price * 0.9
WHERE price >= 120;


