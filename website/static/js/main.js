window.addEventListener('scroll',() => {
    let navbar = document.querySelector('nav');
    if (window.scrollY === 0){
        navbar.classList.remove('nav-scrolled');
    }
    else {
        navbar.classList.add('nav-scrolled');
    }
})
