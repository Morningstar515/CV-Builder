import AddProject from "./AddProject";
import { useState } from "react";
import TechnicalSkills from './TechnicalSkills'

export default function Projects(props){
    const[projects,setProjects] = useState(0);
    let projectsArray = [];

    const updatePdf = () => {
        projectsArray.forEach(item => {
        // Dynamically set keys and values based on variables
        let info = {
            ["PROJECTTITLE" + (item.props.id + 1)]: props.resumeObj["projectTitle" + (item.props.id + 1)],
            ["TECHLIST" + (item.props.id + 1)]: props.resumeObj["toolsUsed" + (item.props.id + 1)],
            ["PROJECT" + (item.props.id + 1) + "BULLET1"]: props.resumeObj["descriptionA" + (item.props.id + 1)],
            ["PROJECT" + (item.props.id + 1) + "BULLET2"]: props.resumeObj["descriptionB" + (item.props.id + 1)],
            ["PROJECT" + (item.props.id + 1) + "BULLET3"]: props.resumeObj["descriptionC" + (item.props.id + 1)],
            ["PROJECT" + (item.props.id + 1) + "BULLET4"]: props.resumeObj["descriptionD" + (item.props.id + 1)],
            ["count"]: [item.props.id + 1]
        };


        fetch("http://localhost:5000/parseProjects", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(info)
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(info)
                console.log(props.resumeObj)

                props.refresh()
            })
        });
    
    }

    function callHeader(){
        if (projectsArray.length < 1){
            fetch("http://localhost:5000/addProjects", {
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



    for (let i = 0; i < projects; i++) {
        projectsArray.push(<AddProject key={i} resumeObj = {props.resumeObj} id={i}/>)
        
    }
    const handleProjects = () => {
        setProjects((count) => count + 1)
    }

    const append = () => {
        handleProjects(projectsArray);
    }

    return(
        <>
            <h1 className="text-5xl italic font-medium mb-4">Have you completed any projects?</h1>
            <div className="flex flex-col min-w-[1000px] h-2/3 shadow-lg rounded-2xl bg-white items-center overflow-scroll" id='main'>
                {projectsArray}
            </div>
            <button onClick={() => {append();callHeader()}} className="flex w-1/5 min-h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add Project</button>
            <button form="EducationForm" onClick={()=> {props.change(<TechnicalSkills change ={props.change} resumeObj = {props.resumeObj} refresh={props.refresh}/>);updatePdf()}} className="mn-10 min-h-10 mt-4 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>

        </>
    )
}