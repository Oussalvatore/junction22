import React from 'react'
import {Link} from 'react-router-dom'

function Header() {
  return (
    <>
        {/* <!--=============== HEADER ===============--> */}
        <header className="header" id="header">
            <nav className="nav container">
                <a href="/" className="nav__logo">CF Delivery</a>

                <div className="nav__menu" id="nav-menu">
                    <ul className="nav__list">
                        <li className="nav__item">
                            <a href="/" className="nav__link active-link">Home</a>
                        </li>
                        <li className="nav__item">
                            <a href="/" className="nav__link">About us</a>
                        </li>
                        <li className="nav__item">
                            <a href="/" className="nav__link">Services</a>
                        </li>
                        <li className="nav__item">
                            <a href="/" className="nav__link">Contact us</a>
                        </li>

                        <i className='bx bx-toggle-left change-theme' id="theme-button"></i>
                    </ul>
                </div>

                <div className="nav__toggle" id="nav-toggle">
                    <i className='bx bx-grid-alt'></i>
                </div>

                <Link to="/order/" className="button button__header">Order Now!</Link>
                {/* <a href="/" className="button button__header">Order Now!</a> */}
            </nav>
        </header>
    </>
  )
}

export default Header
