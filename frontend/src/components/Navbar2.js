import React, {useState} from "react";
import "../styles/Navbar2.css";
import logo from "../imgs/logo.png"
function Navbar2(){

    const [nav, setnav] = useState(false);

    const changeBackground = () => {
        if(window.scrollY >= 50) {
            setnav(true);
        }
        else {
            setnav(false);
        }
    }
    window.addEventListener('scroll', changeBackground);

    return(
        <nav className ={nav ? 'nav active' : 'nav'}>
        <a href='#' className ='logo'>
            
        </a>
        <input type = 'checkbox' className = 'menu-btn' id='menu-btn'/>
        <label className = 'menu-icon' for='menu-btn'>
            <span className = 'nav-icon'></span>
        </label>
        <ul className = 'menu'>
            <li><a href = '/'>Home</a></li>
            <li><a href = '/#skills'>Features</a></li>
            <li><a href = '#'>About</a></li>
        </ul>
    </nav>
    )
}

export default Navbar2