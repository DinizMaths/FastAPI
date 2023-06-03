CREATE TABLE todos (
  id INTEGER NOT NULL,
  title VARCHAR,
  description VARCHAR,
  priority INTEGER,
  complete BOOLEAN,
  PRIMARY KEY (id)
);


INSERT INTO todos (title, description, priority, complete) 
VALUES ("Go to the store", "Pick up eggs", 5, 0);

INSERT INTO todos (title, description, priority, complete) 
VALUES ("Cut the lawn", "Grass is getting long", 3, 0);

INSERT INTO todos (title, description, priority, complete) 
VALUES ("Feed the dog", "He is getting hungry", 5, 0);