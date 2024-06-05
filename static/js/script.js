document.addEventListener("DOMContentLoaded", function() {
    // Get the modal and delete button elements
    var deleteReviewLink = document.getElementById("deleteReviewLink");
    var deleteModal = document.getElementById("myModal");
    var cancelDeleteBtn = document.getElementById("cancelDeleteBtn");
    var confirmDeleteBtn = document.getElementById("confirmDeleteBtn");

    // Add event listeners for the modal
    deleteReviewLink.addEventListener("click", function(event) {
        event.preventDefault();
        deleteModal.style.display = "block";
    });

    cancelDeleteBtn.addEventListener("click", function() {
        deleteModal.style.display = "none";
    });

    confirmDeleteBtn.addEventListener("click", function() {
        deleteModal.style.display = "none";
    });
});
