document.addEventListener("DOMContentLoaded", function () {
    const deleteReviewForm = document.getElementById("deleteReviewForm");
    const deleteGemstone = document.getElementById("deleteGemstone")
    
    if (deleteReviewForm) {
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
    }

    if (deleteGemstone) {
        deleteGemstone.addEventListener("click", function(event) {
            event.preventDefault();

            if (confirm("Are you sure you want to delete this gemstone?")) {
                window.location.href = deleteGemstone.getAttribute("href");
            } else {
                return false;
            }
        });
    }
});
