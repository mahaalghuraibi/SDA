import "./NavBar.css"
import NavBarLink from "./NavBarLink";

const navLinks = [
  { href: "/", text: "Home" },
  { href: "/about-us", text: "About Us" },
  { href: "/money-pit", text: "Investment Opportunities" },
  { href: "/the-fine-print", text: "Terms of Service" },
];

const NavBar = () => {
  return (
      <nav id="top-navbar">
        {
          navLinks.map((linkItem) => (<NavBarLink text={linkItem.text} href={linkItem.href} />))
        }
      </nav>
  )
}

export default NavBar;