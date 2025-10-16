// src/components/NavBar/NavBar.jsx
import './NavBar.css';
import NavbarLink from '../NavBarLink/NavbarLink.jsx';

const Navbar = ({ links }) => {
  return (
    <nav id="top-navbar">
      {links.map((link, index) => (
        <NavbarLink key={index} href={link.href} text={link.text} />
      ))}
    </nav>
  );
};

export default Navbar;
