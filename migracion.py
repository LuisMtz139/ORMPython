from fastapi import FastAPI, UploadFile, File
from sqlalchemy import create_engine, MetaData
import subprocess

app = FastAPI()

# SQLAlchemy 
source_engine = create_engine('mysql://root:13960@localhost/primer')
destination_engine = create_engine('mysql://root:Miller2001@localhost/prueba_uni')

metadata = MetaData()

metadata.reflect(bind=source_engine)
metadata.reflect(bind=destination_engine)

source_table = metadata.tables['people']
destination_table = metadata.tables['people']

@app.get("/migrate")
async def migrate_data():
    with source_engine.connect() as source_conn, destination_engine.begin() as destination_conn:
        source_data = source_conn.execute(source_table.select()).fetchall()

        for row in source_data:
            destination_conn.execute(
                destination_table.insert().values(
                    full_name=row[1],  
                    phone=row[2],    
                    password=row[3]    
                )
            )

    return {"message": "Data migration completed successfully"}

@app.post("/uploadsql")
async def upload_sql(file: UploadFile = File(...)):
    contents = await file.read()
    print(contents.decode()) 

    with open("temp.sql", "wb") as f:
        f.write(contents)

    command = f'"C:\\Program Files\\MySQL\\MySQL Server 5.7\\bin\\mysql.exe" -u root -p13960 prueba < temp.sql'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if error:
        return {"message": "Error occurred while migrating data", "error": error}

    metadata.reflect(bind=destination_engine)

    if 'people' not in metadata.tables:
        return {"message": "Table 'people' does not exist in the destination database"}

    destination_table = metadata.tables['people']

    source_columns = [column.name for column in source_table.columns]
    destination_columns = [column.name for column in destination_table.columns]

    if source_columns != destination_columns:
        return {"message": "The source and destination tables have different schemas"}

    with source_engine.connect() as source_conn, destination_engine.begin() as destination_conn:
        source_data = source_conn.execute(source_table.select()).fetchall()

        for row in source_data:
            destination_conn.execute(
                destination_table.insert().values(
                    full_name=row[1],  
                    phone=row[2],    
                    password=row[3]    
                )
            )

    return {"message": "Data migration completed successfully"}