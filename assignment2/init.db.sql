CREATE TABLE IF NOT EXISTS tasks (
  id SERIAL PRIMARY KEY,
  task TEXT,
  is_completed BOOLEAN,
  notify TEXT
);