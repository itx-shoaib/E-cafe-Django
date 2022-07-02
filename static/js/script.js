// Query selector for menu bar and nav bar inn responsive website 
// reference: @media(max-width:400px;)


let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');


menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}


window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}

/* ------------------------------------------------------------------  */
/*                 Loader Container js                                 */
/* ------------------------------------------------------------------  */


function loader(){
document.querySelector('.loader-container').classList.add('fade-out');
}

function fadeOut(){
    setInterval(loader, 3000);
}

window.onload = fadeOut();

/* ------------------------------------------------------------------  */
/*                 Cart js                                           */
/* ------------------------------------------------------------------  */


