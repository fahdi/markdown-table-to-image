document.getElementById('markdown-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const markdown = document.getElementById('markdown-input').value;
    
    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({markdown: markdown}),
    })
    .then(response => response.json())
    .then(data => {
        const imageContainer = document.getElementById('image-container');
        imageContainer.innerHTML = `<img src="${data.image}" alt="Generated Table">`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});