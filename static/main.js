(function() {
    const messages = document.getElementsByClassName('flash-container');
    for (let message of messages) {
        setTimeout(() => {
            message.remove();
        }, 4000);
    }
})();