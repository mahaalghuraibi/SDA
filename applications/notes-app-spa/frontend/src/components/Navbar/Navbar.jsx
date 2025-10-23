// imports
import { useNavigate, Link } from "react-router-dom";
// APIs
import * as usersAPI from "../../utilities/users-api";

export default function Navbar({ user, setUser }) {
  const navigate = useNavigate();

  function handleLogout() {
    usersAPI.logout();
    setUser(null);
    navigate("/");
  }

  if (user) {
    return (
      <>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/notes">All Notes</Link></li>
        <li><Link to="/notes/new">Add Note</Link></li>
        <li><Link to="/reactions/new">Add Reaction</Link></li>
        <li><Link to="/reactions">All Reactions</Link></li>
        <form id="logout-form" onSubmit={handleLogout}>
          <button type="submit">Log out</button>
        </form>
      </>
    );
  }

  if (!user)
    return (
      <>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/home">Home</Link></li>
        <li><Link to="/signup">SignUp</Link></li>
      </>
    );
}
