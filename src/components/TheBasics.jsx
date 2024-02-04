import { useState } from 'react'

export default function TheBasics(){

    return (
        <>
            <h1 className="text-5xl italic font-medium">Lets start with the basics!</h1>
            <div className="flex flex-col w-2/5 h-1/2 shadow-lg rounded-2xl bg-white justify-evenly items-center" id='main'>
                <form action="" className='flex gap-24'>
                    <div className='flex flex-col gap-3 mt-9'>
                        <label>Name:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='John'/>
                        <label>Phone:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='Smith'/>
                        <label>Email:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='JohnSmith@domain.com'/>
                    </div>
                    <div className='flex flex-col gap-3'>
                        <h1>(Optionals)</h1>
                        <label>Github:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='JohnSmith@github.com'/>
                        <label>LinkedIn:</label>
                        <input type="text" className="shadow-sm border border-grey-200" placeholder='JohnSmith@LinkedIn.com'/>
                        <label>Portfolio:</label>
                        <input type="text" className="shadow-sm border border-grey-200" />
                    </div>

                </form>
                <button className="h-10 w-24 bg-blue-400 text-white rounded-md hover:bg-blue-500 font-medium text-xl">Next</button>
            </div>
        </>
    )
}