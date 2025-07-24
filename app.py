import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Funzione per ottenere una connessione al database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['SQLITE_DB_PATH'])
        g.db.row_factory = sqlite3.Row
    return g.db

# Funzione per chiudere la connessione al database
@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Funzione per inizializzare il database
def init_db():
    db = get_db()
    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Comando per inizializzare il database da riga di comando
@app.cli.command('init-db')
def init_db_command():
    init_db()
    print('Database inizializzato.')

# Verifica se il database esiste, altrimenti lo inizializza
def check_db_exists():
    if not os.path.exists(app.config['SQLITE_DB_PATH']):
        init_db()

# Verifica se l'utente è loggato
def is_logged_in():
    return 'user_id' in session

# Rotta per la pagina di login
@app.route('/', methods=['GET', 'POST'])
def login():
    # Se l'utente è già loggato, reindirizza alla dashboard
    if is_logged_in():
        return redirect(url_for('dashboard'))
    
    # Se la richiesta è POST, processa il form di login
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        
        # Cerca l'utente nel database
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        # Verifica se l'utente esiste e la password è corretta
        if user is None:
            error = 'Username non valido.'
        elif user['password'] != password:  # In produzione, usare check_password_hash
            error = 'Password non valida.'
        
        # Se non ci sono errori, salva l'ID utente nella sessione e reindirizza alla dashboard
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
        
        # Se ci sono errori, mostra un messaggio di errore
        flash(error)
    
    # Renderizza la pagina di login
    return render_template('login.html')

# Rotta per la dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Se l'utente non è loggato, reindirizza alla pagina di login
    if not is_logged_in():
        return redirect(url_for('login'))
    
    db = get_db()
    
    # Se la richiesta è POST, processa il form di inserimento
    if request.method == 'POST':
        nome_studente = request.form['nome_studente']
        voto = request.form['voto']
        error = None
        
        # Verifica se i campi sono stati compilati
        if not nome_studente:
            error = 'Nome studente richiesto.'
        elif not voto:
            error = 'Voto richiesto.'
        
        # Se non ci sono errori, inserisci i dati nel database
        if error is None:
            try:
                db.execute(
                    'INSERT INTO studenti_voti (nome_studente, voto) VALUES (?, ?)',
                    (nome_studente, voto)
                )
                db.commit()
                flash('Studente aggiunto con successo!')
            except db.IntegrityError:
                error = f"Errore nell'inserimento dei dati."
        
        # Se ci sono errori, mostra un messaggio di errore
        if error:
            flash(error)
    
    # Ottieni tutti gli studenti dal database
    studenti = db.execute('SELECT * FROM studenti_voti').fetchall()
    
    # Renderizza la dashboard con i dati degli studenti
    return render_template('dashboard.html', studenti=studenti)

# Rotta per il logout
@app.route('/logout')
def logout():
    # Rimuovi l'ID utente dalla sessione
    session.clear()
    return redirect(url_for('login'))

# Verifica se il database esiste all'avvio dell'applicazione
@app.before_first_request
def before_first_request():
    check_db_exists()

if __name__ == '__main__':
    app.run(debug=True)