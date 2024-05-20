import { useEffect, useState } from 'react'
import Hero from './components/Hero'
import TheBasics from './components/TheBasics'
import axios from 'axios'
import './App.css'

function App() {



	const [state,setState] = useState(<Hero change = {handleState}/>);

	function handleState(next){
		setState(next)
	}

	console.log('\\')


	return (
		<div className='flex flex-col w-screen h-screen justify-center items-center gap-4 bg-slate-100'>
			{state}

		</div>
		
	)
}

export default App



