console.log('asd');
window.addEventListener('scroll',() => {
    let navbar = document.querySelector('nav');
    console.log(window.scrollY);
    if (window.scrollY === 0){
        navbar.classList.remove('nav-scrolled');
    }
    else {
        navbar.classList.add('nav-scrolled');
    }
})


