import React from 'react'
import "./recipetile.css"
export default function RecipeTile({recipe}) {
    return (
        <div className="RecipeTile"onClick={()=>{
            window.open(recipe["recipe" ]["url"])
        }}>
            <img className="rt_img" src={recipe["recipe"]["image"]}/>
        <p className="rt_name" >{recipe["recipe" ]["label"]}</p>
        </div>
    );
}
 