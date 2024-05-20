import { useEffect, useState } from "react"
import axios from 'axios'
import { parse, HtmlGenerator } from 'latex.js'


// Make a new html file from string


export default function BuildResume(props){

    const [template, setTemplate] = useState();

    const fetchAPI = async () => {
        const res = await axios.get("http://localhost:5000/jakes")
        setTemplate(res.data)

        console.log('asda')
        createfile(res.data)

        }


    const createfile = async (data) => {
        console.log(data)

        const createfile = async (data) => {
            console.log(data)
    
            fetch('/parseLatex', {
                method: 'POST',
                headers: {
                    "Content-Type":'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(function (res) {
                console.log(res);
        })    
        }
        
    }

        useEffect(()=>{
            let r = fetchAPI()
            console.log(r)
        },[])

    }
    






