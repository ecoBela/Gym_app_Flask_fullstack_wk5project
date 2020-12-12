DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS members;


CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) 
);

CREATE TABLE activities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    upcoming BOOLEAN
);
CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE
);
