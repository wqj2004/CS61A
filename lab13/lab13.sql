.read data.sql


CREATE TABLE average_prices AS
  SELECT category, sum(MSRP)/count(*) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) from inventory group by item;


CREATE TABLE shopping_list AS
  SELECT name, store from products,lowest_prices where name = item group by category having min(MSRP/rating) order by name ;


CREATE TABLE total_bandwidth AS
  SELECT sum(b.Mbs) from shopping_list as a, stores as b where a.store = b.store;

