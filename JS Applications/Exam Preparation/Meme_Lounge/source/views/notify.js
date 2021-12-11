const spanElement = document.querySelector('#errorBox span');
const notification = document.getElementById('notifications');

export function notify(message) {
    setTimeout(() => {
        spanElement.textContent = message
        notification.style.display = block;
    }, 300);
}