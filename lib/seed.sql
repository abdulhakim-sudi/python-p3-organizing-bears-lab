DROP TABLE IF EXISTS bears;

CREATE TABLE bears (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    sex TEXT,
    color TEXT,
    temperament TEXT,
    alive BOOLEAN
);

-- Multicultural Bear Characters
INSERT INTO bears (name, age, sex, color, temperament, alive) VALUES
('Rupert', 10, 'M', 'brown', 'curious', 1),         -- UK
('Thanh', 6, 'F', 'white', 'gentle', 1),            -- Vietnam
('Ayaka', 5, 'F', 'black', 'elegant', 1),           -- Japan
('Amari', 7, 'M', 'gray', 'playful', 1),            -- Nigeria
('Luka', 9, 'M', 'cream', 'calm', 1),               -- Russia
('Inaya', 8, 'F', 'silver', 'wise', 1),             -- Morocco
('Mateo', 6, 'M', 'golden', 'friendly', 1),         -- Colombia
('Freja', 4, 'F', 'tan', 'brave', 1);               -- Sweden
