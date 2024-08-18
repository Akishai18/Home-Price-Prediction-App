import './App.css';
import Navbar from './componets/Navbar'; 
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import React from 'react';
import '@fortawesome/fontawesome-free/css/all.min.css';
import Home from './componets/Home';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
           <Route path='/' exact element={ <Home />}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
