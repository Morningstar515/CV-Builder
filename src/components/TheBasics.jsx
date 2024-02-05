import { useState } from 'react'

export default function TheBasics(){

    //OnClick putting data into object to be passed along
    function resumeObject(e){
        e.preventDefault();
        let resumeObj = {
            name: name,
            phone:"",
            email:"",
            github:"",
            linkedin:"",
            portfolio:"",
        }

        console.log(resumeObj)
    }

    const [name,setName] = useState("");
    const [phone,setPhone] = useState("");
    const [email,setEmail] = useState("");
    const [github,setGithub] = useState("");
    const [linkedin,setLinkedin] = useState("");
    const [portfolio,setPortfolio] = useState("");

    const handleName = (e) => {
        setName(e.target.value)
    }



    return (
        <>
            <h1 className="text-5xl italic font-medium">Lets start with the basics!</h1>
            <div className="flex flex-col w-2/5 h-1/2 shadow-lg rounded-2xl bg-white justify-evenly items-center" id='main'>
                <form action="" className='flex gap-24' id='basicsForm'>
                    <div className='flex flex-col gap-3 mt-9'>
                        <label>Name:</label>
                        <input type="text" value={name} onChange={handleName} className="shadow-sm border border-grey-200" placeholder='John' id='name'/>
                        <label>Phone:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='Smith' id='phone'/>
                        <label>Email:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='JohnSmith@domain.com' id='phone'/>
                    </div>
                    <div className='flex flex-col gap-3'>
                        <h1>(Optionals)</h1>
                        <label>Github:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='JohnSmith@github.com' id='github'/>
                        <label>LinkedIn:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='JohnSmith@LinkedIn.com' id='linkedin'/>
                        <label>Portfolio:</label>
                        <input type="text" className="shadow-sm border border-grey-200" id='portfolio'/>
                    </div>
                </form>
                <button form="basicsForm" onClick={resumeObject} className="h-10 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>
            </div>
        </>
    )
}