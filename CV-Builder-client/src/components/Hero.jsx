import TheBasics from "./TheBasics"
import { useEffect, useState } from 'react'

export default function Hero(props){
const [selectedTemp,setSelectedTemp] = useState("Jakes")

useEffect( ()=> {
    showSelected(selectedTemp)
},[])

const handleSelected = (selected) => {
    setSelectedTemp(selected)
    showSelected(selected)
}

function baseTex(value){
    fetch("http://localhost:5000/baseTex", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            base: value
        })
    })
    .then((res) => res.json())
    .then((data) =>{
        //
    })
}

function showSelected(template){
    fetch("http://localhost:5000/default", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            template: template
        })
    })
    .then((res) => res.json())
    .then((data) =>{
        props.refresh()
    })
}

function chosenTemplate(value){
    fetch("http://localhost:5000/setTemplate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            template: value
        })
    })
    .then((res) => res.json())
    .then((data) =>{
        baseTex(value)
    })
}



    return (
        <>
            <h1 className="text-5xl italic font-medium">CV-Builder</h1>
            <div className="flex flex-col w-2/3 h-1/4 shadow-lg rounded-2xl bg-white justify-evenly items-center">
                <h3 className="text-2xl italic">The premier resume building application</h3>
                <label htmlFor="templates">Choose a Template:</label>
                <select name="template" id="templates"  onChange={(e) => {handleSelected(e.target.value)}}>
                    <option value="Jakes">Jakes Simple</option>
                    <option value="Stylish">Stylish</option>
                </select> 
                <button onClick = { () => {props.change(<TheBasics change = {props.change} refresh={props.refresh}/>);chosenTemplate(selectedTemp)}} className="h-1/6 w-1/3 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Get Started!</button>
            </div>
        </>
    )
}