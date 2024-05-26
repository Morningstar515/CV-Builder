import { useEffect, useState } from 'react'
import Hero from './components/Hero'
import TheBasics from './components/TheBasics'
import axios from 'axios'
import './App.css'
import ReactPDF from '@react-pdf/renderer'


function App() {


	const [state,setState] = useState(<Hero change = {handleState} refresh={refresh}/>);

	function handleState(next){
		setState(next)
	}

	function refresh(){
		let x = document.getElementById("frame");
		x.contentWindow.location.reload();
	}
	function reset(){
		handleState(<Hero change = {handleState} refresh={refresh}/>)
		fetch('http://localhost:5000/default',{
			method: "GET",
			headers: {
				'Content-Type': "application/json"
			},
		})
		.then((res) => res.json())
		.then((data) => refresh())
	}


	return (
		<div className='flex flex-row w-screen h-screen justify-center items-center gap-4 bg-slate-100'>
			<div className='flex flex-col w-2/3 h-full justify-center items-center'>
				{state}
			</div>
			<div className='flex flex-col w-1/3 h-full m-4 justify-center items-center gap-4'>
				<iframe id="frame" src="./ihope.pdf" width='100%' height='80%' />
				<button className="h-10 w-1/3 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl" onClick={reset}>Restart Form</button>
			</div>
		</div>
	)
}

export default App



