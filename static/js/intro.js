const words = ['Pine', 'Cedar', 'Spruce', 'Larch', 'Fir', 'Oak','Ash','Beech','Birch','Maple'];
let wordIndex = 0;
let letterIndex = 0;
let isDeleting = false;
let typingSpeed = 75;

    function type() {
    const text = words[wordIndex];
    const currentText = text.slice(0, letterIndex + 1);

    document.getElementById('typesofwood').textContent = currentText;

    if (!isDeleting) {
        letterIndex++;
    } else {
        letterIndex--;
    }

    if (letterIndex === text.length + 1) {
        isDeleting = true;
        typingSpeed = 75;
    }

    if (letterIndex === 0) {
        isDeleting = false;
        wordIndex++;
        if (wordIndex === words.length) {
            wordIndex = 0;
        }
        typingSpeed = 75;
    }

    setTimeout(type, typingSpeed);
}

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(type, typingSpeed);
});