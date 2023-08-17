const input = document.getElementById('autocomplete-input');
const results = document.getElementById('autocomplete-results');
const image = document.getElementById('display_image');
let timeout; 


input.addEventListener('input', () => {
    const prefix = input.value;
    image.src = "static/images/typing.gif";
    fetch(`/autocomplete?prefix=${prefix}`)
        .then(response => response.json())
        .then(data => {
            results.innerHTML = '';  // Clear previous results
            data.suggestions.forEach(suggestion => {
                const li = document.createElement('li');
                li.textContent = suggestion;
                results.appendChild(li);
            });
        });
    timeout = setTimeout(() => {
        image.src = "static/images/resting.gif";
    }, 5000);
});