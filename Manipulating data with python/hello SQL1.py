from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
#con = engine.connect()

# Perform query: rs
#rs = con.execute('SELECT * FROM Album')

# Save results of the query to DataFrame: df
#df = pd.DataFrame(rs.fetchall())


# Open engine in context manager
# Perform query and save results to DataFrame: df

with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()



#Close connection
con.close()

#print out results
#print(len(df))
#print(df.head())


with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

#print(df.head())

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

#print(df.head())

#WTF you can actually do all the stuff above within one-line code...
df = pd.read_sql_query('SELECT * FROM Album', engine)
#print(df.head())

## the power of INNER JOIN
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID ')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()


print(df.head())


### WHAT I'VE LEARNED:
# relational database
# queries: SELECT, WHERE, JOIN
