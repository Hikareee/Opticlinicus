import logo from './logo.svg';
import './Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { NavBar } from "./components/NavBar";
import { Banner } from "./components/Banner";
import { Skills } from "./components/Skills";
import { Projects } from "./components/Projects";
import { Footer } from "./components/Footer";

function Home() {
  return (
    <div className="Home">
      <NavBar />
      <Banner />
      <Skills />
      <Projects />
      <Footer />
    </div>
  );
}

export default Home;
