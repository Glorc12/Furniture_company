from .product import db as product_db, Product, ProductType, MaterialType
from .workshop import Workshop, ProductWorkshop

__all__ = ['Product', 'ProductType', 'MaterialType', 'Workshop', 'ProductWorkshop', 'product_db']
