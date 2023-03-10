import mysql.connector as mySQL
import dotenv
import os 

dotenv.load_dotenv()

db = mySQL.connect(
    host= "localhost",
    user= os.getenv("SQLUSER"),
    passwd= os.getenv("SQLPASS"),
    database= "testing"
)

cursor = db.cursor()

# cursor.execute("CREATE TABLE Contacts (email VARCHAR(50), firstname VARCHAR(50), lastname VARCHAR(50), contactID int PRIMARY KEY AUTO_INCREMENT)")

# cursor.execute("DESCRIBE Contacts")

# for x in cursor: 
#     print(x)

# cursor.execute("INSERT INTO Contacts (email, firstname, lastname) VALUES (%s, %s, %s)", ("beamhjcm@gmail.com", "ghajfgme", "aegww"))
# db.commit()

cursor.execute("SELECT email FROM Contacts ORDER BY email")

for x in cursor: 
    print(x)

