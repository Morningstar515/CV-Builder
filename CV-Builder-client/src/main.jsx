import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link
} from 'react-router-dom'
import TheBasics from './components/TheBasics.jsx'
import EducationAndMore from './components/EducationAndMore.jsx'
import Experience from './components/Experience.jsx'
import Projects from './components/Projects.jsx'
import TechnicalSkills from './components/TechnicalSkills.jsx'
import PDFViewer from './components/PDFViewer.jsx'

const router = createBrowserRouter([
{
  path: "/",
  element: <App/>,
  errorElement: <p>404</p>
},

{
  path: "/ihope.pdf",
  element: <PDFViewer/>,
  errorElement: <p>404</p>
},

{
  path: "/thebasics",
  element: <TheBasics/>,
  errorElement: <p>404</p>
},

{
  path: "/school",
  element: <EducationAndMore/>,
  errorElement: <p>404</p>
},

{
  path: "/experience",
  element: <Experience/>,
  errorElement: <p>404</p>
},

{
  path: "/projects",
  element: <Projects/>,
  errorElement: <p>404</p>
},

{
  path: "/technicalskills",
  element: <TechnicalSkills/>,
  errorElement: <p>404</p>
},



])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router = {router}/>
  </React.StrictMode>,
)
