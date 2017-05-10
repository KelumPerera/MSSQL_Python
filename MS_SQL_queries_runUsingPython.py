# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:23:29 2017

@author: Kelum Perera
"""

import pandas as pd
import pyodbc                             # if not installed, run in command line3, pip install pyodbc


# Parameters
server = 'DESKTOP-9999999\SQLEXPRESS'      # chnage to your server name
db = 'mydatabase'                          # change to your batabase to be queried

# Create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')

# query db( Enter your SQL query)
sql = """

SELECT *
FROM mytable

"""
df = pd.read_sql(sql, conn)              # SQL query result will read into to pandas dataframe

df.head()                                # View top 5 records of dataframe
df.info()                                # View column details