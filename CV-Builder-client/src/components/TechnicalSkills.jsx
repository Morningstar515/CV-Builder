import { useState } from "react";
import AddTechnicalSkills from "./AddTechnicalSkills";
import BuildResume from "./BuildResume";

export default function TechnicalSkills(props){
    const[technicalSkill,setTechnicalSkill] = useState([]);
    let i = 0

    const append = () => {

        setTechnicalSkill(technicalSkill => [...technicalSkill, <AddTechnicalSkills key={technicalSkill.length} resumeObj = {props.resumeObj} id={technicalSkill.length}/>])
        i++
        console.log(technicalSkill)
    }
    
    return(
        <>
            <h1 className="text-5xl italic font-medium mb-4">Lets go over your technical skills</h1>
            <div className="flex flex-col min-w-[1000px] h-2/3 shadow-lg rounded-2xl bg-white items-center overflow-scroll" id='main'>
                {technicalSkill}
            </div>
            <button onClick={append} className="flex w-1/5 min-h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add skill set</button>
            <button form="EducationForm" onClick={()=> {props.change(<BuildResume resumeObj = {props.resumeObj}/>)}} className="mn-10 mt-4 min-h-10 w-1/6 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Finalize Resume</button>

        </>
    )
}