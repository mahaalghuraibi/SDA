import './App.css'
import { useEffect, useState } from 'react';
import { Routes, Route, Link } from 'react-router';
import { useLocation, Navigate } from 'react-router';
import HeaderLogo from "../../assets/images/header-logo.svg"
import HomePage from '../HomePage/HomePage';
import AboutPage from '../AboutPage/AboutPage';
import CatIndexPage from '../CatIndexPage/CatIndexPage';
import CatDetailPage from '../CatDetailPage/CatDetailPage';
import CatFormPage from '../CatFormPage/CatFormPage';
import ToyDetailPage from '../ToyDetailPage/ToyDetailPage';
import ToyFormPage from '../ToyFormPage/ToyFormPage';
import ToyIndexPage from '../ToyIndexPage/ToyIndexPage';
import NavBar from '../../components/NavBar/NavBar';
import SignupPage from '../SignupPage/SignupPage';
import { getUser } from '../../utilities/users-api';

function App() {
  const location = useLocation();
  const [user, setUser] = useState(null);
  const routes = ["about", "cats", "home"]
  const mainCSS = routes.filter(r => location.pathname.includes(r) ? r : "").join(" ")

  useEffect(() => {
    async function checkUser() {
      const foundUser = await getUser();
      setUser(foundUser)
    }
    checkUser()
  }, [])

  return (<>
    <header>
      <div className={`${mainCSS} header-logo-container`}>
        <Link to="/"><img src={HeaderLogo} alt="The Cat Collector Logo" /></Link>
      </div>
      <nav>
        <ul>
        <NavBar user={user} setUser={setUser} />
        </ul>
      </nav>
    </header>
    <main className={mainCSS}>
      <Routes>
        {user ? <>
          <Route path="/home"                      element={<HomePage user={user} setUser={setUser} />}/>
          <Route path="/about"                     element={<AboutPage />} />
          <Route path="/cats"                      element={<CatIndexPage />} />
          <Route path="/cats/new"                  element={<CatFormPage createCat={true} />} />
          <Route path="/cats/edit/:id"             element={<CatFormPage editCat={true}   />}/>
          <Route path="/cats/confirm_delete/:id"   element={<CatFormPage deleteCat={true} />}/>
          <Route path="/cats/:catId"               element={<CatDetailPage />} />
          <Route path="/toys"                      element={<ToyIndexPage />} />
          <Route path="/toys/new"                  element={<ToyFormPage createToy={true} />} />
          <Route path="/toys/edit/:id"             element={<ToyFormPage editToy={true}   />}/>
          <Route path="/toys/confirm_delete/:id"   element={<ToyFormPage deleteToy={true} />}/>
          <Route path="/toys/:id"                  element={<ToyDetailPage />} />
          <Route path="/*"                         element={<Navigate to="/home"/>}/>
        </> : <>
          <Route path="/home"                      element={<HomePage user={user} setUser={setUser} />}/>
          <Route path="/about"                     element={<AboutPage />} />
          <Route path="/signup"                    element={<SignupPage user={user} setUser={setUser} />}/>
          <Route path="/*"                         element={<Navigate to="/home"/>}/>
        </>}
      </Routes>
    </main>
  </>)
}

export default App
