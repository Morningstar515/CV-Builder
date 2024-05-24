import AddEducation from "./AddEducation";
import { useState } from "react";
import Experience from "./Experience";

export default function EducationAndMore(props){
    const [addEducation,setEducation] = useState(0);
    let schoolArray = [];

    const updatePdf = () => {
        schoolArray.forEach(item => {
        // Dynamically set keys and values based on variables
        let info = {
            ["SCHOOL" + (item.props.id + 1)]: props.resumeObj["schoolName" + (item.props.id + 1)],
            ["DEGREE" + (item.props.id + 1)]: props.resumeObj["major" + (item.props.id + 1)],
            ["SCHOOLLOCATION" + (item.props.id + 1)]: props.resumeObj["city" + (item.props.id + 1)],
            ["SCHOOLSTATE" + (item.props.id + 1)]: props.resumeObj["state" + (item.props.id + 1)],
            ["DEGREESTART" + (item.props.id + 1)]: props.resumeObj["startDate" + (item.props.id + 1)],
            ["DEGREEEND" + (item.props.id + 1)]: props.resumeObj["endDate" + (item.props.id + 1)]
        };
        console.log(info)


        fetch("http://localhost:5000/parseEducation", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(info)
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data)
                props.refresh()
            })
        });
    
    }


    function handleEducation(){
        setEducation((count) => count + 1);
    }

    // Populate with AddEducation component
    for (let i = 0; i < addEducation; i++) {
        if(i > 2){
            break; /*Limits how many education adds */
        }
        schoolArray.push(<AddEducation key={i} resumeObj = {props.resumeObj} id={i} schoolArray={schoolArray}/>);
    }

    function append(){
        handleEducation(schoolArray);
        console.log(props.resumeObj)
    }

    return(
        <>
            <h1 className="text-5xl italic font-medium">Did you go to school?</h1>
            <div className="flex flex-col min-w-[800px] h-1/2 shadow-lg rounded-2xl bg-white items-center p-3 overflow-scroll" id='main'>
                {schoolArray}
            </div>
            <button onClick={append} className="flex w-1/5 h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add School</button>
            <button form="EducationForm" onClick={()=> {props.change(<Experience change={props.change} resumeObj = {props.resumeObj}/>); updatePdf()}} className="h-10 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>

        </>
    )
}