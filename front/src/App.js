import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomeBody from './components/HomeBody';
import Order from './components/Order';

const App = () =>{
  return(
    <>
    <Router>
      <Routes>
        <Route path='/' element={<HomeBody />}/>
        <Route path='/order/' element={<Order />}/>
      </Routes>
    </Router>
    </>
  )
}

export default App;
