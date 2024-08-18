import React from 'react';
import '../App.css';
import './HeroSection.css';

function HeroSection() {
  // Function to handle scrolling
  const handleScroll = () => {
    window.scrollBy({ top: 1000, behavior: 'smooth' }); // Adjust the number of pixels as needed
  };

  return (
    <div className='hero-container'>
      <video src='/videos/video-1.mp4' autoPlay loop muted />
      <h1>DISCOVER YOUR DREAM HOME</h1>
      <p>Find out the Best Place and Time to Purchase your Dream Home</p>
      <button className="firstbutton" onClick={handleScroll}>Get Started</button>
    </div>
  );
}

export default HeroSection;