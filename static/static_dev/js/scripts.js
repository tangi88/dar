$(document).ready(function(){
    var form = $('#form_buying_product');

    function basket_updating(product_id, nmb, is_delete){
        var data = {};
        data["product_id"] = product_id;
        data["nmb"] = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }

        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                console.log('OK');
                console.log(data.products_total);
                if (data.products_total || data.products_total == 0){
                    $('#basket_total').text("("+data.products_total+")");
                    $('.basket-items ul').html("");
                    $.each(data.products, function(k, v){
                        $('.basket-items ul').append('<li>'+v.name+', '+v.amount+', '+v.price+
                            '  <a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                            '</li>');
                    });
                }
            },
            error: function(){
                console.log('error');
            }
        });

//        $('.basket-items ul').append('<li>'+product_name+', '+nmb+', '+product_price+
//            '  <a class="delete-item" href="">x</a>'+
//            '</li>');

    }

    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product-id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
        console.log(product_name);

        basket_updating(product_id, nmb, is_delete=false);
    });

    function showingBasket(){
        // $('.basket-items').toggleClass('d-none');
        // $('.basket-items').removeClass('hidden');
        // $('.basket-items').addClass('hidden');
    };

    $('.basket-container').on('click', function(e){
        e.preventDefault();
        showingBasket();
        $('.basket-items').removeClass('d-none');
    });

    $('.basket-container').mouseover(function(){
        showingBasket()
        $('.basket-items').removeClass('d-none');
    });

    $('.basket-container').mouseout(function(){
        showingBasket()
        $('.basket-items').addClass('d-none');
    });

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        product_id = $(this).data("product_id");
        nmb = 0;
        basket_updating(product_id, nmb, is_delete=true);
//        $(this).closest('li').remove();
    });

    function calculating_basket(){
        var total_sum = 0;
        $('.product-basket-sum').each(function(){
            total_sum += parseFloat($(this).text());
        });
        console.log(total_sum);
        $('#total_sum').text(total_sum.toFixed(2));
    };

    $(document).on('change', '.product-basket-amount', function(){
        var current_amount = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-basket-price').text()).toFixed(2);
        var current_sum = parseFloat(current_amount * current_price).toFixed(2);
        current_tr.find('.product-basket-sum').text(current_sum);

        calculating_basket();
    })

    calculating_basket();

});