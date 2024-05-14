document.addEventListener("DOMContentLoaded", function() {
    var addToWishlistIcon = document.getElementById("add-to-wishlist");
    var gemstoneId = addToWishlistIcon.getAttribute("data-gemstone-id");

    addToWishlistIcon.addEventListener("click", function() {
        addToWishlist(gemstoneId);
    });
});


function addToWishlist(gemstoneId) {
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var url = "profiles/add_to_wishlist/";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Handle success response
            alert("Gemstone added to wishlist!");
        } else {
            // Handle error response
            alert("Failed to add gemstone to wishlist!");
        }
    };
    xhr.send(JSON.stringify({ gemstone_id: gemstoneId }));
}
