
function toggleTheme() {
   document.body.classList.toggle('dark-mode');
    const modeText = document.getElementById('modeText');
    if (document.body.classList.contains('dark-mode')) {
        modeText.textContent = 'Light';
    } else {
        modeText.textContent = 'Dark';
    }
}

function toggleMenu() {
    const nav = document.querySelector('.navHolder');
    nav.classList.toggle('show');
}
