// Função para enviar solicitação POST para autenticação
function authenticateUser(email, password) {
    fetch('/auth', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email: email, password: password})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('authResult').innerText = 'Token: ' + data.token;
    })
    .catch(error => console.error('Error:', error));
}

// Manipulador de evento para enviar a solicitação POST quando o formulário for enviado
document.getElementById('authForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário padrão
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    authenticateUser(email, password);
});

// Função para fazer solicitação POST para fazer upload de foto
function uploadPhoto() {
    var photoFile = document.getElementById('photoFile').files[0];
    var token = document.getElementById('authResult').innerText.split(':')[1].trim();
    var formData = new FormData();
    formData.append('user_id', '123'); // User ID dummy
    formData.append('photo', photoFile);
    fetch('/upload_photo', {
        method: 'POST',
        headers: {
            'Authorization': 'Basic ' + btoa(token),
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('uploadResult').innerText = 'Photo: ' + data.photo.substring(0, 50) + '...';
    })
    .catch(error => console.error('Error:', error));
}

// Função para fazer solicitação GET para obter a contagem de fotos
function getPhotoCount() {
    var token = document.getElementById('authResult').innerText.split(':')[1].trim();
    fetch('/photo_count', {
        method: 'GET',
        headers: {
            'Authorization': 'Basic ' + btoa(token),
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('photoCount').innerText = 'Photo Count: ' + data.photo_count;
    })
    .catch(error => console.error('Error:', error));
}
