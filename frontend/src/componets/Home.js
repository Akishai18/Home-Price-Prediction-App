import React from 'react';
import '../App.css';
import HeroSection from './HeroSection';
import Footer from './footer';
import Cards from './Cards';

function Home() {
  return (
    <>
      <HeroSection />
      <Cards />
      <Footer />
    </>
  );
}

export default Home;
