class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def display_information(self):
        print(
            f"Supplier ID: {self.supplier_id} | "
            f"Name: {self.name} | "
            f"Contact Email: {self.contact_email}"
        )