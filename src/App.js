
import './App.css';
import Axios from "axios";
import {useState} from "react";
import RecipeTile from "./RecipeTile.js";

function App() {
  const [query,setquery]=useState("");
  const[recipes,setrecipes]=useState([]);
  const [healthLabels,sethealthLabels]=useState("vegan")

  const apiURL = "https://api.edamam.com/search?q=";
  const apiKey = "&app_key=5694759373c7b6d97f52d44a83a0a3e8	";
  const apiId = "&app_id=adb74951";
  const health="&health=";
 
  var url = `${apiURL}${query}${apiId}${apiKey}${health}${healthLabels}`;
  
  async function getRecipes(){
    var result=await Axios.get(url);
    setrecipes(result.data.hits);
    console.log(result.data);
    
  }
  const onSubmit=(e)=>{
    e.preventDefault();
    getRecipes();
  }
  
  return (
    <div className="App">
     <h1 >Recipe Plaza 🍜</h1>
     <form className="app_searchForm" onSubmit={onSubmit}>
      < input type="text"
      className="app_input"
       placeholder="enter ingredients"
      value={query} onChange={(e)=>setquery(e.target.value)}/>
      <input  type="submit" className="app_submit" value="search"/>


    <select className="app_healthlabel">
      <option onClick ={()=>sethealthLabels("vegan")}>vegan</option>
      <option onClick ={()=>sethealthLabels("vegetarian")}>vegetarian</option>
      <option onClick ={()=>sethealthLabels("paleo")}>paleo</option>
      <option onClick ={()=>sethealthLabels("dairy-free")}>dairy-free</option>
      <option onClick ={()=>sethealthLabels("gluten-free")}>gluten-free</option>
      <option onClick ={()=>sethealthLabels("low-sugar")}>low-sugar</option>
    
    
    </select>
     </form>
     <div class="sachi">
      
      </div>
     <div className="app_rec">
      {recipes.map((recipe)=>{
        return < RecipeTile recipe={recipe}/>;

      })}
     </div>

    </div>
   
  );
}

export default App;
 