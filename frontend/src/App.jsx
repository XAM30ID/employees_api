import React from "react";
import "./css/style.css"

import Search from "./components/Search";
import Employees from "./components/Employees";

import { UsersProvider } from './context/UsersContext';

function App() {
  
  return (
    <UsersProvider>
      <div className="App">
        <header className="main-header default-wrapper">
          <Search />
        </header>
        <Employees />
      </div>
    </UsersProvider>
  );
}

export default App;
