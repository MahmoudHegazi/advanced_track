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
