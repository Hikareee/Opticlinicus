import Dispatch from "../assets/img/Ambulance.png";
import Consultation from "../assets/img/Consultation.png";
import Medicine from "../assets/img/Pharmacy.png";
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';
import arrow1 from "../assets/img/arrow1.svg";
import arrow2 from "../assets/img/arrow2.svg";
import colorSharp from "../assets/img/color-sharp.png"
import axios from 'axios';
import { useEffect } from "react";

export const Skills = () => {
  const responsive = {
    superLargeDesktop: {
      // the naming can be any, depends on you.
      breakpoint: { max: 4000, min: 3000 },
      items: 5
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 3
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1
    }
  };

  function YPos() {
    navigator.geolocation.getCurrentPosition(function(position) {
      return("Latitude is :", position.coords.latitude);
      
    });
  }
  function Xpos() {
    navigator.geolocation.getCurrentPosition(function(position) {
      return("Longitude is :", position.coords.longitude);
    });
  }
  const longitudeE = Xpos();
  const latilitititude = YPos();
  const IWantData = async () => {
    try{
      const response = await axios('https://api.geoapify.com/v2/places?categories=healthcare.pharmacy&filter=circle:106.843907,-6.211971,5000&bias=proximity:',{longitudeE},{latilitititude},'&limit=20&apiKey=609b01cdbd5246b091cf2f69356e5318'); 
      const data = response.data;
      console.log(response);
    }

    catch(error){
      console.log(error.response);
    }
  };

  useEffect(()=> {
    IWantData();
  },[]);
                                
  return (
    <section className="skill" id="skills">
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <div className="skill-bx wow zoomIn">
                        <h2>Features</h2>
                        <p>What our app offers</p>
                        <Carousel responsive={responsive} infinite={true} className="owl-carousel owl-theme skill-slider">
                            <div className="item">
                                data
                            </div>
                            <div className="item">
                                <img src={Consultation} alt="Image" />
                                <h5>Medical Consultations</h5>
                            </div>
                            <div className="item">
                                <img src={Medicine} alt="Image" />
                                <h5>Medicinal Needs</h5>

                            </div>
                        </Carousel>
                    </div>
                </div>
            </div>
        </div>
        <img className="background-image-left" src={colorSharp} alt="Image" />
    </section>
  )
}
