import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'northwind_small.sqlite3')

conn = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", conn)

c = conn.cursor()

expensive_items = list(zip(*(c.execute('select ProductName from  Product order by UnitPrice DESC LIMIT 10').fetchall())))[0]

print(f'{expensive_items = }')

avg_hire_age = c.execute('select avg(AgeAtHiring) as avg_hire_age from (select (HireDate - BirthDate) as AgeAtHiring from Employee)').fetchone()[0]

print(f'{avg_hire_age = }')

avg_age_by_city = c.execute('select City, avg(AgeAtHiring) as avg_hire_age from (select City, (HireDate - BirthDate) as AgeAtHiring from Employee) group by City').fetchall()

print(f'{avg_age_by_city = }')

ten_most_expensive = c.execute('select Product.ProductName, Supplier.CompanyName from  Product join Supplier on Product.SupplierId = Supplier.Id order by Product.UnitPrice DESC LIMIT 10').fetchall()

print(f'{ten_most_expensive = }')

largest_category = c.execute('SELECT Category.CategoryName, count(distinct  Product.Id) as num_products  from Product join Category on Product.CategoryId = Category.Id group by Product.CategoryId order by num_products desc').fetchone()[0]

print(f'{largest_category = }')

most_territories = ' '.join(c.execute('select Employee.FirstName, Employee.LastName, count(EmployeeTerritory.TerritoryId) as num_territories from EmployeeTerritory join Employee on EmployeeTerritory.EmployeeId  = Employee.Id group by EmployeeTerritory.EmployeeId order by num_territories DESC').fetchone()[:2])

print(f'{most_territories = }')