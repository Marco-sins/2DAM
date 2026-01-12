import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './styles/App.css'
import { CardVideojuego } from './components/CardVideojuego'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        {CardVideojuego()}
      </div>
    </>
  )
}

export default App
