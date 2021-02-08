import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(
    __file__), 'northwind_small.sqlite3')

conn = sqlite3.connect(DB_FILEPATH)

c = conn.cursor()

expensive_items = c.execute(
    'select * from  Product order by UnitPrice DESC LIMIT 10').fetchall()

avg_hire_age = c.execute('select avg(AgeAtHiring) as avg_hire_age from'
                         '(select (HireDate - BirthDate) as AgeAtHiring \
                             from Employee)').fetchall()


avg_age_by_city = c.execute('select City,avg(AgeAtHiring) as avg_hire_age from'
                            ' (select City, (HireDate - BirthDate) as AgeAtHiring \
                                from Employee) group by City').fetchall()

ten_most_expensive = c.execute('select Product.ProductName, Product.UnitPrice, \
    Supplier.CompanyName from Product join Supplier on Product.SupplierId = \
        Supplier.Id order by Product.UnitPrice DESC LIMIT 10').fetchall()

largest_category = c.execute('SELECT Category.CategoryName, count(distinct'
                             ' Product.Id) as num_products  from Product'
                             ' join Category on Product.CategoryId = '
                             'Category.Id group by Product.CategoryId '
                             'order by num_products desc limit 1').fetchall()

most_territories = c.execute('select Employee.Id, Employee.FirstName, '
                             'Employee.LastName, count(EmployeeTerritory.'
                             'TerritoryId) as num_territories from '
                             'EmployeeTerritory join Employee on '
                             'EmployeeTerritory.EmployeeId  = Employee.Id '
                             'group by EmployeeTerritory.EmployeeId order by'
                             ' num_territories DESC limit 1').fetchall()
