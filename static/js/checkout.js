if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}
console.log(cart);


var sum = 0;
var totalPrice = 0;
if ($.isEmptyObject(cart)) {
    //if object is empty
    mystr = `<p><span class="name">Your cart is empty, please add some items to your cart before checking out!</span></p><a href="/popular" class="btn">view menu</a>`
    $('#items').append(mystr);
} else {
for (item in cart) {

    let name = cart[item][1];
    let qty = cart[item][0];
//    let itemprice = cart[item][2];
    sum = sum + qty;
//    totalPrice = totalPrice + qty * itemprice
//    `<li class="list-group-item d-flex justify-content-between align-items-center">
//                    ${name}
//                    <span class="badge badge-primary badge-pill">${qty}</span>
//                </li>`

    mystr = `<p><span class="name">${name}</span><span class="price">${qty}</span></p>`
    $('#items').append(mystr);
}
}
document.getElementById('cart').innerHTML = sum;
//document.getElementById('totalPrice').innerHTML = totalPrice;
//function clearCart() {
//    cart = JSON.parse(localStorage.getItem('cart'));
//    localStorage.clear();
//    cart = {};
//    updateCart(cart);
//}
$('#itemsJson').val(JSON.stringify(cart));
localStorage.clear();