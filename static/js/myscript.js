$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true, //here it is used to slide all divs from 1 to n and n to 1.it will show the slides continiously from 1 to n and n to 1
    margin: 20,
    responsiveClass: true, //to make the slideder(which uses owlCarousel) responsive 
    responsive: {
        0: {
            items: 1, //from 0px to 599px.it will show one dives or slide
            nav: false,
            autoplay: true,//it will show all the slides continiously (one by one or many by many) (automatically sliding)
        },
        600: {   
            items: 3, //from 600px to 999px.it will show three dives or slides
            nav: true,
            autoplay: true,//it will show all the slides continiously (one by one or many by many) (automatically sliding)
        },
        1000: {
            items: 5, //above 1000px it will show five dives or slides
            nav: true,
            loop: true, //it will show the slides 1 to n and n to 1 continiously 
            autoplay: true, //it will show all the slides continiously(one by one or many by many)  (automatically sliding)
        }
    }
})


$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    console.log(id)
    var eml = this.parentNode.children[2];
    console.log(eml)

    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id:id,
        },
        success: function(data){
            console.log(data);
            // $['#quantity'].html(cart_quant)
            eml.innerText=data.cart_quant
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.total_amount

        }
    });

})


$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    console.log(id)
    var eml = this.parentNode.children[2];
    console.log(eml)

    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id:id,
        },
        success: function(data){
            console.log(data);
            // $['#quantity'].html(cart_quant)
            eml.innerText=data.cart_quant
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.total_amount
            
        }
    });

})

$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    console.log(id)
    var eml =this;

    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id:id,
        },
        success: function(data){
            console.log(data);
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.total_amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    });

})
