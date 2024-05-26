export default function AddProject(props){

    const handleProjectTitle = (e) => {
        props.resumeObj["projectTitle" + (props.id + 1)] = e.target.value;
    }
    const handleTools = (e) => {
        props.resumeObj["toolsUsed" + (props.id + 1)] = e.target.value;
    }
    const handleDescription1 = (e) => {
        props.resumeObj["descriptionA" + (props.id + 1)] = e.target.value;
    }
    const handleDescription2 = (e) => {
        props.resumeObj["descriptionB" + (props.id + 1)] = e.target.value;
    }
    const handleDescription3 = (e) => {
        props.resumeObj["descriptionC" + (props.id + 1)] = e.target.value;
    }
    const handleDescription4 = (e) => {
        props.resumeObj["descriptionD" + (props.id + 1)] = e.target.value;
    }

    return(
        
        <div className="flex h-full w-1/2 justify-center">
            <p className="flex float-left pl-4">Project-{props.id + 1}:</p>
            <div className="flex flex-col border-b-2 border-black pb-4">
                <label>Project Title:</label>
                <input type="text" onChange={handleProjectTitle} className="shadow-sm border border-grey-200" id='projectTitle'/>
                <label>Tools Used (Serperate with " , "):</label>
                <input type="text" onChange={handleTools} className="shadow-sm border border-grey-200" id='Tools'/>
                <h2 className="pt-10 pb-4">-Please provide single sentence descriptions of your project-</h2>
                <label>Description:</label>
                <input type="text"  onChange={handleDescription1} className="shadow-sm border border-grey-200" id='description1'/>
                <label>Description:</label>
                <input type="text" onChange={handleDescription2} className="shadow-sm border border-grey-200" id='description2'/>
                <label>Description:</label>
                <input type="text" onChange={handleDescription3} className="shadow-sm border border-grey-200" id='description3'/>
                <label>Description:</label>
                <input type="text" onChange={handleDescription4} className="shadow-sm border border-grey-200" id='description4'/>
            </div>
        </div>
    )
}