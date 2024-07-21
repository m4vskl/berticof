document.addEventListener("DOMContentLoaded", function () {
    const lazyLoad = function (target) {
        target.querySelectorAll(".lazy").forEach(function (img) {
            if (img.getBoundingClientRect().top <= window.innerHeight && img.getBoundingClientRect().bottom >= 0) {
                img.src = img.dataset.src;
                img.classList.remove("lazy");
            }
        });
    };

    document.querySelectorAll(".accordion-button").forEach(function (accordion) {
        accordion.addEventListener("click", function () {

            let contentPanel = this.nextElementSibling;
            setTimeout(function() { lazyLoad(contentPanel); }, 1000);
        });
    });
});
