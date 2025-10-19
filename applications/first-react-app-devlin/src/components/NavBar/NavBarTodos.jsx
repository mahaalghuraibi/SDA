import { Link } from 'react-router';

export default function NavBarTodos() {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/todo/new">New Todo</Link></li>
                <li><Link to="/todos">All Todos</Link></li>
            </ul>
        </nav>
    );
}
