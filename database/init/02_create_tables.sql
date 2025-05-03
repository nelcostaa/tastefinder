CREATE TABLE
    IF NOT EXISTS tastefinder.restaurants (
        place_id VARCHAR PRIMARY KEY,
        name TEXT NOT NULL,
        latitude FLOAT8 NOT NULL,
        longitude FLOAT8 NOT NULL,
        rating REAL,
        price_level SMALLINT,
        user_ratings_total INT,
        address TEXT,
        types JSONB
    )
