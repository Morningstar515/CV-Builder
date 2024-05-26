export default function AddExperience(props){

    const handlePosition = (e) =>{
        props.resumeObj["experienceTitle" + (props.id + 1)] = e.target.value;
    }
    
    const handleCompanyName = (e) =>{
        props.resumeObj["companyName" + (props.id + 1)] = e.target.value;
    }

    const handleStartDate = (e) =>{
        props.resumeObj["startDate" + (props.id + 1)] = e.target.value;
    }

    const handleEndDate = (e) =>{
        props.resumeObj["endDate" + (props.id + 1)] = e.target.value;
    }

    const handleLocation = (e) =>{
        props.resumeObj["location" + (props.id + 1)] = e.target.value;
    }

    const handleDescriptionOne = (e) =>{
        props.resumeObj["descriptionA" + (props.id + 1)] = e.target.value;
    }

    const handleDescriptionTwo = (e) =>{
        props.resumeObj["descriptionB" + (props.id + 1)] = e.target.value;
    }

    const handleDescriptionThree = (e) =>{
        props.resumeObj["descriptionC" + (props.id + 1)] = e.target.value;
    }

    const handleDescriptionFour = (e) =>{
        props.resumeObj["descriptionD" + (props.id + 1)] = e.target.value;
    }

    
    
    
    

    return(
        <div className="flex flex-col min-w-[1000px] bg-white justify-evenly items-center m-10 border-b-2 border-black p-2">
        <form action="" className='flex flex-col' id='experienceForm'>
            <div className="flex flex-row gap-5 justify-between">
                <div className='flex flex-col h-1/2 w-1/2'>
                    <label>Position Title:</label>
                    <input type="text" onChange={handlePosition} className="shadow-sm border border-grey-200" id='position'/>
                    <label>Company Name:</label>
                    <input type="text" onChange={handleCompanyName} className="shadow-sm border border-grey-200" id='companyName'/>
                </div>
                <div className="flex flex-col h-1/2 w-1/2">    
                    <label>Start Date:</label>
                    <input type="text" onChange={handleStartDate} className="shadow-sm border border-grey-200" id='startDate'/>
                    <label>End Date:</label>
                    <input type="text" onChange={handleEndDate} className="shadow-sm border border-grey-200" id='endDate'/>
                    <label>Location:</label>
                    <input type="text" onChange={handleLocation} className="shadow-sm border border-grey-200" id='location'/>
                </div>
            </div>
            <div className="flex flex-col gap-3">
                <label>Description 1:</label>
                <input type="text" onChange={handleDescriptionOne} className="shadow-sm border border-grey-200" id='description1'/>
                <label>Description 2:</label>
                <input type="text" onChange={handleDescriptionTwo} className="shadow-sm border border-grey-200" id='description2'/>
                <label>Description 3:</label>
                <input type="text" onChange={handleDescriptionThree} className="shadow-sm border border-grey-200" id='description3'/>
                <label>Description 4:</label>
                <input type="text" onChange={handleDescriptionFour} className="shadow-sm border border-grey-200" id='description4'/>
            </div>
        </form>
    </div>
    )

}