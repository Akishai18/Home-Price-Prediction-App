import React, { useState } from 'react';
import './Footer.css';

function Footer() {
  // State for newsletter and feedback
  const [newsletterMessage, setNewsletterMessage] = useState('');
  const [feedbackMessage, setFeedbackMessage] = useState('');
  const [newsletterEmail, setNewsletterEmail] = useState('');
  const [feedbackText, setFeedbackText] = useState('');

  // Handle newsletter subscription
  const handleNewsletterSubmit = (e) => {
    e.preventDefault();
    setNewsletterMessage('Thank you for subscribing!');
    setNewsletterEmail(''); // Clear the email field
  };

  // Handle feedback submission
  const handleFeedbackSubmit = (e) => {
    e.preventDefault();
    setFeedbackMessage('Thank you for the feedback!');
    setFeedbackText(''); // Clear the feedback field
  };

  return (
    <div className='footer-container'>
      <section className='footer-subscription'>
        <p className='footer-subscription-heading'>
          Join the newsletter to receive updates about any new features or additions to our services
        </p>
        <p className='footer-subscription-text'>
          You can unsubscribe at any time.
        </p>
        <div className='input-areas'>
          <form onSubmit={handleNewsletterSubmit}>
            <input
              className='footer-input'
              name='email'
              type='email'
              placeholder='Your Email'
              value={newsletterEmail}
              onChange={(e) => setNewsletterEmail(e.target.value)}
            />
            <button className="secondbutton" type="submit">Submit</button>
          </form>
          {newsletterMessage && <p>{newsletterMessage}</p>}
        </div>
      </section>
      <section className='footer-subscription'>
        <p className='footer-subscription-heading'>
          If you have any feedback please feel free to let us know!
        </p>
        <div className='input-areas'>
          <form onSubmit={handleFeedbackSubmit}>
            <input
              className='footer-input'
              name='feedback'
              type='text'
              placeholder='Your Feedback'
              value={feedbackText}
              onChange={(e) => setFeedbackText(e.target.value)}
            />
            <button className="secondbutton" type="submit">Send</button>
          </form>
          {feedbackMessage && <p>{feedbackMessage}</p>}
        </div>
      </section>
    </div>
  );
}

export default Footer;
