from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(DATABASE_URL)

# SQL statements as separate commands
MOCK_DATA = [
    """
    INSERT INTO resources (name, type, address, city, state, zip_code, latitude, longitude) VALUES
    ('Comfort Inn Downtown', 'hotel', '123 Main St', 'Portland', 'OR', '97201', 45.5155, -122.6789),
    ('Emergency Shelter A', 'shelter', '456 Oak Ave', 'Portland', 'OR', '97209', 45.5255, -122.6899),
    ('Family Haven Hotel', 'hotel', '789 Pine St', 'Vancouver', 'WA', '98660', 45.6272, -122.6744);
    """,
    """
    INSERT INTO resource_attributes (resource_id, key, value) VALUES
    (1, 'sleeps', '4'),
    (1, 'ada_compliant', 'true'),
    (1, 'pets_allowed', 'true'),
    (2, 'sleeps', '6'),
    (2, 'ada_compliant', 'true'),
    (2, 'meal_provided', 'true'),
    (3, 'sleeps', '5'),
    (3, 'ada_compliant', 'false'),
    (3, 'pets_allowed', 'true');
    """,
    """
    INSERT INTO inventory (resource_id, units_available) VALUES
    (1, 5),
    (2, 10),
    (3, 3);
    """,
    """
    INSERT INTO inventory_history (inventory_id, previous_units, new_units, change_type) VALUES
    (1, 6, 5, 'reservation'),
    (2, 12, 10, 'update'),
    (3, 4, 3, 'reservation');
    """
]

def insert_mock_data():
    with engine.connect() as conn:
        for statement in MOCK_DATA:
            conn.execute(text(statement))
        conn.commit()

if __name__ == "__main__":
    insert_mock_data() 