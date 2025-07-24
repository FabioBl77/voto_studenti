DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS studenti_voti;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE studenti_voti (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_studente TEXT NOT NULL,
  voto REAL NOT NULL
);

-- Inserimento di un utente di default per il test
INSERT INTO users (username, password) VALUES ('admin', 'password');

-- Inserimento di alcuni dati di esempio
INSERT INTO studenti_voti (nome_studente, voto) VALUES ('Mario Rossi', 8.5);
INSERT INTO studenti_voti (nome_studente, voto) VALUES ('Giulia Bianchi', 9.0);
INSERT INTO studenti_voti (nome_studente, voto) VALUES ('Luca Verdi', 7.5);