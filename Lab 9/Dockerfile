
FROM python:3.14.7-slim

WORKDIR /app

# Copy Product classes
COPY product.py .
COPY physical_product.py .
COPY digital_product.py .
COPY can_be_shipped.py .

# Copy new Lab 8 classes
COPY supplier.py .
COPY order.py .
COPY order_line.py .

# Copy Inventory and main application
COPY inventory.py .
COPY inventory_manager.py .

# Copy inventory data
COPY inventory.json .

# Start the application
CMD ["python", "inventory_manager.py"]
