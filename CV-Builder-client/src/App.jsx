import { useEffect, useState } from 'react'
import Hero from './components/Hero'
import TheBasics from './components/TheBasics'
import axios from 'axios'
import './App.css'

function App() {


const fetchAPI = async () => {
	const res = await axios.get("http://localhost:5000/hello")
	console.log(res)
}

useEffect(()=>{
	fetchAPI()
},[])
	const [state,setState] = useState(<Hero change = {handleState}/>);

	function handleState(next){
		setState(next)
	}



	return (
		<div className='flex flex-col w-screen h-screen justify-center items-center gap-4 bg-slate-100'>
			{state}

		</div>
		
	)
}

export default App



