import React, { useState } from 'react';
import Carditem from './Carditem';
import './Cards.css'; // Ensure this matches the filename and path
import axios from 'axios';

function Cards() {
  // Use Prediction as a custom hook or as a component if needed
  const [location1, setLocation1] = useState("");
  const [location2, setLocation2] = useState("");
  const [location3, setLocation3] = useState("");
  const [location4, setLocation4] = useState("");
  const [location5, setLocation5] = useState("");
  const [finallocation, setFinalLocation] = useState("");

  const [date1, setDate1] = useState("");
  const [date2, setDate2] = useState("");
  const [date3, setDate3] = useState("");
  const [date4, setDate4] = useState("");
  const [date5, setDate5] = useState("");
  const [finaldate, setFinalDate] = useState("");
  const [finalhometype, setFinalHometype] = useState("");


  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  
  const handleLocation1Change = (event) => {
    setLocation1(event.target.value);
  };
  
  const handleLocation2Change = (event) => {
    setLocation2(event.target.value);
  };

  const handleLocation3Change = (event) => {
    setLocation3(event.target.value);
  };

  const handleLocation4Change = (event) => {
    setLocation4(event.target.value);
  };

  const handleLocation5Change = (event) => {
    setLocation5(event.target.value);
  };

  const handleDate1Change = (event) => {
    setDate1(event.target.value);
  };
  const handleDate2Change = (event) => {
    setDate2(event.target.value);
  };
  const handleDate3Change = (event) => {
    setDate3(event.target.value);
  };
  const handleDate4Change = (event) => {
    setDate4(event.target.value);
  };
  const handleDate5Change = (event) => {
    setDate5(event.target.value);
  };

  const handleCombinedActions1 = () => {
    handleSubmit("Comp",1);
  };

  const handleCombinedActions2 = () => {
    handleSubmit("SFDetach",2);
  };

  const handleCombinedActions3 = () => {
    handleSubmit("SFAttach",3);
  };

  const handleCombinedActions4 = () => {
    handleSubmit("THouse",4);
  };

  const handleCombinedActions5 = () => {
    handleSubmit("Apart",5);
  };

  const handleSubmit = async (hometype,num) => {
    if (num == 1){
      var location = location1
      var date = date1
      setFinalHometype("Average Home")
    }else if(num == 2){
      var location = location2
      var date = date2
      setFinalHometype("Standard Family Detached Home")
    }else if(num == 3){
      var location = location3
      var date = date3
      setFinalHometype("Standard Family Attached Home")
    }else if(num == 4){
      var location = location4
      var date = date4
      setFinalHometype("Standard Family Attached Townhome")
    }else if(num == 5){
      var location = location5
      var date = date5
      setFinalHometype("Standard Family Apartment")
    }
    if (location && date) {
      setLoading(true); // Set loading state to true
      try {
        const response = await axios.post('http://localhost:5000/predict_price', {
          location,
          date,
          hometype
        });
        setPrediction(response.data.predictions);
        setFinalLocation(location)
        setFinalDate(date)
        setLoading(false); // Reset loading state
      } catch (error) {
        console.error('Error fetching prediction info:', error);
        setPrediction("An error occurred while fetching prediction information.");
      }
    } else {
      setPrediction("Please fill out all required fields.");
    }
  };

  return (
    <div className='cards'>
      <h1>Find out the price of various different home types!</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <Carditem src="images/img-21.jpg" />
            <Carditem src="images/img-22.jpg" />
          </ul>

          {/* Content under img-21 */}
          <h1 className='SFDetach-Header'>Average Family Home</h1>
          <div className='location-container'>
            <h3 className='Location'>Location:</h3>
            <input 
              type='text'
              placeholder='Enter location'
              className='location-textbox'
              value={location1}
              onChange={handleLocation1Change}
            />
          </div>
          <div className='date-container'>
            <h3 className='date'>Date:</h3>
            <input 
              type='text'
              placeholder='YYYY/MM/DD'
              className='date-textbox'
              value={date1}
              onChange={handleDate1Change}
            />
          </div>
          <div className='submit-button-container'>
            <button className='submit1' type='button' onClick={handleCombinedActions1}>
              <span className='text'>Submit</span>
            </button>
          </div>

          {/* Content under img-22 */}
          <h1 className='Comp-Header'>Standard Family Detach Home</h1>
          <div className='comp-location-container'>
            <h3 className='Comp-Location'>Location:</h3>
            <input 
              type='text'
              placeholder='Enter location'
              className='comp-location-textbox'
              value={location2}
              onChange={handleLocation2Change}
            />
          </div>
          <div className='comp-date-container'>
            <h3 className='Comp-Date'>Date:</h3>
            <input 
              type='text'
              placeholder='YYYY/MM/DD'
              className='comp-date-textbox'
              value={date2}
              onChange={handleDate2Change}
            />
          </div>
          <div className='submit-button-container'>
          <button className='submit2' type='button' onClick={handleCombinedActions2}>
          <span className='text'>Submit</span>
            </button>
          </div>
      
          <ul className='cards__items'>
            <Carditem src="images/img-23.jpg" />
            <Carditem src="images/img-24.jpg" />
            <Carditem 
              src="images/img-25.jpg"
              text="Art and Mental Health Exhibits: Showcasing artwork created by individuals with mental health challenges or art that explores mental health themes. This can help express experiences and foster empathy and understanding."
            />
          </ul>
          {/* Content under img-23 */}
          <h2 className='SFAttach-Header'>Standard Family Attached Home</h2>
          <div className='SFAttach-location-container'>
            <h3 className='SFAttach-Location'>Location:</h3>
            <input 
              type='text'
              placeholder='Enter location'
              className='SFAttach-location-textbox'
              value={location3}
              onChange={handleLocation3Change}
            />
          </div>
          <div className='SFAttach-date-container'>
            <h3 className='SFAttach-Date'>Date:</h3>
            <input 
              type='text'
              placeholder='YYYY/MM/DD'
              className='SFAttach-date-textbox'
              value={date3}
              onChange={handleDate3Change}
            />
          </div>
          <h2 className='THouse-Header'>Standard Family Townhome</h2>
          <div className='THouse-location-container'>
            <h3 className='THouse-Location'>Location:</h3>
            <input 
              type='text'
              placeholder='Enter location'
              className='THouse-location-textbox'
              value={location4}
              onChange={handleLocation4Change}
            />
          </div>
          <div className='THouse-date-container'>
            <h3 className='THouse-Date'>Date:</h3>
            <input 
              type='text'
              placeholder='YYYY/MM/DD'
              className='THouse-date-textbox'
              value={date4}
              onChange={handleDate4Change}
            />
          </div>
          <h2 className='Apart-Header'>Standard Family Apartment</h2>
          <div className='Apart-location-container'>
            <h3 className='Apart-Location'>Location:</h3>
            <input 
              type='text'
              placeholder='Enter location'
              className='Apart-location-textbox'
              value={location5}
              onChange={handleLocation5Change}
            />
          </div>
          <div className='Apart-date-container'>
            <h3 className='Apart-Date'>Date:</h3>
            <input 
              type='text'
              placeholder='YYYY/MM/DD'
              className='Apart-date-textbox'
              value={date5}
              onChange={handleDate5Change}
            />
          </div>

        </div>
        <div className='submit-button-container'>
        <button className='submit3' type='button' onClick={handleCombinedActions3}>
        <span className='text'>Submit</span>
          </button>
        </div>
        <div className='submit-button-container'>
        <button className='submit4' type='button' onClick={handleCombinedActions4}>
        <span className='text'>Submit</span>
          </button>
        </div>
        <div className='submit-button-container'>
        <button className='submit5' type='button' onClick={handleCombinedActions5}>
        <span className='text'>Submit</span>
          </button>
        </div>
        {loading && <p>Loading...</p>}

        {prediction !== null && (
        <h3 className='SFDetach-Header2'>
          The price of a {finalhometype} in {finallocation} on {finaldate} is ${prediction}
          </h3>
          )}  
      </div>
    </div>
  );
}

export default Cards;
