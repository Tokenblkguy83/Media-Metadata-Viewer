document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData();
    var fileInput = document.getElementById('fileInput');
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            displayMetadata(data.metadata);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function displayMetadata(metadata) {
    var metadataDisplay = document.getElementById('metadataDisplay');
    metadataDisplay.innerHTML = '<pre>' + JSON.stringify(metadata, null, 2) + '</pre>';
}
