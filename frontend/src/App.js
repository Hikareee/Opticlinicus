import Login from "./components/Login";
import Register from "./components/Register";
import { BrowserRouter as Router, Route, Routes, Navigate} from "react-router-dom";
import Teleconf from "./components/Teleconf";
import Home from "./homepage/Home";
import HomeLoggedIn from "./homepage - Copy/HomeLoggedIn";

function App() {
  return (
    <div className="app">
      <Router>
        <Routes>
          <Route exact path="/Login" element={<Login />} />
          <Route exact path="/register" element={<Register />} />
          <Route exact path = "/meet"element={<Teleconf/>}/>
          <Route path = "/" element={<Home />}/>
          <Route path='/home' element = {<HomeLoggedIn/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;