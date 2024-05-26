import { useState } from "react";
import AddTechnicalSkills from "./AddTechnicalSkills";
import BuildResume from "./BuildResume";

export default function TechnicalSkills(props){
    const[technicalSkill,setTechnicalSkill] = useState([]);
    let i = 0


    const updatePdf = () => {
        technicalSkill.forEach(item => {
        // Dynamically set keys and values based on variables
        let info = {
            ["SKILLSTITLE" + (item.props.id + 1)]: props.resumeObj["skillHeader" + (item.props.id + 1)],
            ["SKILLS" + (item.props.id + 1)]: props.resumeObj["skill" + (item.props.id + 1)],

            ["count"]: [item.props.id + 1]
        };


        fetch("http://localhost:5000/parseSkills", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(info)
        })
            .then((res) => res.json())
            .then((data) => {
            console.log(info)
                props.refresh()
            })
        });
    }

    function callHeader(){
        if (technicalSkill.length < 1){
            fetch("http://localhost:5000/addSkills", {
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

    const append = () => {
        setTechnicalSkill(technicalSkill => [...technicalSkill, <AddTechnicalSkills key={technicalSkill.length} resumeObj = {props.resumeObj} id={technicalSkill.length}/>])
        i++
    }
    
    return(
        <>
            <h1 className="text-5xl italic font-medium mb-4">Lets go over your technical skills</h1>
            <div className="flex flex-col min-w-[1000px] h-2/3 shadow-lg rounded-2xl bg-white items-center overflow-scroll" id='main'>
                {technicalSkill}
            </div>
            <button onClick={() => {append();callHeader()}} className="flex w-1/5 min-h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add skill set</button>
            <button form="EducationForm" onClick={()=> {updatePdf()}} className="mn-10 mt-4 min-h-10 w-1/6 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Finalize Resume</button>

        </>
    )
}