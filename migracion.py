from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData

app = FastAPI()

# SQLAlchemy configuration
source_engine = create_engine('mysql://root:13960@localhost/primer')
destination_engine = create_engine('mysql://root:13960@localhost/prueba')

metadata = MetaData()

# Reflect the existing tables from the database
metadata.reflect(bind=source_engine)
metadata.reflect(bind=destination_engine)

# Define the source and destination tables
source_table = metadata.tables['users']
destination_table = metadata.tables['users']

@app.get("/migrate")
async def migrate_data():
    with source_engine.connect() as source_conn, destination_engine.begin() as destination_conn:
        # Select data from source table
        source_data = source_conn.execute(source_table.select()).fetchall()

        # Insert data into destination table
        for row in source_data:
            destination_conn.execute(
                destination_table.insert().values(
                    full_name=row[1],  # Usa el índice numérico en lugar del nombre de la columna
                    phone=row[2],      # Usa el índice numérico en lugar del nombre de la columna
                    password=row[3]    # Usa el índice numérico en lugar del nombre de la columna
                )
            )

    return {"message": "Data migration completed successfully"}
