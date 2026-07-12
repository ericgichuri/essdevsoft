$(function () {

    // ================= MOBILE MENU =================

    function openMenu() {

        $("#mobile-overlay").removeClass("hidden");

        $("body").css("overflow", "hidden");

        setTimeout(function () {

            $("#mobile-menu").removeClass("translate-x-full");

        }, 10);

    }

    function closeMenu() {

        $("#mobile-menu").addClass("translate-x-full");

        $("body").css("overflow", "");

        setTimeout(function () {

            $("#mobile-overlay").addClass("hidden");

        }, 300);

    }

    $("#mobile-btn").on("click", openMenu);

    $("#close-btn").on("click", closeMenu);

    $("#mobile-overlay").on("click", function (e) {

        if (e.target === this) {

            closeMenu();

        }

    });

    $("#mobile-menu a").on("click", closeMenu);

    // ================= DARK MODE =================

    function updateIcon() {

        if ($("html").hasClass("dark")) {

            $("#theme-icon")
                .removeClass("fa-moon")
                .addClass("fa-sun");

        } else {

            $("#theme-icon")
                .removeClass("fa-sun")
                .addClass("fa-moon");

        }

    }

    if (localStorage.getItem("theme") === "dark") {

        $("html").addClass("dark");

    }

    updateIcon();

    $("#theme-toggle").on("click", function () {

        $("html").toggleClass("dark");

        if ($("html").hasClass("dark")) {

            localStorage.setItem("theme", "dark");

        } else {

            localStorage.setItem("theme", "light");

        }

        updateIcon();

    });

});