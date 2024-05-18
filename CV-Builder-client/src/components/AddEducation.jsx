import { useState } from "react"

export default function AddEducation(props){

    /*Note: Using states to set data has strange behavior when "add school" clicked more than allowed times*/
    const handleSchoolName = (e) => {
        switch(props.id){
            case(0):
                ///setSchoolName(e.target.value)
                props.resumeObj.schoolName = e.target.value;
                break;

            case(1):
                props.resumeObj.secondSchoolName = e.target.value;
                break;
                
            case(2):
                props.resumeObj.finalSchoolName = e.target.value;        
                break;
        }
    }
    const handleMajor = (e) => {
        switch(props.id){
            case(0):
                props.resumeObj.major = e.target.value;
                break;                

            case(1):
                props.resumeObj.secondMajor = e.target.value;
                break;
                
            case(2):
                props.resumeObj.finalMajor= e.target.value;        
                break;
        }
    }
    const handleMinor = (e) => {
        switch(props.id){
            case(0):
                props.resumeObj.minor = e.target.value;
                break;
                
            case(1):
                props.resumeObj.secondMinor = e.target.value;
                break;
                
            case(2):
                props.resumeObj.finalMinor = e.target.value;        
                break;
        }
    }
    const handleStartDate = (e) => {
        switch(props.id){
            case(0):
                props.resumeObj.startDate = e.target.value;
                break;
                
            case(1):
                props.resumeObj.secondStartDate = e.target.value;
                break;
                
            case(2):
                props.resumeObj.finalStartDate = e.target.value;        
                break;
        }
    }
    const handleEndDate = (e) => {
        switch(props.id){
            case(0):
                props.resumeObj.endDate = e.target.value;
                break;

            case(1):
                props.resumeObj.secondEndDate = e.target.value;
                break;
                
            case(2):
                props.resumeObj.finalEndDate = e.target.value;        
                break;
        }
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
                    <input type="text" onChange={handleMajor} className="shadow-sm border border-grey-200" placeholder='Major' id='name'/>
                    <label>Start Date:</label>
                    <input type="text" onChange={handleStartDate} className="shadow-sm border border-grey-200" placeholder='Start' id='phone'/>
                </div>
                <div className="flex flex-col gap-2">    
                    <label>Minor:</label>
                    <input type="text" onChange={handleMinor} className="shadow-sm border border-grey-200" placeholder='Minor' id='name'/>
                    <label>End Date:</label>
                    <input type="text" onChange={handleEndDate} className="shadow-sm border border-grey-200" placeholder='End' id='phone'/>
                </div>
            </div>
        </form>    
    </div>
    )
}