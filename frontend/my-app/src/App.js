import './App.css';
import {useState} from 'react'
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Home from './components/Home/Home'
// function CreateTask({addTodo}) {
//   const [value , setValue] = useState('')
//   const handleSubmit = e => {
//     e.preventDefault()
//     if (!value) return ;
//     addTodo( value)
//     setValue('')
//   }

//   return(
//     <form onSubmit={handleSubmit}>
//       <input type='text' value ={value} onChange = { e => setValue(e.target.value)}/>
//     </form>
//   );

// }


function App() {
  // const [todos , setTodos] = useState([])


  // const addTodo = (value) => {
  //   const newTodos = [...todos, value] 
  //   setTodos(newTodos)

  // }
  return (
  // <div>
  //   <p> Todo app </p>
  //   <CreateTask addTodo={addTodo}/>
  //   <div>
  //     { todos.map(todo => {return (<p> {todo}</p> )})}
  //   </div>
  //   </div>

  <div className="app">
    <Router>
      <Route path="/" component={Home} />
    </Router>

  </div>
  );
}

export default App;
