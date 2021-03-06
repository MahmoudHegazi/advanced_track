# advanced_track

```python
class Product(db.Model):
  ...
  price = db.Column(db.Float, db.CheckConstraint('price>0'))

```


## new relation

```python
invoice_item = Table('invoice_item', metadata,
    Column('item_id', Integer, primary_key=True),
    Column('item_name', String(60), nullable=False),
    Column('invoice_id', Integer, nullable=False),
    Column('ref_num', Integer, nullable=False),
    ForeignKeyConstraint(['invoice_id', 'ref_num'], ['invoice.invoice_id', 'invoice.ref_num'])
)

```


# Inner Join
Let’s say we wanted to get a list of those customers who placed an order and the details of the order they placed. This would be a perfect fit for an inner join, since an inner join returns records at the intersection of the two tables.
```SQL
select first_name, last_name, order_date, order_amount
from customers c
inner join orders o
on c.customer_id = o.customer_id
```

# Left Join
If we wanted to simply append information about orders to our customers table, regardless of whether a customer placed an order or not, we would use a left join. A left join returns all records from table A and any matching records from table B.

```SQL
select first_name, last_name, order_date, order_amount
from customers c
left join orders o
on c.customer_id = o.customer_id
```


###### So why would this be useful? By simply adding a “where order_date is NULL” line to our SQL query, it returns a list of all customers who have not placed an order:

```SQL
select first_name, last_name, order_date, order_amount
from customers c
left join orders o
on c.customer_id = o.customer_id
where order_date is NULL
```

# Right Join (good to handle the deleted records)
Right join is a mirror version of the left join and allows to get a list of all orders, appended with customer information.

select first_name, last_name, order_date, order_amount
from customers c
right join orders o
on c.customer_id = o.customer_id



# Full Join
Finally, for a list of all records from both tables, we can use a full join.

select first_name, last_name, order_date, order_amount
from customers c
full join orders o
on c.customer_id = o.customer_id


first_name |	last_name |	order_date |	order_amount
--- | --- | --- | ---
George |	Washington |	07/04/1776 |	$234.56
Thomas |	Jefferson |	03/14/1760 |	$78.50
John |	Adams |	05/23/1784 |	$124.00
Thomas |	Jefferson |	09/03/1790 |	$65.50
NULL |	NULL |	07/21/1795 |	$25.50
NULL |	 |NULL	11/27/1787	$14.40
James |	Madison |	NULL |	NULL
James |	Monroe |	NULL |	NULL
