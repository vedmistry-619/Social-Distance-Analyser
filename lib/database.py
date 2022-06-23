# importing modules
import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Database():
    """ Connects to Database
        Foreign Key Check=ON
        Key Arguments : None
    """
    def __init__(self):
        # Create a db or connect to one
        self.conn = sqlite3.connect("lib\Database.db")

        # Enabling foreign key constraints
        self.conn.execute("PRAGMA foreign_keys = 1")

        # Create cursor
        self.c = self.conn.cursor()
        
    ####=====================METHODS=========================####
            
    #======================== CATEGORY TABLE =====================================#

    def create_category_table(self):
        with self.conn:
            self.c.execute("""CREATE TABLE category (
                cat_name TEXT PRIMARY KEY  NOT NULL
            )""")
    
    def insert_category(self, cat_name):
        """Insert Category value in Database
        Key Arguments: cat_name -- String
        """
        with self.conn:
            self.c.execute("INSERT INTO category (cat_name) VALUES (?)", (cat_name,))
    
    def update_cateory(self, new_cat_name, old_cat_name):
        """Update Category name in Database
        Key Arguments: new_cat_name -- String
                       old_cat_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE category SET cat_name = ? WHERE cat_name = ?", (new_cat_name, old_cat_name))

    def delete_category(self, cat_name):
        """Delete Category value in Database
        Key Arguments: cat_name -- String
         """
        with self.conn:
            self.c.execute("DELETE FROM category WHERE cat_name = ?", (cat_name,))
    
    def get_category(self):
        """Fetches all Category name from Database
        Key Arguments: None
         """
        with self.conn:
            self.c.execute("SELECT * FROM category")
            result = self.c.fetchall()
            # print(result)
            return result
    
    #======================== SUB-CATEGORY TABLE =====================================#

    def create_sub_category_table(self):
        with self.conn:
            self.c.execute("""CREATE TABLE sub_category (
                sub_cat_name TEXT PRIMARY KEY  NOT NULL,
                cat_name TEXT NOT NULL,
                FOREIGN KEY(cat_name) REFERENCES category(cat_name)
            )""")
    
    def insert_sub_category(self, sub_cat_name, cat_name):
        """Insert Sub-Category value in Database
        Key Arguments: sub_cat_name -- String
                    cat_name -- String
        """
        with self.conn:
            self.c.execute("INSERT INTO sub_category VALUES (?,?)", (sub_cat_name, cat_name,))
    
    def update_sub_cateory(self, new_subcat_name, old_subcat_name):
        """Update Sub-Category name in Database
        Key Arguments: new_subcat_name -- String
                       old_subcat_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE sub_category SET sub_cat_name = ? WHERE sub_cat_name = ?", (new_subcat_name, old_subcat_name))

    def delete_sub_category(self, sub_cat_name):
        """Delete Category value in Database
        Key Arguments: cat_name -- String
         """
        with self.conn:
            self.c.execute("DELETE FROM sub_category WHERE sub_cat_name = ?", (sub_cat_name,))

    def get_sub_category(self, category_name):
        """Fetches all Category name from Database
        Key Arguments: category_name -- String
         """
        with self.conn:
            self.c.execute("SELECT * FROM sub_category WHERE cat_name LIKE (?)",(category_name,))
            result = self.c.fetchall()
            # print(result)
            return result

   #======================== PRODUCT TABLE =====================================#

    def create_product_table(self):
       with self.conn:
           self.c.execute("""CREATE TABLE product (
               prod_name TEXT PRIMARY KEY  NOT NULL,
               prod_price REAL  NOT NULL,
               prod_quantity INTEGER  NOT NULL,
               sub_cat_name TEXT  NOT NULL,
               cat_name TEXT NOT NULL,
               FOREIGN KEY(sub_cat_name) REFERENCES sub_category(sub_cat_name)
               FOREIGN KEY(cat_name) REFERENCES category(cat_name)
           )""")

    def insert_product(self, prod_name, prod_price, prod_quantity, sub_cat_name, cat_name):
        """Insert Product value in Database
        Key Arguments: prod_name -- String,
                        prod_price -- Float, prod_quantity -- Int,
                        sub_cat_name--String, cat_name--String.
        """
        with self.conn:
            self.c.execute("""INSERT INTO product (
                prod_name, prod_price, prod_quantity, sub_cat_name, cat_name)
                VALUES (?,?,?,?,?)""", (prod_name, prod_price, prod_quantity, sub_cat_name, cat_name))

    def update_product_price(self, prod_price, prod_name):
        """Update Product price in Database
        Key Arguments: prod_price -- Float
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_price = ? WHERE prod_name = ?", (prod_price, prod_name))

    def update_product_quantity(self, prod_quantity, prod_name):
        """Update Product price in Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_quantity=? WHERE prod_name=?", (prod_quantity, prod_name))

    # Add Amount from Backup Product Table
    def update_add_product_quantity(self, add_prod_quantity, prod_name):
        """Add Product Quantity in Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_quantity = prod_quantity + ? WHERE prod_name=?", (add_prod_quantity, prod_name))

    # Minus Amount from Backup Product Table
    def update_deduct_product_quantity(self, deduct_prod_quantity, prod_name):
        """Deduct/Minus Product Quantity in Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_quantity = prod_quantity - ? WHERE prod_name=?", (deduct_prod_quantity, prod_name))    

    # Delete product from Product table            
    def delete_product(self, prod_name):
        """Delete Product value in Database
        Key Arguments: prod_name -- String
        """
        with self.conn:
            self.c.execute("DELETE FROM product WHERE prod_name = (?)",(prod_name,))
    
    def get_products(self, sub_category_name):
        """Fetches set/group of Product values which has a common Sub-Category
        Key Arguments: sub_category_name -- String
        """
        with self.conn:
            self.c.execute("SELECT * FROM product WHERE sub_cat_name=(?)",(sub_category_name,))
            result = self.c.fetchall()
            return result
    
    def get_product_details(self, prod_name):
        """Fetches all Product info/values of a single product.
        Key Arguments: prod_name -- String
        """
        with self.conn:
            self.c.execute("SELECT * FROM product WHERE prod_name LIKE (?)",(prod_name,))
            result = self.c.fetchall()
            return result



   ############################################################################################################################################

    def drop_table(self, table_name):
        """Drops given table from the Database.
        Key Arguments: table_name -- String
        """
        with self.conn:
            self.c.execute(f"DROP TABLE {table_name}")




if __name__ == "__main__":
    
    db_obj = Database()
    
   