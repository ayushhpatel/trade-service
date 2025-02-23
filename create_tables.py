from database import engine, Base
from models import Order

# Create the orders table (and any other defined tables)
Base.metadata.create_all(bind=engine)
