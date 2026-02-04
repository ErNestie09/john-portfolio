document.addEventListener("DOMContentLoaded", function () {

    const filterButtons = document.querySelectorAll(".filter-btn");

    filterButtons.forEach(button => {

        button.addEventListener("click", () => {

            // Remove active state
            filterButtons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");

            const filterValue = button.dataset.filter;


            // Select cards AFTER they are generated
            const cards = document.querySelectorAll(".card");

            cards.forEach(card => {

                const categories = card.dataset.categories;

                if (filterValue === "All" || categories.includes(filterValue)) {
                    card.parentElement.style.display = "block"; 
                } else {
                    card.parentElement.style.display = "none";
                }

            });

        });

    });

});


