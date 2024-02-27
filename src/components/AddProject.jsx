export default function AddProject(props){
    return(
        <div className="flex flex-col h-full w-1/2 justify-center">
            <div className="flex flex-col">
                <label>Project Title:</label>
                <input type="text" className="shadow-sm border border-grey-200" id='projectTitle'/>
                <label>Tools Used (Serperate with " , "):</label>
                <input type="text" className="shadow-sm border border-grey-200" id='Tools'/>
                <h2 className="pt-10 pb-3">-Please provide single sentence descriptions of your project-</h2>
                <label>Description:</label>
                <input type="text" className="shadow-sm border border-grey-200" id='description1'/>
                <label>Description:</label>
                <input type="text" className="shadow-sm border border-grey-200" id='description2'/>
                <label>Description:</label>
                <input type="text" className="shadow-sm border border-grey-200" id='description3'/>
                <label>Description:</label>
                <input type="text" className="shadow-sm border border-grey-200" id='description4'/>
            </div>
        </div>
    )
}