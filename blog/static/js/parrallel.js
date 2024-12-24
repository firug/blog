tinymce.init({
    selector: '#editor',
    plugins: 'collaboration',
    toolbar: 'undo redo | bold italic',
    collaboration: {
        channel: 'unique-channel-name', // Уникальный канал для каждой статьи
        apiKey: 'your-api-key', // Ваш API-ключ от TinyMCE
    },
});