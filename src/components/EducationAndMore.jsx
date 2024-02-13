import AddEducation from "./AddEducation";
import { useState } from "react";
import Experience from "./Experience";


export default function EducationAndMore(props){
    const [addEducation,setEducation] = useState(0);
    let schoolArray = [];

    function handleEducation(){
        setEducation((count) => count + 1);
    }

    // Populate with AddEducation component
    for (let i = 0; i < addEducation; i++) {
        if(i > 2){
            break; /*Limits how many education adds */
        }
        schoolArray.push(<AddEducation key={i} resumeObj = {props.resumeObj} id={i}/>);
    }

    function append(){
        handleEducation(schoolArray);
    }

    return(
        <>
            <h1 className="text-5xl italic font-medium">Did you go to school?</h1>
            <div className="flex flex-col min-w-[800px] h-1/2 shadow-lg rounded-2xl bg-white justify-evenly items-center p-3" id='main'>
                {schoolArray}
                <button onClick={append} className="flex w-1/5 h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add School</button>
                <button form="EducationForm" onClick={()=> {props.change(<Experience change={props.change} />); console.log(props.resumeObj)}} className="h-10 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>
            </div>
        </>
    )
}