import { useState } from "react";
import AddExperience from "./AddExperience";
import Projects from "./Projects";

export default function Experience(props){
    const[experience,setExperience] = useState(1);
    let experienceArray = [];

    for (let i = 0; i < experience; i++) {
        experienceArray.push(<AddExperience key={i} resumeObj = {props.resumeObj} id={i}/>)
        
    }
    const handleExperience = () => {
        setExperience((count) => count + 1)
    }

    const append = () => {
        handleExperience(experienceArray);
    }

    return(
        <>
            <h1 className="text-5xl italic font-medium mb-4">Tell us about your work experience</h1>
            <div className="flex flex-col min-w-[1000px] h-2/3 shadow-lg rounded-2xl bg-white items-center overflow-scroll" id='main'>
                {experienceArray}
            </div>
            <button onClick={append} className="flex w-1/5 min-h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add Experience</button>
            <button form="EducationForm" onClick={()=> {props.change(<Projects change={props.change} resumeObj = {props.resumeObj}/>)}} className="mn-10 min-h-10 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>

        </>
    )
}