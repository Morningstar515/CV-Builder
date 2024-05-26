

export default function AddTechnicalSkills(props){
    const handleSkillsHeader = (e) => {
        props.resumeObj["skillHeader" + (props.id + 1)] = e.target.value
    }
    const handleSkills = (e) => {
        props.resumeObj["skill" + (props.id + 1)] = e.target.value
    }


    return (
        <div className="flex flex-col gap-4 justify-center">
            <h1 className="flex float-left">Skill set-{props.id + 1}</h1>

            <div className="flex flex-col mb-6">
                <label htmlFor="">Skills Header</label>
                <input type="text" className="shadow-sm border border-grey-200" id='skillTitle' onChange={handleSkillsHeader}/>
                <label htmlFor="">Skills Listed (Separate by  " , " )</label>
                <input type="text" className="shadow-sm border border-grey-200" id='skills' onChange={handleSkills}/>
            </div>


        </div>
    )
}