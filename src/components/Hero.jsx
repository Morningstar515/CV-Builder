import TheBasics from "./TheBasics"
import { useState } from 'react'

export default function Hero(props){
    return (
        <>
            <h1 className="text-5xl italic font-medium">CV-Builder</h1>
            <div className="flex flex-col w-1/3 h-1/4 shadow-lg rounded-2xl bg-white justify-evenly items-center">
                <h3 className="text-2xl italic">The premier resume building application</h3>
                <button onClick = { () => props.change(<TheBasics change = {props.change}/>)} className="h-1/6 w-1/3 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Get Started!</button>
            </div>
        </>
    )
}