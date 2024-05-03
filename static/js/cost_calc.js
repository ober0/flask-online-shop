window.onload = function(){
    var priceElements = document.querySelectorAll('.price');
    var totalPrice = 0;

    priceElements.forEach(function (element) {
        var priceText = element.innerText;
        var priceValue = parseFloat(priceText.replace("руб", "").trim());
        totalPrice += priceValue;
    })

    document.getElementById('total-price').innerText = totalPrice + ' руб';
}