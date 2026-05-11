# 📚 Voto Studenti

Un'applicazione web per la gestione dei voti degli studenti. Consente ai docenti di autenticarsi e registrare/gestire i voti degli studenti tramite un'interfaccia web intuitiva.

## 🎯 Funzionalità

- **Autenticazione**: Sistema di login sicuro con username e password
- **Gestione Voti**: Aggiungere, visualizzare e gestire i voti degli studenti
- **Dashboard**: Interfaccia intuitiva per la visualizzazione dei dati
- **Database SQLite**: Persistenza dei dati in locale
- **Design Responsivo**: Interfaccia web moderna e user-friendly

## 🛠️ Tecnologie Utilizzate

- **Backend**: Python 3 con Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Sicurezza**: Hashing delle password con Werkzeug

## 📋 Requisiti di Sistema

- Python 3.8+
- pip (gestore pacchetti Python)

## 🚀 Installazione e Avvio

### 1. Installare le dipendenze
```bash
pip install -r requirements.txt
```

### 2. Inizializzare il database
```bash
python -m flask init-db
```
Oppure tramite lo script Python:
```bash
python init_db.py
```

### 3. Avviare l'applicazione
```bash
python app.py
```

L'applicazione sarà disponibile all'indirizzo: **http://localhost:5000**

## 📝 Credenziali di Default

- **Username**: `admin`
- **Password**: `password`

⚠️ **Nota**: Cambiare le credenziali di default prima di usare in produzione!

## 📂 Struttura del Progetto

```
voto_studenti/
├── app.py                 # Applicazione principale Flask
├── config.py              # Configurazione dell'app
├── database.db            # Database SQLite (creato al primo avvio)
├── init_db.py             # Script per inizializzare il database
├── requirements.txt       # Dipendenze Python
├── schema.sql             # Schema del database
├── static/                # File statici (CSS, JS, immagini)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # Template HTML
│   ├── login.html
│   ├── dashboard.html
│   └── base.html
└── README.md              # Questo file
```

## 📊 Schema del Database

### Tabella `users`
```
- id (PRIMARY KEY)
- username (UNIQUE)
- password (hashed)
```

### Tabella `studenti_voti`
```
- id (PRIMARY KEY)
- nome_studente
- voto
```

## 🔒 Sicurezza

- Le password sono hashate tramite Werkzeug
- Uso di sessioni Flask per l'autenticazione
- CSRF protection (raccomandato abilitare)

## 📌 Dati di Esempio

L'applicazione include alcuni dati di esempio:
- Mario Rossi - Voto: 8.5
- Giulia Bianchi - Voto: 9.0
- Luca Verdi - Voto: 7.5

## 🐛 Troubleshooting

### Port 5000 già in uso
```bash
python app.py --port 5001
```

### Errore con il database
Eliminare `database.db` e reinizializzare:
```bash
rm database.db
python init_db.py
```

## 📄 Licenza

Questo progetto è open source e disponibile sotto licenza MIT.

## 👤 Autore

**FabioBl77** - [GitHub](https://github.com/FabioBl77)

---

Per domande o suggerimenti, apri una issue su GitHub! 😊
