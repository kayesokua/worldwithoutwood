const woodWords = ['pine', 'larch', 'beech', 'spruce', 'maple', 'fir', 'oak', 'ash', 'cedar', 'birch'];
const productWords2 = ['paper', 'cartons', 'furnitures', 'sportswear', 'lightweight cars', 'veneers', 'guitars'];
const productWords = ['sawdust', 'bark', 'chips', 'pulp', 'shavings', 'resin', 'veneers','pellets','paving slabs'];


let woodIndex = 0;
let productIndex = 0;
let woodLetterIndex = 0;
let productLetterIndex = 0;
let isDeletingWood = false;
let isDeletingProduct = false;
let typingSpeed = 75;

function typeWood() {
    const text = woodWords[woodIndex];
    const currentText = text.slice(0, woodLetterIndex + 1);
    document.getElementById('woodtypes').textContent = currentText;

    if (!isDeletingWood) {
        woodLetterIndex++;
    } else {
        woodLetterIndex--;
    }

    if (woodLetterIndex === text.length + 1) {
        isDeletingWood = true;
        typingSpeed = 100;
    }

    if (woodLetterIndex === 0) {
        isDeletingWood = false;
        woodIndex++;
        if (woodIndex === woodWords.length) {
            woodIndex = 0;
        }
        typingSpeed = 100;
    }

    setTimeout(typeWood, typingSpeed);
}

function typeProduct() {
    const text = productWords[productIndex];
    const currentText = text.slice(0, productLetterIndex + 1);
    document.getElementById('woodproducts').textContent = currentText;

    if (!isDeletingProduct) {
        productLetterIndex++;
    } else {
        productLetterIndex--;
    }

    if (productLetterIndex === text.length + 1) {
        isDeletingProduct = true;
        typingSpeed = 50;
    }

    if (productLetterIndex === 0) {
        isDeletingProduct = false;
        productIndex++;
        if (productIndex === productWords.length) {
            productIndex = 0;
        }
        typingSpeed = 50;
    }

    setTimeout(typeProduct, typingSpeed);
}

document.addEventListener('DOMContentLoaded', function () {
    typeWood();
    setTimeout(typeProduct, typingSpeed);
});