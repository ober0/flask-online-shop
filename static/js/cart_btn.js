$(document).ready(function() {
    $('.addToCartBtn').click(function() {
        var button = $(this);

        var productId = button.data('product-id');

        $.ajax({
            url: '/add_to_cart',
            type: 'POST',
            data: {productId: productId},
            success: function(response){
                if (response.status === "OK") {
                    button.text("В корзине");
                    button.css("background-color", 'rgb(100, 155, 255)');
                    $('#cart').text('В корзине: ' + response.cart_count);
                } else if (response.status === "REM") {
                    button.text("Добавить в корзину");
                    button.css("background-color", 'rgb(0, 105, 217)');
                    $('#cart').text('В корзине: ' + response.cart_count);
                }
            }
        });
    });
});