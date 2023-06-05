import logo from './logo.svg';
import './Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { NavBar } from "./components/NavBar";
import { Skills } from "./components/Skills";
import { Projects } from "./components/Projects";
import { Footer } from "./components/Footer";

function Needs() {
  return (
    <div className="Home">
      <NavBar />
      <Skills />
      <Projects />
      <Footer />
    </div>
  );
}

export default Needs;
