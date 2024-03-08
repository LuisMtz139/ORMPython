from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData

app = FastAPI()

# SQLAlchemy configuration
source_engine = create_engine('mysql://root:13960@localhost/primer')
destination_engine = create_engine('mysql://root:13960@localhost/prueba')

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
