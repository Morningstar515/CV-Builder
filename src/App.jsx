import { useState } from 'react'
import Hero from './components/Hero'
import TheBasics from './components/TheBasics'
import './App.css'

function App() {

	let resumeObj = {
		name:"",
		phone:"",
		email:"",
		github:"",
		linkedin:"",
		portfolio:"",
	}

	const [state,setState] = useState(<Hero change = {handleState}/>);

	function handleState(){
		setState(<TheBasics/>)
	}
	return (
		<div className='flex flex-col w-screen h-screen justify-center items-center gap-24 bg-slate-100'>
			{state}
		</div>
	)
}

export default App
