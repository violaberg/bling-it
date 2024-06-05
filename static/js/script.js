document.addEventListener("DOMContentLoaded", function () {
    const deleteReviewForm = document.getElementById("deleteReviewForm");
    
    deleteReviewForm.addEventListener("submit", function(event) {
        event.preventDefault();

        if (confirm("Are you sure you want to delete this review?")) {
            // If the user confirms, submit the form
            this.submit();
        } else {
            // If the user cancels, do nothing
            return false;
        }
    });
});
