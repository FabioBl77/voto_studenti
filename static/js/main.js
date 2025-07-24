// Funzione per nascondere i messaggi flash dopo 5 secondi
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    
    if (flashMessages.length > 0) {
        setTimeout(function() {
            flashMessages.forEach(function(message) {
                message.style.opacity = '0';
                setTimeout(function() {
                    message.style.display = 'none';
                }, 500);
            });
        }, 5000);
    }
    
    // Validazione del form di inserimento studenti
    const addStudentForm = document.querySelector('.add-student-form form');
    
    if (addStudentForm) {
        addStudentForm.addEventListener('submit', function(event) {
            const nomeStudente = document.getElementById('nome_studente').value.trim();
            const voto = document.getElementById('voto').value;
            
            if (nomeStudente === '') {
                event.preventDefault();
                alert('Inserisci il nome dello studente.');
                return;
            }
            
            if (voto === '' || isNaN(voto) || voto < 0 || voto > 10) {
                event.preventDefault();
                alert('Inserisci un voto valido tra 0 e 10.');
                return;
            }
        });
    }
});