import React from 'react'
import {useSelector} from 'react-redux';

function Home() {
    const isLogged = useSelector(state => state.isLogged)
    return ( 
        <div>
            {isLogged ? <p> This is your home</p> : <p> This is home</p>}
        </div>
     );
}

export default Home;