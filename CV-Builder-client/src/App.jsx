import { useEffect, useState } from 'react'
import Hero from './components/Hero'
import TheBasics from './components/TheBasics'
import axios from 'axios'
import './App.css'
import PDFViewer from './components/PDFViewer'
import ReactPDF from '@react-pdf/renderer'


function App() {


	const [state,setState] = useState(<Hero change = {handleState}/>);

	function handleState(next){
		setState(next)
	}



	return (
		<div className='flex flex-row w-screen h-screen justify-center items-center gap-4 bg-slate-100'>
			<div className='flex flex-col w-2/3 h-full justify-center items-center'>
				{state}
			</div>
			<div className='w-1/3 h-full m-4'>
				<iframe src="./ihope.pdf" width='100%' height='80%' />
			</div>
		</div>


	)
}

export default App



