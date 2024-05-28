import { useState } from "react";
import AddExperience from "./AddExperience";
import Projects from "./Projects";

export default function Experience(props){
    const[experience,setExperience] = useState(0);
    let experienceArray = [];

    const updatePdf = () => {
        experienceArray.forEach(item => {
        // Dynamically set keys and values based on variables
        let info = {
            ["TITLE" + (item.props.id + 1)]: props.resumeObj["experienceTitle" + (item.props.id + 1)],
            ["STARTDATE" + (item.props.id + 1)]: props.resumeObj["startDate" + (item.props.id + 1)],
            ["ENDDATE" + (item.props.id + 1)]: props.resumeObj["endDate" + (item.props.id + 1)],
            ["COMPANY" + (item.props.id + 1)]: props.resumeObj["companyName" + (item.props.id + 1)],
            ["LOCATION" + (item.props.id + 1)]: props.resumeObj["location" + (item.props.id + 1)],
            ["STATE" + (item.props.id + 1)]: props.resumeObj["state" + (item.props.id + 1)],
            ["EXPERIENCE" + (item.props.id + 1) + "BULLET1"]: props.resumeObj["descriptionA" + (item.props.id + 1)],
            ["EXPERIENCE" + (item.props.id + 1) + "BULLET2"]: props.resumeObj["descriptionB" + (item.props.id + 1)],
            ["EXPERIENCE" + (item.props.id + 1) + "BULLET3"]: props.resumeObj["descriptionC" + (item.props.id + 1)],
            ["EXPERIENCE" + (item.props.id + 1) + "BULLET4"]: props.resumeObj["descriptionD" + (item.props.id + 1)],
            ["count"]: [item.props.id + 1]
        };


        fetch("http://localhost:5000/parseExperience", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(info)
        })
            .then((res) => res.json())
            .then((data) => {
                props.refresh()
            })
        });
    
    }
    

    function callHeader(){
        if (experienceArray.length < 1){
            fetch("http://localhost:5000/addExperience", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            })
                .then((res) => res.json())
                .then((data) => {
                    props.refresh()
                })
        }
    }



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
            <button onClick={() => {append();callHeader()}} className="flex w-1/5 min-h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add Experience</button>
            <button form="EducationForm" onClick={()=> {props.change(<Projects change={props.change} resumeObj = {props.resumeObj} refresh={props.refresh}/>);updatePdf()}} className="mn-10 min-h-10 mt-4 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>

        </>
    )
}