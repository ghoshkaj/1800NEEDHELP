-- Wait and check if tables exist
DO $$
BEGIN
    -- Wait for migrations
    PERFORM pg_sleep(5);
    
    -- Check if tables exist
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'resources') THEN
        -- Insert resources (hotels/shelters)
        INSERT INTO resources (name, type, address, city, state, zip_code, latitude, longitude) VALUES
        ('Comfort Inn Downtown', 'hotel', '123 Main St', 'Portland', 'OR', '97201', 45.5155, -122.6789),
        ('Emergency Shelter A', 'shelter', '456 Oak Ave', 'Portland', 'OR', '97209', 45.5255, -122.6899),
        ('Family Haven Hotel', 'hotel', '789 Pine St', 'Vancouver', 'WA', '98660', 45.6272, -122.6744);

        -- Rest of the inserts...
    END IF;
END $$; 