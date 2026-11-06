FROM python:3.14.7-slim

WORKDIR /app

# Copy all required Python files and inventory data
COPY product.py .
COPY can_be_shipped.py .
COPY physical_product.py .
COPY digital_product.py .
COPY inventory.py .
COPY inventory_manager.py .
COPY inventory.json .

# Run the inventory management system
CMD ["python", "inventory_manager.py"]
