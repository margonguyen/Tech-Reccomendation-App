import {combineReducers} from 'redux'
import LoggedReducer from 'isLogged'
const allReducers = combineReducers( {
    isLogged : LoggedReducer
}
)

export default allReducers;