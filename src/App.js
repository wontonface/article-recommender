import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import Landing from "./components/Landing";

function App() {
  // const [getMessage, setGetMessage] = useState({})

  // useEffect(()=>{
    // axios.get('https://react-flask-tutorial.herokuapp.com/flask/hello').then(response => {
      // console.log("SUCCESS", response)
      // setGetMessage(response)
    // }).catch(error => {
      // console.log(error)
    // })

    // axios.get('http://localhost:5000/flask/hello').then(response => {
    //   console.log("SUCCESS", response)
    //   setGetMessage(response)
    // }).catch(error => {
    //   console.log(error)
    // })

  // }, [])
  return (
    <div className="App">
      <header className="App-header">
        <div id="content">
          <Landing></Landing>
        </div>
      </header>
    </div>
  );
}

export default App;
