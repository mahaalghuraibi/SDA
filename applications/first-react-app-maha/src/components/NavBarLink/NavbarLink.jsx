// src/components/NavBarLink/NavbarLink.jsx
const NavbarLink = ({ href, text }) => {
  return (
    <a href={href}>
      {text}
    </a>
  );
};

export default NavbarLink;
