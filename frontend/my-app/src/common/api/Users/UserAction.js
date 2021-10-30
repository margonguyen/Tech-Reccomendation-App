import axios from 'axios'
import {FETCH_USER_SUCCESS , FETCH_USER_REQUEST,  FETCH_USER_FAILURE} from UserTypes ;


export const fetchUsers = () => {
    
}
export const fetchUserRequest = () =>{
    return {
        type : FETCH_USER_REQUEST
    }
}

export const fetchUserSuccess = (users) =>{
    return {
        type : FETCH_USER_SUCCESS ,
        payload : users

    }
}

export const fetchUserRequest = (error) =>{
    return {
        type : FETCH_USER_REQUEST,
        payload : error
    }
}