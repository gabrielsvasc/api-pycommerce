CREATE TABLE user_type (
    type_id SERIAL,
    type_name TEXT NOT NULL,
    PRIMARY KEY (type_id, type_name)
);
