const menu = document.querySelector('.nav__right')
const navButton  = document.querySelector('.nav__menu')
const navClose = document.querySelector('#nav_close')
let page = document.querySelector('.page')

let navRightMenus = menu.querySelectorAll('.nav__right__menu')
let navRightMenuCloses = menu.querySelectorAll('.nav__right__menu__close')
let navRightMenuOpens = menu.querySelectorAll('.nav__right__menu__open')


if (window.innerWidth <= 900) {
    navButton.onclick = () => {
        if (menu.style.left == '-100%') {
            menu.style.left = 0
            body.style.overflowY = 'hidden'
            // page.style.opacity = 0
        } else {
            menu.style.left = '-100%'
            body.style.overflowY = 'scroll'
            // page.style.opacity = 1
        }
    }
    
    navClose.addEventListener('click', () => {
        menu.style.left = '-100%'
        document.body.style.overflowY = 'scroll'
    })
    
    for (let i = 0; i < navRightMenus.length; i++) {
        navRightMenuOpens[i].addEventListener('click',(e) => {
            navRightMenus[i].style.left = 0
            console.log(e.target)
        })
        
        navRightMenuCloses[i].addEventListener('click',(e) => {
            navRightMenus[i].style.left = '-100%'
            console.log(e.target)
        })
    }   
}
