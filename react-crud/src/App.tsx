import React from 'react';
import './App.css';
import Nav from './components/Nav';
import Menu from './components/Menu';
import Products from './admin/Products';

function App() {
  return (
    <div className="App">
      <Nav />

      <div className="container-fluid">
        <div className="row">
          <Menu />
          <main role="main" className="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
              <Products />
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;
