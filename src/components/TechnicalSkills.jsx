export default function TechnicalSkills(props){
    const[technicalSkill,setTechnicalSkill] = useState(1);
    let skillsArray = [];

    for (let i = 0; i < skillsArray; i++) {
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
                {skillsArray}
            </div>
            <button onClick={append} className="flex w-1/5 min-h-10 bg-blue-400 rounded-md text-white justify-center items-center">Add Project</button>
            <button form="EducationForm" onClick={()=> {console.log(props.resumeObj)}} className="mn-10 min-h-10 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>

        </>
    )
}