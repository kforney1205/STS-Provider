import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='STS', password='@dD12iT', host='20.65.96.229', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()
Connection established to: (
   'STS Rapid Consult Database',
)

#--------------------------------------------

import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='STS', password='@dD12iT', host='20.65.96.229', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO stsMain(runNumber, caseType, patientFirst, patientLast, gender, dob, patientEmail, patientPhone, mrnNumber, complaint) VALUES ('1234567', 'urgent', 'Jane', 'Doe', 'F', '12-05-1944', 'sample@mail.com', 7736067101, '00036484643', 'Here is some sample info')''')


# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()




#--------------------------------------------------------------
#|                                                             |
runNumber "char" NOT NULL
caseType "char" 
patientFirst "char"
patientLast "char"
gender "char"
dob "date"
patientEmail "char"
patienPhone "numeric"
mrnNumber "char"
complaint "char"
CONTSTRAINT "stsMain_pkey" PRIMARY KEY ("runNumber")