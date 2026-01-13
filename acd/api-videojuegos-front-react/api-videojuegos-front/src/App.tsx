import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './styles/App.css'
import { Home } from './pages/Home'
import { AñadirVideojuego } from './pages/AñadirVideojuego'
import { DetallesVideojuego } from './pages/DetallesVideojuego'

function App() {

  return (
    <Router> {/* Router envuelve toda la app */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/crear-videojuego" element={<AñadirVideojuego />} />
        <Route path="/detalle-videojuego/:id" element={<DetallesVideojuego />} />
      </Routes>
    </Router>
  )
}

export default App
