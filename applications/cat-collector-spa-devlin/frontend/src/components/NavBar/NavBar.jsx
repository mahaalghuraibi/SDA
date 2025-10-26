import { useNavigate, Link } from "react-router";
import * as usersAPI from "../../utilities/users-api"

export default function NavBar({ user, setUser }) {
    const navigate = useNavigate()

    function handleLogout(evt) {
        evt.preventDefault();
        usersAPI.logout();
        setUser(null);
        navigate("/");
    }

    if (user) return (<>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/cats">All Cats</Link></li>
        <li><Link to="/cats/new">Create New Cat</Link></li>
        <li><Link to="/toys">All Toys</Link></li>
        <li><Link to="/toys/new">Create New Toy</Link></li>
        <form id="logout-form" onSubmit={handleLogout}>
            <button type="submit">Log out</button>
        </form>
    </>)


    if (!user) return (<>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/home">Home</Link></li>
        <li><Link to="/signup">SignUp</Link></li>
    </>)

}
