

export default function AddTechnicalSkills(props){
    return (
        <div className="flex flex-col gap-4 justify-center">
            <h1 className="flex float-left">Skill set-{props.id + 1}</h1>

            <div className="flex flex-col mb-6">
                <label htmlFor="">Skills Header</label>
                <input type="text" className="shadow-sm border border-grey-200" id='skillTitle' onChange={(e) => props.resumeObj[e.target.id + props.id] = e.target.value}/>
                    {console.log(props.resumeObj)}
                <label htmlFor="">Skills Listed (Separate by  " , " )</label>
                <input type="text" className="shadow-sm border border-grey-200" id='skills'/>
            </div>


        </div>
    )
}