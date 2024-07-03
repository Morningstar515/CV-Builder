
export default function AddEducation(props){

    /*Note: Using states to set data has strange behavior when "add school" clicked more than allowed times*/
    const handleSchoolName = (e) => {
        props.resumeObj["schoolName" + (props.id + 1)] = e.target.value;
 
    }
    const handleMajor = (e) => {
        props.resumeObj["major" + (props.id + 1)] = e.target.value;
        
    }
    const handleCity = (e) => {
        props.resumeObj["city" + (props.id + 1)] = e.target.value;
    }
    const handleState = (e) => {
        props.resumeObj["state" + (props.id + 1)] = e.target.value;
    }
    
    const handleStartDate = (e) => { 
        props.resumeObj["startDate" + (props.id + 1)] = e.target.value;
    }
    const handleEndDate = (e) => {
        props.resumeObj["endDate" + (props.id + 1)] = e.target.value;
    }
    return(
    <div className="flex w-full h-auto">
        <p className="float-left">Education-{props.id + 1}:</p>
        <form action="" className='flex gap-24 w-full justify-center' id='EducationForm'>
            <div className='flex gap-3 border-b-2 p-3 border-black'>
                <div className="flex flex-col gap-2">
                    <label>School Name:</label>
                    <input type="text" onChange={handleSchoolName} className="shadow-sm border border-grey-200" placeholder='University' id='name'/>
                    <label>Major:</label>
                    <input type="text" onChange={handleMajor} className="shadow-sm border border-grey-200" placeholder='Major' id={"major"}/>
                    <label>Start Date:</label>
                    <input type="text" onChange={handleStartDate} className="shadow-sm border border-grey-200" placeholder='Start' id='phone'/>
                </div>
                <div className="flex flex-col gap-2">    
                    <label>City:</label>
                    <input type="text" onChange={handleCity} className="shadow-sm border border-grey-200" placeholder='City' id='name'/>
                    <label>State Abreveate "ex. CA":</label>
                    <input type="text" onChange={handleState} className="shadow-sm border border-grey-200" placeholder='State' id='name'/>
                    <label>End Date:</label>
                    <input type="text" onChange={handleEndDate} className="shadow-sm border border-grey-200" placeholder='End' id='phone'/>
                </div>
            </div>
        </form>    
    </div>
    )
}