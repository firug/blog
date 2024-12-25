window.addEventListener('beforeunload', function(event) {
    fetch("{% url 'unlock_article' article.id %}", {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    });
});