# advanced_track

```python
class Product(db.Model):
  ...
  price = db.Column(db.Float, db.CheckConstraint('price>0'))

```
